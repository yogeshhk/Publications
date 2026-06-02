# ==============================================================================
#   Execute Neural Network specified in an XML by Tenforflow
#   Original: http://stackoverflow.com/questions/40824149/complete-tensorflow-usage-for-training-from-iris-csv-data
#   Additional changes have been done by yogeshhk (Yogesh H. Kulkarni)
# ==============================================================================

import tensorflow as tf
import numpy as np
import time

from nn_pmml_reader import NN_PMML_Reader

class Model:
    W1 = None
    b1 = None
    W2 = None
    b2 = None

    def print(self):
        print("Weights Layer 1: {}".format(self.W1))
        print("Biases Layer 1: {}".format(self.b1))
        print("Weights Layer 2: {}".format(self.W2))
        print("Biases Layer 2: {}".format(self.b2))


# Utility class for loading training and test CSV files.
class Data:

    def __init__(self):
        self.training_features = None
        self.training_labels = None
        self.training_labels_1hot = None
        self.test_features = None
        self.test_labels = None
        self.test_labels_1hot = None

    def load(self,source_data_dict ):
        training_filename = source_data_dict["training_set"]
        test_filename = source_data_dict["test_set"]

        # Training Data load
        training_set = tf.contrib.learn.datasets.base.load_csv_with_header(filename=training_filename,
                                                                           target_dtype=np.int,
                                                                           features_dtype=np.float32,
                                                                           target_column=-1)

        self.training_features    = training_set.data.astype(np.float32)
        self.training_labels      = training_set.target
        self.training_labels_1hot = self.convert_to_one_hot(self.training_labels)

        # Testing Data load
        test_set = tf.contrib.learn.datasets.base.load_csv_with_header(filename=test_filename,
                                                                       target_dtype=np.int,
                                                                       features_dtype=np.float32,
                                                                       target_column=-1)

        self.test_features    = test_set.data.astype(np.float32)
        self.test_labels      = test_set.target
        self.test_labels_1hot = self.convert_to_one_hot(self.test_labels)

    def convert_to_one_hot(self, vector, num_classes=None):
        assert isinstance(vector, np.ndarray)
        assert len(vector) > 0
        if num_classes is None:
            num_classes = np.max(vector)+1
        else:
            assert num_classes > 0
            assert num_classes >= np.max(vector)
        result = np.zeros(shape=(len(vector), num_classes))
        result[np.arange(len(vector)), vector] = 1
        return result.astype(int)

class Tensorflow_PMML:
    def __init__(self,pmml):
        self.data = None
        self.pmml = pmml
        self.function_dict = {
            'softmax' : getattr(tf.nn,"softmax"),
            'softmax_cross_entropy_with_logits': getattr(tf.nn,"softmax_cross_entropy_with_logits"),
            'tanh' : getattr(tf.nn,"tanh"),
            'relu' :  getattr(tf.nn,"relu"),
        }
    def loadData(self):
        self.data = Data()
        self.data.load(self.pmml._source_data)

    def trainModel(self):
        """
        Trains a 2-layer NN model using TensorFlow.
        Layers: Input --> Hidden --> Output
        """
        num_features = self.data.training_features.shape[1]
        num_classes = self.data.training_labels_1hot.shape[1]

        # Create placeholders for the training data. Note that the
        # number of rows is set to None so that different size data sets
        # (or batches) can be loaded.
        x_ph = tf.placeholder(tf.float32, [None, num_features])
        y_ph = tf.placeholder(tf.float32, [None, num_classes])

        h1_size = self.pmml._hidden_layer_size
        # Construct hidden layer.
        W1 = tf.get_variable(name="W1",
                             shape=[num_features, h1_size],
                             initializer=tf.contrib.layers.xavier_initializer())
        b1 = tf.get_variable(name="b1",
                             shape=[h1_size],
                             initializer=tf.constant_initializer(0.0))
        H1 = tf.matmul(x_ph, W1) + b1
        fn_1 = self.function_dict[self.pmml._functions[0]]
        H1 = fn_1(H1)

        # Construct output layer.
        W2 = tf.get_variable(name="W2",
                             shape=[h1_size, num_classes],
                             initializer=tf.contrib.layers.xavier_initializer())
        b2 = tf.get_variable(name="b2",
                             shape=[num_classes],
                             initializer=tf.constant_initializer(0.0))
        y_hat = tf.matmul(H1, W2) + b2
        fn_2 = self.function_dict[self.pmml._functions[1]]

        # Loss function. Computes cross-entropy loss between computed y_hat
        # and y_ph (which holds true values). The y_hat values are normalized
        # with softmax.
        regularization_strength = self.pmml._regularization_strength
        learning_rate = self.pmml._learning_rate
        num_epochs = self.pmml._num_epochs

        J = tf.reduce_mean(
                fn_2(y_hat, y_ph) + \
                regularization_strength * tf.nn.l2_loss(W1) + \
                regularization_strength * tf.nn.l2_loss(W2))

        train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(J)

        sess = tf.Session(config=tf.ConfigProto(device_count = {'GPU' : 0}))
        sess.run(tf.global_variables_initializer())

        start_time = time.time()

        # --- Gradient descent loop. -----------------------------------------
        for i in range(num_epochs):
            op, J_result = sess.run([train_step, J], feed_dict={x_ph:self.data.training_features, y_ph: self.data.training_labels_1hot})

            if (i % 1000 == 0):
                print("Epoch %6d/%6d: J=%10.5f" % (i, num_epochs, J_result))
        # --------------------------------------------------------------------

        end_time = time.time()

        total_time_in_seconds = end_time-start_time
        print("Training took %.2f seconds" % total_time_in_seconds)

        # Save the model parameters in case you need it.
        model = Model()
        model.W1, model.b1, model.W2, model.b2 = sess.run([W1, b1, W2, b2])

        # Compute accuracy on training set.
        correct_predictions_op = tf.equal(tf.argmax(y_hat, 1), tf.argmax(y_ph, 1)) # List of T,F
        accuracy_op = tf.reduce_mean(tf.cast(correct_predictions_op, tf.float32))
        correct_predictions, accuracy = \
            sess.run([correct_predictions_op, accuracy_op],
                     feed_dict={x_ph:self.data.training_features, y_ph:self.data.training_labels_1hot})
        print()
        print("Predictions on training data:")
        print(correct_predictions)
        print("Training accuracy = {}".format(accuracy))

        # Compute accuracy on test set.
        correct_predictions, accuracy = \
            sess.run([correct_predictions_op, accuracy_op],
                     feed_dict={x_ph:self.data.test_features, y_ph:self.data.test_labels_1hot})
        print()
        print("Predictions on test data:")
        print(correct_predictions)
        print("Test accuracy = {}".format(accuracy))

        return model


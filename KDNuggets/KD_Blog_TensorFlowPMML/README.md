# TensorFlow program via XML
Script to run a Tensorflow program by specifications in XML file

Copyright (C) 2017 Yogesh H Kulkarni

## License:
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or any later version.

## Requirements:
* Problem Statement: Neural Network program is still hard to program, even though actual specification is far easier.
* This python program takes a Neural Network specified in an XML as input and executes a TensorFlow program.
* The XML specification is PMML (Predictive Modeling Markup Language, dmg.org) like (but not strictly compliant).
* A sample "data/iris_for_tf.pmml" specifies 2 layers Neural Network on the iris dataset.
* NN_PMML_reader (nn_pmml_reader.py) reads the pmml as well as data, which can then be leveraged by any Deep Learning library. take the config file as well as the directory having text resumes, as arguments.
* The program here, demonstrates use if TensorFlow to take the pmml object and builds a model to be used for further predictions.

## Dependencies:
* Needs Python 3.5

## How to Run:
* Prepare your own .pmml similar to the given one and keep it in "data/" directory
* Prepare your own driver program like "iris_tensorflow_pmml.py" and specify the .pmml as input
* Adjust parameters in .pmml file till satisfactory results are obtained.

## Disclaimer:
* Author (yogeshkulkarni@yahoo.com) gives no guarantee of the results of the program. It is just a fun script. Lot of improvements are still to be made. So, don’t depend on it at all.

import robobrowser
from requests import Session
#import requests
import csv


class BSNL_Parser(object):

    def __init__(self):
        self.main_url = "http://dq.wdc.bsnl.co.in/bsnl-web/residentialSearch.seam"
        self.session = None
        self.cookies = None
        self.comma = "%2C"

        self._data = None
        self.session = Session()
        self.browser = robobrowser.RoboBrowser(session=self.session, history=True, parser='html.parser')


    def process(self, method, inputs):
        if method == "N":  #By number
            self.search_by_number(inputs[0])  # right now only one number is parsed
        #

    def get_cust_details_writer(self):

        f = open('CustomerDetails_Numberwise' + '.tsv', 'wt')
        try:
            pfieldnames = ['FirstName', 'LastName', 'Category', 'HouseNum', 'Street_Locality', 'Area'
                , 'Pincode', 'City', 'State', 'CurrentPhoneNum', 'PrevPhoneNum', 'Type']
            writer = csv.DictWriter(f, fieldnames=pfieldnames, delimiter = '|')
            writer.writeheader()
            return writer
        except Exception as e:
            print(e)


    def clean_string(self, input_string):
        input_string = input_string.strip()
        return input_string.replace('\n', '')

    def search_by_number(self, input):
        tel_number = input["TelNumber"]
        city = input["City"]
        url_by_number = 'http://dq.wdc.bsnl.co.in/bsnl-web/reversePhone.seam?actionMethod=reversePhone.xhtml%3AtelephoneSearch.resetform'
        url_content = 'http://dq.wdc.bsnl.co.in/bsnl-web/revPhSrchDtls.seam'
        self.browser.open(url=self.main_url)
        self.browser.open(url=url_by_number)
        f1 = self.browser.get_form(id="revPhone")
        #print(f1.fields)
        f1.fields['revPhone:firstField'].value = tel_number
        f1.fields['revPhone:city'].value = city
        self.browser.submit_form(f1,submit="revPhone:search")
        self.browser.open(url=url_content)
        body_table = self.browser.find(id="contentSrchResult").find('table').find('tbody')
        #body_table = body.find('table')
        #print(body_table)
        e = body_table.find('tr')
        #print(e)
        writer = self.get_cust_details_writer()

        for t in body_table.find_all('tr'):
            for td in t.find_all('td'):
                # 1: name, 2: number, 3: address, 4: state
                a = td.find('a')
                if a:
                    print(a.get('href'))
                    #details = requests.get("http://dq.wdc.bsnl.co.in/" + a.get('href'))
                    self.browser.open("http://dq.wdc.bsnl.co.in" + a.get('href'))
                    details = self.browser.find(id="contentSubscriber").find('table')
                    #print(details.text)
                    for idx, t1 in enumerate(details.find_all('tr')):
                        td_s = t1.find_all('td')
                        if idx == 0:
                            f_name = self.clean_string(td_s[1].text)
                        elif idx == 1:
                            l_name = self.clean_string(td_s[1].text)
                        elif idx == 2:
                            cat = self.clean_string(td_s[1].text)
                        elif idx == 3:
                            house_num = self.clean_string(td_s[1].text)
                        elif idx == 4:
                            street = self.clean_string(td_s[1].text)
                        elif idx == 5:
                            area = self.clean_string(td_s[1].text)
                        elif idx == 6:
                            pincode = self.clean_string(td_s[1].text)
                        elif idx == 7:
                            city = self.clean_string(td_s[1].text)
                        elif idx == 8:
                            state = self.clean_string(td_s[1].text)
                        elif idx == 9:
                            current_num = self.clean_string(td_s[1].text)
                        elif idx == 10:
                            prev_num = self.clean_string(td_s[1].text)
                        elif idx == 11:
                            type = self.clean_string(td_s[1].text)
                            #
                    #
                    data = {"FirstName": f_name, "LastName": l_name, "Category": cat,
                            "HouseNum": house_num, "Street_Locality": street, "Area": area,
                            "Pincode": pincode, "City": city, "State": state,
                            "CurrentPhoneNum": current_num, "PrevPhoneNum": prev_num, "Type": type}
                    writer.writerow(data)
                #print(td)

        #
        print("all done")

    def search_by_last_name(self, input):
        l_name = input["LastName"]
        city = input["City"]
        url_by_number = 'http://dq.wdc.bsnl.co.in/bsnl-web/reversePhone.seam?actionMethod=reversePhone.xhtml%3AtelephoneSearch.resetform'
        url_content = "http://dq.wdc.bsnl.co.in/bsnl-web/residentialSearch.seam"


if __name__ == '__main__':
    print("Started")
    ms = BSNL_Parser()
    ms.process("N", [{"TelNumber": 3689, "City": "PUNE"}])
    print("end")

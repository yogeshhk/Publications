from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urlrequest
from pyvirtualdisplay import Display
from time import sleep
#import Image
from PIL import Image
import pytesseract

class MTNL_Parser(object):

    def __init__(self):
        self.search_site_url = 'http://202.159.228.58/mweb/web/dirhome'
        self.session = None
        self.cookies = None
        self.comma = "%2C"

        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        #self.session = Session()
        #self.browser = robobrowser.RoboBrowser(session=self.session, history=True, parser='html.parser')

    def start_search(self, url, prep_url=None):

        if prep_url:
            self.driver.get(prep_url)
        self.driver.get(url)

    def get_captcha(self, cap_url):
        img_file = "captcha.png"
        urlrequest.urlretrieve(cap_url, img_file)

        img = Image.open(img_file)
        img = img.convert("RGBA")

        pixdata = img.load()

        # Make the letters bolder for easier recognition

        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][0] < 90:
                    pixdata[x, y] = (0, 0, 0, 255)

        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][1] < 136:
                    pixdata[x, y] = (0, 0, 0, 255)

        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][2] > 0:
                    pixdata[x, y] = (255, 255, 255, 255)

        img.save("input-black.tif")

        #   Make the image bigger (needed for OCR)
        im_orig = Image.open('input-black.tif')
        im_big = im_orig.resize((1000, 500), Image.BILINEAR)
        # filename = "input_resized.tif"
        # im_big.save(filename)
        captcha_text = pytesseract.image_to_string(im_big, lang='eng', config="-psm 8")
        print(captcha_text)
        sleep(2)
        return captcha_text



    def solve_for_captcha(self, captcha_text, number):

        fld_phone = self.driver.find_element_by_name("TEL_NO")
        #fld_phone.clear()
        #fld_phone.send_keys(number)
        #fld_phone.send_keys(Keys.RETURN)

        fld_cap_txt = self.driver.find_element_by_name("dqauth")
        fld_cap_txt.clear()
        fld_cap_txt.send_keys(captcha_text.rstrip().lstrip())
        #fld_cap_txt.send_keys(Keys.RETURN)

        #self.driver.find_element_by_name("Go").click()


        form = self.driver.find_element_by_name('fm3')
        form.submit()
        self.driver.get("http://202.159.228.58/mweb/web/tel_php.php")
        body = self.driver.page_source
        print(body)
        err_p = self.driver.find_element_by_id("errormesg")
        if err_p is not None:
            #print(err_p.text)
            return False, err_p.text
        else:
            return True, body


    def search_by_number(self, number):
        site_url = "http://202.159.228.58/mweb/web/tel_html.php"
        prep_url = 'http://202.159.228.58/mweb/web/dirhome'
        self.start_search(site_url, prep_url=prep_url)
        fld_phone = self.driver.find_element_by_name("TEL_NO")
        fld_phone.clear()
        fld_phone.send_keys(number)
        fld_phone.send_keys(Keys.RETURN)
        #body = self.driver.page_source
        #print(body)
        fld_cap_img_src = self.driver.find_element_by_id("nimg").get_attribute("src")
        print(fld_cap_img_src)

        IsSolved = False

        while not IsSolved:
            IsLen4 = False
            while not IsLen4:
                cap_text = self.get_captcha(fld_cap_img_src)
                print(len(cap_text))
                if len(cap_text) == 4: IsLen4 = True
            #if len(cap_text) != 4:
            #    cap_text = self.get_captcha(fld_cap_img_src)
            res, resp = self.solve_for_captcha(captcha_text=cap_text, number=number)
            # <img id="nimg" src="../comm_file/captcha_img.php">;
            # http://202.159.228.58/mweb/comm_file/captcha_img.php
            #fld_cap_img_src = "http://202.159.228.58/mweb/comm_file/captcha_img.php"
            if res:
                print(resp)
                IsSolved = True
            else:
                print(resp)

        self.driver.quit()
        self.display.stop()


if __name__ == '__main__':
    print("Started")
    ms = MTNL_Parser()
    ms.search_by_number("23232323")
    print("end")

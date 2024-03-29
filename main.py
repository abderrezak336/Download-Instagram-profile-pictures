from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import urllib
import requests
import time
import os



#your password and email
NAME = os.environ.get("USERNAME_FACEBOOK")
PASSWORD = os.environ.get("PASSWORD_INS")


#profile name
PROFILE_NAME = "python.hub"


driver = None

class Profile:
    def __init__(self, name, password, profile):
        self.name = name
        self.password = password
        self.profile = profile
        self.src_img = []

    def login(self):
        #sign in your instagram account
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        global driver
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.instagram.com/")
        username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(self.name)

        time.sleep(2)

        password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(self.password)

        time.sleep(2)

        login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(5)

    def get_profile(self):
        #go to the profile page
        driver.get(f"https://www.instagram.com/{self.profile}/")
        time.sleep(5)

    def scroll(self, num_scroll):
        #scroll down so you can get all source image
        for i in range(1, num_scroll):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

    def get_src_images(self):
        #get the src of image
        photos = driver.find_elements(By.CSS_SELECTOR, "a div._aagu div._aagv  img")
        self.src_img = [ph.get_attribute("src") for ph in photos]

    def get_length(self):
        #get the length of list of src image
        return len(self.src_img)

    def donwload_images(self):
        #download the all images
        for s in range(len(self.src_img[:self.get_length()])):
            urllib.request.urlretrieve(self.src_img[s], f"images/photo{s}.png")




profile = Profile(NAME, PASSWORD, PROFILE_NAME)
profile.login()
profile.get_profile()
profile.scroll(5)
profile.get_src_images()
profile.donwload_images()










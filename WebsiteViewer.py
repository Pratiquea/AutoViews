#!/usr/bin/env/ python3

import webbrowser
import time
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import os
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from vpnlist import vpn_country_list
from list_of_mobile_devices import mobile_device_list

class AutoWebsiteViewer():
    def __init__(self):
        self.k=PyKeyboard()
        self.myWebsiteUrl = 'https://pratiquea.github.io/'
        # self.urls = ['https://github.com/Pratiquea']
        self.urls = ['https://pratiquea.github.io/','https://github.com/Pratiquea']
        self.list_len = len(vpn_country_list)
        self.totalCount = 1000
        self.quit_counter = 5 


    def getButton(self, driver_chrome, id):
        l = []
        about = driver_chrome.find_element_by_id('about_tag')
        resume = driver_chrome.find_element_by_id('resume_tag')
        portfolio = driver_chrome.find_element_by_id('portfolio_tag')
        contact = driver_chrome.find_element_by_id('contact_tag')
        linkedin = driver_chrome.find_element_by_class_name('linkedin')
        github = driver_chrome.find_element_by_class_name('github')
        instagram = driver_chrome.find_element_by_class_name('instagram')
        l.append(about)
        l.append(resume)
        l.append(portfolio)
        l.append(contact)
        # l.append(linkedin)
        # l.append(github)
        # l.append(instagram)
        return l[id]

    def setupMobileChromeDriver(self):
        mobile_id  = random.randint(0,len(mobile_device_list)-1)
        print("mobile used is {}".format(mobile_device_list[mobile_id]))
        # print("mobile device is {} and type is {}".format(mobile_device_list[mobile_id]), mobile_device_list[mobile_id]
        # print("mobile device is {} and type is ".format(mobile_device_list[7]))
        mobile_emulation = { "deviceName": str(mobile_device_list[mobile_id]) } 
        # mobile_emulation = { "deviceName": "Galaxy S9" } 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_argument('--ignore-certificate-errors')
        driver_chrome = webdriver.Chrome(chrome_options=chrome_options)
        return driver_chrome
    
    def setupWebChromeDriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--ignore-certificate-errors')
        driver_chrome = webdriver.Chrome(chrome_options=chrome_options)
        return driver_chrome

    def chooseDeviceAndSetupDriver(self):
        if random.randint(0,11) > 4:
            return self.setupMobileChromeDriver(), 'Mobile'
        else:
            return self.setupWebChromeDriver(), 'Web'

    def chooseButton(self, driver_chrome):
        num = random.randint(0,3)
        try:
            return self.getButton(driver_chrome, num)
        except Exception as e:
            print(e)

    def ConnectToVpn(self):
        rand_int = random.randint(0, self.list_len-1)
        try:
            os.system("nordvpn c "+ vpn_country_list[rand_int])
        except Exception as e:
            print(e)


    def fetchPrateeksWebsite(self,url,device):
        if url == self.myWebsiteUrl:
            device.get(url)
        else:
            device.get(url)
            time.sleep(2)

            myWebsiteLink = device.find_element_by_partial_link_text('pratiquea.github.io')
            myWebsiteLink.click()
        

    def main(self):
        count = 0
        while count < self.totalCount:
            for url in self.urls:
                try:
                    rand_wait = random.randint(3, 10)
                    # call function to connect to VPN
                    self.ConnectToVpn()
                    time.sleep(2)

                    driver_chrome, device = self.chooseDeviceAndSetupDriver()
                    print("\nUsing {} device\n".format(device))

                    self.fetchPrateeksWebsite(url,driver_chrome)

                    if device =='Web':
                        driver_chrome.fullscreen_window()
                    time.sleep(2)
                    for i in range(4):
                        if device == 'Mobile':
                            nav_button = driver_chrome.find_element_by_id('mobile-nav')
                            nav_button.click()
                            time.sleep(0.5)
                        button = self.chooseButton(driver_chrome)
                        try:
                            button.click()
                        except Exception as e:
                            print(e)
                        driver_chrome.fullscreen_window()
                        time.sleep(0.8)

                    # webbrowser.open_new(url)
                    time.sleep(rand_wait)
                    if(count%self.quit_counter):
                        driver_chrome.quit()
                        driver_chrome.quit()
                        driver_chrome.quit()
                except Exception as e:
                    print(e)
                count = count + 1


if __name__ == '__main__':
    wesbiteViewer = AutoWebsiteViewer()
    wesbiteViewer.main()
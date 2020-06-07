#!/usr/bin/env/ python3

import webbrowser
import time
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import os
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# class websiteVisit:


# vpn_country_list = [
#                     "Moldov"\
#                         ]





vpn_country_list = ["United_States Atlanta",\
                    "United_States Chicago",\
                    "United_States Los_Angeles",\
                    "United_States New_York",\
                    "United_States Salt_Lake_City",\
                    "United_States Buffalo",\
                    "United_States Dallas",\
                    "United_States Manassas",\
                    "United_States Phoenix",\
                    "United_States San_Francisco",\
                    "United_States Charlotte",\
                    "United_States Denver",\
                    "United_States Miami",\
                    "United_States Saint_Louis",\
                    "United_States Seattle",\
                    "Canada Montreal",\
                    "Canada Toronto",\
                    "Canada Vancouver",\
                    "Mexico",\
                    "United_Kingdom",\
                    "Albania",\
                    "Austria",\
                    "Belgium",\
                    "Bosnia",\
                    "Bulgaria",\
                    "Croatia",\
                    "Cyprus",\
                    "Czech_Republic",\
                    "Denmark",\
                    "Estonia",\
                    "Estonia",\
                    "Finland",\
                    "France",\
                    "Germany",\
                    "Germany Berlin",\
                    "Germany Frankfurt",\
                    "Greece",\
                    "Hungary",\
                    "Iceland",\
                    "Ireland",\
                    "Italy",\
                    "Latvia",\
                    "Luxembourg",
                    "Macedonia",\
                    "Netherlands",\
                    "Norway",\
                    "Poland",\
                    "Portugal",\
                    "Romania",\
                    "Serbia",\
                    "Slovakia",\
                    "Spain",\
                    "Sweden",\
                    "Switzerland",\
                    "Turkey",\
                    "Ukraine",\
                    "Australia Adelaide",\
                    "Australia Brisbane",\
                    "Australia Melbourne",\
                    "Australia Perth",\
                    "Australia Sydney",\
                    "New_Zealand ",\
                    "Hong_Kong",\
                    "India",\
                    "India Chennai",\
                    "India Mumbai",\
                    "Indonesia",\
                    "Israel",\
                    "Japan",\
                    "Malaysia",\
                    "Singapore",\
                    "South_Korea",\
                    "Taiwan",\
                    "Vietnam",\
                    "Thailand",\
                    "Costa_Rica",\
                    "Argentina",\
                    "Brazil",\
                    "Chile",\
                    "South_Africa",\
                    "Moldova",\
                    "Moldova"\
                        ]

def closeTab(k):
    k.press_keys([k.control_key,"W"])


def getButton(driver_chrome, id):
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

def chooseButton(driver_chrome):
    num = random.randint(0,3)
    try:
        return getButton(driver_chrome, num)
    except Exception as e:
        print(e)



k=PyKeyboard()
count = 0
urls = ['https://pratiquea.github.io/']
list_len = len(vpn_country_list)
totalCount = 500
quit_counter = 5 
while count < totalCount:
    for url in urls:
        rand_wait = random.randint(3, 15)
        rand_int = random.randint(0, list_len-1)
        try:
            os.system("nordvpn c "+ vpn_country_list[rand_int])
        except Exception as e:
            print(e)

        time.sleep(2)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--ignore-certificate-errors')
        driver_chrome = webdriver.Chrome(chrome_options=chrome_options)
        driver_chrome.get(url)
        driver_chrome.fullscreen_window()
        time.sleep(1)
        for i in range(4):
            button = chooseButton(driver_chrome)
            try:
                button.click()
            except Exception as e:
                print(e)
            driver_chrome.fullscreen_window()
            time.sleep(0.8)

        # webbrowser.open_new(url)
        time.sleep(rand_wait)
        if(count%quit_counter):
            driver_chrome.quit()
            driver_chrome.quit()
            driver_chrome.quit()
        count = count + 1


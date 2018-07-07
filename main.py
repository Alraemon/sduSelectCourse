#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 18:08:05 2018

@author: erwin
"""

from selenium import webdriver
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser=webdriver.Chrome(executable_path="./chromedriver",chrome_options=None)
print("\033[1;35m //Headless Chrome Constructed// \033[0m")
browser.get("http://bkjwxk.sdu.edu.cn/f/login")
while 1:
    userInput=browser.find_element_by_name("j_username")
    passwdInput=browser.find_element_by_name("j_password")
    loginButton=browser.find_element_by_id("loginButtonId")
    print("\033[1;35m //Analyzed Login Page// \033[0m")
    username=input("输入你的教务账号:")
    password=input("输入你的教务密码:")
    userInput.send_keys(username)
    passwdInput.send_keys(password)
    loginButton.click()
    sleep(1)
    print(browser.current_url)
    if browser.current_url=="http://bkjwxk.sdu.edu.cn/f/common/main":
        break
    else:
        print("\033[1;35m //输错了 重新来// \033[0m")
        browser.refresh()
wsxkButton=browser.find_element_by_id("wsxk")
wsxkButton.click()
sleep(1)
coursesToSelect=browser.find_elements_by_xpath("//table[@id='kcTable']/tbody/tr")
print("\n可选课程:")
print("\033[1;35m 课程名\t\t课程ID \033[0m")
toBeVerified=[]
for course in coursesToSelect[1:]:
    courseId=course.find_element_by_xpath("./td[2]")
    toBeVerified.append(courseId.text)
    courseName=course.find_element_by_xpath("./td[3]")
    print(courseName.text,"\t\t",courseId.text)
print("\n")
while 1:
    toSelectId=input("\033[1;35m 输入你要选的课程ID: \033[0m")
    if toSelectId not in toBeVerified:
        print("\033[1;35m //输错了 重新来// \033[0m")
    else:
        break
selectButton=browser.find_element_by_xpath("//table[@id='kcTable']/tbody/tr[@id='"+toSelectId+"']/td[1]/a")
selectButton.click()
confirmButton=browser.find_element_by_xpath("/body/div[1]/table[1]/tbody[1]/tr[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/button[1]")
confirmButton.click()

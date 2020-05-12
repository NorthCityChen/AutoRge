'''
@Author: Mr.Sen
@LastEditTime: 2020-05-12 11:36:42
@Website: https://449293786.site
@Mr.Sen All rights reserved
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import pyperclip
import time
import os
import init

def login_vpn(vpn_pwd,browser):
    browser.get('https://222-27-166-246.webvpn.nefu.edu.cn/')
    usr=browser.find_element_by_id('username')
    usr.send_keys(vpn_pwd.get('usrname'))
    pwd=browser.find_element_by_id('password')
    pwd.send_keys(vpn_pwd.get('pwd'))
    # print(vpn_pwd.get('usrname'))
    # print(vpn_pwd.get('pwd'))
    browser.find_element_by_id('login').click()
    return browser

def login_rg(rg_pwd,browser):
    usrname=browser.find_element_by_id('loginMail')
    pwd=browser.find_element_by_id('loginPass')
    usrname.send_keys(rg_pwd.get('usrname'))
    pwd.send_keys(rg_pwd.get('pwd'))
    browser.find_element_by_id('loginSubmit').click()
    return browser

def get_code(lst,browser):
    cd={}
    browser.get('https://222-27-166-246.webvpn.nefu.edu.cn/studentExercise/index?currentClassId=455')
    for i in lst:
        browser.get('https://222-27-166-246.webvpn.nefu.edu.cn/studentExercise/index?currentClassId=455#%d_exercise_709_solId' % (i-1000))
        browser.refresh()
        code=browser.find_element_by_id('myCoder_1')
        code.send_keys(Keys.CONTROL,'a')
        code.send_keys(Keys.CONTROL,'c')
        scode=pyperclip.paste()
        cd[i]=scode
        browser.save_screenshot(os.getcwd()+'\\pic\\'+str(i)+".png")
    return cd

def get_lst():
    nlst=[]
    with open(os.getcwd()+'/settings/problems.txt','r') as f:
        lst=f.readlines()
    for i in lst:
        nlst.append(int(i))
    return nlst


def main():
    lst=get_lst()
    try:
        with open(os.getcwd()+'\\settings\\pwd.json') as f:
            pwd=json.load(f)
    except FileNotFoundError:
        init.init()
        with open(os.getcwd()+'\\settings\\pwd.json') as f:
            pwd=json.load(f)
            
    vpn_pwd=pwd['vpn']
    rg_pwd=pwd['rg']
    browser=webdriver.Chrome()
    # browser=webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser=login_vpn(vpn_pwd,browser)
    browser=login_rg(rg_pwd,browser)
    cd=get_code(lst,browser)
    browser.close()
    return cd

if __name__=='__main__':
    main()
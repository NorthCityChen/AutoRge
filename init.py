'''
@Author: Mr.Sen
@LastEditTime: 2020-05-19 20:39:01
@Website: https://449293786.site
@Mr.Sen All rights reserved
'''
import json
import os
import time


def init():

    if not os.path.exists(os.getcwd()+'/settings/'):
        os.mkdir(os.getcwd()+'/settings/')
        
    if not os.path.exists(os.getcwd()+"/settings/pwd.json"):
        vpn_cnt=input("请输入VPN账号：")
        vpn_pwd=input("请输入VPN密码：")
        rg_cnt=input("请输入锐格账号：")
        rg_pwd=input("请输入锐格密码：")

        print("正在设置……")
        dc={
            'vpn':{
                'usrname':vpn_cnt,
                'pwd':vpn_pwd
            },
            'rg':{
                'usrname':rg_cnt,
                'pwd':rg_pwd
            }
        }
        with open(os.getcwd()+"/settings/pwd.json",'w') as f:
            json.dump(dc,f)
            print("设置成功！")
    if not os.path.exists(os.getcwd()+'/bg/'):
        os.mkdir(os.getcwd()+'/bg/')
    if not os.path.exists(os.getcwd()+'/pic/'):
        os.mkdir(os.getcwd()+'/pic/')

if __name__=='__main__':
    init()
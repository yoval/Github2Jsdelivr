# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:59:56 2022

@author: Administrator
"""

import PySimpleGUI as sg

#https://raw.githubusercontent.com/yoval/Qidiantu/master/shouye_2022-4.json
def getCdnUrl(githuburl):    
    userName = githuburl.split('/',6)[-4]
    repository = githuburl.split('/',6)[-3]
    branche = githuburl.split('/',6)[-2]
    filename = githuburl.split('/',6)[-1]
    cdnUrl = 'https://cdn.jsdelivr.net/gh/%s/%s@%s/%s'%(userName,repository,branche,filename)
    return cdnUrl
#https://github.com/yoval/Qidiantu/blob/master/shouye_2022-4.json
def getCdnUrl2(githuburl):
    userName = githuburl.split('/',7)[-5]
    repository = githuburl.split('/',7)[-4]
    branche = githuburl.split('/',7)[-2]
    filename = githuburl.split('/',7)[-1]
    cdnUrl = 'https://cdn.jsdelivr.net/gh/%s/%s@%s/%s'%(userName,repository,branche,filename)
    return cdnUrl









sg.theme('Green')   # 设置当前主题
layout = [
            [sg.Multiline('输入Github链接，如 \nhttps://raw.githubusercontent.com/yoval/Qidiantu/master/shouye_2022-4.json\nhttps://github.com/yoval/Qidiantu/blob/master/shouye_2022-4.json',size=(80,15), key='GithubUrl')],
            [sg.Button('转换链接')],
            [sg.Output(size=(80, 20))],
        ]
# 创造窗口
window = sg.Window('Github CDN链接转换', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    GithubUrlList = values['GithubUrl']
    GithubUrlList = GithubUrlList.split('\n')
    for GithubUrl in GithubUrlList:
        if 'githubusercontent' in GithubUrl or 'blob' in GithubUrl:
            try:
                cdnUrl = getCdnUrl(GithubUrl)
                if 'blob' in cdnUrl:
                    cdnUrl = getCdnUrl2(GithubUrl)
                print(cdnUrl)
            except:
                print('Invalid URL')
        else:
            print('Invalid URL')
    print('*'*8)
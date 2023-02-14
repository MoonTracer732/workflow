#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import os.path

path = input("Enter filepath :")

#C:\Users\Administrator\Desktop\录屏视频

if os.path.isdir(path):
    # 判断当前文件路径是否存在
    print("file list is:")
    for filename in os.listdir(path):
        curr_path = os.path.join(path, filename)
        print(curr_path)
    flag = input("file name will raplace into date,sure? (y/n)")
    if flag == "y" or flag == "Y" or flag == "yes" or flag == "YES":
        for filename in os.listdir(path):
            curr_path = os.path.join(path, filename)
            filemt = time.localtime(os.stat(curr_path).st_mtime)
            time_str = time.strftime("%y-%m-%d_%H_%M_%a", filemt)
            
            timename = filename.split(".")[-1]
            srcFile = os.path.join(path, filename)
            dstFile = os.path.join(path, time_str+"."+timename)
            print("dealing ",filename ,"to", time_str+"."+timename)
            if os.path.exists(srcFile):
                os.rename(srcFile,dstFile)
    else :
        print("Not doing anything!!!")
else:
    print("Dirs in not found");

# filemt = time.localtime(os.stat(filename).st_mtime)
# print(time.strftime("%Y-%m-%d", filemt))
 
 
# 输出

# -*- coding: utf-8 -*-
# @Author: Zhoubin
# @Date:   2016-11-29 14:25:45
# @Last Modified by:   Zhoubin
# @Last Modified time: 2016-12-06 14:20:14

import pandas as pd
import numpy as np
import codecs,re


def calRoom(str_room):
    return re.match(r'(\d+?)室(\d+?)厅',str_room.strip()).groups()

def calArea(area):
    return area.strip()[:-2]
    # return re.match(r'(\d+?)平米',area.strip()).groups()

def calTowards(x):
    s=x.strip()
    ans=0
    for c in s:
        if c==' ':
            continue
        if c=='东':
            ans+=8
        elif c=='南':
            ans+=4
        elif c=='西':
            ans+=2
        elif c=='北':
            ans+=1
    return str(ans)




def calDecoration(x):
    s=x.strip()
    if(s=='精装'):
        return '0'
    elif s=='简装':
        return '1'
    elif s=='毛坯':
        return '2'
    else:
        return '3'

def calElevator(x):
    s=x.strip()
    if s=='无电梯':
        return '0'
    else:
        return '1'

def calFocus(x):
    return re.match(r'(\d+?)人关注',x.strip()).groups()[0]

def calWatch(x):
    return re.match(r'共(\d+?)次带看',x.strip()).groups()[0]

def calTime(x):
    if  '年' in x:
        return "365"
    number=re.match(r'(\d+)*',x.strip()).groups()[0]
    if '月' in x:
        number=int(number)*30
    return str(number)

cnt=0
result=open('res.csv','w')
result.write('R1,R2,Area,Dir,Des,Ele,Add,Tag1,Tag2,Tag3,Price'+'\n')
for line in open("lianjia.csv",encoding="utf8"):
    cnt+=1
    if cnt==1:
        continue
    print(cnt)
    line=line.replace('\ufeff','')
    line=line.strip('\n')
    tmp=[]
    attrs=line.split(',')
    # tmp.append(attrs[0])
    #condition
    condition=attrs[0].split('|')
    # print(condition)
    tmp+=calRoom(condition[1])      #室厅
    tmp.append(calArea(condition[2]))      #面积
    tmp.append(calTowards(condition[3]))        #朝向
    tmp.append(calDecoration(condition[4]))        #装修
    if(len(condition))>5:
        tmp.append(calElevator(condition[5]))        #电梯
    else:
        tmp.append("2")
    #address
    tmp.append(attrs[1])
    tag=attrs[2].split('/')
    tmp.append(calFocus(tag[0]))
    tmp.append(calWatch(tag[1]))
    tmp.append(calTime(tag[2]))
    #price
    tmp.append(attrs[3])

    print(tmp)
    result.write(','.join(tmp))
    result.write('\n')
result.close()



# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import math

#矩阵乘法，输入两个矩阵输出乘后矩阵
def matrix_multiple(tup_1,tup_2):
    n,m,p=len(tup_1),len(tup_2),len(tup_2[0])    
    return tuple(tuple(sum((tup_1[x][i]*tup_2[i][y] for i in range(m))) for y in range(p)) for x in range(n))

#矩阵求逆，输入矩阵返回逆矩阵
def matrix_inverse(tup):
    temp,length=np.matrix(tup).I,len(tup)
    return tuple(tuple(np.array(temp)[i][j] for j in range(length)) for i in range(length))

#通过经纬度算距离
def itude_to_distance(long1,lati1,long2,lati2):
    x=abs(lati1-lati2)*111
    y=abs(long1-long2)*math.cos((lati1+lati2)*math.pi/360)*111
    return round((x**2+y**2)**0.5)

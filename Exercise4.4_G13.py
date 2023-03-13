#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:46:04 2023

@author: avariqfr30
"""
from __future__ import division, print_function
import time
import datetime

st = datetime.datetime.now()

from numpy import linspace, sqrt
from math import pi
N = 10000000
h = 2/N
x = linspace(-1,1,N)
y = sqrt(1 - x**2)

I = h*sum(y)*2
delta = I - pi
print('The value of integral is I = {}'.format(I))
print('delta = {}'.format(delta))

et = datetime.datetime.now()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
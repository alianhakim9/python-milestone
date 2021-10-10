#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:10:06 2021

@author: alian
"""

import requests

class SimpleWebService:
    def __init__(self,url):
        self.url = url
        
    def getData(self):
        data = requests.get(self.url)
        return data
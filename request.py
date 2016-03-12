#!/usr/bin/env python

import requests
import json
import time 

class MyRequest():
  url = 'https://www.schappet.com/automation/rest/metric'
  
  
  def post(self, value, strValue):
    payload ={'name': 'WATERMETER' ,'textValue':strValue,'numericValue':value,'dateAdded':time.strftime("%Y-%m-%dT%H:%M:%S.%z"),'source':'WATERPI' }
    r = requests.post(self.url, json=payload)
    return r.text


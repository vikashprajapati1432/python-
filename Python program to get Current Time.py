# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:00:37 2022

@author: ugly
"""

from datetime import *
import pytz


tz_INDIA = pytz.timezone('Asia/Kolkata')
datetime_INDIA = datetime.now(tz_INDIA)
print("INDIA time:", datetime_INDIA.strftime("%H:%M:%S"))

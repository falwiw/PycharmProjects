#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

phone = "https://www.so.com/s?src=lm&ls=sm1972121&q=%E6%B2%99%E9%87%91%E8%AE%BE%E5%A4%87&lmsid=00306d301210faf8&lm_extend=ctype:7"

words = "关键词"
# 替换字符串中的关键词
num = re.sub(r'&q=(.*)&lmsid', '&q='+words+'&lmsid', phone)
print("电话号码是: ", num)


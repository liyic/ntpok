#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

with open('ntpok-check-output.txt') as f:
    lines = f.read().splitlines()
lines = map(lambda x: x.strip(), lines)
lines = filter(None, lines)

ul='<ul>'
for i in range(len(lines)):
    ul=ul+'<li>'+lines[i]+'</li>'
ul=ul+'</ul>'
ul=ul.replace(' - X',' - ✘')

now = datetime.datetime.now()
t=now.strftime("%Y-%m-%d %H:%M:%S")

with open('ntpok-page-template.html') as f:
    a=f.read()
a=a.replace("[LIST]",ul).replace('[TIME]',t)
with open('ntpok-page-output.html','w') as f:
    f.write(a)
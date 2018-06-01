#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntplib
import timeit

def ntpok_query():
    global ntp_client
    global ntp_server
    global ntp_error
    try:
        response=ntp_client.request(ntp_server,version=3)
    except:
        ntp_error=1

def ntpok_check():
    global ntp_client
    global ntp_server
    global ntp_error
    with open('ntpok-list.txt') as f:
        lines = f.read().splitlines()
    lines = map(lambda x: x.strip(), lines)
    lines = filter(None, lines)
    for i in range(len(lines)):
        ntp_server=lines[i]
        t=timeit.timeit(ntpok_query,number=1)
        if ntp_error:
            print ntp_server+" - X"
            ntp_error=None
        else:
            print ntp_server+" - "+str(int(t*1000))+"ms"

ntp_client = ntplib.NTPClient()
ntp_server = ""
ntp_error = None
ntpok_check()
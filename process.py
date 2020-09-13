#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint
import subprocess
import datetime
import socket
import json
import os

def get_processes():
    computer = socket.gethostname()
    timestamp = datetime.datetime.utcnow().isoformat()
    subprocess.check_output("ps aux | grep 'java -jar' | grep -v grep | awk '//{print $2}'", shell=True)
    headers = ['user', 'pid', 'vsz', 'rss', 'tty', 'stat', 'start', 'cpuTime', 'command', 'Computer', 'timestamp']
    raw_data = list(map (lambda s: s.strip().split(None, len(headers) - 3), output[1:]))
    for i in range(0, len(raw_data)):
        raw_data[i].append(computer)
        raw_data[i].append(timestamp)
    return [dict(zip(headers, r)) for r in raw_data]

procs = get_processes()
for p in procs:
    print (p)

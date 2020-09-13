#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint
import subprocess
import datetime
import socket
import json

def get_processes():
    computer = socket.gethostname()
    timestamp = datetime.datetime.utcnow().isoformat()

    output = subprocess.Popen(['ps', 'aux', '--no-headers'], stdout=subprocess.PIPE).stdout.readlines()
    headers = ['user', 'pid', 'cpuUtilization', 'memoryUtilization', 'vsz', 'rss', 'tty', 'stat', 'start', 'cpuTime', 'command', 'Computer', 'timestamp']
    raw_data = map(lambda s: s.strip().split(None, len(headers) - 3), output[1:])
    for i in range(0, len(raw_data)):
        raw_data[i].append(computer)
        raw_data[i].append(timestamp)
    return [dict(zip(headers, r)) for r in raw_data]

procs = get_processes()
for p in procs:
    print json.dumps(p)

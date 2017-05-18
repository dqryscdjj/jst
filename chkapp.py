#!/usr/bin/env python

from __future__ import print_function

from __future__ import absolute_import

import os, sys, re, getopt, getpass
import pexpect


try:
    raw_input
except NameError:
    raw_input = input

def main():
    child=pexpect.spawn('/opt/onos/apache-karaf-3.0.8/bin/client')
    child.expect ("onos>")
    child.sendline('apps -s -a')
    #print(child.before, child.after)
    i=child.expect ([
    'org.onosproject.drivers',
    pexpect.EOF,
    pexpect.TIMEOUT
])
    if i == 0:
        print ("drivers app ok!")
    else:
        child.sendline('app activate org.onosproject.drivers')
    j=child.expect ([
    'org.onosproject.openflow ',
    pexpect.EOF,
    pexpect.TIMEOUT
])
    if j == 0:
        print ("drivers openflow ok!")
    else:
        child.sendline('app activate org.onosproject.openflow')
    k=child.expect ([
    'org.onosproject.vpls ',
    pexpect.EOF,
    pexpect.TIMEOUT
])
    if j == 0:
        print ("drivers vpls ok!")
    else:
        child.sendline('app activate org.onosproject.vpls')

if __name__ == "__main__":
    main()

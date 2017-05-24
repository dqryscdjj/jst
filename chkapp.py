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

    k=child.expect ([
        'org.onosproject.fwd',
        pexpect.EOF,
        pexpect.TIMEOUT
    ])
    if k == 0:
        print ("drivers fwd ok!")
    else:
        child.sendline('app activate org.onosproject.fwd')
        child.expect ("Activated org.onosproject.fwd")
        child.sendline('apps -s -a')
    i=child.expect ([
        'org.onosproject.drivers',
        pexpect.EOF,
        pexpect.TIMEOUT
        ])
    if i == 0:
        print ("drivers app ok!")
    else:
        child.sendline('app activate org.onosproject.drivers')
        child.expect ("Activated org.onosproject.drivers")
        child.sendline('apps -s -a')
    j=child.expect ([
        'org.onosproject.proxyarp',
        pexpect.EOF,
        pexpect.TIMEOUT
    ])
    if j == 0:
        print ("drivers proxyarp ok!")
    else:
        child.sendline('app activate org.onosproject.proxyarp')
        child.expect ("Activated org.onosproject.proxyarp")
        child.sendline('apps -s -a')
    m=child.expect ([
        'org.onosproject.openflow ',
        pexpect.EOF,
        pexpect.TIMEOUT
        ])
    if m == 0:
        print ("drivers openflow ok!")
    else:
        child.sendline('app activate org.onosproject.openflow')
        child.expect ("Activated org.onosproject.proxyarp")
        child.sendline('apps -s -a')
    n=child.expect ([
        'org.onosproject.vpls',
        pexpect.EOF,
        pexpect.TIMEOUT
        ])
    if n == 0:
        print ("drivers vpls ok!")
    else:
        child.sendline('app activate org.onosproject.vpls')
        child.expect ("Activated org.onosproject.vpls")
        child.sendline('logout')

if __name__ == "__main__":
    main()

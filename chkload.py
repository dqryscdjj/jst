#!/usr/bin/env Python   
import os 
import sys, getopt

def load_stat(): 
    loadavg = {} 
    f = open("/proc/loadavg") 
    con = f.read().split() 
    f.close() 
    loadavg['lavg_1']=con[0] 
    loadavg['lavg_5']=con[1] 
    loadavg['lavg_15']=con[2] 
    loadavg['nr']=con[3] 
    loadavg['last_pid']=con[4] 
    return loadavg 
def usage():
	return
chkload=load_stat()['lavg_15']
loadavg=float(chkload)
print "loadavg",loadavg
opts, args = getopt.getopt(sys.argv[1:], "hl:")
loadhigh = 8
for op, value in opts:
	if op == "-l":
		loadhigh = float(value)
	elif op == "-h":
		usage()
		sys.exit()
if loadavg > loadhigh :
	reason="echo `date`' restart onos for loadavg "+chkload+" > "+str(loadhigh)+"'>>/opt/onosrestart.log"
	os.system(reason)
	os.system("ps aux  |  grep -I onos|grep -v grep |  awk '{print $2}'|xargs sudo kill -9")
	os.system("service onos start")


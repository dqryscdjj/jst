import sys, getopt
from yahoo_finance import Currency

def getchange( fromto='USDCNY'):
    change = Currency(fromto)
    bid=change.get_bid()
    ask=change.get_ask()
    rate=change.get_rate()
    return rate

def useage():
    print 'getchg -i '
    print '\t-i currency from to such USDCNY'
    return

opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
for op, value in opts:
    if op == "-i":
        print getchange(value)
        sys.exit()
    elif op == "-h":
        useage()
        sys.exit()
print getchange()

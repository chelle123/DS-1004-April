#!/usr/bin/python

import sys


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, attributes = line.strip().split('\t')
    
    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,f1,f2,f3,f4,f5,f6,f7 = attributes.split(',')
        
    print "%s\t%s\t%s\t%s\t%s" %( key[-19:-12], f2,f3,f5,f6)

#!/usr/bin/env python3

import re
from collections import Counter
import argparse

# regular expression
regexp_parsingApacheAcesslog = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \-\ \- .*?"(GET|POST|.*? ).*?\" (\d{3})'
# create counter dictionary
counter_IP = Counter()
counter_Method = Counter()
counter_ReturnCode = Counter()
counter_Mixed=Counter()

#usage 
##parser=argparse.ArgumentParser()
##parser.add_argument('filename', help='filename to parse. example apacheaccess.log')

##args = parser.parse_args()
##sfilename = args.filename


#f = open('dns.log', 'r')
#f = open(sfilename, 'r')
#with open(sfilename, 'r') as f:
with open('apacheaccess.rand.log', 'r') as f:
    matched = 0
    failed = 0

    for line in f:
        m = re.match(regexp_parsingApacheAcesslog, line)
        if m:
            #print (m.groups())
            scombinedMatchesExtract=str(m.group(1)+"|"+m.group(2)+"|"+m.group(3))
            counter_IP.update([m.group(1)]) # Extracting the IP as first () in the regexp
            counter_Method.update([m.group(2)]) # Extracting the IP as first () in the regexp
            counter_ReturnCode.update([m.group(3)]) # Extracting the IP as first () in the regexp
            counter_Mixed.update([scombinedMatchesExtract])
            matched += 1
        else:
            failed += 1
"""
#    print("""\
#timestamp ...: %s
#client ......: %s
#domain ......: %s
#qtype .......: %s
#dns server ..: %s
#""" % ( m.group('timestamp'),
#        m.group('client'),
#        m.group('domain'),
#        m.group('qtype'),
#        m.group('server'),
#    ))

# Output Results
print('[*] %d lines matched the regular expression' % (matched))
print('[*] %d lines failed to match the regular expression' % (failed), end='\n\n')
print('[*] ============================================')
print('[*] Most Frequently Occurring IP ')
print('[*] ==============counter_IP====================')

for IP, count in counter_IP.most_common(100):
    print('[*] %30s: %d' % (IP, count))


print('[*] =================counter_Method===============')
for retmethod, count2 in counter_Method.most_common(100):
    print('[*] %30s: %d' % (retmethod, count2))

print('[*] ==========couter_ReturnCode==================')
for retcode, count3 in counter_ReturnCode.most_common(100):
    print('[*] %30s: %d' % (retcode, count3))
print('[*] ==========counter_Mixed================')
for sConcat, count4 in counter_Mixed.most_common(100):
    print('[*] %30s: %d' % (sConcat, count4))

print('[*] ============================================')



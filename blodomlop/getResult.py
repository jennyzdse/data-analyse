#!/usr/bin/python
# Version 0.1: fetch the result
# Date:   20160610
#

import urllib2
import sys 
import re
import os

def getRes(addr, header):
   data = urllib2.urlopen(addr).read()
   data = data.replace('\n','').replace('r','')

   df = re.findall('<td valign="top" class="yob_column" style="width:3em;">(.*?)</td>.*?<td valign="top" class="cat_column">\s+(\w+)\s+</td>.*?<td valign="top" style="width:3em;">\s+(\S+)\s+</td>', data)

   for item in df:
       item += (header,)
       print item

   #print df
   return df     

def main(argv):
   # get address list 
   head = "http://www.racetimer.se/sv/race/resultlist/3296?checkpoint=9999&layout=racetimer&page="
   end  = "&rc_id="
   addrlist5 = []
   addrlist10 = []
   for i in range(1,5):
      addrlist5.append(head+str(i)+end+"12798")
   for i in range(1,8):
      addrlist5.append(head+str(i)+end+"12961")
   for i in range(1,3):
      addrlist5.append(head+str(i)+end+"12962")
   for i in range(1,6):
      addrlist10.append(head+str(i)+end+"12963")
  
   #print addrlist

   # get all results
   data5 = []
   for addr in addrlist5:       
      data5 += getRes(addr,'5KM')
   
   data10 = []
   for addr in addrlist10:       
      data10 += getRes(addr, '10KM')

   # save to file

if __name__ == '__main__':
   main(sys.argv)

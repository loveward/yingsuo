#-*-coding:utf8 -*-
import httplib as client
import time
import os

def get_webservertime(host):
    conn=client.HTTPConnection(host)
    conn.request("GET", "/")
    r=conn.getresponse()
    ts=  r.getheader('date')
    local_time= time.mktime(time.strptime(ts[5:], "%d %b %Y %H:%M:%S GMT")) + (16 * 60 * 60)
    ltime = time.gmtime(local_time)
    dat = 'date -u -s "%d-%d-%d %d:%d:%d" ' % (ltime.tm_year,ltime.tm_mon,ltime.tm_mday,ltime.tm_hour,ltime.tm_min,ltime.tm_sec)
    #print dat
    #print local_time
    a= os.system(dat)
    if a == 256:
      print "设置时间失败，请用更高权限运行，系统时间必须为互联网时间才可以进行加密计算。"

get_webservertime('www.baidu.com')

###代码是从
# http://outofmemory.cn/code-snippet/711/python-usage-baidu-fuwuqi-time-setting-caozuoxitong-time
#  抄的
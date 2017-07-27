#-*-coding:utf8 -*-
import httplib as client
import time
def get_webservertime(host):
    conn=client.HTTPConnection(host)
    conn.request("GET", "/")
    r=conn.getresponse()
    ts=  r.getheader('date')
    local_time= time.mktime(time.strptime(ts[5:], "%d %b %Y %H:%M:%S GMT")) + (8 * 60 * 60)
    ltime = time.gmtime(local_time)
    dat = 'date -u -s "%d-%d-%d %d:%d:%d" ' % (ltime.tm_year,ltime.tm_mon,ltime.tm_mday,ltime.tm_hour,ltime.tm_min,ltime.tm_sec)
    print dat

get_webservertime('www.baidu.com')

###代码是从
# http://outofmemory.cn/code-snippet/711/python-usage-baidu-fuwuqi-time-setting-caozuoxitong-time
#  抄的
import urllib2
import time

time.sleep (X)
print "Turn GoPro ON"
urllib2.urlopen ("http://10.5.5.9/bacpac/PW?t=WIFIPASSWORD&p=%01")
time.sleep (4)
print "Start recording"
urllib2.urlopen ("http://10.5.5.9/bacpac/SH?t=WIFIPASSWORD&p=%01")
time.sleep (Y)
print "Stop recording"
urllib2.urlopen ("http://10.5.5.9/bacpac/SH?t=WIFIPASSWORD&p=%00")
time.sleep (3)
print "Be a HERO"

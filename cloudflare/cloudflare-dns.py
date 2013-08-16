#!/usr/bin/env python
# Script by Phantium

import sys, urllib2, socket

ip_url_address = "http://ip.raw.re" # Website providing IP lookup, can be anything as long it outputs just the IP.
username = "your@email.com" # Username for cloudflare
apikey = "yourapikey" # API key for cloudflare

def getIP():
    try:
        ip = urllib2.urlopen(ip_url_address).read()
    except URLError as e:
        print e.reason
    except:
        print "Unable to retrieve IP."
    else:
        return ip

def checkIP(host):
    current_ip = socket.getaddrinfo(host, None, 0)[0][4][0]
    new_ip = getIP()
    if not current_ip == new_ip:
        print "IP changed, updating..."
        return new_ip
    else:
        print "IP: '%s' is already defined for '%s', nothing to do." % (current_ip,host)

def setIP(hostname):
    check_ip = checkIP(hostname)
    if check_ip:
        api_url = "https://www.cloudflare.com/api_json.html"
        api_params = ("?a=DIUP&hosts=%s&u=%s&tkn=%s&ip=%s" % (hostname, username, apikey, check_ip))
        request_url = api_url + api_params
        print "IP for '%s' set to: '%s'" % (hostname, check_ip)
        try:
            urllib2.urlopen(request_url).read()
        except URLError as e:
            print e.reason
        except:
            print "Something broke but I don't know why!"

setIP("dns.yourdomain.com")


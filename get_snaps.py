#!/usr/bin/python

import os
k = os.popen('whoami').read().strip()

path_kde = '/usr/share/applications/'
path_snap = '/var/lib/snapd/desktop/applications/'

if k == 'root':    
    z = os.popen('ls {}*.desktop'.format(path_kde)).read().replace(path_kde,'').split('\n')
    o = os.popen('ls {}*.desktop'.format(path_snap)).read().replace(path_snap,'').split('\n')
    o.pop(-1)
    z.pop(-1)
    for x in o:
        s = 0
        if x not in z:
            e = "cp {}{} {}{}".format(path_snap,x,path_kde,x)
            os.popen(e)
            s += 1
    print "[+] Apps founded: {}\n[+] Apps copied: {}".format(len(o),s)
else:
    print "Run the script as root!!"

#!/usr/bin/python

import os,sys,subprocess

pages_shared = open('/sys/kernel/mm/ksm/pages_shared', 'r').read()
pages_sharing = open('/sys/kernel/mm/ksm/pages_sharing', 'r').read()
pages_unshared = open('/sys/kernel/mm/ksm/pages_unshared', 'r').read()
pages_volatile = open('/sys/kernel/mm/ksm/pages_volatile', 'r').read()
page_size = subprocess.Popen(['getconf', 'PAGESIZE'], stdout=subprocess.PIPE).communicate()[0]

#print linestring.split('\n')

print "\n   pages_shared: %s   pages_sharing: %s   pages_unshared: %s   pages_volatile: %s   page_size: %s" % (pages_shared,pages_sharing,pages_unshared,pages_volatile,page_size)



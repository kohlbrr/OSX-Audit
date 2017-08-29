'''
This is a script to check the current fitness of a given Mac.

Run with `sudo python osx_audit.py`
Tested on OSX 10.10
'''

import subprocess
from distutils.version import StrictVersion
import re

# Subprocess function to execute shell commands
def sp_cmd(command):
  process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
  proc_stdout = process.communicate()[0].strip()
  return proc_stdout

# Helper function to convert bytes to GBs
def get_gb(bytes):
  return ((bytes / 1024) / 1024) / 1024

# Helper function to return a status string based off a boolean
def status(boolean):
  return 'Valid -' if boolean else 'INVALID -'

# OSX Version
# Checks if the OSX version is greater or equal to 10.11
osv = sp_cmd('sw_vers -productVersion')
print 'OSX Version:', \
  status(StrictVersion(osv) >= StrictVersion('10.11.0')), \
  osv

# RAM
# Checks if the system has at least 8GB of RAM
ram = sp_cmd('sysctl hw.memsize')
ramGb = get_gb(int(re.findall(r'\d+', ram)[0]))
print 'RAM Size:', \
  status(ramGb >= 8), \
  ramGb, \
  'GB'

# Disk Usage
# Ensures the main partition is not 75% or more full
disk = sp_cmd('df -k | grep /dev/')
diskUsage = int(re.findall(r'\d+', disk)[7])
print 'Disk Usage:', \
  status(diskUsage < 75), \
  diskUsage, \
  '%'

# /tmp Size
# Checks to see how large /tmp is
tmp = sp_cmd('du -k /tmp')
tmpSize = int(re.findall(r'\d+', tmp)[0])
print '/tmp Size:', \
  status(tmpSize < 1000000), \
  tmpSize, \
  'KB'

# Filevault
# Determines if Filevault is enabled
filevault = sp_cmd('fdesetup status')
print 'Filevault:', \
  status("On" in filevault), \
  filevault

# SSH Access
# REQUIRES SUDO
# Checks to see if SSH access is enabled in sharing settings
ssh = sp_cmd('systemsetup -getremotelogin')
print 'SSH Access:', \
  status("Off" in ssh), \
  ssh

# Software Install Restrictions
# Sees if there are any install restrictions set under Security and Privacy
restrictions = sp_cmd('spctl --status')
if status("disabled" in restrictions): # one-try enable if disabled
    sp_cmd('spctl --enable')
    restrictions = sp_cmd('spctl --status')
print 'Software Install Restrictions:', \
  status("enabled" in restrictions), \
  restrictions


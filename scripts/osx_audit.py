import subprocess
from distutils.version import StrictVersion
import re

def sp_cmd(command):
  process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
  proc_stdout = process.communicate()[0].strip()
  return proc_stdout

def get_gb(bytes):
  return ((bytes / 1024) / 1024) / 1024

def status(boolean):
  return 'Valid -' if boolean else 'INVALID -'

# OSX Version
osv = sp_cmd('sw_vers -productVersion')
print 'OSX Version:', \
  status(StrictVersion(osv) >= StrictVersion('10.7.0')), \
  osv

# RAM
ram = sp_cmd('sysctl hw.memsize')
ramGb = get_gb(int(re.findall(r'\d+', ram)[0]))
print 'RAM Size:', \
  status(ramGb >= 8), \
  ramGb, \
  'GB'

# Disk Usage
disk = sp_cmd('df -k | grep /dev/')
diskUsage = int(re.findall(r'\d+', disk)[7])
print 'Disk Usage:', \
  status(diskUsage < 75), \
  diskUsage, \
  '%'

# /tmp Size
tmp = sp_cmd('du -k /tmp')
tmpSize = int(re.findall(r'\d+', tmp)[0])
print '/tmp Size:', \
  status(tmpSize < 1000000), \
  tmpSize, \
  'KB'

# Filevault
filevault = sp_cmd('fdesetup status')
print 'Filevault:', \
  status("On" in filevault), \
  filevault

# SSH Access
ssh = sp_cmd('systemsetup -getremotelogin')
print 'SSH Access:', \
  status("Off" in ssh), \
  ssh

# Software Install Restrictions
restrictions = sp_cmd('systemsetup -getremotelogin')
print 'Software Install Restrictions', \
  status("On" in restrictions), \
  restrictions


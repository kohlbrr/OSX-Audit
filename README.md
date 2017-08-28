# OSX-Audit
Python script to pull data from OSX devices

This is meant to be an MVP of a script I would concievably run on new Mac computers I was handed in an environment. The goal of the assignment was to surface potential issues with the machines. As what constitutes an 'issue' is dependant on policies and the environment, I've made some assumptions as to what an issue could be. These assumptions are listed below:

- The OSX version should be >= 10.11
- The system should have adequite RAM
- The disk should have adequite free space
- The /tmp file should not be bloated (> 1GB)
- Filevault should be enabled
- SSH access should be restricted
- Software install restrictions should be enabled

This list is not complete by any means, but contains potential issues.

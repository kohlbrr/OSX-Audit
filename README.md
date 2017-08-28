# OSX-Audit
Python script to pull data from OSX devices

This is meant to be an MVP of a script I would concievably run on new Mac computers I was handed in an environment. The goal of the assignment was to surface potential issues with the machines. As what constitutes an 'issue' is dependant on policies and the environment, I've made some assumptions as to what an issue could be. These assumptions are listed below:

- The OSX version should be >= 10.11
- The system should have adequite RAM (>= 8GB)
- The disk should have adequite free space (< 75% full)
- The /tmp file should not be bloated (> 1GB)
- Filevault should be enabled
- SSH access should be restricted
- Software install restrictions should be enabled

This list is not complete by any means, but contains potential issues.

The script is not using any dependencies not preinstalled on OSX.

# Running the script
On an OSX system, download `osx_audit.py` and run:
`> sudo python osx_audit.py`
Note that this uses `sudo`. This is only neccesary for the SSH check at present (`c328c93`), so all other checks can be made without `sudo` access.

# Upstream reporting
The reason I chose Python for this task is twofold:
1) It is not my primary language, but the correct hammer for this particular nail (in addition to a language I want to use more). As all Mac systems come with Python standard, it seemed a fair choice.
2) This opens up the possibility for easier future extensibility as a possible agent-based reporting system, which would be harder with a pure bash script.

The data I'm gathering can be easily contained in a dict, then converted to json for upstream reporting off of a set interval.

# Benefits and Failings
The benefit to this particular script is providing a quick-and-easy visual reference to see how a machine individually stands up to the checks being performed. This saves time remembering / running / parsing the bash commands that are being run by this script. It functions well as a lightweight solution.

Where it breaks down is in the scope of reporting, and the scale it can run at.

The checks it is currently making are important ones, but not comprehensive ones. Part of this will be fixed by adding check to tailor the script to the environment it's being run in, but another part is just automating more checks. This is an easy area for expansion.

Since it's just a "run-and-done" command line `.py` script, it does not scale well to checking many systems. This could be alleviated by packaging the data into an object to be ent upstream, or even more simply through generating an output file to be referenced later (which is possible presently with output redirection).

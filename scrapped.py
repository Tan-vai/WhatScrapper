import os, platform, time, sys
os.system('git pull')
print('\033[1;31m[\x1b[38;5;48m●\033[1;31m]\x1b[38;5;48m Checking For Update...')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;31m[\x1b[38;5;48m●\033[1;31m]\x1b[38;5;48m 64Bit Found')
 import what

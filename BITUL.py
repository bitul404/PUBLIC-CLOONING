import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('git pull')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from BITUL_V264 import login
 
        login()
 
 
 
elif bit == "32bit":
 
        from BITUL_V232 import login
 
 
        login()

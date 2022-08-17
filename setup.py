# /usr/python3.8.10/setupy.py
# Call library to move source to packages
from shutil import move
import platform

python_ver = platform.python_version()[0:3]
username = platform.node().split("-")[0]
# With this high code, we can get the Python version used in the operating system.
try:
   # And we'll send him to the following path.
   move(f"colorRandom" , dst=f'/home/{username}/.local/lib/python{python_ver}/site-packages')
except:
   print('error to set setup!')



# --> Section 1

# Alert install:
      # This code can only be used on Linux according to the specific conditions I am currently stating :
      # If you've moved this transmission route, this operation will not take place.
      # if you manipulate the source, it won't work again.
      # If you delete the surrounding folders, the source will be confused and can't
      # move the required file and you'll be with the text :‌ [ error to set setup! ] You'll be confronted.

# --> Section 2

# Manual installation‌:
      # To manually install the file, you need to [ colorRandom ]
      # Send Python packages to a folder path
      # In Linux, this is the default path :
      # /home/username/.local/lib/python/site-packages.
      # I don't know about other trading systems.

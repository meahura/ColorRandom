from setuptools import setup
from shutil import copy , move
import platform


python_ver = platform.python_version()[0:3]
username = platform.node().split("-")[0]



try:
   move(f"colorRandom" , dst=f'/home/{username}/.local/lib/python{python_ver}/site-packages')
except:
   print('error to set setup!')


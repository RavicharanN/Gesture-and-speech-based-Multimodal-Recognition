import os 


path = "/home/gaurav/Desktop" + "pynaoqi-python2.7-2.5.5.5-linux64" + "lib/python2.7/site-packages"

# Change path

print(path) 

cmd = "export PYTHONPATH=${PYTHOPATH}:" + path

os.system(cmd)


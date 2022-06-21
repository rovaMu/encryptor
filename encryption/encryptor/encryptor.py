from cryptography.fernet import Fernet
from tkinter import *
from tkinter.filedialog import askopenfilename
import os



Tk().withdraw()
filename = askopenfilename()
 
#with open('mykey.key', 'rb')as mykey:
    #key = mykey.read()
key = ("l5CWSCYRxGNOziSqQMctFbHfSmyOOWHup9wtxjbSxI8=")

f = Fernet(key)

with open(filename, 'rb')as original_file:
    original = original_file.read()
encrypted = f.encrypt(original)
with open('file_encrypted.rova', 'wb')as encrypted_file:
    encrypted_file.write(encrypted)
f_name, f_ext = os.path.splitext(filename)
with open('extension.txt', 'w') as f:
    f.write(f_ext)

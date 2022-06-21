from cryptography.fernet import Fernet
from tkinter import *
from tkinter.filedialog import askopenfilename



Tk().withdraw()
filename = askopenfilename()
 

key = ("l5CWSCYRxGNOziSqQMctFbHfSmyOOWHup9wtxjbSxI8=")
with open('extension.txt')as ext:
    extf = ext.read()

f = Fernet(key)


with open('file_encrypted.nigus', 'rb')as encrypted_file:
    encrypted = encrypted_file.read()
decrypted = f.decrypt(encrypted)
with open('decrypted'+ extf, 'wb')as decrypted_file:
    decrypted_file.write(decrypted)

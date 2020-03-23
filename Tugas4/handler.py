import shelve
import uuid
import socket
import os
import base64

class Handle:
    def __init__(self):
        if not os.path.exists("stock"):
            os.makedirs("stock")
    def addfile(self,filename=None,file=None):
        data_file = file
        f = open("stock/"+filename,"wb")
        f.write(data_file)
        return True

    def getfile(self,filename=None):
        temp = []
        f = open("stock/" +filename, "rb")
        hasil = f.read()
        f.close()
        hasil = str(hasil, "utf-8")
        return hasil

    def listfile(self):
        file_list = os.listdir("stock")
        return file_list

if __name__=='__main__':
    p = Handle()
    print(p.listfile())
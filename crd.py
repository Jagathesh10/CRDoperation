import threading 
from threading import*
import time
g={} 
def create(attribute_name,attribute_value,timeout=0):
    if attribute_name in g:
        print("Attribute name already exists") 
    else:
        if(attribute_name.isalpha()):
            if len(g)<(1024*1020*1024) and attribute_value<=(16*1024*1024): 
                if timeout==0:
                    l=[attribute_value,timeout]
                else:
                    l=[attribute_value,time.time()+timeout]
                if len(attribute_name)<=32: 
                    g[attribute_name]=l
            else:
                print("Memory limit exceeded")
        else:
            print("Invalid attribute name.Attribute name must contain only alphabets.No special characters or digits")
def read(attribute_name):
    if attribute_name not in g:
        print("Attribute name does not exist in database.Enter a valid attribute name") 
    else:
        b=g[attribute_name]
        if b[1]!=0:
            if time.time()<b[1]: 
                key=str(attribute_name)+":"+str(b[0])
                return key
            else:
                print("Time-to-live of",attribute_name,"has expired") 
        else:
            key=str(attribute_name)+":"+str(b[0])
            return key
def delete(attribute_name):
    if attribute_name not in g:
        print("Attribute name does not exist in database.Enter a valid attribute name") 
    else:
        b=g[attribute_name]
        if b[1]!=0:
            if time.time()<b[1]: 
                del g[attribute_name]
                print("Attribute name is successfully deleted")
            else:
                print("Time-to-live of",attribute_name,"has expired") 
        else:
            del g[attribute_name]
            print("Attribute name is successfully deleted")

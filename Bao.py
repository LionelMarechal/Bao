import os.path
import zipfile
  
import glob  

  
def listdirectory2(path):  
    fichier=[]  
    l = glob.glob(path+'\\*')  
    for i in l:  
        if os.path.isdir(i): fichier.extend(listdirectory2(i))  
        else: fichier.append(i)  
    return fichier

def listdirectory(path):  
    fichier=[]
    for root, dirs, files in os.walk(path):
        for i in files:
            fichier.append(os.path.join(root, i))  
    return fichier

def listdirectoryzip (path):
    fichier=[]
    for root, dirs, files in os.walk(path):
        for i in [f for f in files if f.endswith(".zip")]:
            fichier.append(os.path.join(root,i))
    return fichier

def lirelistzip (fichier):
     for unzip in [f for f in fichier if zipfile.is_zipfile]:
        zf = zipfile.ZipFile(unzip)
        for i in zf.infolist():
            print i.filename
        
        
        

def listzipsousrep (path) :
    f=listdirectory(path)
    for i in f:
        lz=listdirectoryzip(i)
        for j in lz :
            lirelistzip (j)

import os
import subprocess
import glob
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np




#=================== TO CHANGE ========================
transversal=25 #(z)
vertical=50 #(y)
replication_y = 2 #1 if not replicated
replication_z = 3
#======================================================

WORKDIR = glob.glob(os. getcwd())[0]

total=0




def findline(file_path, word):

    with open(file_path, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        count = 0
        for line in lines:
            count = count+1
            if line.find(word) != -1:
                if line[0:5] == 'print':
                    line = lines[count]
                    return(line)
                else:
                    return(line)


def findword(increment, file_path, word, first, last):
    line = findline(file_path, word)
    try:
        start = line.index(first) + len(first)
        end = line.index(last, start)
        value = line[start:end]
        return value
    except ValueError:
        return ""


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


def cmd(command):
    launch='cmd /c '+command
    subprocess.call([launch],shell=True,stdout=subprocess.DEVNULL)
def delete(command):
    os.remove(glob.glob(WORKDIR+"\\"+str(command))[0])


fichier=glob.glob(WORKDIR+'\\GB*')[0]+' '
NAME = find_between(fichier,WORKDIR+'\\',' ')


ybox=(findline(fichier,'ylo').split())[1]
ybox=float(ybox)/replication_y
ybox=str(ybox)
zbox=(findline(fichier,'zlo').split())[1]
zbox=float(zbox)/replication_z
zbox=str(zbox)

ystep=float(ybox)/vertical
zstep=float(zbox)/transversal





for i in range(0,vertical):
    for j in range(0,transversal):
        total=total+1
        print('atomsk '+str(NAME)+' -shift above 0.4999999999999999*BOX x 0 '+str(-ystep*i)+' '+str(zstep*j)+' '+str(NAME)+'_'+str(total)+'.cfg lammps')
        cmd('atomsk '+str(NAME)+' -shift above 0.4999999999999999*BOX x 0 '+str(-ystep*i)+' '+str(zstep*j)+' '+str(NAME)+'_'+str(total)+'.cfg lammps')
      
total=0        
for i in range(0,vertical):
    for j in range(0,transversal):     
        total=total+1
        delete(str(NAME)+'_'+str(total)+'.cfg')
        
        
        
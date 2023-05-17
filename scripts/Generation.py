# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:00:56 2023

@author: petrazol2
"""
import os
import subprocess
import glob
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np



def init():
    global WORKDIR
    global CL
    global LP
    global Mat
    global angle
    global dangle
    global dup
    WORKDIR = glob.glob(os. getcwd())[0]

def process_2planes(orient1,orient2,count,val1x,val1y,val1z,val2x,val2y,val2z):

    print('\n')
    print('Enter generations parameter. To go back, enter "R" in a section \n \n')
    
    
    go1='R'
    while go1=='R':
        Mat=input('Material ? : ') or "Ni"
        
        
        if Mat == 'Ni':
            CL='fcc'
            LP='3.5295'
            print('Structure : '+CL+' -  Lattice parameter : ' + LP +'\n')
            go1=input('Keep these parameters ?')
            
        elif Mat == 'Cu':
            CL='fcc'
            LP='3.61491'
            print('Structure : '+CL+' -  Lattice parameter : ' + LP +'\n')
            go1=input('Keep these parameters ?')
        
        else:
            go1=0
            CL=input('Cristal lattice ? (fcc, ...) : ')
            while CL=='R':
                Mat=input('Material ? : ')
                CL=input('Cristal lattice ? (fcc, ...) : ')
                
            LP=input('Lattice parameter ? (in A) : ')
            while LP=='R':
                CL=input('Cristal lattice ? (fcc, ...) : ')
                LP=input('Lattice parameter ? (in A) : ')

    dup=input('Duplicate X Y Z ? : ') or "0 0 0"
    while dup=='R':
        angle=LP=input('Lattice parameter ? (in A) : ')
        dup=input('Duplicate X Y Z ? : ')
        
    Go=input('Start generation ? (Enter if yes, "R" to undo the last command, "K" to keep all the intermediates files) \n \n')
    while Go=='R':
        dup=input('Duplicate X Y Z ? : ')
        Go=input('Start generation ? (Enter if yes, "R" to undo the last command, "K" to keep all the intermediates files) \n \n')
        
        
    print('Processing... \n \n')
    
    
       

    cmd('atomsk --create '+str(CL)+' '+str(LP)+' '+str(Mat)+' orient ' + str(orient1) +' -orthogonal-cell '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'.cfg -dup '+str(dup))
    cmd('atomsk --create '+str(CL)+' '+str(LP)+' '+str(Mat)+' orient ' + str(orient2) +' -orthogonal-cell '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val2x)+'.cfg -dup '+str(dup))
    cmd('atomsk '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'.cfg -cut below 0.5*BOX x '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_cut.cfg')
    cmd('atomsk '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val2x)+'.cfg -cut above 0.5*BOX x '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val2x)+'_cut.cfg')
    cmd('atomsk --merge 2 '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_cut.cfg GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val2x)+'_cut.cfg Final_structure_without_removed.cfg')
    cmd('atomsk Final_structure_without_removed.cfg -remove-doubles 10.0 GB'+str(count+1)+'_'+str(Mat)+'_'+str(val1x)+'_'+str(val1z)+'.cfg lammps')
    
    if Go!='K':
        delete('GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'.cfg')
        delete('GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val2x)+'.cfg')
        delete('GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_cut.cfg')
        delete('GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val2x)+'_cut.cfg')
        delete('Final_structure_without_removed.cfg')
        delete('GB'+str(count+1)+'_'+str(Mat)+'_'+str(val1x)+'_'+str(val1z)+'.cfg')


    print('==========   Done   ===========')
    print('LMP File generated with these parameters :')
    print('-orientation cristal 1: '+orient1)
    print('-orientation cristal 2: '+orient2)
    print('-'+str(CL)+' lattice')
    print('-'+str(LP)+ ' Angstrom - lattice parameter')
    print('-'+'Material : '+str(Mat))
    print('-'+'Duplication : '+str(dup))
    print('===============================')
    
    with open('GB'+str(count+1)+'_log_generation.txt','w') as file:
        file.write('-----log_generation-----')
        file.write('\n')
        file.write('\n')
        file.write('Orientation cristal 1 : '+str(orient1))
        file.write('\n')
        file.write('Orientation cristal 2 : '+str(orient2))
        file.write('\n')
        file.write('Structure : '+str(CL))
        file.write('\n')
        file.write('Lattice parameter : '+str(LP)) 
        file.write('\n')
        file.write('Material : '+str(Mat))          
        file.write('\n')
        file.write('Duplication : '+str(dup))
        
    
    print('Log file generated correctly')
    


def process_axis(orient1,count,val1x,val1y,val1z,angle,dangle):

    print('\n')
    print('Enter generations parameter. To go back, enter "R" in a section \n \n')
    
    
    go1='R'
    while go1=='R':
        Mat=input('Material ? : ') or "Ni"
        
        
        if Mat == 'Ni':
            CL='fcc'
            LP='3.5295'
            print('Structure : '+CL+' -  Lattice parameter : ' + LP +'\n')
            go1=input('Keep these parameters ?')
            
        elif Mat == 'Cu':
            CL='fcc'
            LP='3.61491'
            print('Structure : '+CL+' -  Lattice parameter : ' + LP +'\n')
            go1=input('Keep these parameters ?')
        
        else:
            go1=0
            CL=input('Cristal lattice ? (fcc, ...) : ')
            while CL=='R':
                Mat=input('Material ? : ')
                CL=input('Cristal lattice ? (fcc, ...) : ')
                
            LP=input('Lattice parameter ? (in A) : ')
            while LP=='R':
                CL=input('Cristal lattice ? (fcc, ...) : ')
                LP=input('Lattice parameter ? (in A) : ')

    dup=input('Duplicate X Y Z ? : ') or "0 0 0"
    while dup=='R':
        angle=LP=input('Lattice parameter ? (in A) : ')
        dup=input('Duplicate X Y Z ? : ')
        
    Go=input('Start generation ? (Enter if yes, "R" to undo the last command, "K" to keep all the intermediates files) \n \n')
    while Go=='R':
        dup=input('Duplicate X Y Z ? : ')
        Go=input('Start generation ? (Enter if yes, "R" to undo the last command, "K" to keep all the intermediates files) \n \n')
        
        
    print('Processing... \n \n')
    
    
       

    cmd('atomsk --create '+str(CL)+' '+str(LP)+' '+str(Mat)+' orient ' + str(orient1) +' -rotate Z '+ str(dangle)+' -orthogonal-cell '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'.cfg -dup '+str(dup))
    cmd('atomsk --create '+str(CL)+' '+str(LP)+' '+str(Mat)+' orient ' + str(orient1) +' -rotate Z '+ str(-dangle)+' -orthogonal-cell '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'m.cfg -dup '+str(dup))
    cmd('atomsk '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'.cfg -cut below 0.5*BOX x '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'_cut.cfg')
    cmd('atomsk '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'m.cfg -cut above 0.5*BOX x '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'m_cut.cfg')
    cmd('atomsk --merge 2 '+'GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'_cut.cfg GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'m_cut.cfg Final_structure_without_removed.cfg')
    cmd('atomsk Final_structure_without_removed.cfg -remove-doubles 0.0 GB'+str(count+1)+'_'+str(Mat)+'_'+str(val1x)+'_'+str(val1z)+'_'+str(angle)+'.cfg lammps')
    
    if Go!='K':
        delete('GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'.cfg')
        delete('GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'m.cfg')
        delete('GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'_cut.cfg')
        delete('GB'+str(count+1)+'_'+str(Mat)+'_oriented_'+str(val1x)+'_'+str(angle)+'m_cut.cfg')
        delete('Final_structure_without_removed.cfg')
        delete('GB'+str(count+1)+'_'+str(Mat)+'_'+str(val1x)+'_'+str(val1z)+'_'+str(angle)+'.cfg')


    print('==========   Done   ===========')
    print('LMP File generated with these parameters :')
    print('-Orientation cristal 1 : '+str(orient1))
    print('tilt axis : '+str(val1z))
    print('-Misorientation angle : '+str(angle)+' - Half rotation : '+str(dangle))
    print('-'+str(CL)+' lattice')
    print('-'+str(LP)+ ' Angstrom - lattice parameter')
    print('-'+'Material : '+str(Mat))
    print('-'+'Duplication : '+str(dup))
    print('===============================')
    
    with open('GB'+str(count+1)+'_log_generation.txt','w') as file:
        file.write('-----log_generation-----')
        file.write('\n')
        file.write('\n')
        file.write('Orientation cristal 1 : '+str(orient1))
        file.write('\n')
        file.write('tilt axis : '+str(val1z))
        file.write('\n')
        file.write('-Misorientation angle : '+str(angle)+' - Half rotation : '+str(dangle))
        file.write('\n')
        file.write('Structure : '+str(CL))
        file.write('\n')
        file.write('Lattice parameter : '+str(LP)) 
        file.write('\n')
        file.write('Material : '+str(Mat))          
        file.write('\n')
        file.write('Duplication : '+str(dup))
        
    
    print('Log file generated correctly')
    


    
def cmd(command):
    launch='cmd /c '+command
    p=subprocess.call([launch],shell=True,stdout=subprocess.DEVNULL)
    
    
def delete(command):
    os.remove(glob.glob(WORKDIR+"\\"+str(command))[0])



def list():
    import os
    initial_count = 0
    dir = os.getcwdb()
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            if path[-4:].decode('UTF-8')=='.txt':
                initial_count += 1
    
    return initial_count

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""


def main():

    init()
    count=list()
    
    val2='R'

    while val2=='R':
        val1='R'

        while val1=='R':
            val1=input('Enter the orientation of the cristal 1 - XXX YYY ZZZ (separated with space) \n')
        val2=input('Enter either a tilt axis [between bracket] or a misorientation angle (finish with °) \n')
        
        
    if val2[-1]!='°':
        print('\nCrystal 1 orientation : '+ str(val1))
        print('Crystal 2 orientation : '+ str(val2))  
    if val2[-1]=='°':
        print('\nCrystal 1 orientation : '+ str(val1))
        print('Misorientation angle : '+ str(val2))
        
        
        
    Go=input('Keep this strcucture ? (enter to continue, "R" to redo)')  
    
    
    while Go=='R':
        val2='R'
        while val2=='R':
            val2=input('Enter either a tilt axis [between bracket] or a misorientation angle (finish with °) \n')
            
            
        if val2[-1]!='°':
            print('\nCrystal 1 orientation : '+ str(val1))
            print('Crystal 2 orientation : '+ str(val2))  
        if val2[-1]=='°':
            print('\nCrystal 1 orientation : '+ str(val1))
            print('Misorientation angle : '+ str(val2))
        
        
        
        
        Go=input('Keep this strcucture ? (enter to continue, "R" to redo the last choice)')  
  
        
        
    val1=str(val1+' ')
    val1x=(find_between( val1, '', ' ' ))
    val1y=(find_between( val1, str(val1x+' '), ' ' ))
    val1z=(find_between( val1, str(val1y+' '), ' ' ))
    
    
    if val2[-1]!='°':
        val2x=(find_between( val2, '', ' ' ))
        val2y=(find_between( val2, str(val2x+' '), ' ' ))
        val2z=(find_between( val2, str(val2y+' '), ' ' ))
        process_2planes(val1,val2, count,val1x,val1y,val1z,val2x,val2y,val2z)

    
    if val2[-1]=='°':
        
        angle=val2[:-1]
        print(angle)
        dangle=float(angle)/2

        process_axis(val1,count,val1x,val1y,val1z,angle,dangle)

            
            
if __name__ == '__main__':  
    main()


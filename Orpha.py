orpha = 'href="http://www.orpha.net/'

import os
import DataLoad

Accs = {0:[], ## list of Uniprot pages 
        1:[]  ## all orpha linxx
        }

DI = {}


dna = 'C:\\Il\\PlasmaProt\\PlasmaUniprot'
Accs[0] = os.listdir(dna)

DataLoad.AI['Orpha'] = {}
DataLoad.ParamsDI['dna'] = 'C:\\Il\\PlasmaProt'

def Write__orpha__csv():

    fi = open('Orpha.csv', 'w')
    for k, v in DataLoad.AI['Orpha'].items():
        arr = [k, v[0], v[1]]
        ls = ';'.join(arr) + '\n'
        fi.write(ls)
    
    fi.close()
    print 'Write__orpha: done'


def Dump__orpha():

    DataLoad.DumpDI('Orpha')
    print 'Dump__orpha: done'
####    


def Get__all__orpha():

#    DI.clear()
    for y in range(len(Accs[0])):
        fname = Accs[0][y]
#        Get__protname(fname)
        Get__orpha(fname)
        

def Get__orpha(fname):

    fn = fname
    inx = fname.split('.')[0]    
    
#    print fn
    fna = dna +'\\'+fn
    fi = open(fna)
    line = fi.read()
    fi.close()

    if orpha in line:
        start = line.find(orpha)
        line = line[(start+6):]
        end = line.find('"')
        orpha_ul = line[:end]
        #print orpha_ul
        the_orpha = orpha_ul.split('=')[-1]
        line = line[end:]
        start_pos = line.find('</a>')
        
        end_pos = line.find('<br/>')
        orpha_disease = line[(start_pos+4):end_pos]
        orpha_disease = orpha_disease.strip()
        if orpha_disease[-1] == '.':
            orpha_disease = orpha_disease[:-1]
        print inx, the_orpha, orpha_disease 
         
        DataLoad.AI['Orpha'][inx] = [the_orpha, orpha_disease] 



def Start():
    
    Get__all__orpha()
    #Dump__orpha()
    Write__orpha__csv()

Start()

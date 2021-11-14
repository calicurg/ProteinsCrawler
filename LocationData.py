##Q9UPV0
import os
import DataLoad

Accs = {0:[], ## list of Uniprot pages 
        1:[]  ## all linxx
        }

DI = {}


dna = 'C:\\Il\\PlasmaProt\\PlasmaUniprot'
Accs[0] = os.listdir(dna)

DataLoad.AI['Disease'] = {}
DataLoad.AL['LocLI'] = []
DataLoad.ParamsDI['dna'] = 'C:\\Il\\PlasmaProt'

def Write__locations():

    fi = open('ExtraList.txt', 'w')
    
    for si in DataLoad.AL['LocLI']:
        si += '\n'
        fi.write(si)
    fi.close()
    print 'Write__locations: done'
##    


def Get__all__locations():

#    DI.clear()
    for y in range(len(Accs[0])):
        fname = Accs[0][y]
#        Get__protname(fname)
        Get__location(fname)
        

def Get__location(fname):

    fn = fname
    inx = fname.split('.')[0]
    
    
#    print fn
    fna = dna +'\\'+fn
    fi = open(fna)
    line = fi.read()
    fi.close()

    start = line.find('</span>Subcellular location')
    end = line.find('<h4>Topology')
    if end == -1:
        end = line.find('</span>GO - Cellular component')
    if start > 0 and end > 0:
        fr = line[start:end]
        if 'extracellular ' in fr:
            print inx
            DataLoad.AL['LocLI'].append(inx)
    else:
        print fname, 'fr not detrmined'

     



def Start():
    
##    Get__all__protnames()
##    Write__protnames()
##    fname = Accs[0][40]
##    Get__diseases(fname)
##    Get__all__diseases()
    Get__all__locations()
    Write__locations()

Start()




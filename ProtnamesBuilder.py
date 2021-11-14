##Q9UPV0
import os

Accs = {0:[], ## list of Uniprot pages 
        1:[]
        }

DI = {}

dna = 'C:\\Il\\PlasmaProt\\PlasmaUniprot'
Accs[0] = os.listdir(dna)

def Write__protnames():

    fi = open('Protnames.txt', 'w')
    for k, v in DI.items():
        ls = k+';'+v+'\n'
        fi.write(ls)
    fi.close()

    print 'Write__protnames: done'
    

def Get__all__protnames():

    DI.clear()
    for y in range(len(Accs[0])):
        fname = Accs[0][y]
        Get__protname(fname)

            
##    for k, v in DI.items():
##        print k, v

    

def Get__protname(fname):
#fn = Accs[0][0]
    fn = fname
#    print fn
    fna = dna +'\\'+fn
    fi = open(fna)
    line = fi.read()
    fi.close()

    try:
        header = line.split('h1')[1]
        header = header.split('>')[1]
        header = header.split('</')[0]

        inx = fname.split('.')[0]
        DI[inx] = header
    except:
        print fname, ': not done'

#    print header


def Start():
    
    Get__all__protnames()
    Write__protnames()

Start()




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

def Write__protnames():

    fi = open('Protnames.txt', 'w')
    for k, v in DI.items():
        ls = k+';'+v+'\n'
        fi.write(ls)
    fi.close()

    print 'Write__protnames: done'
    

def Get__all__diseases():

    DI.clear()
    for y in range(len(Accs[0])):
        fname = Accs[0][y]
#        Get__protname(fname)
        Get__diseases(fname)

    DataLoad.DumpDI('Disease')
##    DataLoad.DumpLI('LocLI')
##    for k, v in DI.items():
##        print k, v

def Get__all__locations():

#    DI.clear()
    for y in range(len(Accs[0])):
        fname = Accs[0][y]
#        Get__protname(fname)
        Get__location(fname)
        
    fi = open('C:\\Il\\PlasmaProt\\ExtraList.txt', 'w')
    for si in DataLoad.AL['LocLI']:
        si += '\n'
        fi.write(si)
        
    fi.close()
##    DataLoad.DumpLI('LocLI')
##    for k, v in DI.items():
##        print k, v

def Get__location(fname):

    EL = ['extracellular region',
          'extracellular space',
          'extracellular vesicle',
          #'extracellular matrix'
          ]

    fn = fname
    inx = fname.split('.')[0]
    
    
#    print fn
    fna = dna +'\\'+fn
    fi = open(fna)
    line = fi.read()
    fi.close()

##    start = line.find('</span>Subcellular location')
##    end = line.find('<h4>Topology</h4>')
    for elsi in EL:
        if elsi in line:
            print inx
            DataLoad.AL['LocLI'].append(inx)
            break
        

     

def Get__diseases(fname):
#fn = Accs[0][0]
    fn = fname
    inx = fname.split('.')[0]
    
#    print fn
    fna = dna +'\\'+fn
    fi = open(fna)
    line = fi.read()
    fi.close()

    Array = []

##    if 'extracellular ' in line:
##        DataLoad.AI['LocLI'].append(inx)


    if 'Involvement in disease' in line:

        asl = line.split('<a ')
        for al in asl:
            href =  al.split('</a>')[0]
            if 'href="/diseases/' in href:
                start = href.find('href="/diseases/')
                href = href[(start+16):]
                di_sl = href.split('">')
                Array.append(di_sl)
            
        DataLoad.AI['Disease'][inx] = Array
##    else:
##        
##        print fname, 'no diseases involved'
                
#    print DI            
##        try:
##            header = line.split('h1')[1]
##            header = header.split('>')[1]
##            header = header.split('</')[0]
##
##            inx = fname.split('.')[0]
##            DI[inx] = header
##        except:
##            print fname, ': not done'

#    print header


def Start():
    
##    Get__all__protnames()
##    Write__protnames()
##    fname = Accs[0][40]
##    Get__diseases(fname)
##    Get__all__diseases()
    Get__all__locations()

Start()




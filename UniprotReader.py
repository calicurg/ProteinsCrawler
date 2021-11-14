import urllib as UL

Accs = {0:[], ## rl
        1:[]}


def Read__uniprot__page(inx):
    
    ul = 'http://www.uniprot.org/uniprot/'+inx
    fi = UL.urlopen(ul)
    line = fi.read()
    fi.close()

    dna = 'C:\\Il\\PlasmaProt\\PlasmaUniprot'
    fna = dna+'\\'+inx+'.html'
    fi = open(fna, 'w')
    fi.write(line)
    fi.close()

    print 'done'



def GetUniprot():

    for y in range(8500, 9500):
        inx = Accs[0][y]
        Read__uniprot__page(inx)
        print y, inx        
        

    

def ReadUniprotIDList():

    Accs[0] = []
    fi = open('UniprotIDList.txt', 'r')
    rl =  fi.readlines()
    fi.close()
    for si in rl:
        si = si.strip()
        Accs[0].append(si)
        
    
    print len(Accs[0])

##    for inx in Accs[0]:
##        ls = '<'+inx+'>'
##        print ls
        
    print 'ReadUniprotIDList: done'


def WriteUniprotIDList():

    fi = open('UniprotIDList', 'w')
    for si in Accs[1]:
        si += '\n'
        fi.write(si)
    fi.close()
    print 'WriteUniprotIDList: done'

def GetUnprotID():

    for ls in Accs[0]:
        inx = ls.split('	')[0]
        inx = inx.strip()
        if inx == 'Null' or inx == 'NULL':
            continue
        else:
            Accs[1].append(inx)
            
        
#        print inx
        
    print 'GetUnprotIDs: done'
    print 'total', len(Accs[1]) 
    
def ReadHIP():

    fi = open('HIP2.txt', 'r')
    Accs[0] = fi.readlines()
    fi.close()

    print 'ReadHIP: done'
    


def Read__fibrionogen():
    ul = 'http://www.uniprot.org/uniprot/P02671'
    fi = UL.urlopen(ul)
    line = fi.read()
    fi.close()

    fi = open('P02671.html', 'w')
    fi.write(line)
    fi.close()

    print 'done'


def Start():

##    ReadHIP()
##    GetUnprotID()
##    WriteUniprotIDList()
    ReadUniprotIDList()
    GetUniprot()
    
Start()    












    

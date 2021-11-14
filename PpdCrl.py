import urllib as UL
import os

LI = []
Linxx = []

fi = open('Linxx.txt', 'r')
rl = fi.readlines()
fi.close()

for ls in rl:
    ls = ls.strip()
    Linxx.append(ls)
       
    
    

def Get__single__pages():

    print 'total Linxx:', len(Linxx)
    
    for y in range(10339, 10435):
        ul = 'http://www.plasmaproteomedatabase.org/'+Linxx[y]
        fi = UL.urlopen(ul)
        uline = fi.read()
        fi.close()

        letter = str(y)
        dna = 'C:/Il/PlasmaProt/PlasmaProteomeData/SinglePages/'
        fna = dna + letter + '.html'
        fi = open(fna, 'w')
        fi.write(uline)
        fi.close()
        print letter, ': done'
        
#        print ul
    

    
            

def Write__linxx():
    
    print 'Writing:', len(LI), ' linxx'
    
    fi = open('Linxx.txt', 'w')
    
    for ls in LI:
        fi.write(ls)
    fi.close()
    print 'Write__linxx: done'    
        
def Get__linxx(fname):   

    dna = 'C:/Il/PlasmaProt/PlasmaProteomeData/StartPages/'
    fna = dna + fname
    fi = open(fna, 'r')
    line = fi.read()
    fi.close()


    asl = line.split('<a ')
    for al in asl:
        al = al.split('</a>')[0]
        
        if 'href="molecule_page?ppd_id=' in al:
            al = al[7:]
            ls = al.split('">')[0]+'\n'
            LI.append(ls)
    
    print 'Get__linxx', fname, ': done'
                

#Get__linxx('F')


def Get__all__linxx():

    flist = os.listdir('C:/Il/PlasmaProt/PlasmaProteomeData/StartPages/')
    for fname in flist:
        print fname
        Get__linxx(fname)
    

def Get__start__pages():
    fi = open('Letters.txt', 'r')
    ls = fi.read()
    fi.close()

    #ul = 'http://www.plasmaproteomedatabase.org/browse.html?Alphabet='
    LettersLI = ls.split('\t')
    for letter in LettersLI:
        letter = letter.strip()
        ul = 'http://www.plasmaproteomedatabase.org/browse.html?Alphabet='+ letter
        print ul 
        fi = UL.urlopen(ul)
        uline = fi.read()
        fi.close()

        dna = 'C:/Il/PlasmaProt/PlasmaProteomeData/StartPages/'
        fna = dna + letter + '.html'
        fi = open(fna, 'w')
        fi.write(uline)
        fi.close()
        print letter, 'done'
    



def Start():

##    Get__all__linxx()
##    Write__linxx()
    Get__single__pages()    

Start()    
























import os

flist = os.listdir('SinglePages')
#print flist[:10]

dna = 'C:/Il/PlasmaProt/PlasmaProteomeData/SinglePages/'

LI = []

def Write__concentrations():

    fi = open('Concentrations.csv', 'w')
    for sl in LI:
        ls = ';'.join(sl)+'\n'
        fi.write(ls)
        
    fi.close()       
        
    print 'Write__concentrations: done'
    

def Get__all():

    for y in range(len(flist)):
        fn = flist[y]
        value_line = Get__conc(fn)
        value = value_line[1]
        if value != 0:
            print value_line, ':', fn
            LI.append(value_line)


def Get__uniprot__inx(line):

    startpos = line.find('http://www.uniprot.org/uniprot/')
    line = line[startpos:]
    endpos = line.find('"')
    link = line[:endpos]
    inx = link.split('/')[-1]
    return inx
        
def Get__conc(fname):

    value = 0

    fna = dna + fname    
    
    fi = open(fna, 'r')
    line = fi.read()
    fi.close()

    unprot_inx = Get__uniprot__inx(line)

    sl = line.split('<table ')
#    print len(sl)

#    print fname
##    for el in enumerate(sl):
##        if 'not present' in el[1]:##'Protein concentration' in el[1]:
##            print el[0]
##    print ''
##    print '============================='
    if len(sl) < 42:
        value = 0
    else:
        if 'not present' in sl[41]:
            value = 0
        else:
            conc_fr = sl[41]
            tr_sl = conc_fr.split('<tr ')
    ##        print ''
    ##        print '============================='
    ##
    ##        print len(tr_sl)
            row = tr_sl[3]
            cells = row.split('<td ')
            conc_cell = cells[1]
            pos = conc_cell.find('>')
            conc_cell = conc_cell[(pos+1):]
            conc_cell = conc_cell.replace('</td>', '')
            conc_cell = conc_cell.replace('&nbsp;', '')
            conc_cell = conc_cell.strip()
            if '&mu;' in conc_cell:
                conc_cell = conc_cell.replace('&mu;', 'u')
            value = conc_cell
        
#    print value
    return [unprot_inx, value]

def Start():    
    #Get__conc('526.html')
    Get__all()
    Write__concentrations()

Start()


























import pickle as PI
import LightLinter as LL
import webbrowser
import tkFileDialog as TFD
import time
import os



TK = LL.TK

ProtNamesDI = {}
ExtraLI = []

ConcDI = {}

SetDI = {0:[], ## all prots
         1:[]
        # 2:[]
         }

OlDI = {0:[],
        1:[]
        }


fi = open('C:\\Il\\PlasmaProt\\Disease.li', 'rb')
DI = PI.load(fi)
fi.close()
print len(DI)


fi = open('C:\\Il\\PlasmaProt\\Protnames.txt', 'r')
rl = fi.readlines()
fi.close()

for ls in rl:
    ls = ls.strip()
    sl = ls.split(';')
    ProtNamesDI[sl[0]] = sl[1]

fi = open('C:\\Il\\PlasmaProt\\ExtraList.txt', 'r')
rl = fi.readlines()
fi.close()

for ls in rl:
    ls = ls.strip()
    ExtraLI.append(ls)


def Write__top__proteins():

    fi = open('TopProts.csv', 'w')
    sz = LL.TKDI['lx']['inxx'].size()
    for y in range(sz): ##sz):
        winx = LL.TKDI['lx']['inxx'].get(y)        
        dis_list = DI[winx]
        inci = len(dis_list)
        conc = ''
        if winx in ConcDI:
            conc = ConcDI[winx]
        if inci == 4:
            break
        #print winx
        for sl in dis_list:
            sl.insert(0, str(inci))
            prot_name = ProtNamesDI[winx]
            sl.insert(0, conc)
            sl.insert(0, prot_name)
            sl.insert(0, winx)
            ls = ';'.join(sl)+'\n'
            fi.write(ls)
            #print sl
##        print ''
##        print '========================'
      
    fi.close()
    print 'Write__top__proteins: done'

        


def Read__concentrations():

    fi = open('C:/Il/PlasmaProt/PlasmaProteomeData/Concentrations.csv', 'r')
    rl = fi.readlines()
    fi.close()

    for ls in rl:
        ls = ls.strip()
        sl = ls.split(';')
        ConcDI[sl[0]] = sl[1]       
        
    print 'Read__concentrations: done'


    

def Get__proteins__with__deficiency__disease():

    arr = [] 
    primer = 'deficiency'
    init_set =  'all'
    
    cur_set_inx = 2
    SetDI[cur_set_inx] = []
    
    #sz = LL.TKDI['lx']['inxx'].size()
    for y in range(len(SetDI[0])):
        uniprot_inx = SetDI[0][y]
        dis_list = DI[uniprot_inx]
        for dis_line in dis_list:
            disease = dis_line[1].lower()
            if primer in disease:
                arr.append(uniprot_inx)
                break
                
    arr.sort()
    print 'total:', len(arr), 'deficiency proteins'
    
    for uniprot_inx in arr:
        SetDI[cur_set_inx].append(uniprot_inx)
        
    Assign__protset(cur_set_inx)
    setline = init_set+'__'+primer
    LL.TKDI['lx']['protset'].insert(TK.END, setline)        
        

def Write__deficiency():

##    Get__proteins__with__deficiency__disease()    

    cs = 2
    setline = 'all__deficiency'

    prot_inxx = LL.TKDI['lx']['inxx'].get(0, TK.END)

    dna = LL.TKDI['en']['dna'].get()
    dna = dna.strip()
    if len(dna) < 2:
        dna = os.getcwd()
        LL.TKDI['en']['dna'].insert(0, dna)

    
    fn = setline+'.csv'
                
    LL.TKDI['en']['fna'].delete(0, TK.END)
    LL.TKDI['en']['fna'].insert(0, fn) 

    fna = dna +'/'+fn       
    fi = open(fna, 'w')
    for inx in prot_inxx:
        uniprot_link = 'http://www.uniprot.org/uniprot/'+inx            
        protname = ProtNamesDI[inx]
        
        extracell = 'no'
        if inx in SetDI[1]:
            extracell = 'yes'

        conc = ''
        if inx in ConcDI:
            conc = ConcDI[inx]
            
        sl = [uniprot_link, inx, conc, extracell, protname]
        dis_list = DI[inx]
        for dis_line in dis_list:
            disease = dis_line[1].lower()
            if 'deficiency' in disease:
                sl.append(disease)
                #break
        ls = ';'.join(sl)+'\n'        
        fi.write(ls)
        
    fi.close()
    
    print 'Write deficiency: done'      
            
    

def Save__protset():

    cs = LL.TKDI['lx']['protset'].curselection()
    if len(cs) == 0:
        print 'Please, select the set of proteins!'
    else:
        cs = int(cs[0])
        si = LL.TKDI['lx']['protset'].get(cs)                
        prot_inxx = LL.TKDI['lx']['inxx'].get(0, TK.END)

        dna = LL.TKDI['en']['dna'].get()
        dna = dna.strip()
        if len(dna) < 2:
            dna = os.getcwd()
            LL.TKDI['en']['dna'].insert(0, dna)

        
        fn = si+'.txt'
                    
        LL.TKDI['en']['fna'].delete(0, TK.END)
        LL.TKDI['en']['fna'].insert(0, fn) 

        fna = dna +'/'+fn        
        fi = open(fna, 'w')
        for inx in prot_inxx:
            inx += '\n'
            fi.write(inx)
            
        fi.close()
    
        print 'the set', si, 'was saved'      
        
    
    

def Get__timeline():

    LTI = time.localtime()
    timeline = str(LTI[0])+str(LTI[1])+str(LTI[3])+'_'+str(LTI[3])+str(LTI[4])+str(LTI[5])
    return timeline

def Write__session():

    ok = 0
    dna =  LL.TKDI['en']['dna'].get()
    dna =  dna.strip()
    if len(dna) < 2:
        print 'Please, select file directory!'
        ok = 1
    else:        
        fn =  LL.TKDI['en']['fna'].get()
        fn =  fn.strip()
        if len(fn) < 2:
            timeline = Get__timeline()
            fn =  'Plasma_proteins_'+timeline
            LL.TKDI['en']['fna'].delete(0, TK.END)
            LL.TKDI['en']['fna'].insert(0, fn) 
         
        
    if ok == 0:
        fna = dna+'/'+fn+'.li'
        fi = open(fna, 'w')
        DI = {}
        for k,v in SetDI.items():
            DI[k] = {}
            protset = LL.TKDI['lx']['protset'].get(k)
            DI[k]['protset'] = protset
            DI[k]['inxlist'] = v
            
        PI.dump(DI, fi)            
        fi.close()
    
    

def Select__file():

    fna = TFD.askopenfilename()
    fpath = fna.split('/')
    dna = '/'.join(fpath[:-1])
    fn = fpath[-1]
    LL.TKDI['en']['dna'].delete(0, TK.END)
    LL.TKDI['en']['dna'].insert(0, dna) 

    LL.TKDI['en']['fna'].delete(0, TK.END)
    LL.TKDI['en']['fna'].insert(0, fn) 
    

def Select__directory():

    dna = TFD.askdirectory()
    LL.TKDI['en']['dna'].delete(0, TK.END)
    LL.TKDI['en']['dna'].insert(0, dna) 

    

def Get__proteins__with__the__disease():

    arr = [] 
    primer = LL.TKDI['en']['disease'].get()
    primer = primer.lower()

    init_set =     LL.TKDI['en']['protset'].get()
    
    if len(primer) <= 2:
        print 'please, enter the disease (more than two letters)'
        
    elif len(primer) > 2:
        cur_set_inx = len(SetDI)
        SetDI[cur_set_inx] = []
        
        sz = LL.TKDI['lx']['inxx'].size()
        for y in range(sz):
            uniprot_inx = LL.TKDI['lx']['inxx'].get(y)
            dis_list = DI[uniprot_inx]
            for dis_line in dis_list:
                disease = dis_line[1].lower()
                if primer in disease:
                    arr.append(uniprot_inx)
                    break
                    
        arr.sort()
        print 'total:', len(arr), ' proteins that can trigger ', primer
        
        for uniprot_inx in arr:
            SetDI[cur_set_inx].append(uniprot_inx)
            
        Assign__protset(cur_set_inx)
        setline = init_set+'__'+primer
        LL.TKDI['lx']['protset'].insert(TK.END, setline)        
        
    

def Sort__protinxx():

    cs = int(LL.TKDI['lx']['protset'].curselection()[0])
    SetDI[cs] = []

    OlDI[1] = []
    sz = LL.TKDI['lx']['inxx'].size()
    for y in range(sz):
        k = LL.TKDI['lx']['inxx'].get(y)
        OlDI[1].append(k)

    OlDI[1].sort()
    
    for si in OlDI[1]:
        
        SetDI[cs].append(si)

    Assign__protset(cs)
        


def Ol__diseases():

    #lxname = 'protset'
    cs = int(LL.TKDI['lx']['protset'].curselection()[0])
    SetDI[cs] = []

    OlDI[0] = []
    sz = LL.TKDI['lx']['inxx'].size()
    for y in range(sz):
        k = LL.TKDI['lx']['inxx'].get(y)
        dis_list = DI[k]   
        inci = len(dis_list)
        ol = [inci, k]
        OlDI[0].append(ol)

    OlDI[0].sort()
    OlDI[0].reverse()
    
    LL.TKDI['lx']['inxx'].delete(0, TK.END)
    for ol in OlDI[0]:
        
        si = ol[1]
        SetDI[cs].append(si)
#        LL.TKDI['lx']['inxx'].insert(0, si)

    Assign__protset(cs)
        

def LimitToExtracell():

    sz = LL.TKDI['lx']['inxx'].size()
    for y in range(sz):
        si = LL.TKDI['lx']['inxx'].get(y)
        if si in ExtraLI:
            SetDI[1].append(si)

    print 'total: ', len(SetDI[1]), 'extracell. proteins'

    Assign__protset(1)            
    LL.TKDI['lx']['protset'].insert(TK.END, 'extracellular') 
    


def Create__frames():

    LL.Create__root('Plasma protein diseases')
    LL.Add__one__frame(0, 'root', 1, 1)
    LL.Add__one__frame(1, 'root', 2, 1)
    LL.Add__one__frame(2, 'root', 3, 1)

def Create__entries():

    #pass
    LL.TKDI['en']['dna'] = LL.TK.Entry(LL.TKDI['fr'][2])
    LL.TKDI['en']['dna'].grid(row = 1, column = 1)
    LL.TKDI['en']['dna']['width'] = 70

    LL.TKDI['bu']['dna'] = LL.TK.Button(LL.TKDI['fr'][2])
    LL.TKDI['bu']['dna'].grid(row = 1, column = 2)
    LL.TKDI['bu']['dna']['text'] = 'Select directory'
    LL.TKDI['bu']['dna']['command'] = Select__directory
    
    
    LL.TKDI['en']['fna'] = LL.TK.Entry(LL.TKDI['fr'][2])
    LL.TKDI['en']['fna'].grid(row = 2, column = 1)
    LL.TKDI['en']['fna']['width'] = 70

    LL.TKDI['bu']['fna'] = LL.TK.Button(LL.TKDI['fr'][2])
    LL.TKDI['bu']['fna'].grid(row = 2, column = 2)
    LL.TKDI['bu']['fna']['text'] = 'Select file'
    LL.TKDI['bu']['fna']['command'] = Select__file
    

def reflect__protset(event):
    
    lxname = 'protset'
    cs = int(LL.TKDI['lx'][lxname].curselection()[0])
    si = LL.TKDI['lx'][lxname].get(cs)
    LL.TKDI['en'][lxname].delete(0, TK.END)
    LL.TKDI['en'][lxname].insert(0, si)

    Assign__protset(cs)    
      

def reflect__inx(event):

    if LL.TKDI['lx']['inxx'].size() > 0:
        
        lxname = 'inxx'
        cs = int(LL.TKDI['lx'][lxname].curselection()[0])
        si = LL.TKDI['lx'][lxname].get(cs)
        LL.TKDI['en'][lxname].delete(0, TK.END)
        LL.TKDI['en'][lxname].insert(0, si)

        inx = si
        LL.TKDI['lx']['disease'].delete(0, TK.END)

        prot_name = ProtNamesDI[inx]
        LL.TKDI['tx'][0].delete('1.0', TK.END)
        LL.TKDI['tx'][0].insert(TK.END, prot_name)         
        
        
        dis_list = DI[si]## diseases list
        for dis_line in dis_list:
            ls = dis_line[1] ## disease
            LL.TKDI['lx']['disease'].insert(TK.END, ls)

def reflect__open__firefox(event):

    if LL.TKDI['lx']['inxx'].size() > 0:
        
        lxname = 'inxx'
        cs = int(LL.TKDI['lx'][lxname].curselection()[0])
        si = LL.TKDI['lx'][lxname].get(cs)
##        LL.TKDI['en'][lxname].delete(0, TK.END)
##        LL.TKDI['en'][lxname].insert(0, si)

        ul = 'http://www.uniprot.org/uniprot/'+si
        webbrowser.open_new(ul)
        
    
def Assign__protset(inx):
    
    array = SetDI[inx]
    LL.TKDI['lx']['inxx'].delete(0, TK.END)
    for si in array:               
        LL.TKDI['lx']['inxx'].insert(TK.END, si)            
    
    

def Create__lxx():

    LL.Add__lx('protset', 0, 1, 0, 30, 7, 'Arial 14')
    LL.TKDI['lx']['protset'].bind('<KeyRelease>', reflect__protset)
    LL.TKDI['lx']['protset'].bind('<ButtonRelease>', reflect__protset)

    LL.Add__lx('inxx', 0, 1, 1, 10, 7, 'Arial 14')
    LL.TKDI['la']['inxx']['text'] = 'Uniprot index'
        
    array = []
    for k, v in DI.items():
        if len(v) > 0:
            array.append(k)
            
    array.sort()
    for si in array:
        si = si.strip()
        if len(si) > 2:
            #LL.TKDI['lx']['inxx'].insert(TK.END, si)
            SetDI[0].append(si)

    Assign__protset(0)            
    LL.TKDI['lx']['protset'].insert(TK.END, 'all')
    print 'Total:', len(SetDI[0]), ' proteins'
    
    LL.TKDI['lx']['inxx'].bind('<KeyRelease>', reflect__inx)
    LL.TKDI['lx']['inxx'].bind('<ButtonRelease>', reflect__inx)

    LL.TKDI['lx']['inxx'].bind('<KeyPress-x>', reflect__open__firefox)    
    
    LL.Add__lx('disease', 0, 1, 2, 55, 7, 'Arial 17')
    LL.TKDI['en']['disease']['font'] = 'Arial 17'

def Create__Txx():

    LL.TKDI['tx'][0] = TK.Text(LL.TKDI['fr'][1])
    LL.TKDI['tx'][0].grid(row = 1, column = 1)
    LL.TKDI['tx'][0]['font'] = 'Courier 17 bold'
    LL.TKDI['tx'][0]['width'] = 70
    LL.TKDI['tx'][0]['height'] = 3
    
    
def Create__menu():

    LL.Create__menu()
####    TKDI['me'][0] = TK.Menu(TKDI['fr']['root'])
####    TKDI['me'][1] = TK.Menu(TKDI['me'][0])
##    LL.TKDI['me'][1].add_command(label = 'Limit to extracellular proteins', command = LimitToExtracell)
    LL.TKDI['me'][1].add_command(label = 'Get proteins with the disease', command = Get__proteins__with__the__disease)
    LL.TKDI['me'][1].add_separator()
    LL.TKDI['me'][1].add_command(label = 'Sort by amount of diseases', command = Ol__diseases)
    LL.TKDI['me'][1].add_command(label = 'Sort by Uniprot index', command = Sort__protinxx)

    LL.TKDI['me'][2] = TK.Menu(LL.TKDI['me'][0])
    LL.TKDI['me'][2].add_command(label = 'Save protein set', command = Save__protset)
    LL.TKDI['me'][2].add_command(label = 'Write deficiency subset', command = Write__deficiency)
    LL.TKDI['me'][2].add_command(label = 'Write__top__proteins', command = Write__top__proteins)

    
                      
##    LL.TKDI['me'][2].add_command(label = 'Write session', command = Write__session)

##Write__session
    
##TKDI['me'][1].add_command(label = 'Accept_block_content', command = Accept_block_content)


    LL.TKDI['me'][0].add_cascade(label = 'Data', menu = LL.TKDI['me'][2])
##
##    TKDI['fr']['root'].config(menu = TKDI['me'][0])
    
    

def Create__forms():

    Create__frames()
    Create__lxx()
    Create__Txx()
    Create__entries()
    Create__menu()

    
    

def Start():

    Create__forms()
    LimitToExtracell()
    Read__concentrations()
    Get__proteins__with__deficiency__disease()

    LL.TKDI['fr']['root'].mainloop()

Start()    

##for k, v in DI.items():
##	print k
##	print v
##	print '========'

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from array import array


def repeats(string):
    for x in range(0, len(string)):
        for y in range(x+1,len(string)):
            fstring=""
            sstring=""
            i=0
            while fstring==sstring and y+i<len(string):
                fstring=fstring+string[x+i]
                sstring=sstring+string[y+i]
                i=i+1
            if i>2:
                print("index:",x,",",y,", block:",fstring,",",sstring)
    print(string)

def separateV(string,n):
    ary=[[] ,[]]
    for i in range(len(string)):
        ary[i%n].append(string[i])
    return ary

def checkNum(ary):
    dict={}
    for i in ary:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    return dict

def coincidence(ary):
    dict=checkNum(ary)
    c=0
    for i in dict.keys():
        c=c+dict[i]*(dict[i])
    c=c/(len(ary)*(len(ary)))
    return c


freqList={"E": 12.02, "T" :9.10,"A" :8.12,"O": 7.68, "I" :7.31,
        "N": 6.95, "S" :6.28, "R":6.02,"H": 5.92,  "D": 4.32,
        "L" :3.98, "U": 2.88 ,"C" :2.71,"M" :2.61,"F" :2.30,
        "Y": 2.11,"W" :2.09, "G": 2.03,"P": 1.82,"B":1.49,
        "V": 1.11,"K": 0.69,"X" :0.17,"Q":0.11,"J": 0.10,"Z": 0.07}
def convert(c,k):
    return chr((ord(c)-65-k+26)%26+65)
def cor(dict, freqList,arylen):
    cor=999999
    k=-1
    for i in range(26):
        curcor=0
        llist=[]
        for j in dict.keys():
            curcor=curcor+((dict[j]/arylen)*100-freqList[convert(j,i)])**2
            llist.append(convert(j,i))
        for j in freqList.keys():
            if j not in llist:
                curcor=curcor+freqList[j]**2
        if curcor<cor:
            cor,k=curcor,i
    print("cor: ",cor,", k: ",k)
    return 0


ct="""
EDJCR HKDCP UPHPM YWLTM ONAQO TVKNM
EBAVK HJWPA LUWJI DUHTY WUNOC ACGCG"""
ct=ct.replace(" ","")
ct=ct.replace("\n","")
pt=""
for i in separateV(ct,2):
    print(coincidence(i))

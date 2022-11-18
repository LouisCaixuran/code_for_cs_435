import numpy
import math
from numpy import matrix
from numpy import linalg

def LFSR(start_state,taps):
  lfsr = start_state
  while len(bin(lfsr))<170:
    bit=0
    for i in taps:
      bit=bit^(lfsr >> (4-i)) & 1 
      
    bit = bit & 1  
    lfsr = (lfsr << 1) | bit
  return bin(lfsr),lfsr

def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=matrix(A)
  adj=numpy.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=numpy.array(A)
  minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

string="""1 1 1 0 1 0 1 0 1 1 0 0 1 0 0 1 1 1 1 0 0 1 0 1 1 0 1 0 1 1 0 0
0 0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0 0 1 1 0 0 1 1 1 0 0 0 1 0 0 1
1 0 1 0 1 0 0 1 0 1 0 1 1 0 1 0 1 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1
1 0 0 1 0 0 1 1 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 0 1 1 1 0
1 1 1 0 0 1 1 0 0 0 0 0 0 1 1 1 0 1 1 1 1 1 1 1 0 1 1 0 0 0 0 0
0 0 0 0 0 0 1 1"""
string=string.replace("\n"," ")
numberList=string.split(" ")
pm=0b0101000001001101
i=0

LFSR(0b10111,[0,2])
register=0
while(i<153):
  cipher=int(''.join(map(str, numberList[i:i+16])), 2)
  lsfrlist=bin(cipher^pm)
  n_list=[eval(j) for j in lsfrlist[2:]]
  A_list=[]
  B_list=[]
  for j in range(5):
    A_list.append(n_list[j:j+5])
    B_list.append([n_list[j+5]])
  A=numpy.matrix(A_list)
  try: 
    inverseA=modMatInv(A,2)
    B=numpy.matrix(B_list)
    C=numpy.matmul(inverseA, B)
    taps=[]
    for j in range(5):
      if C[j][0]%2==1:
        taps.append(j)
    
    lfsr,re=LFSR(int(lsfrlist[2:7], 2),taps)
    if lfsr[:len(lsfrlist)]==lsfrlist:
      print(i)
      print(lfsr)
      print(lsfrlist)
    if i==0:
      register=re
    i=i+8
  except ValueError:
    i=i+8


print(len(bin(register)))
cipher=int(''.join(map(str, numberList)), 2)
cipher_16=int(''.join(map(str, numberList[0:16])), 2)
plaintext=bin(register^cipher)
plaintext=plaintext[2:]
plaintext="0"+plaintext
text=""
for i in range(21):
  text=text+chr(int(plaintext[i*8:i*8+8],2))
print(text)
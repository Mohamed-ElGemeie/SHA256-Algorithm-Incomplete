#-----------------------------------------------
#Mohamed Galal ElGemeie 202000206
#CSCI-201 3A project SHA256 hashing algorithem
#-----------------------------------------------
import cmath
user_input=str(input("enter your data to be hashed: "))

#------------------------------------------------------------------------------------------------------------------------
def prime_founder(n):
    y = True
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            y = False
            break
    return (y, n)

#------------------------------------------------------------------------------------------------------------------------
def xor(*args):
    count= 0
    for i in range(len(args)):
        if len(args[i]) > count:
            count = len(args[i])
    lotuscream=[]
    for i in range(len(args)):
        if len(args[i])!=count:
            lotuscream.append(('0'*(count-len(args[i])))+ args[i])
        else:
            lotuscream.append(args[i])
    for i in range(len(lotuscream)-1):
        ans=''
        for g in range(len(lotuscream[i])):
            if lotuscream[i][g]==lotuscream[i+1][g]:
                ans+='0'
            else:
                ans+='1'
        lotuscream[i+1]=ans
    return(ans)

#------------------------------------------------------------------------------------------------------------------------
def SRROT(a,shift):
    ans=""
    a=str(a)
    a = list(a)
    for i in range(shift):
        a.insert(0,a[-1])
        a.pop(-1)
    ans=ans.join(a)
    return (ans)

#------------------------------------------------------------------------------------------------------------------------
def SR(a,shift):
    ans=""
    a=str(a)
    for i in range(shift):
        ans+="0"
    ans+=a[0:-shift:1]
    return (ans)

#------------------------------------------------------------------------------------------------------------------------
def donwshift1(*args):
    x=[]
    for i in range(len(args[0])):
        x.append(args[0][i])
    for i in range(len(x)-1,0,-1):
        x[i]=x[i-1]
    x[0]=''
    return (x)

#------------------------------------------------------------------------------------------------------------------------
def majority(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    ans = ""
    for i in range(0, len(a)):
        x=[]
        x.append(int(a[i]))
        x.append(int(b[i]))
        x.append(int(c[i]))
        if sum(x)>=2:
            ans+='1'
        else:
            ans+='0'
    return (ans)

#------------------------------------------------------------------------------------------------------------------------
def judge(a,b,c):
    a = str(a)
    b = str(b)
    c = str(c)
    ans=""
    for i in range(0,len(a)):
        if a[i]=='1':
            ans+=b[i]
        else:
            ans+=c[i]
    return (ans)

#------------------------------------------------------------------------------------------------------------------------
def addition_nomod(*args):
    c = str(args[0])
    for i in range(1,len(args)):
        c= bin(int(c,2)+int(args[i],2))
        c=str(c)
        c=c[2:]
    return (c)

#------------------------------------------------------------------------------------------------------------------------
def addition(*args):
    c = str(args[0])
    for i in range(1, len(args)):
        c = bin(int(c, 2) + int(args[i], 2))
        c = str(c)
        c = c[2:]
    while len(c) != 32:
        if len(c) < 32:
            c = "0" + c
        else:
            c = c[-32::1]
    return (c)

#-----------------------------------------------compound fuctions--------------------------------------------------------
def sigma_0(x):
    a=SRROT(x,7)
    b=SRROT(x,18)
    c=SR(x,3)
    x = xor(a, b, c)
    return (str(x))

def sigma_1(x):
    a=SRROT(x,17)
    b=SRROT(x,19)
    c=SR(x,10)
    x = xor(a,b,c)
    return (str(x))

def Sigma_0(x):
    a = SRROT(x, 2)
    b = SRROT(x, 13)
    c = SRROT(x, 22)
    x = xor(a,b,c)
    return (str(x))

def Sigma_1(x):
    a = SRROT(x, 6)
    b = SRROT(x, 11)
    c = SRROT(x, 25)
    x = xor(a,b,c)
    return (str(x))

#-----------------------------------------------turn input into binary---------------------------------------------------
binary_input=''
for i in bytearray(user_input, encoding ='utf-8'):
    binary_input+=''.join(format(i, '08b'))

#-----------------------------------------------save the binary length in a variable-------------------------------------
binary_input_len=binary_input

#-----------------------------------------------add 1 at the end of the binary interpetaion------------------------------
binary_input+="1"

#-----------------------------------------add zero until input data is divisible by 512 or 2^32--------------------------
while len(binary_input)%512!=0:
    binary_input+="0"

#-----------------------------------------------count len of input and replace with last 8 bits--------------------------
binary_input_len=bin(len(binary_input_len))
binary_input_len=binary_input_len[2:]
binary_input=binary_input[0:-len(binary_input_len)]
binary_input+=binary_input_len

#-----------------------------------------------initiliaze first 8 constants---------------------------------------------
prime_8=[2,3,5,7,11,13,17,19]
prime_8dic={'H0':""
    ,'H1':""
    ,'H2':""
    ,'H3':""
    ,'H4':""
    ,'H5':""
    ,'H6':""
    ,'H7':""}
for i in range(len(prime_8)):
    prime_8[i]=cmath.sqrt(prime_8[i])
    prime_8[i]=str(prime_8[i])
    prime_8[i]=prime_8[i][1:-4]
    prime_8[i]=float(prime_8[i])
    prime_8[i]=float(prime_8[i])-int(prime_8[i]) 
    prime_8[i]=prime_8[i]*(4294967296)
    prime_8[i]=int(prime_8[i])
    prime_8[i]=bin(prime_8[i])
    prime_8[i] = prime_8[i][2:]
    while len(prime_8[i]) < 32:
        prime_8[i]="0"+prime_8[i]
    prime_8dic["H{}".format(i)]+=prime_8[i]

#-----------------------------------------------count the first 64 prime numbers-----------------------------------------
prime_64=[]
n = 311
for i in range(2, n+1, 1):
    if prime_founder(i)[0]==True:
        prime_64.append(prime_founder(i)[1])

#-----------------------------------------------initilaize 64 prime constants--------------------------------------------
for i in range(len(prime_64)):
    prime_64[i]=pow(prime_64[i],1/3)
    prime_64[i]=str(prime_64[i])
    prime_64[i]=prime_64[i][1:-4]
    prime_64[i]=float(prime_64[i])
    prime_64[i]=float(prime_64[i])-int(prime_64[i])
    prime_64[i]=prime_64[i]*(4294967296)
    prime_64[i]=int(prime_64[i])
    prime_64[i]=bin(prime_64[i])
    prime_64[i] = prime_64[i][2:-1] + prime_64[i][-1]
    while len(prime_64[i]) != 32:
        if len(prime_64[i])<32:
            prime_64[i] = "0" + prime_64[i]
        else:
            prime_64[i] = prime_64[i][len(prime_64[i])-32:-1:1]+prime_64[i][-1]

#-----------------------------------------------sort the binary input into 64 words in a list----------------------------
bin_inp_word_list=[]
for i in range(len(binary_input)+1):
    if i%32==0:
        bin_inp_word_list.append(binary_input[i-32:i])
bin_inp_word_list=bin_inp_word_list[1:]
while len(bin_inp_word_list)%64!=0:
    bin_inp_word_list.append('00000000000000000000000000000000')

#-----------------------------------------------create message schedule--------------------------------------------------
for i in range(16,64):
    bin_inp_word_list[i]=addition(sigma_1(bin_inp_word_list[i-2]),bin_inp_word_list[i-7],sigma_0(bin_inp_word_list[i-15]),bin_inp_word_list[i-16])

#-----------------------------------------------shuffle the 8 constants with message schedule----------------------------
for i in range(64):
    Temp1=addition(Sigma_1(prime_8[4]),judge(prime_8[4],prime_8[5],prime_8[6]),prime_8[7],prime_64[i],bin_inp_word_list[i])
    Temp2=addition(Sigma_0(prime_8[0]),majority(prime_8[0],prime_8[1],prime_8[2]))
    prime_8=donwshift1(prime_8)
    prime_8[4]=addition(prime_8[4], Temp1)
    prime_8[0]=addition(Temp1,Temp2)
output=''
for i in range(len(prime_8)):
    prime_8[i]=addition(prime_8dic['H{}'.format(i)],prime_8[i])
    output+=hex(int(prime_8[i],2))[2:]
output=str(output)
print(output)

#-----------------------------------------------
#Mohamed Galal ElGemeie 202000206

#CSCI-201 3A project SHA256 hashing algorithem
#-----------------------------------------------

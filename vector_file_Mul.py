import random
random.seed(14)

s="radix 1 4 1 4 \nio i i i i\nvname B_d<4> B_d<[3:0]> A_d<4> A_d<[3:0]>\ntunit ns\nslope 0.005\nvih 1.0\nvil 0.0\ntrise 0.005\ntfall 0.005\n"
f1=open("Mul_golden.txt",mode='w')
f2=open("Vector_mul_final.vec",mode='w')

f1.write("A(DEC)\t")
f1.write("B(DEC)\t")
f1.write("PROD(DEC)\t")
f1.write("A(BIN)\t\t")
f1.write("B(BIN)\t\t")
f1.write("PROD(BIN)\n")

f2.write(s)
f2.write("\n")

def twoComp(a,len):
    return bin(a & (2**len-1)).replace("0b","")

t=0
for i in range(0,6):
    a=random.randint(-16,15)
    f1.write(f"{a}\t")
    b=random.randint(-16,15)
    f1.write(f"{b}\t")
    c=a*b
    f1.write(f"{c}\t\t")
    
    adc_a=str(twoComp(a,5))
    if(len(adc_a)<5):
        adc_a=(5-len(adc_a))*'0'+adc_a
        
    f1.write(adc_a)
    f1.write("\t\t")
    as1=(hex(int(adc_a[1:5], 2)).upper()).replace("0X","")
    
    adc_b=str(twoComp(b,5))
    if(len(adc_b)<5):
        adc_b=(5-len(adc_b))*'0'+adc_b
        
    f1.write(adc_b)
    f1.write("\t\t")
    as2=(hex(int(adc_b[1:5], 2)).upper()).replace("0X","")
    
    adc=str(twoComp(c,10))
    if(len(adc)<10):
        adc=(10-len(adc))*'0'+adc
    f1.write(adc)
    f1.write("\n")
    
    f2.write((f'{t} {adc_a[0]} {as1} {adc_b[0]} {as2}'))
    f2.write("\n")
    t+=4
    
f1.close()
f2.close()
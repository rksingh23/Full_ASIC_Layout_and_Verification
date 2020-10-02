import random
random.seed

s="radix 1 1 1\nio i i i\nvname A B C\ntunit ns\nslope 0.005\nvih 1.0\nvil 0.0\ntrise 0.005\ntfall 0.005\n"


f1=open("Add_golden_1bit.txt",mode='w')
f2=open("Vector_add_final_1bit.vec",mode='w')

f1.write("A(DEC)\t")
f1.write("B(DEC)\t")
f1.write("Cin(DEC)\t")
f1.write("SUM(DEC)\t")
f1.write("A(BIN)\t")
f1.write("B(BIN)\t")
f1.write("Cin(BIN)\t")
f1.write("SUM(BIN)\n")

f2.write(s)
f2.write("\n")
t=0

for i in range(0,12):
    a=random.randint(0,1)
    f1.write(f"{a}\t")
    b=random.randint(0,1)
    f1.write(f"{b}\t")
    cin=random.randint(0,1)
    f1.write(f"{cin}\t\t")
    c=a+b+cin
    f1.write(f"{c}\t\t")
    
    d=str(bin(a));
    fa=d.replace("0b", "");
    
    f1.write(f"{fa}")
    f1.write("\t")
    
    d=str(bin(b));
    fb=d.replace("0b", "");

    f1.write(f"{fb}")
    f1.write("\t")
    
    
    f1.write(f"{cin}")
    f1.write("\t\t")
    
    
    
    d=str(bin(c));
    fc=d.replace("0b", "");
    if(len(fc)<3):
        fc=(3-len(fc))*'0'+fc
    f1.write(f"{fc}")
    f1.write("\n")
    
    f2.write((f'{t} {a} {b} {cin}'))
    f2.write("\n")
    t+=2
f1.close()
f2.close()
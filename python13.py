import random
dna_seq = 'AATGCCGTAGCTGA'
x=random.randint(0,13)
print("First Mutation at position:",x)
a=random.randint(0,13)
print("Second Mutation at position :",a)
b=random.randint(0,13)
print("Third Mutation at position :",b)
c=random.randint(0,13)
print("Fourth Mutation at position :",c)
y=random.randint(1,4)
print(y)
if y==1:
    z='A'
    print(z)
elif y==2:
    z='T'
    print(z)
elif y==3:
    z='G'
    print(z)
elif y==4:
    z='C'
    print(z)
dna_seq = dna_seq[:x] + z + dna_seq[x+1:]
print(dna_seq)
dna_seq = dna_seq[:a] + z + dna_seq[a+1:]
print(dna_seq)
dna_seq = dna_seq[:b] + z + dna_seq[b+1:]
print(dna_seq)
dna_seq = dna_seq[:c] + z + dna_seq[c+1:]
print(dna_seq)

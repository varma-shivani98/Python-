seq='AATTTGGGCCTGTAGCGTAGCCAAAGGGTACGTTAATGCCTGATCGT'
countg=0
countc=0
for i in seq:
    if i=='G':
        countg+= 1
    if i=='C':
        countc+= 1
length = len(seq)
print("No.of G bases:",countg)
print("No.of C bases:",countc)
Total=countg+countc
percentage=(float(Total)/len(seq))*100
print("Total GC content in sequence : ",percentage, '\n')

seq='AATTTGGGCCTGTAGCGTAGCCAAAGGGTACGTTAATGCCTGATCGT'
counta=0
countt=0
countg=0
countc=0
for i in seq:
    if i== 'A':
        counta+= 1
    elif i== 'T':
        countt+= 1
    elif i=='G':
        countg+= 1
    elif i=='C':
        countc+= 1
length=len(seq)
per_a=(float(counta)/length) *100
per_t=(float(countt)/length) *100
per_g=(float(countg)/length) *100
per_c=(float(countc)/length) *100
print("Percentage of A bases:",per_a,'\n')
print("Percentage of T bases:",per_t,'\n')
print("Percentage of G bases:",per_g,'\n')
print("Percentage of C bases:",per_c,'\n')
print("Maximum frequency percentage of a base:",max(per_a,per_t,per_g,per_c),'\n')
print("Minimum frequency percentage of a base:",min(per_a,per_t,per_g,per_c,'\n'))

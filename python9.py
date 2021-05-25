seq='AATTTGGGCCTGTAGCGTAGCCAAAGGGTACGTTAATGCCTGATCGT'
print(seq)
mRNA=' '
for i in seq:
    if i=='A':
        j='T'
    elif i=='T':
        j='U'
    elif i=='G':
        j='C'
    elif i=='C':
        j='G'
    else:
        print("It is not a base")
    mRNA=mRNA+j
print(mRNA)

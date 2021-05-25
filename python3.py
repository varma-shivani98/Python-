seq='AATTTGGGCCTGTAGCGTAGCCAAAGGGTACGTTAATGCCTGATCGT'
print(seq)
compl_Dna=' '
for i in seq:
    if i=='A':
        j='T'
    elif i=='T':
        j='A'
    elif i=='G':
        j='C'
    elif i=='C':
        j='G'
    else:
        print("It is not a base")
    compl_Dna=compl_Dna+j
print(compl_Dna)

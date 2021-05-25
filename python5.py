seq='AATTTGGGCCTGTAGCGTAGCCAAAGGGTACGTTAATGCCTGATCGT'
countg = seq.count("G")
countc = seq.count("C")
print("No.of G bases:", countg ,'\n')
print("No.of C bases:", countc ,'\n')
Total=countg+countc
percentage=(Total/2)*100
print("Total GC percentage in sequence : ",percentage , '\n')

seq='AATTT- --GGGC  C-TGTAGCGT- -AGC--CA AAG GGTAC-G-T-T-A ATGC -CTGA--TC-G---T'
count=0
for i in seq:
    if i == '-' or i == ' ':
        count+= 1
print("No.of gaps:",count , '\n')

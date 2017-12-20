# Using python, calculate and print a table 
# for the capability of integers using 1, 2, 4, and 8 bytes of storage
T="{:<6} {:<22} {:<22} {:<22}"
print(T.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
for bytes in range(1,9):
    bits=8*bytes
    size=2**bits-1
    min_si = -2**(bits-1)
    max_si = 2**(bits-1) -1
    print(T.format(bytes,size,min_si,max_si))
  
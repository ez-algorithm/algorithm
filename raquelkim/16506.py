import sys
n = int(sys.stdin.readline())
assem = [list(input().split()) for _ in range(n)]

code = {'ADD' : 0, 'SUB' : 1, 'MOV' : 2, \
        'AND' : 3, 'OR' : 4, 'NOT' : 5, 'MULT' : 6, \
        'LSFTL' : 7, 'LSFTR' : 8, 'ASFTR' : 9,\
        'RL' : 10, 'RR' : 11 }

result = []
for op, rd, ra, rb in assem:
    sen = ""
    if op[-1] == "C":
        sen += bin(code[op[:-1]])[2:].zfill(4)
        sen += "10"
    else:
        sen += bin(code[op])[2:].zfill(4)
        sen += "00" 
    sen += bin(int(rd))[2:].zfill(3)
    sen += bin(int(ra))[2:].zfill(3)

    if op[-1] == "C":
        sen += bin(int(rb))[2:].zfill(4)
    else:
        sen += bin(int(rb))[2:].zfill(3)
        sen += "0"
    result.append(sen)

for i in range(n):
    print(result[i])


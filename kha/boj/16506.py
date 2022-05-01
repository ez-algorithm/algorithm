#기본형 opcode
opcode_list = ["ADD", "SUB", "MOV", "AND", "OR", "NOT", "MULT", "LSFTL", "LSFTR", "ASFTR", "RL", "RR"]

def operationToBinary(opcode: str, ctype: bool, rd: int, r1: int, r2: int):

    result = ""

    #1. opcode -> binary
    result += "{:0>4b}".format(opcode_list.index(opcode))
    if ctype:
        result += "10"
    else:
        result  += "00"

    #2. rD -> binary
    result += "{:0>3b}".format(rd)

    #3. rA -> binary
    result += "{:0>3b}".format(r1)

    #4. rB or C -> binary
    if ctype:
        result += "{:0>4b}".format(r2)
    else:
        result += "{:0>3b}".format(r2) + "0"
    
    return result


N = int(input())

for _ in range(N):
    op, rd, r1, r2 = map(str, input().split())

    if op[-1] == 'C':
        print(operationToBinary(op[:-1], True, int(rd), int(r1), int(r2)))
    else:
        print(operationToBinary(op, False, int(rd), int(r1), int(r2)))

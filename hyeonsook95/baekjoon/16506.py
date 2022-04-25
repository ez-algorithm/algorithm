import sys

input = sys.stdin.readline

commands = {
    "ADD": "0000",
    "SUB": "0001",
    "MOV": "0010",
    "AND": "0011",
    "OR": "0100",
    "NOT": "0101",
    "MULT": "0110",
    "LSFTL": "0111",
    "LSFTR": "1000",
    "ASFTR": "1001",
    "RL": "1010",
    "RR": "1011",
}

N = int(input().strip())

for _ in range(N):
    opcode, rD, rA, rB = input().strip().split()

    b_opcode = "0"
    b_rD = bin(int(rD))[2:].rjust(3, "0")
    b_rA = bin(int(rA))[2:].rjust(3, "0")
    b_rB = bin(int(rB))[2:].rjust(3, "0") + "0"

    if opcode[-1] == "C":
        opcode = opcode[:-1]
        b_opcode = "1"
        b_rB = bin(int(rB))[2:].rjust(4, "0")

    b_opcode = commands[opcode] + b_opcode

    print(b_opcode + "0" + b_rD + b_rA + b_rB)

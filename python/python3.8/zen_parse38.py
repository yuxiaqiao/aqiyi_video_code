# python3.8
#  Assignment expressions

with open('zen.txt', 'r') as f:
    while line:=f.readline():
        print(line.upper(), end='')
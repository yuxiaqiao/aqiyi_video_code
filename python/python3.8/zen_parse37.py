# python3.7
with open('zen.txt', 'r') as f:
    while True:
        line=f.readline()
        if line:
            print(line.upper(), end='')
        else:
            break
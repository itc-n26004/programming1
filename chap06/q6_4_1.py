%%time
with open('some.txt', 'r') as f:
    for c, l in enumerate(f):
        print(l, end='')
        if c==2:
            break 

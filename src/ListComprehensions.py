# List Comprehensions 
# 

def raw_input():
    return 2

if __name__ == '__main__':    
    # initialization example

    x, y, z, n = (int(raw_input()) for _ in range(4))
    x, y, z, n = 1, 1, 1, 2

    print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c!=n])
import textwrap

def wrap(string, max_width):
    return "\n".join([string[i: i+max_width] for i in range(0,len(string), max_width)])

def wrap2(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4
    result = wrap(string, max_width)
    print(result)
    result = wrap2(string, max_width)
    print(result)
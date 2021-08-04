number = 17
width = len("{0:b}".format(number))

print("{}\t{}\t{}\t{}".format('Decimal','Octal', 'Hex', 'Binary'))
for i in range(1,number+1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
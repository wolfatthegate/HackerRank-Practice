def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return ''.join(string)

def mutate_string2(string, position, character):
    return string[:position]+ character+string[position+1: ]

print(mutate_string('Sarah', 4, 'a'))
print(mutate_string2('Sarah', 4, 'a'))
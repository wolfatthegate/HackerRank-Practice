def swap_case(s):
    news = ''
    for p in range(len(s)):
        if s[p].isupper(): 
            news += s[p].lower()
        else: 
            news += s[p].upper()
    return news


print(swap_case('White Walker'))
print('White Walker'.swapcase())
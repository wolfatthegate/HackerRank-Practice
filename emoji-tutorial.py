''' https://stackoverflow.com/questions/47716217/converting-emojis-to-unicode-and-vice-versa-in-python-3 '''

s = '😀'
print(f'U+{ord(s):X}')
t = s.encode('unicode-escape').decode('ASCII')
if t == '\\U0001f600':
    print('happy')
    
s = '😀'
print(s.encode('unicode-escape'))
print(s.encode('unicode-escape').decode('ASCII'))

sentence = "Head-Up Displays (HUD)💻 for #automotive🚗 sector\nThe #UK-based #startup🚀 Envisics got €42 million #funding💰 from l… "
print("normal sentence - ", sentence)

uc_sentence = sentence.encode('unicode-escape')
print("\nunicode represented sentence - ", uc_sentence)

decoded_sentence = uc_sentence.decode('unicode-escape')
print("\ndecoded sentence - ", decoded_sentence)
import re

emoji_pattern = re.compile("["
                        u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                    u"\U00002702-\U000027B0"
                    u"\U000024C2-\U0001F251"
                    u"\U0001f926-\U0001f937"
                    u'\U00010000-\U0010ffff'
                    u"\u200d"
                    u"\u2640-\u2642"
                    u"\u2600-\u2B55"
                    u"\u23cf"
                    u"\u23e9"
                    u"\u231a"
                    u"\u3030"
                    u"\ufe0f"
        "]+")

emoji_dict = {'\\U0001f4bb': 'Laptop', 
              '\\U0001f697': 'car', 
              '\\U0001f680': 'rocket', 
              '\\U0001f4b0': 'money', 
              '\\U0001f489': 'syringe', 
              '\\U0001f48a': 'pill'}

def listEmoji(sentence, unicodePrint):
    print("Original sentence - ", sentence)
    
    if unicodePrint == True: 
        uc_sentence = sentence.encode('unicode-escape')
        print("\nUnicode represented sentence - ", uc_sentence)
    
    emoji_list = emoji_pattern.findall(sentence)   
    print('\nEmoji List: ', emoji_list)
    
    for emoji in emoji_list: 
        print(emoji + ' -> ' + emoji_dict[emoji.encode('unicode-escape').decode('ASCII')])
        sentence = sentence.replace(emoji, '[' + emoji_dict[emoji.encode('unicode-escape').decode('ASCII')] + ']')
        
    print('\n', sentence, '\n')
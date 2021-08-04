'''
Find the second lowest scores and sort the name alphabetically. 

Sample Input 0

5

Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
'''


sheet = [['Harry', 37.21],['Berry', 37.21],['Tina', 37.2],['Akriti', 41],['Harsh', 39]]
scoresheet = [37.21, 37.21, 37.2, 41, 39]
name = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']

scoresheet = list(set(scoresheet))
scoresheet.remove(min(scoresheet))
sec_lowest = min(scoresheet)

print('\n'.join(sorted([a for a,b in sheet if b == sec_lowest])))
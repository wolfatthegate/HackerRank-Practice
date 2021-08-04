def count_substring(string, sub_string):
    count = 0
    for _ in range(0, len(string)-len(sub_string)+1):
        if string[_:_+len(sub_string)] == sub_string:
            count += 1
    
    return count



print(count_substring('ABCDCDC', 'CDC'))
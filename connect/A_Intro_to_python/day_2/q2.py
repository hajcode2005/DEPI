def compress_string(s):
    result = ""          
    count = 1          
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1   
        else:
            result += s[i] + str(count)  
            count = 1    
    result += s[-1] + str(count)
    return result
print(compress_string("aaabccddda"))  
print(compress_string("abc"))        
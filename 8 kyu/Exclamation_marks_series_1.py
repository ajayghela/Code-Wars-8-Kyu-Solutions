#Description:
#Remove an exclamation mark from the end of a string. 
# For a beginner kata, you can assume that the input data is always a string, no need to verify it.

#Examples:
#remove("Hi!") === "Hi"

# confirm if the string contains an "!" and if the last character is a "!"
#delete if it's a '!'


s= "!Hi!"
if s and s[-1] == "!" :
    x = s[:-1]
        print(x)
    else:
        print(s)

def remove(s):
    return s[:-1] if s and s[-1] == '!' else s

s = "!Hi!"
if s.endswith('!'): 
    x = s[:-1] 
        print(x)        
    else:
        print(s)

def remove(s):
    return s[:-1] if s.endswith('!') else s 

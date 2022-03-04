#Description:
#Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

#Examples
#remove("Hi!") === "Hi!"
#remove("Hi!!!") === "Hi!"
#remove("!Hi") === "Hi!"
#remove("!Hi!") === "Hi!"
#remove("Hi! Hi!") === "Hi Hi!"
#remove("Hi") === "Hi!"

# remove all '!' and concatenate '!' to the end
s = ("Hi! Hi!")
x = s.replace('!', '') + '!'
print(x)

def remove(s):
    return s.replace('!', '') + '!'


#Description:
# Remove all exclamation marks from the end of sentence.

#Examples:
#remove("Hi!!!") === "Hi"

#while the end character is a !
#or use  rstrip('!')

s = "Hi!!!"
while s[-1] == "!":
    s = s[:-1]
print(s)

def remove(s):
    return s.rstrip("!")


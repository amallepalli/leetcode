def isAnagram(s: str, t: str) -> bool:
    sdict = {}
    for char in s:
        if (sdict.get(char) != None):
            sdict[char] += 1
        else:
            sdict[char] = 1
    
    tdict = {}
    for char in t:
        if (tdict.get(char) != None):
            tdict[char] += 1
        else:
            tdict[char] = 1
    for x in sdict:
        if (sdict.get(x) != tdict.get(x)):
            return False
    for x in tdict:
        if (sdict.get(x) != tdict.get(x)):
            return False
    return True

s = "xx"
t = "x"
print(isAnagram(s, t))
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    sorted_strs = [0] * len(strs)
    for i in range(len(strs)):
        sorted_strs[i] = "".join(sorted(strs[i]))
    thisdict = {}
    for i in range(len(strs)):
        thisdict.setdefault(sorted_strs[i], []).append(strs[i])
    final_array = []
    for x,y in thisdict.items():
        final_array.append(y)
    return final_array

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs=strs))
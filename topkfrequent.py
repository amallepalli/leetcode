def topKFrequent(nums, k):
    thisdict = {}
    for x in nums:
        if thisdict.get(x) != None:
            thisdict[x] += 1
        else:
            thisdict[x] = 1
    list = sorted(thisdict.items(), key=lambda item: item[1], reverse=True)
    final_list = list[:k]
    final_list = [x[0] for x in final_list]
    return final_list

nums = [7, 7]
k = 1
print(topKFrequent(nums, k))
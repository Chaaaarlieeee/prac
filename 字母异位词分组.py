from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs:list[str]):
        groups=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            print(sorted(s))
            groups[key].append(s)
        return list(groups.values())

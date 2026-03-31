class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sort = sorted(s)
            sorted_str = "".join(sort)
            d[sorted_str].append(s)
        result = [x for x in d.values()]
        return result
    
        


        
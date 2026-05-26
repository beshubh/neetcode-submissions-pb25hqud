class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        source_chars = set(source)
        for c in target:
            if c not in source_chars:
                return -1
        
        source_itr = 0
        subsequences = 0 
        for char in target:
            if source_itr == 0:
                subsequences += 1
            while source[source_itr] != char:

                source_itr = (source_itr + 1) % len(source)
                if source_itr == 0:
                    subsequences += 1 # we need some other extra subseqeuence
            source_itr = (source_itr + 1) % len(source)
                
        return subsequences

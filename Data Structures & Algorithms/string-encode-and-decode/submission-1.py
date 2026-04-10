from io import StringIO

class Solution:

    def encode(self, strs: List[str]) -> str:
        str_len = len(strs)
        res = StringIO()
        res.write("*") # list encode
        res.write(str(str_len))
        for s in strs:
            res.write("+")
            res.write(str(len(s)))
            res.write('-')
            res.write(s)
        return res.getvalue()
    

    def get_num(self, i: int, s: str) -> tuple[int, int]:
        slen = ''
        while i < len(s):
            if not s[i].isdigit(): # what if string is the number itself?
                break
            slen += s[i]
            i += 1
        slen = int(slen)
        return slen, i
    
    def decode(self, s: str) -> List[str]:
        print('dec s', s)
        if s[0] != '*':
            raise ValueError('s should be a list')
        idx = 1 # move 1 place over to skip *
        slen = len(s)
        strs_len, idx = self.get_num(idx, s)
        idx += 1 # move over + so next will be the character of string

        strs_found = 0
        res: list[str] = []
        while strs_found < strs_len:
            str_len, idx = self.get_num(idx, s)
            res.append(s[idx + 1:idx + 1 + str_len])
            strs_found += 1
            idx = 1 + idx + str_len + 1 # +1 for skipping +
        return res


def take(n: int, s: str) -> str:
    r = s[:n]
    return r


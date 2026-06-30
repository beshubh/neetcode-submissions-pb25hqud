class Solution:

    def distribute_spaces(self, s: str, ns: int) -> str:
        spaces = len(s.split()) - 1
        if spaces == 0:
            return s + ' ' * ns
        sd = ns // spaces
        remaining = ns % spaces
        output = ''
        parts = s.split()
        print('parts: ', parts)
        print('spaces: ', spaces)
        print('num of spaces: ', ns)
        print('sd: ', sd)
        print('extra: ', remaining)
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                output += part
                continue
            output += part + ' ' + ' '*sd
            if remaining > 0:
                output += ' '
                remaining -= 1
        return output

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        buf = ""
        output = []
        for i, s in enumerate(words):
            if len(buf) + len(s) + 1 <= maxWidth:
                if not buf:
                    buf = s
                else:
                    buf += ' ' + s
            else:
                ns = maxWidth - len(buf)
                print('buf before: ', buf, len(buf))
                output.append(self.distribute_spaces(buf, ns))
                buf = s
        if buf:
            output.append(buf + ' ' * (maxWidth - len(buf)))
        return output

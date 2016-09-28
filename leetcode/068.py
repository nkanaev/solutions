class Solution(object):
    def fullJustify(self, words, maxWidth):
        lines = []
        line = []
        total_length = 0
        for w in words:
            if total_length + len(w) + len(line) <= maxWidth:
                line.append(w)
                total_length += len(w)
            else:
                lines.append(line)
                total_length = len(w)
                line = [w]
        if line:
            lines.append(line)
        return [
            self.justifyline(l, maxWidth, i == len(lines)-1) 
            for i, l in enumerate(lines)
        ]

    def justifyline(self, words, width, is_last=False):
        extra = width - sum(map(len, words))
        if len(words) == 1:
            return words[0] + (' ' * extra)
        if is_last:
            return ' '.join(words) + (' ' * (extra - len(words) + 1))
        line = ''
        space_length = extra / (len(words) - 1)
        rem = extra % (len(words) - 1)
        for i in xrange(len(words)-1):
            l = space_length + int(i < rem)
            line += words[i] + (' ' * l)
        line += words[-1]
        return line

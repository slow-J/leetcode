class Solution:

    def makeGood(self, s):
        if len(s) < 2:
            return s
        lists = list(s)
        done = False
        i = 0
        while not done:
            if (lists[i].lower() == lists[i + 1].lower() and
                    (lists[i].isupper() and lists[i + 1].islower() or lists[i].islower() and lists[i + 1].isupper())):
                lists.pop(i + 1)
                lists.pop(i)
                i = 0
            else:
                i += 1

            if i >= len(lists) - 1:
                done = True

        return ''.join(lists)

class Solution:
    # def lemonadeChange(self, bills: List[int]) -> bool:
    def lemonadeChange(self, bills):
        purse = {5: 0, 10: 0}
        for amount_paid in bills:
            if amount_paid == 5:
                purse[5] += 1
            elif amount_paid == 10:
                if purse[5] > 0:
                    purse[5] -= 1
                    purse[10] += 1
                else:
                    return False
            elif amount_paid == 20:
                if purse[5] > 0 and purse[10] > 0:
                    purse[5] -= 1
                    purse[10] -= 1
                elif purse[5] > 2:
                    purse[5] -= 3
                else:
                    return False
        return True

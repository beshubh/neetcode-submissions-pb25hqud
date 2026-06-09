class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        score = defaultdict(int)
        for f, t, a in transactions:
            score[f] -= a
            score[t] += a
        
        debtors = [val for val in score.values() if val > 0]
        lenders = [val for val in score.values() if val < 0]

        def backtrack(debtors, lenders):
            # debt to be paid
            if len(debtors) + len(lenders) == 0:
                return 0
            debt = debtors[0]
            count = math.inf
            for lent_amount in lenders:
                new_debtors = debtors.copy()
                new_lenders = lenders.copy()

                # remove this debt and lend
                new_debtors.remove(debt)
                new_lenders.remove(lent_amount)

                if debt == -lent_amount:
                    # debt needs to be paid is exactly as lent amount, best case
                    # no need to do anything
                    pass
                elif debt > -lent_amount:
                    # debt is more than the lent amount
                    # pay this much debt, and add remaining to the new_debt
                    new_debtors.append(debt + lent_amount)
                else:
                    # debt is less than the lent amount
                    # pay this much debt and add remaining to the new_lent
                    new_lenders.append(debt + lent_amount)
                count = min(count, 1 + backtrack(new_debtors, new_lenders))
            return count
        return backtrack(debtors, lenders)


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for num in coins:
            for i in range(1, len(dp)):
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[amount]

'''
let amount = 4, coins = [1, 2]

for i in range(1, len(dp)):
    for num in coins:
        i = 1, 2, 3, 4
        coins = 1, 2
        (1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2)...
        0: set with empty set
        1: {{1}}
        2: {{2}, {1, 1}}
        3: {{1, 2}, {2, 1}, {1, 1, 1}} -- allows for duplicates

for num in coins:
    for i in range(1, len(dp)):
        num = 1, 2
        i = 1, 2, 3, 4
        (num, i): (1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4)
        0: set with empty set
        1: {{1}}
        2: {{1, 1}}
        
'''

        # Run Time: O(n*k), Space Complexity: O(n)
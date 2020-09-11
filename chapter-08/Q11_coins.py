def change_possibilities(amount, denominations):
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for coin in denominations:
        for curr_amount in range(coin, amount + 1):
            dp[curr_amount] += dp[curr_amount - coin]

    return dp[-1]

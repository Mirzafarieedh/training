    ans = 0
        mp = float('inf') #mp=min_price
        for i in prices:
            if i < mp:
                mp = i
            elif i - mp > ans:
                ans = i-mp
        return ans
        
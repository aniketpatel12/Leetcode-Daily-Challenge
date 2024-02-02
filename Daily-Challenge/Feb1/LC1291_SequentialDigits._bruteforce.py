'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
----------
Input: low = 100, high = 300
Output: [123,234]

Example 2:
----------
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

'''
def sequentialDigits(self, low: int, high: int) -> List[int]:
        # BRUTE-FORCE solution:
        
        def chechSequentialNumber(num):
            strNum = str(num)
            for i in range(len(strNum)-1):
                if int(strNum[i]) + 1 != int(strNum[i+1]):
                    return False
            return True
        
        ans = []
        for num in range(low, high):
            res = chechSequentialNumber(num)
            if res:
                ans.append(num)
        return ans

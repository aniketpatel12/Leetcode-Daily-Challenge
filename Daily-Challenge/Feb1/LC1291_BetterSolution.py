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
        lowDigit = len(str(low))
        highDigit = len(str(high))
        ans = []

        for digit in range(lowDigit, highDigit+1):
            for start in range(1, 9):
                if digit + start > 10:
                    break
                
                num = start # 1
                prev = start # 1

                for i in range(digit - 1):
                    num = num*10         # 1 * 10 = 10
                    prev += 1            # 1 + 1 = 2
                    num += prev          # 10 + 2 = 12
                if low <= num <= high:   # 10 < 12 < 20
                    ans.append(num) 
        return ans
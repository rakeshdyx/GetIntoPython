## Loop Through List

class Solution:
    def highScore(self, student_score: list) -> int:
        score = 0
        for i in student_score:
            if i > score:
                score = i
        return score
    
highest_score = Solution()
x = highest_score.highScore([78, 65, 89, 86, 55, 91, 64, 89])

print(f"The highest score in the class is: {x}")

## Loop Through Range()

class Solution:
    def evenNumberSum(self) -> int:
        sum = 0
        for i in range(1, 101):
            if i % 2 == 0:
                sum += i
        return sum

sumOfEvens = Solution()
print(sumOfEvens.evenNumberSum())


    
    
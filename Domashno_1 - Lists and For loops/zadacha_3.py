words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]
palindromes = []

for i in range(len(words)):
    left = 0
    right = len(words[i]) - 1
    is_palindrome = True
    while left < right:
        if words[i][left] != words[i][right]:
            is_pal = False
            break
        left += 1
        right -= 1
    if is_palindrome:
        palindromes.append(words[i])

print("Palindromes:")
for num in palindromes:
    print(num)
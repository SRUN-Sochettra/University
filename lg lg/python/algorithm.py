# Print Hello N times
# N=int(input("Input the Number: "))
# for i in range(1,N+1):
#     print("Hello")
# print()

# Print the second largest number
# A = [12, 35, 1, 10, 34, 1, 1, 33, 12]
# A.sort()
# print("The second largest number is:", A[-2])

# Print Unique Elements in a List
# A = [12, 35, 1, 10, 34, 1, 1, 33, 12]
# unique_elements = list(set(A))
# print(unique_elements)
# B = len(unique_elements)
# print("The number of unique elements is:", B)

# Print the sum of 2 numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("The sum of", num1, "and", num2, "is", num1 + num2)

# Print the sum of a list
# A = [1, 2, 3, 4, 5]
# print("The sum of the list is:", sum(A))

# Print the maximum element
# A = [12, 35, 1, 10, 34, 1, 1, 33, 12]
# print("The maximum element is:", max(A))

# Print the count even and odd
# A = [12, 35, 1, 10, 34, 1, 1, 33, 12]
# even_count = 0
# odd_count = 0
# for num in A:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("The number of even numbers is:", even_count)
# print("The number of odd numbers is:", odd_count)

# Print the reverse of a string
# str1 = input("Enter a string: ")
# print("The reverse of the string is:", str1[::-1])

# Print the Palindrome Check
# str1 = input("Enter a string: ")
# if str1 == str1[::-1]:    
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")

# Print the character frequency
# str1 = input("Enter a string: ")
# char_freq = {}
# for char in str1:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1
# print("The character frequency is:", char_freq)

# Print the swap of two numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("The swap of", num1, "and", num2, "is", num2, "and", num1)

# Print the check of leap year
# year = int(input("Enter a year: "))    
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("The year is a leap year")
# else:
#     print("The year is not a leap year")

# Print the check of even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# Print the comparation of two numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print("The first number is greater than the second number")
# elif num1 < num2:
#     print("The first number is less than the second number")
# else:
#     print("The first number is equal to the second number")

# Print the factorial of a number
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("The factorial of", num, "is", factorial)

# Print the Fibonacci series
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# Print 1 to N
# N = int(input("Enter a number: "))
# for i in range(1, N + 1):
#     print(i, end=" ")

# Print N to 1
# N = int(input("Enter a number: "))    
# for i in range(N, 0, -1):
#     print(i, end=" ")

# Print the sum of the first N numbers
# N = int(input("Enter a number: "))
# sum = 0
# for i in range(1, N + 1):
#     sum += i
# print("The sum of the first", N, "numbers is", sum)

# Print the multiplication table
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# Print the maximum in an array
# A = [12, 35, 1, 10, 34, 1, 1, 33, 12]
# max_element = max(A)
# print("The maximum element is:", max_element)

# Print the reversed array
# A = [12, 35, 1, 10, 34, 1, 1, 33, 12]
# reversed_A = A[::-1]
# print("The reversed array is:", reversed_A)

# Print the count of the posivive and negative numbers
# A = [12, -35, 1, -10, 34, -1, 1, -33, 12]
# positive_count = sum(1 for x in A if x > 0)
# negative_count = sum(1 for x in A if x < 0)
# print("The positive count is:", positive_count)
# print("The negative count is:", negative_count)

# Print the vowels count in a string
# str1 = input("Enter a string: ")
# vowels = set("aeiou")
# count = sum(1 for ch in str1.lower() if ch in vowels)
# print("The number of vowels in the string is:", count)

# Print GCD and LCM of two numbers
# import math
# num1 = int(input("Enter first number: "))    
# num2 = int(input("Enter second number: "))
# gcd = math.gcd(num1, num2)
# lcm = (num1 * num2) // gcd
# print("The GCD of", num1, "and", num2, "is", gcd)
# print("The LCM of", num1, "and", num2, "is", lcm)

# Print the prime number check
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("The number is not prime")
#             break
#     else:
#         print("The number is prime")
# else:
#     print("The number is not prime")

# Print the sum of digits of a number
# num = int(input("Enter a number: "))
# original = num
# digit_sum = 0
# num = abs(num)
# while num > 0:
#     digit_sum += num % 10
#     num //= 10
# print("The sum of digits of", original, "is", digit_sum)

# Print a equilateral triangle of stars
# N = int(input("Enter the number of rows: "))
# for i in range(1, N + 1):
#     print(" " * (N - i) + "*" * (2 * i - 1))

# Print a square of numbers
# N = int(input("Enter the size of the square: "))
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         print(i * j, end=" ")
#     print()

# Print the array digit sum
# A = [12, 35, 1, 10, 34, 1, 1, 33, 12]
# digit_sum = 0
# for number in A:
#     temp = abs(number)
#     while temp > 0:
#         digit_sum += temp % 10
#         temp //= 10
# print("The digit sum of the array is:", digit_sum)

# Print the array sum
# A = [12, 35, 1, 10, 34, 1, 1, 33, 12]
# sum = 0
# for number in A:
#     sum += number
# print("The sum of the array is:", sum)

# Print the second smallest number
# A = [12, 35, 1, 10, 34, 1, 1, 33, 12]
# A.sort()
# print("The second smallest number is:", A[1])

# Print the Armstrong number check
# num = int(input("Enter a number: "))
# original = num
# digit_sum = 0
# while num > 0:
#     digit = num % 10
#     digit_sum += digit ** 3
#     num //= 10
# if original == digit_sum:
#     print("The number is an Armstrong number")
# else:
#     print("The number is not an Armstrong number")

# Print the if the brackets are balanced
# def are_brackets_balanced(expr: str) -> bool:
#     if not isinstance(expr, str):
#         raise TypeError("Expression must be a string")
        
#     stack = []
#     for ch in expr:
#         if ch == '(':
#             stack.append(ch)
#         elif ch == ')' and (not stack or stack.pop() != '('):
#             return False
#     return not stack

# Print the majority check
# def is_majority_element(arr: list, candidate: int) -> bool:
#     if not isinstance(arr, list):
#         raise TypeError("Array must be a list")
#     if not isinstance(candidate, int):
#         raise TypeError("Candidate must be an integer")
#     if not arr:
#         return False
    
#     count = sum(1 for num in arr if num == candidate)
#     return count > len(arr) // 2
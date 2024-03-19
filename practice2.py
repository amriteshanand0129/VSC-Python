# r = {4: 12,5: 52,6: 162,7:0,8:13458,9:45228}
# print(r[int(input().strip())])


# import math
# n = int(input())
# digit = [int(x) for x in range(1, n+1)]
# sum_ = 0
# for i in range(1, 10 ** 4 - 1):
#     if '0' in str(i):
#         continue
#     for j in range(2, int(math.sqrt(i))+1):
#         if i % j == 0:
#             m_cand = j
#             m_er = i // j
#             digit_lst = [int(x) for x in (list(str(i) + str(m_cand) + str(m_er))) if x != '0']
#             digit_lst.sort()
#             # print(i, digit_lst)
#             # print(digit)
#             if digit_lst == digit:
#                 sum_ += i
#                 # print("IN************************", i, digit_lst, m_cand, m_er)
#                 break
# print(sum_)



# import re
#
# set1 = set()
# sum = 0
# n = int(input())
# for i in range(1964, 1, -1):
#     for j in range(100):
#         if j not in set1:
#             value = i * j
#             str1 = str(value) + str(i) + str(j)
#             if value not in set1:
#                 matcher = ''.join(str(k) for k in range(1, n + 1))
#                 if (re.fullmatch(matcher, ''.join(sorted(str1)))):
#                     sum = sum + value
#                     set1.add(value)
#
# print(sum)


# Enter your code here. Read input from STDIN. Print output to STDOUT



# def group(num):
#     word = ""
#     if len(str(num)) == 3:
#         while num > 0:
#             word += (ones[num // 100] + "Hundred ")
#             num = num % 100
#             dig = num // 10
#             if (dig == 1):
#                 num = num % 10
#                 word += tens1[num]
#                 break
#             else:
#                 word += (tens[dig] )
#             num %= 10
#             word += ones[num]
#             num //= 10
#     elif len(str(num)) == 2:
#         if num // 10 == 1:
#             word += tens1[num % 10]
#         else:
#             word += tens[num // 10]
#             word += ones[num % 10]
#     else:
#         word += ones[num]
#     return word
#
#
# n = int(input())
# ones = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "]
# tens1 = ["Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
# tens = ["", "", "Twenty ", "Thirty ", "Fourty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
# grps = [" ", "Thousand ", "Million ", "Billion "]
# for i in range(1, n + 1):
#     num = int(input())
#     c = 0
#     fword = ""
#     while num > 0:
#         word = group(num % 1000)
#         num = num // 1000
#         if word != "":
#             fword = (word + grps[c]) + fword
#         c+=1
#     print(fword)



#!/bin/python3

# import sys
# import math
#
#
# def isprime(n):
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return 0
#     return 1
#
#
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     for i in range(2, n//2):
#         if n % i == 0:
#             if isprime(n//i) and isprime(i):
#                 print(max(i, n//i))
#                 break
#             elif isprime(n//i):
#                 print(n//i)
#                 break

def median(X):
    N = len(X)
    if N % 2 == 0:
        return (X[int(N / 2)] + X[int(N/2) - 1]) / 2
    return X[int((N - 1) / 2)]

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    new_list = []
    for i in range(0, len(values)):
        new_list.extend([values[i]]*freqs[i])
    new_list.sort()
    # Q1
    q1 = median(new_list[:int((len(new_list)/2))])
    print(q1)
    # Q3
    q3 = median(new_list[int(len(new_list)/2+1):])
    print(q3)
    print(round(float(q3-q1),1))

values = [int(x) for x in input().split()]
freqs = [int(x) for x in input().split()]
interQuartile(values, freqs)
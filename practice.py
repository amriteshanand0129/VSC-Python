# # HackerRank Project Euler question
# # Sum of multiple of 3 and 5
# n = int(input("n: "))
# sum1 = 0
# for i in range(n):
#     if i % 15 == 0:
#         sum1 += i
#         print(i)
#
#
# def sum1_(a, n):
#     n = int(n)
#     return (n/2) * (2*a + (n-1) * a)
#
#
# sum2 = sum1_(15, (n-1)/15)
# print("\n", sum1, sum2)
#
# """ Problem with this method is that in case of bigger data,
#     the one slash division generates errors in rounding.
#
#     Therefore the correct solution will be using the formula
#     n * (n + 1) / 2
# """

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def lcm_list(nums):
    result = 1
    for num in nums:
        result = lcm(result, num)
    return result


# t = int(input().strip())
# prime = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0, 23: 0, 29: 0, 31: 0, 37: 0}
for a0 in range(3, 4):
    # r = int(input().strip())
    r = a0
    print("num:", r)
    lcm = 1
    prime = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0, 23: 0, 29: 0, 31: 0, 37: 0}
    for n in range(2, r+1):
        if n in prime.keys():
            prime[n] += 1
        else:
            for i in prime.keys():
                if n % i == 0:
                    n //= (i ** prime[i])
                    while n > 1 and n % i == 0:
                        n //= i
                        prime[i] += 1
                    break
    for i in prime.keys():
        lcm *= (i ** prime[i])
    print(lcm)
    n = a0
    nums = list(range(1, n + 1))
    print(lcm_list(nums))


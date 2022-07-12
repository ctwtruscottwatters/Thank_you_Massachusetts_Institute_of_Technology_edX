import os
import datetime
import math

""" Authored by Charles Truscott Watters. Thank you Massachusetts Institute of Technology"""
""" Thank you John Guttag, Eric Grimson and Ana Bell and MIT staff and edX staff """
""" Authored on the beginning of Week 11 and 12 in 6.0001 """
""" Final draft of mathematical data mining software """
""" engineering formulas etc, approximations """
""" Rest in Peace Ramanujan. Incredible life story of a number theorist """
""" Silly string for Mathematics research

.14 x 46 equals 144 truncated to no decimal places
46 is the Least Common Multiple of 3 and 43
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 32 equals 100 truncated to no decimal places
32 is the Least Common Multiple of 3 and 29
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46 equals 144 truncated to no decimal places
46 is the Least Common Multiple of 3 and 43
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7
3.14 x 46.76537180435969 equals 147 truncated to no decimal places
46.76537180435969 is the Square root of the power of 3 and 7


21 is the Product of 3 and 7
3.14 x 21 equals 66 truncated to no decimal places
21 is the Product of 3 and 7
3.14 x 21 equals 66 truncated to no decimal places
21 is the Product of 3 and 7
3.14 x 21 equals 66 truncated to no decimal places
21 is the Product of 3 and 7
3.14 x 21 equals 66 truncated to no decimal places
21 is the Product of 3 and 7
3.14 x 21 equals 66 truncated to no decimal places
21 is the Product of 3 and 7
3.14 x 21 equals 66 truncated to no decimal places
21 is the Product of 3 and 7
3.14 x 32 equals 100 truncated to no decimal places
32 is the Least Common Multiple of 3 and 29
3.14 x 46 equals 144 truncated to no decimal places
46 is the Least Common Multiple of 3 and 43
3.14 x 32 equals 100 truncated to no decimal places
32 is the Least Common Multiple of 3 and 29
3.14 x 46 equals 144 truncated to no decimal places
46 is the Least Common Multiple of 3 and 43
3.14 x 32 equals 100 truncated to no decimal places
32 is the Least Common Multiple of 3 and 29
3.14 x 46 equals 144 truncated to no decimal places
46 is the Least Common Multiple of 3 and 43
3.14 x 32 equals 100 truncated to no decimal places
32 is the Least Common Multiple of 3 and 29
3.14 x 46 equals 144 truncated to no decimal places
46 is the Least Common Multiple of 3 and 43
3.14 x 32 equals 100 truncated to no decimal places
32 is the Least Common Multiple of 3 and 29
3.14 x 46 equals 144 truncated to no decimal places
46 is the Least Common Multiple of 3 and 43

""" 

class ArithmeticOperations(object):
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
    def add(self):
        count_one = 0
        count_two = 0
        count_three = 0
        count_four = self.a
        count_five = self.b
        while count_four is not 0:
            count_one += 1
            count_four -= 1
            #print(count_one, a)
        while count_five is not 0:
            count_two += 1
            count_five -= 1
            #print(count_two, b)
        #print(a, b, count_one, count_two)
        for x in range(0, count_one + count_two, 1):
            #print(count_three)
            count_three += 1

        return count_three
    def subtract(self):
        subtrahend = self.a - self.b
        return subtrahend

    def multiply(self):
        multiplicand = self.a * self.b
        return multiplicand

    def divide(self):
        no_remainder = self.a // self.b
        return no_remainder
    def exponentiate(self):
        base = self.a
        exponent = self.b
        exponent_copy = self.b
        while exponent_copy is not 1:
            #print(base, exponent)
            base *= self.a
            exponent_copy -= 1
        power = base
        return power

def is_prime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
        else:
            return True

def main():
    math_research = open('./What_is_Pi_to_Two_Decimal_Places_Number_Theory.txt', 'w+')
    count = 0
    p = []
    q = []
    r = []
    s = []
    for x in range (2, 100 + 1, 1):
        for y in range(2, 100 + 1, 1):
            if is_prime(x) and is_prime(y):
#                print(x, y)
                count += 1
                temp = ArithmeticOperations(x, y)
                p += [["Sum", x, y, temp.add()]]
                p += [["Quotient", x, y, temp.divide()]]
                q += [["Product", x, y, temp.multiply()]]
                q += [["Exponent", x, y, temp.exponentiate()]]
                r += [["Difference", x, y, temp.subtract()]]
                r += [["Sum Squared", x, y, temp.add() ** 2]]
                s += [["Square root of the power", x, y, math.sqrt((x ** y))]]
                s += [["Greatest Common Divisor", x, y, math.gcd(x, y)]]
                s += [["Least Common Multiple", x, y, math.lcm(x + y)]]
                s += [["Square root of sum of the two numbers", x, y, math.sqrt(x + y)]]
                s += [["Base 10 logarithm of the sum", x, y, math.log10(x + y)]]
    #            print("Sum: {} ({} + {}) Difference: {} ( {} minus {} )".format(str(temp.add()), str(x), str(y), str(temp.subtract()), str(x), str(y)))
    #            print("Product: {} ({} x {}) Quotient: {} ({} / {})".format(str(temp.multiply()), str(x), str(y), temp.divide(), str(x), str(y)))
    #            print("Power: {} ({} ^ {})".format(str(temp.exponentiate()), str(x), str(y)))
    #            print("{} ({} + {}) is a prime number?: {}".format(str(temp.add()), str(x), str(y), is_prime(temp.add())))
    #            print("{} ({} - {}) is a prime number?: {}".format(str(temp.subtract()), str(x), str(y), is_prime(temp.subtract())))
    #            print("{} ({} to the power of {}) is a prime number?: {}".format(str(temp.exponentiate()), str(x), str(y), is_prime(temp.exponentiate())))

                # What about writing Fermat's Last Theorem
                temp = 0
        #print(p, q, r, s)
        reference = []
        for a in p:
            for b in q:
                for c in r:
                    for d in s:
                        if type(a) == list and type(b):
                            if a[3] == b[3] and a[3] > 2 and a[0] is not "Sum" and b[0] is not "Difference":
                                print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(a[3], b[3], a[0], a[1], a[2], b[0], b[1], b[2]))
                                math_research.write("{} equals {} which is the {} of {} and {} and the {} of {} and {}\n".format(a[3], b[3], a[0], a[1], a[2], b[0], b[1], b[2]))

                        if type(c) == list and type(a) == list:
                            if a[3] == c[3] and a[3] > 2 and a[0] is not "Sum" and c[0] is not "Difference":
                                print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(a[3], c[3], a[0], a[1], a[2], c[0], c[1], c[2]))
                                math_research.write("{} equals {} which is the {} of {} and {} and the {} of {} and {}\n".format(a[3], c[3], a[0], a[1], a[2], c[0], c[1], c[2]))
                        if type(a) == list and type(d) == list:
                            if a[3] == d[3] and a[3] > 2 and a[0] is not "Sum" and d[0] is not "Difference":
                                print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(a[3], d[3], a[0], a[1], a[2], d[0], d[1], d[2]))
                                math_research.write("{} equals {} which is the {} of {} and {} and the {} of {} and {}\n".format(a[3], d[3], a[0], a[1], a[2], d[0], d[1], d[2]))
                        if type(b) == list and type(c) == list:
                            if b[3] == c[3] and b[3] > 2 and b[0] is not "Sum" and c[0] is not "Difference":
                                print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(b[3], c[3], b[0], b[1], b[2], c[0], c[1], c[2]))
                                math_research.write("{} equals {} which is the {} of {} and {} and the {} of {} and {}\n".format(b[3], c[3], b[0], b[1], b[2], c[0], c[1], c[2]))
                        if type(b) == list and type(d) == list:
                            if b[3] == d[3] and b[3] > 2 and b[0] is not "Sum" and d[0] is not "Difference":
                                print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(b[3], d[3], b[0], b[1], b[2], d[0], d[1], d[2]))
                                math_research.write("{} equals {} which is the {} of {} and {} and the {} of {} and {}\n".format(b[3], d[3], b[0], b[1], b[2], d[0], d[1], d[2]))
                        if round(round(math.pi, 2) * a[3], 0) == b[3] and a[3] >= 20 and b[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), a[3], b[3]))
                            print("{} is the {} of {} and {}".format(a[3], a[0], a[1], a[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), a[3], b[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(a[3], a[0], a[1], a[2]))
                        if round(round(math.pi, 2) * a[3], 0) == c[3] and a[3] >= 20 and c[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), a[3], c[3]))
                            print("{} is the {} of {} and {}".format(a[3], a[0], a[1], a[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), a[3], c[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(a[3], a[0], a[1], a[2]))
                        if round(round(math.pi, 2) * a[3], 0) == d[3] and a[3] >= 20 and d[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), a[3], d[3]))
                            print("{} is the {} of {} and {}".format(a[3], a[0], a[1], a[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), a[3], d[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(a[3], a[0], a[1], a[2]))
                        if round(round(math.pi, 2) * b[3], 0) == a[3] and b[3] >= 20 and a[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), b[3], a[3]))
                            print("{} is the {} of {} and {}".format(b[3], b[0], b[1], b[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), b[3], a[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(b[3], b[0], b[1], b[2]))
                        if round(round(math.pi, 2) * b[3], 0) == c[3] and b[3] >= 20 and c[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), b[3], c[3]))
                            print("{} is the {} of {} and {}".format(b[3], b[0], b[1], b[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), b[3], c[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(b[3], b[0], b[1], b[2]))
                        if round(round(math.pi, 2) * b[3], 0) == d[3] and b[3] >= 20 and d[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), b[3], d[3]))
                            print("{} is the {} of {} and {}".format(b[3], b[0], b[1], b[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), b[3], d[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(b[3], b[0], b[1], b[2]))
                        if round(round(math.pi, 2) * c[3], 0) == a[3] and c[3] >= 20 and a[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), c[3], a[3]))
                            print("{} is the {} of {} and {}".format(c[3], c[0], c[1], c[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), c[3], a[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(c[3], c[0], c[1], c[2]))
                        if round(round(math.pi, 2) * c[3], 0) == b[3] and c[3] >= 20 and b[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), c[3], b[3]))
                            print("{} is the {} of {} and {}".format(c[3], c[0], c[1], c[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), c[3], b[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(c[3], c[0], c[1], c[2]))
                        if round(round(math.pi, 2) * c[3], 0) == d[3] and c[3] >= 20 and d[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), c[3], d[3]))
                            print("{} is the {} of {} and {}".format(c[3], c[0], c[1], c[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), c[3], d[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(c[3], c[0], c[1], c[2]))
                        if round(round(math.pi, 2) * d[3], 0) == a[3] and d[3] >= 20 and a[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), d[3], a[3]))
                            print("{} is the {} of {} and {}".format(d[3], d[0], d[1], d[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), d[3], a[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(d[3], d[0], d[1], d[2]))
                        if round(round(math.pi, 2) * d[3], 0) == b[3] and d[3] >= 20 and b[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), d[3], b[3]))
                            print("{} is the {} of {} and {}".format(d[3], d[0], d[1], d[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), d[3], b[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(d[3], d[0], d[1], d[2]))
                        if round(round(math.pi, 2) * d[3], 0) == c[3] and d[3] >= 20 and c[3] >= 20:
                            print("{} x {} equals {} truncated to no decimal places".format(round(math.pi, 2), d[3], c[3]))
                            print("{} is the {} of {} and {}".format(d[3], d[0], d[1], d[2]))
                            math_research.write("{} x {} equals {} truncated to no decimal places\n".format(round(math.pi, 2), d[3], c[3]))
                            math_research.write("{} is the {} of {} and {}\n".format(d[3], d[0], d[1], d[2]))
    math_research.close()

    # 6257 (5000 + 1257) is a prime number?: True
    # 3743 (5000 - 1257) is a prime number?: True
    print("Charles Truscott Watters")
if __name__ == "__main__": main()
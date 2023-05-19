# ----------   := walrus морж  -----------
# print("----------   := walrus морж  -----------")

# def give_me_five():
#     return 5

# give_me_five = lambda : 5

# if x := give_me_five():
#     print(x)


# while (value := input("gime me something: ")) != "":
#     print(value)


# def double_it(x):
#     return x * 2

# data = [1,2,3,4,5]

# f_data = [y for x in data if (y := double_it(x)) != 4]
# print(f_data)

# lines = ["11", "22", "33", "#44", "55"]

# if any((comment := line).startswith('#') for line in lines):
#     print(comment)


# print(t := 9)   # значение, а не аргумент

# ----------------- Ellipsis и NotImplented в Python -------------------
# print("----------------- Ellipsis ... и NotImplented в Python -----------------")
# print(...)
# def some_func1():
#     ...

# def some_func2():
#     pass

# print(some_func1)
# print(some_func2)


# for i in range(10):
#     print(i, end=" ")


# for i in range(10, 20):
#     print(i, end=" ")

# import math

# factorial = lambda n: 1 if n < 2 else n * factorial(n - 1)


# print(factorial(5))
# print(sum(range(10)))
# print(math.prod(range(1,6)))
# print(math.factorial(5))


# new_list = list(range(10))
# print(new_list)



# // https://leetcode.com/problems/contains-duplicate/
# nums1 = [1,2,3,1]
# nums2 = [1,2,3,4]
# nums3 = [1,1,1,3,3,4,3,2,4,2]

# def containsDuplicate(nums):
#     for i in nums:
#         if nums.count(i) > 1 :
#             return True

#     return False
        
# print(containsDuplicate(nums1))
# print(containsDuplicate(nums2))
# print(containsDuplicate(nums3))






# # https://leetcode.com/problems/reverse-words-in-a-string/
# 151. Reverse Words in a String
# def reverseWords(s):
#     #  s = ' '.join(s.split())#[::-1]
#     res = ""
#     for x in s.split():
#         res = x + f" {res}"

#     return res[0:-1]


# s1 = "the sky is blue"
# s2 = "  hello world  "
# s3 = "a good   example"
# print(reverseWords(s1))
# print(reverseWords(s2))
# print(reverseWords(s3))



# # https://leetcode.com/problems/find-peak-element/
# def findPeakElement(nums):
#     match len(nums):
#         case 1:
#             return 0
#         case 2:
#             return 0 if nums[0] > nums[1] else 1
#         case _:
#             for i in range(1, len(nums) - 1):
#                 if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
#                     return i
#             return 0 if nums[0] > nums[-1] else len(nums) - 1
                
# nums1 = [1,2,3,1]
# nums2 = [1,2,1,3,5,6,4]
# nums3 = [1]
# nums4 = [2,1]
# nums5 = [3,2,1]
# nums6 = [1,2,3]

# print(findPeakElement(nums1))
# print(findPeakElement(nums2))
# print(findPeakElement(nums3))
# print(findPeakElement(nums4))
# print(findPeakElement(nums5))
# print(findPeakElement(nums6))



class Dude:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.lastname = "london"

    def Introducing(self):
        return f"Hello, my name is {self.name} {self.lastname}. I`m {self.age}"
    
    def Get_Something(self, something):
        self.something = something


class Son(Dude):
    def __init__(self, age, name):
        super().__init__(age, name)


        
jon = Dude(14, "jon")
jon.something = 10.5
print(jon.age)
print(jon.name)
print(jon.lastname)
print(jon.Introducing())
print(jon.something)

jonjr = Son(3, "jack")
print(jonjr.age)
print(jonjr.name)
print(jonjr.lastname)
print(jonjr.Introducing())
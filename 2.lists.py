

# 1. Write a program that sum of all elements:
one = [613, 955, 291, 497, 562, 483, 165, 210, 864, 789]

# s = 0
# for x in one:
#     s += x
# print(s)

# s2 = sum(one)
# print(s2)

# 2.  Write a program that find the largest element:
two = [386, 850, 274, 316, 526, 937, 998, 249, 269, 922]

# m = 0
# for x in two: 
#     if(m < x):
#         m = x
    
# print(m)
# m2 = max(two)
# print(m2)


# 3. Write a program that duplicates that doubles the value of each elements in the list:
# for example: [1,2,3] should result in [2,4,6]
# three = [211, 36, 295, 455, 147, 977, 381, 253, 327, 617]

# double = []
# for x in three: 
#     double.append(x * 2)

# print(double)


# 4. Write a program that concatenates these two list into a single list:
four_a = [582, 427, 534, 143, 567, 604, 12, 48, 686, 825]
four_b = [357, 728, 406, 989, 380, 800, 201, 410, 452, 141]
# c = four_a + four_b
# print(c)

# 5. Write a program that removes a specific element from a list by its value.
five = [456, 942, 944, 762, 836, 451, 314, 559, 954, 211]
# rm = 762
# five.remove(rm)
# print(five)

# 6. Write a program that removes a specific element from a list by its index.
six = [993, 245, 896, 250, 226, 313, 918, 877, 793, 695]
# rm_ind = 1
# six.pop(rm_ind)
# print(six)

# 7. Write a program that sorts a list of numbers in ascending order.
seven = [887, 106, 368, 603, 35, 455, 728, 449, 108, 47]
# seven.sort()
# print(seven)

# 8. Write a program that filters out all elements in a list that are less than a specified value.
# use for loop and conditionals
eight = [309, 122, 27, 240, 453, 174, 193, 649, 804, 171]
# threshold = 200

# fl=[]
# for x in eight:
#     if(x >= threshold):
#         fl.append(x)

# print(fl)

# 9. Calculate and print the length (number of elements) of a given list.
nine = [679, 697, 657, 171, 503, 582, 656, 82, 724, 796]

# l = len(nine)
# print(l)


# 10. Write a program that take a list and print a subset of its elements by its start and end index.
ten = [64, 800, 662, 185, 630, 612, 181, 210, 738, 12]
start_index = 1
end_index = 4

# answer should be this: 
# [800, 662, 185, 630]

# ss=[]
# for x in range(len(ten)):
#     if(x >= start_index and x <= end_index):
#         ss.append(ten[x])

# print(ss)

# 11. Write a program iterates the list and
# prints 'FizzBuzz' when divisable by 3 and 5.  
# prints 'Fizz' when divisable by 3 .  
# prints 'Buzz' when divisable by 5. 
eleven = [213, 927, 265, 39, 860, 421, 550, 884, 991, 1500]

# for num in eleven:
#     if num % 3 == 0 and num % 5 == 0: 
#         print('fizzbuzz')
#     elif num % 3 == 0: 
#         print('fizz')
#     elif num % 5 == 0:
#         print('buzz')


# 12. Write a program that appends an element to the end of a list.
twelve = [36, 632, 155, 350, 746, 642, 113, 534, 9, 34]
# ap = 1
# twelve.append(ap)
# print(twelve)

# 13. Write a program that inserts an element at a specific position in a list.
thirteen = [191, 871, 990, 163, 687, 747, 606, 799, 373, 851]
element_to_insert = 4
# position = 3

# thirteen.insert(position, element_to_insert)
# print(thirteen)

# 14. Write a program that counts how many times a specific element appears in a list.
fourteen = [1, 1, 1, 2, 2, 1, 3, 3, 2, 1]
element_to_count = 1

# try using for loop and conditional
# and then try .count() method

# c1 = 0
# for num in fourteen:
#     if num == element_to_count:
#         c1 += 1
# print(c1)

# c1b = fourteen.count(element_to_count)
# print(c1b)

# 15.  Write a program that extracts all even numbers from a list and stores them in even_only:
# use for loop and conditionals
fifteen = [267, 688, 88, 755, 680, 746, 559, 710, 283, 451]
even_only = []

# for num in fifteen:
#     if num  % 2 == 0:
#         even_only.append(num)
# print(even_only)

# 16. Write a program that reverses this list but does not change the original sixteen variable:
# The answer is not sixteen.reverse(). 
sixteen = [378, 763, 856, 566, 847, 795, 313, 540, 67, 219]
rev = []

# for num in sixteen:
#     rev.insert(0, num)
# print(rev)

# reversed_sixteen = sixteen[::-1]
# print(reversed_sixteen)

# 17. Write a flattens this double nested listbelow:
# Result should be [1, 2, 3, 4, 5, 6, 7, 8]
# Hint: try a nested loop (2 for in loops) 
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

# unnest = []

# for ar in nested_list:
#     for num in ar:
#         unnest.append(num)

# print(unnest)



# 18. Write a program that finds duplicates from the 2 lists below:
# Hint: try a nested loop (2 for in loops) and use equality
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]


# dup = []

# for n1 in list1:
#     for n2 in list2:
#         if(n1 == n2):
#             dup.append(n1)
# print(dup)

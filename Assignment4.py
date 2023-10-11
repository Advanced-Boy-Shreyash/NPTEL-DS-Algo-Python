# Write a Python function histogram(l) that takes as input a list of integers with repetitions and returns a list of pairs as follows:
#     > for each number n that appears in l, there should be exactly one pair (n,r) in the list returned by the function, where r is the number
#     of repetitions of n in l.
#     > the final list should be sorted in ascending order by r, the number of repetitions. For numbers that occur with the same number of
#     repetitions, arrange the pairs in ascending order of the value of the number.

# For Instance:
#     >>> histogram([13,12,11,13,14,13,7,7,13,14,12])
#     [(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]

#     >>> histogram([7,12,11,13,7,11,13,14,12])
#     [(14, 1), (7, 2), (11, 2), (12, 2), (13, 2)]

#     >>> histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7])
#     [(11, 2), (12, 2), (7, 4), (13, 4), (14, 4)]


# def histogram(l):
#     count = 0
#     a = []
#     b = []
#     for i in range(len(l)):
#         index = i
#         count = 0
#         for j in range(index, len(l)):
#             if l[index] == l[j] and l[index] not in b:
#                 count = count+1
#         b = b+[l[index]]
#         if count != 0:
#             a = a+[(l[index], count)]
#     a.sort()
#     a = sorted(a, key=lambda a: a[1])
#     return a

# print(histogram([13,12,11,13,14,13,7,7,13,14,12]))

# def histogram(l):
#     # Initialize an empty list to store the result
#     result = []

#     # Loop through the input list 'l'
#     for item in l:
#         # Check if the item is already in the result list
#         if (item, l.count(item)) not in result:
#             # If not, add a tuple of (item, count of item) to the result list
#             result.append((item, l.count(item)))

#     # Sort the result list first by item value and then by count
#     result.sort(key=lambda x: (x[0], x[1]))

#     return result


# print(histogram([13, 12, 11, 13, 14, 13, 7, 7, 13, 14, 12]))


def histogram(l):
    d = {}
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    ans = []
    for a in d.keys():
        number_of_times = d[a]
        ans.append((a, number_of_times))
    ans = sorted(ans, key=lambda x: x[0])
    ans = sorted(ans, key=lambda x: x[1])
    return ans


print(histogram([13, 12, 11, 13, 14, 13, 7, 7, 13, 14, 12]))


# Que. 2
# A college maintains academic information about students in three separate lists

# Course details: A list of pairs of form (coursecode,coursename), where both entries are strings. For instance,
# [ ("MA101","Calculus"),("PH101","Mechanics"),("HU101","English") ]

# Student details: A list of pairs of form (rollnumber,name), where both entries are strings. For instance,
# [ ("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar") ]

# A list of triples of the form (rollnumber,coursecode,grade), where all entries are strings. For instance,
# [ ("UGM2018001", "MA101", "AB"), ("UGP2018132", "PH101", "B"), ("UGM2018001", "PH101", "B") ]. You may assume that each roll number and course code in the grade list appears in the student details and course details, respectively.

# Your task is to write a function transcript (coursedetails,studentdetails,grades) that takes these three lists as input and produces
# consolidated grades for each student. Each of the input lists may have its entries listed in arbitrary order. Each entry in the returned
# list should be a tuple of the form

# (rollnumber, name,[(coursecode_1,coursename_1,grade_1),...,(coursecode_k,coursename_k,grade_k)])

# where the student has grades for k ≥ 1 courses reported in the input list grades.

# The output list should be organized as follows.
# The tuples shold sorted in ascending order by rollnumber
# Each student's grades should sorted in ascending order by coursecode

# For Instance
# >>>transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2021001","Rohit Grewal"),("UGP2021132","Neha Talwar")],[("UGM2021001","MA101","AB"),("UGP2021132","PH101","B"),("UGM2021001","PH101","B")])

# [('UGM2021001', 'Rohit Grewal', [('MA101', 'Calculus', 'AB'), ('PH101', 'Mechanics', 'B')]), ('UGP2021132', 'Neha Talwar', [('PH101', 'Mechanics', 'B')])]

# >>>transcript([("T1","Test 1"),("T2","Test 2"),("T3","Test 3")],[("Captain","Rohit Sharma"),("Batsman","Virat Kohli"),("No3","Cheteshwar Pujara")],[("Batsman","T1","14"),("Captain","T1","33"),("No3","T1","30"),("Batsman","T2","55") ,("Captain","T2","158"),("No3","T2","19"), ("Batsman","T3","33"),("Captain","T3","95"),("No3","T3","51")])

# [('Batsman', 'Virat Kohli', [('T1', 'Test 1', '14'), ('T2', 'Test 2', '55'), ('T3', 'Test 3', '33')]), ('Captain', 'Rohit Sharma', [('T1', 'Test 1', '33'), ('T2', 'Test 2', '158'), ('T3', 'Test 3', '95')]),('No3', 'Cheteshwar Pujara', [('T1', 'Test 1', '30'), ('T2', 'Test 2', '19'), ('T3', 'Test 3', '51')])]


def transcript(coursedetails, studentdetails, grades):
    list1 = []
    coursedetails.sort()
    studentdetails.sort()
    grades.sort()

    for i in studentdetails:
        a = i
        list2 = []
        for j in grades:
            if i[0] == j[0]:
                for k in coursedetails:
                    if j[1] == k[0]:
                        b = k
                        b = b+(j[2],)
                        list2.append(b)

        a = a+(list2,)
        list1.append(a)
    return list1


print(transcript([("MA101", "Calculus"), ("PH101", "Mechanics"), ("HU101", "English")],
                 [("UGM2021001", "Rohit Grewal"), ("UGP2021132", "Neha Talwar")],
                 [("UGM2021001", "MA101", "AB"), ("UGP2021132", "PH101", "B"), ("UGM2021001", "PH101", "B")]))

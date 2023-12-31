def Gvalue(code):
    if code == "A":
        return (10)
    if code == "AB":
        return (9)
    if code == "B":
        return (8)
    if code == "BC":
        return (7)
    if code == "C":
        return (6)
    if code == "CD":
        return (5)
    if code == "D":
        return (4)

# varibles used for storing data


ROLL_GRADEsum = {}
Roll_course_count = {}
Roll_name = {}

# COURSES INPUT SECTION

type_course = input()
enter_course_detail = input()
next_input = input()
while (next_input != "Students"):
    next_input = input()

# STUDENT INPUT SECTION

# if it fails in courses section then
# it will automatically enter students
# contact us at youtube.com/c/getpythoncode

roll, name = input().split('~')
Roll_name[roll] = name
ROLL_GRADEsum[roll] = 0
Roll_course_count[roll] = 0
next_input = input()
while ('~' in next_input):
    roll, name = next_input.split('~')
    Roll_name[roll] = name
    ROLL_GRADEsum[roll] = 0
    Roll_course_count[roll] = 0
    next_input = input()

# GRADES INPUT SECTION

code, sem, year, Rnum, grade = input().split('~')
if Rnum in ROLL_GRADEsum.keys():
    ROLL_GRADEsum[Rnum] = ROLL_GRADEsum[Rnum]+Gvalue(grade)
    Roll_course_count[Rnum] = Roll_course_count[Rnum]+1
next_input = input()
while (next_input != "EndOfInput"):
    code, sem, year, Rnum, grade = next_input.split('~')
    if Rnum in ROLL_GRADEsum.keys():
        ROLL_GRADEsum[Rnum] = ROLL_GRADEsum[Rnum]+Gvalue(grade)
        Roll_course_count[Rnum] = Roll_course_count[Rnum]+1
    next_input = input()

# print(Roll_course_count)
# print(ROLL_GRADEsum)
# print(Roll_name)

# RESULT COMPUTATION

Sort_roll = sorted(Roll_name)
for key in Sort_roll:
    if ROLL_GRADEsum[key] != 0:
        ans = round((ROLL_GRADEsum[key]/Roll_course_count[key]), 2)
        print(key+"~"+Roll_name[key]+"~"+str(ans))
    else:
        print(key+"~"+Roll_name[key]+"~"+"0")

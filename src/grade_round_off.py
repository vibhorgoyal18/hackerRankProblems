# WhoMustNotBeNamed University has the following grading policy:

# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
# For example, grade = 84 will be rounded to 85 but 23 will not be rounded
# because the rounding would result in a number that is less than .

# Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

# Sample Input

# 4
# 73
# 67
# 38
# 33
# Sample Output

# 75
# 67
# 40
# 33


def gradingStudents(grades):
    return [((5 * round(float(x)/5)) if (x % 5 >= 3 and x >= 38) else x) for x in grades]


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

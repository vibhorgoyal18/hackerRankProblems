# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

# Input:
# The first line of input contains an integer T denoting the number of test cases.
# Then T test cases follow.
# Each test case consists of two lines.
# The first line of each test case is N and S, where N is the size of array and S is the sum.
# The second line of each test case contains N space separated integers denoting the array elements.

# Output:
# For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= Ai <= 1010

# Example:
# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10
# Output:
# 2 4
# 1 5

# Explanation :
# Testcase1: sum of elements from 2nd position to 4th position is 12
# Testcase2: sum of elements from 1st position to 5th position is 15


def user_input():
    global size_and_sum, temp_array
    try:
        test_case_count = int(input('Enter the number of test cases: '))
    except ValueError:
        print('test_case_count should only be a positive integer')
        return None
    if not test_case_count > 0:
        print('test_case_count should only be a positive integer')
        return None
    for test_case_number in range(int(test_case_count)):
        try:
            size_and_sum = [int(val.strip()) for val in
                            input('Enter the size of array and sum to be found separated by a space: ').split(' ') if
                            val is not '']
        except ValueError:
            return None
        temp_array = [int(val.strip()) for val in
                      input('Enter ' + str(size_and_sum[0]) + ' numbers separated by space: ').split(' ') if
                      val is not '']

        find_sub_array(size_and_sum, temp_array)


def find_sub_array(size_and_sum, temp_array):
    sum = 0
    start_index = 1
    for i in range(len(temp_array)):
        sum += temp_array[i]
        if sum == size_and_sum[1]:
            print(i + 1, j + i + 1)
            return
    print(-1)


user_input()

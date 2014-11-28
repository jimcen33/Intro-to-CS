# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

#Solution from Alex-066335 in Udacity
def longest_repetition(lst_input):
    max_chr = None
    curr_length = 1
    max_length = 1
    if lst_input == []:
        return None
    else:
        max_chr = lst_input[0]
        for i in range(1, len(lst_input)):
            if lst_input[i] == lst_input[i-1]:
                curr_length += 1
                if curr_length > max_length:
                    max_length = curr_length
                    max_chr = lst_input[i]
            else:
                curr_length = 1
        return max_chr
        



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None


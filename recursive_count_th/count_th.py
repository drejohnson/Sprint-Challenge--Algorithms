'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # intial occurrence of "th"
    th = 0 
    # Base case: if length of word is less than 2 return 0
    if len(word) < 2 :
        return 0
    # check of occurrences of "th". if found increment th count
    if word[-2:] == 'th' :
        th +=1

    # loop through word, slicing 1 letter at a time until we reach 0
    return th + count_th(word[:len(word)-1])
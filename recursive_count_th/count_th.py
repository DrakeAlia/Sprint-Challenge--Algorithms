'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
# * Your function should take in a signle parameter (a string `word`)
# * Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
# * Your function must utilize recursion. 
# * >>>>>>>>> It cannot contain any loops <<<<<<<<<<<<

     # The base case is when we have one or less letters left
    if len(word) <= 1:
        return 0
    elif word[-2:] == "th":
        # If they are "th", remove them and return count_th + 1
        return count_th(word[:-2]) + 1
         # If the second to last letter isn't h, remove them and return count_th
    elif word[-2] != "h": 
        return count_th(word[:-2])
    else:
        # Else, remove only the last letter and return count_th
        # So we can check again for "th"
        return count_th(word[:-1]) 

    # This solution would run in O(n) time
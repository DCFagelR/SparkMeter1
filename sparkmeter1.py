# n the language of your choice, write code that prints every third element of this list using recursion. 
# [1, 2, 3, 4, 5, 6, 7, 8, 9]. Please create a public Github or Gitlab snippet with your response and submit the link here.

# ----------------------------------------------------------------------------------------------
# Functions

def recThird(data, curr):

    # base case
    if curr > len(data):
        return

    print(data[curr])
    recThird(data, (curr + 3))


# ----------------------------------------------------------------------------------------------
# Main

data = [1,2,3,4,5,6,7,8,9]

recThird(data, 2)

# Found that first element in the list(16) is the char (p) in a-z alphabet letters
list_to_convert = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
alphabet ="abcdefghijklmnopqrstuvwxyz"

# Iterate through the list and perform conversion
for i in list_to_convert:
    if isinstance(i,int):
        print(alphabet[i-1],end='')
    else:
        print(i,end='')

# method 1
# def count_substring(string, sub_string):
#     len_of_substr = len(sub_string)
#     first_ch = sub_string[0]
#     count = 0
#     for i in range(0, len(string) - len_of_substr + 1):
#         if string[i] == first_ch:
#             str = ""
#             for j in range(i, i+len_of_substr):
#                 str += string[j]
#             if str == sub_string:
#                 count += 1
#     return count

# method 2
def count_substring(string, sub_string):
    len_of_substr = len(sub_string)
    count = 0
    for i in range(0, len(string) - len_of_substr + 1):
        str = string[i:i+len_of_substr]
        if str == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
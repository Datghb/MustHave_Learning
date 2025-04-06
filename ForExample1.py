#tính tổng số chẵn trong list

# def sum_even_number(numbers):
#     tatol = 0
#     for numbers in numbers:
#         if numbers % 2 == 0:
#             tatol += numbers
#     return tatol
#
# result = sum_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(result)


def is_palindrome(string):
    cleaner = ''.join(c.lower() for c in string if c.isalum())
    for i in range(len(string) // 2):
        if cleaner[i] != cleaner[-(i +1)]:
            return False
    return True

text = "A man a plan a canal Panama"
print("palindrome?", is_palindrome(text))
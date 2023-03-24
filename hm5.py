# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам".

array = ["etam", "team", "txan", "pate", "natx", "bat", "wjdqi", "wjd", "iqdwj", "tame"]
word1 = ''
list_1 = []
list_2 = []
list_3 = []
for i in range(len(array)):
    for j in range(len(array)):
        if array[j] not in list_3:
            if len(array[i]) == len(array[j]):
                for k in array[j]:
                    if k in array[i]:
                        word1 = word1 + k
                    else:
                        word1 = ''
                        break
                if word1 != '':
                    list_1.append(word1)
                word1 = ''
    if list_1 !=[]:
        list_2.append(list_1)
        list_1 = []
    for m in range(len(list_2)):
        for n in range(len(list_2[m])):
            list_3.append(list_2[m][n])
print(list_2)


# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
#
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
#
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество
# повторений.


some_string = input('Введите строку из букв A-Z: ')
def RLE(str_input):
    str_result = []
    count_letter = 1
    if str_input == '':
        print(str_input)
    else:
        set_for_check = set(str_input)
        acceptable_symbols = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                              'S', 'T', 'U', 'U', 'V', 'W', 'X', 'Y', 'Z'}
        find_similarities = set_for_check.intersection(acceptable_symbols)
        if len(find_similarities) < len(set_for_check):
            print('Ошибка! Невалидная строка')
        else:
            for i in range(len(str_input) - 1):
                if str_input[i] == str_input[i + 1]:
                    count_letter +=1
                else:
                    if count_letter == 1:
                        str_result.append(str_input[i])
                    else:
                        str_result.append(str_input[i])
                        str_result.append(count_letter)
                        count_letter = 1
            if count_letter == 1:
                str_result.append(str_input[-1])
            else:
                str_result.append(str_input[-1])
                str_result.append(count_letter)
    return str_result

print(*RLE(some_string), sep="")
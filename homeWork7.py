# Задача про винни пуха
def check_rhythm(poem):
    lines = poem.split(" ")
    syllables = []
    for i in lines:
        words = i.split("-")
        for j in words:
            vowel_count = count_vowels(j)
            syllables.append(vowel_count)
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"
def count_vowels(word):
    vowels = "уаеоиэыюУЕАОИЭЫЮ"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count
poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6)
def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            result = operation(row, column)
            print(result, end ='\t')
        print()
print(print_operation_table(lambda x, y: x*y))
  

    
            
            


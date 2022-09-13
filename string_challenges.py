# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
new_word = list(word.lower())
print(new_word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

my_list = ["а", "е", "ы", "о", "э", "ю", "и", "я", "у"]

letter_count = 0
for i in word.lower():
    if i in my_list:
        letter_count += 1

print(letter_count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words2 = sentence.split()
letter_count2 = 0

for word2 in words2:
    letter_count2 += len(word2)

avg_word = letter_count2 // len(words2)
print(avg_word)

# 9.38 (а)
# Дано слово из 12 букв. Поменять местами его трети след образом:
# - 1-ую треть слова разместить на месте третьей, 2-ую на месте
# первой, 3-ю на месте - второй.

word = 'конкатенация'

w1 = word[0:4]
w2 = word[4:8]
w3 = word[8:]

newWord = w2 + w3 + w1
print(newWord)


# 9.105
# Дано слово из 12-ти букв. Переставить в обратном порядке буквы, располо-
# женные между второй и десятой буквами (т.е. с третьей по девятую).

word = 'молниеносный'

w1 = word[0:2]
w2 = word[2:9]
w20 = w2[::-1]
w3 = word[9:]

result = w1 + w20 + w3
print(result)


#9.153
# Дан текст. Найти наибольшее количество идущих подряд одинаковых символов

text = input('Input text: ')
symbol = input('input symbol: ')

lenText = len(text)
index = 0
cntSymbol = 0

while index < lenText:
    if text[index] == symbol and text[index+1] == symbol:
        cntSymbol += 1
    index += 1

result = cntSymbol + 1

print(f'Количество символов: {result}')

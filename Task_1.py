# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
s = input('Введите строку: ').split()
ss = 'абв'
s2 = ''
for i in range(len(s)):
    if not ss in s[i].lower():
        s2=s2 + ' '+ s[i]
print(s2[1:])
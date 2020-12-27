#! python3
# Находит телефонные номера и адреса электронной почты в буфере обмена

import pyperclip
import re

# создание регулярного выражения для телефонных номеров
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # территориальный код
    (\s|-|\.)?                      # разделитель
    (\d{3})                         # первые 3 цифры
    (\s|-|\.)                       # разделитель
    (\d{2})                         # еще 2 цифры
    (\s|-|\.)                       # разделитель
    (\d{2})                         # последние 2 цифры
    )''', re.VERBOSE)

# создание регулярного выражения для адресов электронной почты
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # имя пользователя
    @                               # символ @
    [a-zA-Z0-9.-]+                  # имя домена
    (\.[a-zA-Z]{2,4})               # остальная часть
    )''', re.VERBOSE)

# поиск соответствий в тексте, содержащемся в буфере обмена
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5], groups[7]])
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# копирование результатов в буфер обмена
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты не обнаружены')

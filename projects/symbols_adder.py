#! Python 3
# Добавляет символы в каждую строку текста,
# сохраненного в буфере обмена.

import pyperclip

# выгрузка из буфера обмена
text = pyperclip.paste()
print('Получение данных из буфера обмена')

# Разделяет строки и добавляет символы
lines = text.split('\n')
for i in range(len(lines)):
    line = lines[i].rstrip()
    lines[i] = '(* ' + line + ' *)'

# Объединение измененных строк
text = '\n'.join(lines)

# корирование в буфер обмена
pyperclip.copy(text)
print('Копирование данных в буфер обмена')

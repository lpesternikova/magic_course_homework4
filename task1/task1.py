# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.

import os

def create_library():
    os.mkdir("library")
    os.makedirs("library/fiction")
    os.makedirs("library/non-fiction")
    os.makedirs("library/history")
    os.makedirs("library/fantasy")
    pass

create_library()
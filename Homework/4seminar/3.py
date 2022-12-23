from typing import List

def change_spisok(spisok: List[str], accept: str) -> str:
    file_spisok = ''
    for name in spisok:
        if name.count(accept):
            name = name.upper()
        string = name + '\n'
        file_spisok += string
    return file_spisok

file_spisok = open('vedomost.txt', 'r', encoding='unf-8')
lines_spisok = file_spisok.read().split('\n')
file_spisok.close

spisok_new = change_spisok(lines_spisok, accept='5')

file_spisok = open('vedomost.txt', 'w', encoding='utf-8')
file_spisok.write(spisok_new)
file_spisok.close

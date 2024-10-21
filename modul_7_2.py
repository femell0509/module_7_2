def custom_write(file_name: str, string: list):
    number_srt = 0
    string_position = {}
    for new_str in string:
        number_srt += 1
        file = open(file_name, 'a', encoding='utf-8')
        a = file.tell()
        file.write(f'{new_str}\n')
        file.close()
        string_position.update({(number_srt, a):new_str})
    return string_position

if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
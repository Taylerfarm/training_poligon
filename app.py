def read_and_write_to_set(input_filename, output_filename):
    # Читаем строки из файла и добавляем их в множество
    with open(input_filename, 'r') as file:
        lines = file.readlines()
        site_set = set(map(str.strip, lines))

    # Записываем множество в новый файл
    with open(output_filename, 'w') as output_file:
        for site in site_set:
            output_file.write(f'{site}\n')

if __name__ == "__main__":
    read_and_write_to_set('sites.txt', 'true_sites.txt')
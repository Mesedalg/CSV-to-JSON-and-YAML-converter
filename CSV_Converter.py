import csv
import json
import os.path


class FileName:
    """Класс расширения файлов, прикручен сюда как элемент ООП,
    на самом деле он здесь не сильно нужен."""

    def __init__(self, extension):
        self.extension = extension

    def success(self):
        print(f"Конвертирование из csv в {self.extension} успешно завершено!")


def convert_csv_to_json(csv_input):
    """ Функция, конвертирующая csv файлы в json"""
    # while True:
    #     json_path = input("Введите полный путь к конечному файлу с расширением .json: ")
    #     if os.path.exists(os.path.dirname(json_path)) and json_path.split('.')[-1].lower() == "json":
    #         break
    #     else:
    #         print("Ошибка: Введите корректный путь для сохранения файла в формате: \
    # путь_существующей_папки\название_файла.json")
    json_instance = FileName("json")
    list = []
    dict = {}
    with open(csv_input, "r", encoding='utf-8') as csv_file:
        # with open(json_path, "w") as json_file:
        with open(f"{os.path.dirname(csv_input)}\{os.path.basename(csv_input).replace('csv', 'json')}", "w",
                  encoding="utf-8") as json_file:
            csv_read = csv.DictReader(csv_file)
            for row in csv_read:
                list.append(row)
            dict[os.path.basename(csv_input)] = list
            json.dump(dict, json_file, indent=4)
    json_instance.success()


def convert_csv_to_yaml(csv_input):
    """ Функция, конвертирующая csv файлы в yaml"""
    # while True:
    #     yaml_path = input("Введите полный путь к конечному файлу с расширением .yaml: ")
    #     if os.path.exists(os.path.dirname(yaml_path)) and yaml_path.split('.')[-1].lower() == "yaml":
    #         break
    #     else:
    #         print("Ошибка: Введите корректный путь для сохранения файла в формате: \
    # путь_существующей_папки\название_файла.yaml")
    yaml_instance = FileName("yaml")
    yaml_text = ""
    with open(csv_input, "r", encoding='utf-8') as csv_file:
        with open(f"{os.path.dirname(csv_input)}\{os.path.basename(csv_input).replace('csv', 'yaml')}", "w",
                  encoding="utf-8") as yaml_file:
            csv_read = csv.reader(csv_file, delimiter=',', quotechar='"')
            headers = []
            for row_index, row in enumerate(csv_read):
                if row_index == 0:
                    heading = row
                else:

                    for cell_index, cell in enumerate(row):
                        cell_header = heading[cell_index].lower().replace(" ", "_").replace("-", "")
                        cell_repl = cell.replace("\n", ", ")
                        cell_text = f"{cell_header}: {cell_repl}\n"
                        yaml_text += cell_text
                    yaml_text += "---\n"
            yaml_text += "..."
            yaml_file.write(yaml_text)
    yaml_instance.success()


while True:
    csv_input = input("Введите полный путь к исходному файлу с расширением .csv: ")
    if os.path.isfile(csv_input) and csv_input.split('.')[-1].lower() == "csv":
        break
    else:
        print("Ошибка: Введите действительный адрес файла csv")
while True:
    print('Напишите YAAAML!!! (или просто 1) если хотите конвертировать в yaml формат ')
    print('или JSOOON!!! (или просто 2) если нужно сконвертировать файл в json формат')
    choice = input()
    if choice == "YAAAML!!!" or choice == "1":
        convert_csv_to_yaml(csv_input)
        break
    elif choice == "JSOOON!!!" or choice == "2":
        convert_csv_to_json(csv_input)
        break
    else:
        print("Не выбран ни один из вариантов, повторите ввод")

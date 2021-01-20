import csv
from collections.abc import Iterable

#комментарий для Git
class main_base():
    """Родительский класс для класса child_base"""

    def __init__(self):
        """Конструктор класса main_base
        """
        self.database = []
        self.iterator = 0
    color = 'red'

    @staticmethod
    def reader_file(database):
        """Функция считывает данные для словаря из файла.
        param: database - словарь
        """
        with open('data.csv') as File:
            reader = csv.DictReader(File, delimiter=';')
            for row in reader:
                database.append(row)

    @staticmethod
    def writer_file(database):
        """Функция записывает данные из словаря в файл.
        param: database - словарь
        """
        with open('data.csv', 'w', newline='\n') as out_file:
            writer = csv.DictWriter(out_file, delimiter=';', fieldnames=(
            'number', 'type', 'chastota', 'power', 'temperature', 'series_number'))
            writer.writeheader()
            for row in database:
                writer.writerow(row)


class child_base(main_base):
    """ Этот класс создаёт словарь, а также методы для взаимодейстия со словарём.
    """

    def __init__(self):
        """Конструктор класса child_base
        """
        super().__init__()

    def output_database(self, num):
        """Функция выводит словарь в консоль.
        param: num - параметр для вывода строк
        """
        for i in self.database:
            print(i)

    def use_and_work_iterator_and_generator(self):
        """Функция создаёт итератор и генератор, а потом совершает с ними работу.
        """
        list = []
        for i in range(len(self.database)):
            list.append(int(self.database[i]['temperature']))
        print('Температура каждого станка(итератор):')
        self.iterator = iter(list)
        print(next(self.iterator), next(self.iterator), next(self.iterator))
        # генератор
        print('Генератор:')
        generator = (int(x) * 3 for x in list)
        print(next(generator), next(generator), next(generator))

    def __repr__(self):
        """Функция возвращает определённое значение(в данном случае chastota), когда в неё передаётся экземпляр класса.
        """
        return str(self.database[2]['chastota'])

    def __getitem__(self, item):
        """Функция получает индекс элемента, а потом возвращает элемент списка под этим номером.
        """
        return self.database[item]['type']

    def __setattr__(self, attr, value):
        """Вызывается при попытке присвоения полю экземпляра класса какого-либо значения. Производит проверку на тип данных.
        param: attr - имя атрибута
        param: value - значение, которое должно быть присвоено атрибуту
        """
        if isinstance(value, list):
            self.__dict__[attr] = value
        elif isinstance(value, Iterable):
            self.__dict__[attr] = value
        elif value > -1:
            self.__dict__[attr] = value
        else:
            raise (AttributeError, attr + ' not allowed')


def main():
    """Функция создаёт экземпляр класса child_base. Записывает данные из файла в поля экзмепляра класса.
    """
    
    base = child_base()
    base.reader_file(base.database)
    base.output_database(-1)
    base.use_and_work_iterator_and_generator()
    flag = int(input("Введите: \n1, чтобы отсортировать по типу станка.\n2, чтобы отсортировать по частоте.\n3,чтобы использывать settator \n4, чтобы использывать getitem.\n5, чтобы использовать rerp.\n"))
    if (flag == 1):
        base.database.sort(key=lambda i: i['type'])
        base.output_database(base.database)
    elif (flag == 2):
        base.database.sort(key=lambda i: int(i['chastota']))
        base.output_database(-1)
    elif (flag == 3):
        b = input('Введите значение')
        base.__setattr__(base.color, b)
        print(base.color)
    elif (flag == 4):
        choice_item = int(input("Введите число. Будет выведен тип станка под этим индексом.\n"))
        print("Использовали getiem: ", base[choice_item])
    elif (flag == 5):
        print("Использовали repr: ", base)
    else:
        print("Вы ввели не те данные, пожалуйста, введите цифры от 1 до 5.")
    save_flag = int(input("Введите 1, чтобы сохранить.\n"))
    if (save_flag == 1):
        base.writer_file(base.database)


main()
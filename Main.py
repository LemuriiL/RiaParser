from Parser import Parser

class Main:
    """
    Основной класс. Запускает программу и выводит полученную информацию на экран.
    """

    def __init__(self):
        self.url = 'https://ria.ru/politics/'

    def run(self):
        parser = Parser(self.url)
        parser.parse()


if __name__ == '__main__':
    main = Main()
    main.run()



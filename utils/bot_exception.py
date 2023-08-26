class Error(Exception):
    """Блок кастомных ошибок"""

    def __init__(self, *args) -> None:
        self.data_error = {
            100: 'Ошибка загрузки переменных окружения!',
            101: 'Нарушена конфигурация настроек!'
        }

        if args:
            self.message = f'{args[0]} | {self.data_error[args[0]]}'
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return 'Error {}'.format(self.message)

from abc import ABCMeta


class Warehouse:
    def __init__(self):
        self._store = []

    def add_item(self, item):
        if isinstance(item, OfficeEquipment):
            self._store.append(item)

    def send_item_to_department(self, item_type, items_count, dep, params=None):
        if isinstance(item_type, OfficeEquipment):
            print('На складе нет техники такого типа')

        if items_count < 1:
            print('Количество товара для отправки не может быть меньше 1')
            return

        if params is None:
            params = {}

        items_for_send = []
        for index, item in enumerate(self._store):
            if not isinstance(item, item_type):
                continue

            if params:
                params_match = True
                for key, value in params.items():
                    params_match = key in item.__dict__ and item.__dict__[key] == value

                    if not params_match:
                        break

                if not params_match:
                    continue

            items_for_send.append(self._store.pop(index))
            break

        if len(items_for_send) < items_count:
            print('Недостаточно товара на скаде')
            return

        print(f'Товары успешно отправлены в подразделение "{dep}"')


class OfficeEquipment(metaclass=ABCMeta):
    def __init__(self, manufacturer, model, name=None):
        self._manufacturer = manufacturer
        self._model = model
        self._name = name if name else f'{manufacturer} {model}'

    def __str__(self):
        return self._name


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, printer_type, name=None):
        super().__init__(manufacturer, model, name)
        if printer_type not in ('laser', 'solid_ink'):
            raise ValueError('Wrong type')

        self._type = printer_type


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass

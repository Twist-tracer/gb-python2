from warehouse import Warehouse, Printer

warehouse = Warehouse()

warehouse.add_item(Printer('HP', 'M15w', 'laser', 'LaserJet Pro'))
warehouse.add_item(Printer('Epson', 'M1100', 'solid_ink'))


warehouse.send_item_to_department(Printer, 1, 'Юридический отдел', {
    '_type': 'solid_ink',
})

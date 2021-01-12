from functools import reduce
import json

with open('task7_input.txt', 'r') as file:
    info = [{}, {'average_profit': 0.0}]
    for row in file.readlines():
        company = {}
        (company['name'], company['type'], company['profit'], company['costs']) = row.rstrip().split(' ')

        info[0][company['name']] = int(company['profit']) - int(company['costs'])

    companies_profit = [info[0][profit] for profit in info[0] if info[0][profit] >= 0]
    info[1]['average_profit'] = reduce(lambda carry, item: carry + item, companies_profit) / len(companies_profit)

with open('task7_output.txt', 'w') as file:
    json.dump(info, file)

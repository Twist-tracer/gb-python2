def fact(n):
    for i in range(1, n + 1):
        yield i


fact_number = 4
fact_numbers = []
fact_result = 1
for fact_number in fact(fact_number):
    fact_numbers.append(fact_number)
    fact_result *= fact_number

print(f'{fact_number}! = {" * ".join([str(number) for number in fact_numbers])} = {fact_result}')

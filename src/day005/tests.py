from mortgage_refactored import read_inputs, validate, calculate, format_result


for i in [[500000, 4.8, 25], [10000,0,25], [-2000,-5,0], [2000,-5,0], [2000,5,0]]:
    print(f'Principal: {i[0]}, Rate: {i[1]}, Years: {i[2]}')
    print(f'Validate: {validate(i[0], i[1], i[2])}')
    result = calculate(i[0], i[1], i[2])
    if result is not None:
        print(f'Result: {format_result(calculate(i[0], i[1], i[2]))}')
    else:
        print(f'Result: None')

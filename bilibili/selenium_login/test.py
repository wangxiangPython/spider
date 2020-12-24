code_result = '103,192|218,127|107,113'
result_list = code_result.split('|')
for result in result_list:
    x = result.split(',')[0]
    print(x)
    y = result.split(',')[1]
    print(y)
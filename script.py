def coins():
    source = input()
    try:
        source = int(source)
        one_dollar = source
        rest = 0
    except:
        one_dollar, f_part = source.split('.')
        if len(f_part) == 1:
            f_part += '0'
        rest = int(f_part)

    quarter = 25
    nickel = 10
    dime = 5

    money_dict = {'dollar': 0, 'quarter': 0, 'nickel': 0, 'dime': 0, 'penny': 0}
    money_dict['dollar'] = int(one_dollar)

    while rest >= quarter:
        rest -= quarter
        money_dict['quarter'] += 1

    while rest >= nickel:
        rest -= nickel
        money_dict['nickel'] += 1

    while rest >= dime:
        rest -= dime
        money_dict['dime'] += 1

    money_dict['penny'] = rest
    result = ''
    for key in money_dict:
        new_key = key
        if money_dict[key] > 1:
            if key == 'penny':
                new_key = 'pennies'
            else:
                new_key = key + 's'

        if money_dict[key] == 0:
            pass
        else:
            result += str(money_dict[key]) + ' ' + new_key + '\n'
    print(result)
    return result






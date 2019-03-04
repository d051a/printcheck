'''
Печать кассового чека:
Вот так будет выглядеть итоговый чек:

 _____________________________
|                             |
|Макароны             354 руб.|
|Картофель            435 руб.|
|Помидоры             200 руб.|
|Минеральная вода      50 руб.|
|_____________________________|
'''


PRODUCTS = [
    ['яблоки',100],
    ['швейцарские сырки', 1500],
    ['красная рыба', 450],
]


def checkpositionslist(product_list):
    maxlen_good = len(max(map(
        lambda elem: elem[0], product_list), key=len))
    maxlen_price = len(max(map(
        lambda elem: str(elem[1]), product_list), key=len))
    product_list_out = []
    for good, price in product_list:
        product_list_out.append('{:<{mlg}} {:>{mlp}}'.format(
            good, price, mlg=maxlen_good, mlp=maxlen_price))
    return product_list_out


def printcheck(product_list, horline_sign='_', vertline_sign='|', currency='руб'):
    maxlen_position = len(max(product_list, key=len))
    line = horline_sign * (maxlen_position + len(currency) + 2)
    top_line = ' {} '.format(line)
    print(top_line)
    for good in product_list:
        print('{line}{} {}.{line}'.format(good, currency, line=vertline_sign))
    bottom_line = '{line}{}{line}'.format(line, line=vertline_sign)
    print(bottom_line)


def main(products):
    list = checkpositionslist(products)
    printcheck(list)


if __name__ == '__main__':
    main(PRODUCTS)

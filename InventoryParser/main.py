import ply.lex as lex
import ply.yacc as yacc
import pandas as pd

articles_info = {}


def fill_shop_with_articles():
    csv_article_data = pd.read_csv('shopArticlesInfo.csv').to_string().splitlines()
    csv_article_data.pop(0)
    for row in csv_article_data:
        row = row[1:]
        row = row.replace(" ", '')
        by_columns = row.split(';')
        articles_info[int(by_columns[0])] = int(by_columns[1])


tokens = (
    'NUMBER',
    'OPERATE',
    'SIZE',
    'KIND',
    'COLOR',
    'MATERIAL'
    )


def t_OPERATE(t):
    r'add | remove | show | how | many'
    return t


def t_MATERIAL(t):
    r'metal | plastic'
    if t.value == 'metal':
        t.value = 1
    elif t.value == 'plastic':
        t.value = 2
    return t


def t_COLOR(t):
    r'(black | white | red | green | blue)'
    if t.value == 'black':
        t.value = 1
    elif t.value == 'white':
        t.value = 2
    elif t.value == 'red':
        t.value = 3
    elif t.value == 'green':
        t.value = 4
    elif t.value == 'blue':
        t.value = 5
    return t


def t_SIZE(t):
    r'tiny | small | big | large'
    if t.value == 'tiny':
        t.value = 1
    elif t.value == 'small':
        t.value = 2
    elif t.value == 'big':
        t.value = 3
    elif t.value == 'large':
        t.value = 4
    return t


def t_KIND(t):
    r'box(es)? | ring(s)?'
    if t.value[0] == 'b':
        t.value = 1
    else:
        t.value = 2
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t'


def p_command(p):
    'command : OPERATE NUMBER article'
    index = p[3]
    if p[1] == 'add':
        if articles_info.get(index):
            articles_info[index] += p[2]
            print('\tOK. I am adding ' + str(p[2]) + ' articles indexed as ' + str(index) + '.')
        else:
            articles_info[index] = 0
            articles_info[index] += p[2]
            print('\tOK. I am adding ' + str(p[2]) + ' NEW articles indexed as ' + str(index) + '.')
    elif p[1] == 'remove':
        if articles_info.get(index):
            if p[2] > articles_info[index]:
                print('\tI do not have as many articles as you want to remove.')
            else:
                articles_info[index] -= p[2]
                print('\tOK. I am removing ' + str(p[2]) + ' articles indexed as ' + str(index) + '.')
        else:
            print('\tSorry, there is no article indexed as ' + str(index) + '.')


def p_show_command(p):
    'command : OPERATE'
    if p[1] == 'show':
        for index in articles_info:
            print('\tindex: ' + str(index) + '; available amount: ' + str(articles_info.get(index)))


def p_how_many_command(p):
    'command : OPERATE OPERATE article'
    if p[1] == 'how' and p[2] == 'many':
        index=p[3]
        print('\tindex: ' + str(index) + '; available amount: ' + str(articles_info.get(index)))


def p_attribute_color(p):
    'attribute : COLOR'
    p[0] = p[1]


def p_attribute_material(p):
    'attribute : MATERIAL'
    p[0] = 10 * p[1]


def p_attribute_size(p):
    'attribute : SIZE'
    p[0] = 100 * p[1]


def p_article_kind(p):
    'article : KIND'
    p[0] = 1000 * p[1]


def p_article_attribute(p):
    'article : attribute article'
    p[0] = p[1] + p[2]


def p_error(p):
    print("Syntax error in input!")


lexer = lex.lex()
parser = yacc.yacc()


def main():
    while True:
        try:
            command = input("enter the next command: ")
        except EOFError:
            break
        if not command:
            continue
        elif command == "bye":
            break
        parser.parse(command)


if __name__ == '__main__':
    fill_shop_with_articles()
    main()

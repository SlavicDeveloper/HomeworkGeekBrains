import re

dict_mail = {}
key_1 = "username"
key_2 = "domen"

def mail_parse(address):
    RE_NAME_DOMEN = re.split(r"@", address)
    name = RE_NAME_DOMEN[0]
    domens = RE_NAME_DOMEN[1]

    if not domens == "mail.ru":
        raise ValueError(f'Введен невалидный бомен: {address}')

    dict_mail[key_1] = name
    dict_mail[key_2] = domens

    print(dict_mail)

try:
    mail_parse("mde1533@mail.ru")
except ValueError as msg:
    print(msg)


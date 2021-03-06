from requests import get, utils

request = get("http://www.cbr.ru/scripts/XML_daily.asp")
response = utils.get_unicode_from_response(request)

def currency_rate(cur):
    content = response.split("<Valute ID=")
    for el in content:
        if cur.upper() in el:
            return float(el.replace("/", "").split("<Value>")[-2].replace(",", "."))

print(currency_rate(input()))




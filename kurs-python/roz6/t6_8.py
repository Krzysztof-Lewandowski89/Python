#Dictionary, ważne operacje
options = {
    'env' : 'productions',
    'db' : 'mysql',
    'version' : 1.0,
    'show_errors' : True
}
#del options['db']
# print(options['db'])
# wyrzuci bład bo db juz jest usunięte

#print(options.get('db'))
#tu nie wyrzuci błędy tylko komunikat o braku danego klucza
#print(options.get('version'))

options.update({
    'user': 'admin',
    'app' : 'PoGo',
    'version' : 2.2
})

for key in options:
    print(options[key])

#print(options.values())
#tu zamiast wartości zwróci nam liste (a liste mozemy juz modyfikowac)
print(options.keys())
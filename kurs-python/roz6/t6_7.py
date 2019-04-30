#dictionary 'słownik'
options = {
    'env' : 'productions',
    'db' : 'mysql',
    'version' : 1.0,
    'show_errors' : True
}

options['user'] = 'admin'
#jesli nadpisujemy klucz który nie istnieje, zostanie on dodany do dictionary
print(options['env'])

options['version'] = 2.0
#zmiana wartości klucza version
print(options['version'])
print(options)
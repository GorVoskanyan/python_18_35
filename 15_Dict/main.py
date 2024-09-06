# Dictionary
from pprint import pprint
data = dict()

data['server'] = {
    'host': '127.0.0.1',
    'port': '8000'
}

data['configuration'] = {
    'ssh': {
        'access': 'true',
        'login': 'superuser',
        'password': 'superpassword'
    }
}

# pprint(data, indent=4)

# data['configuration']['ssh']['login'] = 'Aram'
# print(data)

# dict methods
# for i_value in data.values():
#     for j_key in i_value:
#         print(j_key, '-', i_value[j_key])

# print(data['ssh'])
# print(data.get('ssh', {}))


phonebook_dict = {
    'Hermine': '+37491111111',
    'Nare': '+37498888888'
}

other_phonebook_dict = {
    'Aram': '+3741111111',
    'Nare': '+3749777777',
    'Davit': '+3749888888'
}


# phonebook_dict.update(other_phonebook_dict)
# phonebook_dict['Lilit'] = phonebook_dict.pop('Davit')

# d = {i: i ** 2 for i in range(1, 10)}
# print(d)
from collections import defaultdict

default_dict = defaultdict(lambda: 'Unknown key')

site = {
    'html': {
        'head': {
            'title': 'This is my site'
        },
        'body': {
            'div': 'Some block',
            'h1': 'Some title',
            'p': 'Some paragraph'
        }
    }
}



def find_key(struct, key):
    if key in struct:
        return struct[key]

    for substruct in struct.values():
        if isinstance(substruct, dict):
            result = find_key(substruct, key)
            if result != "Unknown key": 
                return result
    return default_dict[key]

   
result = find_key(site, 'h11')
print(result)


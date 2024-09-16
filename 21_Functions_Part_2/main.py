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
            if result is not None:
                return result


result = find_key(site, 'a')
print(result)

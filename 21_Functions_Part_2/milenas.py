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

   
# result = find_key(site, 'html')
# print(result)



# first = ['Ani', 'Jessy', 'Ben']
# second = [1, 2, 3]

# d = dict(zip(second, first))
# print(d)

# d = dict()
#
# def merge_lists(l1, l2):
#     if not l1 or not l2:
#         return dict()
#
#     d[l2[0]] = l1[0]
#     return merge_lists(l1[1:], l2[1:])
#
#
# merge_lists(first, second)
# print(d)



def f(n: int) -> int:
    return sum(i for i in range(3, n) if not i % 3 or not i % 5)

r = f(10)
print(r)
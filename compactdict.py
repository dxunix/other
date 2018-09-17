import sys
from pprint import pprint


class UserProperty:
    def __init__(self, v0, v1, v2, v3, v4):
        self.guido = v0
        self.sarah = v1
        self.barry = v2
        self.rachel = v3
        self.tim = v4

    def __repr__(self):
        return 'UserProperty(%r, %r, %r, %r, %r)' \
                % (self.guido, self.sarah, self.barry, self.rachel, self.tim)


colors = UserProperty('blue', 'orange', 'green', 'yellow', 'red')
cities = UserProperty('austin', 'dallas', 'tuscon', 'reno', 'portland')
fruits = UserProperty('apple', 'banana', 'orange', 'pear', 'peach')

for user in [colors, cities, fruits]:
    print(vars(user))

print(list(map(sys.getsizeof, map(vars, [colors, cities, fruits]))))

print(dict.keys(vars(colors)))

def data():
    keys = 'guido sarah barry rachel tim'.split()
    value1 = ['blue', 'orange', 'green', 'yellow', 'red']
    value2 = ['austin', 'dallas', 'tuscon', 'reno', 'portland']
    value3 = ['apple', 'banana', 'orange', 'pear', 'peach']
    return keys, value1, value2, value3

def data_entries():
    keys, value1, value2, value3 = data()
    hashes = list(map(abs, map(hash, keys)))
    entries = list(zip(hashes, keys, value1))
    comb_entires = list(zip(hashes, keys, value1, value2, value3))
    return hashes, entries, comb_entires


def database():
    keys, value1, value2, value3 = data()
    hashes, entries, comb_entires = data_entries()
    pprint(hashes)
    pprint(entries)
    pprint(comb_entires)


def lisp():
    """
    association list
    """
    keys, value1, value2, value3 = data()
    pprint([
        list(zip(keys, value1)),
        list(zip(keys, value2)),
        list(zip(keys, value3))
    ])


def separate_chaining(number_of_buckets, data_entries):
    buckets = [[] for i in range(number_of_buckets)]
    for pair in data_entries:
        h, key, value = pair
        i = h % number_of_buckets
        buckets[i].append(pair)
    print('%s buckets' % number_of_buckets)
    pprint(buckets)


def demo_sep_chaining(number_of_buckets):
    hashes, entries, comb_entires = data_entries()
    separate_chaining(number_of_buckets, entries)


def open_addressing_linear(table_size, data_entries):
    """
    make the table more dense
    reduce memory allocator demands
    cope with collions with linear probing
    """
    table = [None] * table_size
    for h, key, value in data_entries:
        i = h % table_size
        while table[i] is not None:
            print('cannot allocate %r, %r is taken by %r' % (key, i, table[i][0]))
            i = (i + 1) % table_size
        table[i] = (key, value)
    pprint(table)


def demo_addressing_linear(table_size):
    hashes, entries, comb_entires = data_entries()
    open_addressing_linear(table_size, entries)


def open_addressing_multihash(table_size, data_entries):
    """
    use all the bits in hash and use a liner congrutial random number 
    generator i = 5 * i + 1
    """
    table = [None] * table_size
    for h, key, value in data_entries:
        perturb = h
        i = h % table_size
        while table[i] is not None:
            print('cannot allocate %r, %r is taken by %r' % (key, i, table[i][0]))
            i = (5 * i + perturb + 1) % table_size
            perturb >>= 5
            print('%r, %r' % (i, perturb))
        table[i] = (key, value)
    pprint(table)


def demo_addressing_multihash(table_size):
    hashes, entries, comb_entires = data_entries()
    open_addressing_multihash(table_size, entries)


def compact_and_ordered(table_size, data_entries):
    table = [None] * table_size
    for pos, entry in enumerate (data_entries):
        pprint(pos)
        pprint(entry)
        perturb = h = entry[0]
        i = h % table_size
        while table[i] is not None:
            print('cannot allocate %r, %r is taken by %r' % (entry[1], i,
                                                             data_entries[table[i]][1]))
            i = (5 * i + perturb + 1) % table_size
            perturb >>= 5
            print('%r, %r' % (i, perturb))
        table[i] = pos
    pprint(data_entries)
    pprint(table)


def demo_compact_and_ordered(table_size):
    hashes, entries, comb_entires = data_entries()
    compact_and_ordered(table_size, entries)


def shared_and_compact(table_size, data_entries):
    table = [None] * table_size
    for pos, entry in enumerate (data_entries):
        pprint(pos)
        pprint(entry)
        perturb = h = entry[0]
        i = h % table_size
        while table[i] is not None:
            print('cannot allocate %r, %r is taken by %r' % (entry[1], i,
                                                             data_entries[table[i]][1]))
            i = (5 * i + perturb + 1) % table_size
            perturb >>= 5
            print('%r, %r' % (i, perturb))
        table[i] = pos
    pprint(data_entries)
    pprint(table)


def demo_shared_and_compact(table_size):
    hashes, entries, comb_entires = data_entries()
    shared_and_compact(table_size,comb_entires)

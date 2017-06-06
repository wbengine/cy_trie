import trie
import pytrie
import time

"""
the performance comparation of pytrie (using python build-in type dict())
and the trie (realized by C++ and compile to python using Cython)
Result: (max_order=4, find_epoch=1)
+---------------------------------------------------------------+
|  model       |  create  |  search  |  write  |  memory usage  |
+---------------------------------------------------------------+
|  pytrie      |     9.0s |     6s   |    21s  |    about 1B    |
|  trie        |     2.4s |     2s   |    11s  |    about 500M  |
+---------------------------------------------------------------+
"""


file = 'ptb.train.id'
max_order = 4
find_epoch = 1


def load_data():
    ngram_list = []
    with open(file, 'rt') as f:
        for line in f:
            a = [-1] + [int(i) for i in line.split()] + [-2]
            n = len(a)
            for order in range(1, max_order+1):
                for pos in range(0, n-order+1):
                    ngram_list.append(a[pos: pos+order])

    print('ngram count =', len(ngram_list))
    return ngram_list


def run_pytrie(ngram_list, write_file):
    t = pytrie.node()

    print('create trie...')
    beg = time.time()
    for ngram in ngram_list:
        sub = t.setdefault(ngram, 0)
        sub.data += 1
    print('time=', time.time() - beg, 's')

    print('Search...')
    beg = time.time()
    for i in range(find_epoch):
        for ngram in ngram_list:
            sub = t.find_node(ngram)
            sub.data += 1
    print('time=', time.time() - beg, 's')

    print('write1...')
    beg = time.time()
    with open(write_file + '.1.txt', 'wt') as f:
        for keys, sub in pytrie.trie_iter(t, is_sorted=True):
            f.write(' '.join(str(i) for i in keys) + '\t{}\n'.format(sub.data))
    with open(write_file + '.2.txt', 'wt') as f:
        for n in range(1, max_order+1):
            for keys, sub in pytrie.level_iter(t, n, is_sorted=True):
                f.write(' '.join(str(i) for i in keys) + '\t{}\n'.format(sub.data))
    print('time=', time.time() - beg, 's')


def run_ctrie(ngram_list, write_file):
    t = trie.trie()

    print('create trie...')
    beg = time.time()
    for ngram in ngram_list:
        sub = t.setdefault(ngram, 0)
        sub.data += 1
    print('time=', time.time() - beg, 's')

    print('Search...')
    beg = time.time()
    for i in range(find_epoch):
        for ngram in ngram_list:
            sub = t.find_trie(ngram)
            sub.data += 1
    print('time=', time.time() - beg, 's')

    print('write1...')
    beg = time.time()
    with open(write_file + '.1.txt', 'wt') as f:
        for keys, data in trie.TrieIter(t, True):
            f.write(' '.join(str(i) for i in keys) + '\t{}\n'.format(data))
    with open(write_file + '.2.txt', 'wt') as f:
        for n in range(1, max_order+1):
            for keys, data in trie.LevelIter(t, n, True):
                f.write(' '.join(str(i) for i in keys) + '\t{}\n'.format(data))
    print('time=', time.time() - beg, 's')


if __name__ == '__main__':

    ngram_list = load_data()
    run_pytrie(ngram_list, 'pytrie')
    run_ctrie(ngram_list, 'ctrie')


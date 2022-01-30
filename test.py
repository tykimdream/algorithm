# 4358

from collections import defaultdict
import sys

trees = defaultdict(int)
n = 0

for line in sys.stdin:
    if line == '\n':
        break
    tree = line.rstrip()
    trees[tree] += 1
    n += 1

tree_lst = list(trees.keys())
tree_lst.sort()

for tree in tree_lst:
    print('%s %.4f' % (tree, trees[tree]/n*100))


# test
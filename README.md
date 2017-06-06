
## Introduction

This is a fast trie structure, written with C++ and compiled to python using Cython.

Compared to the pytrie, which is based the python build-in type dict, 
our method achieves 3 time faster and about half memory usage.

We using the two method to exact all the 4gram features in ptb corpus,
the results are shwon as follows:

**result:** 
(max_order=4, find_epoch=1)

|  model       |  create  |  search  |  write  |  memory usage  |
|--------------|----------|----------|---------|----------------|
|  pytrie      |     9.0s |     6s   |    21s  |    about 1B    |
|  trie        |     2.4s |     2s   |    11s  |    about 500M  |    



## Install and compile the trie source codes:

First, you need the python with Cython.

Then to compile the C++ code,  run: 
```shell
python setup.py build_ext --inplace
```

Then run
```shell
python test.py
```
to evaulate the performance.





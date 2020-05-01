# Tips and Tricks for following PEP8
### Knowing Classes & Methods:
One can identify if a class is being referenced or a method is being referenced on a module by knowing the case sensitivitiy.
1. The below convention indicates that the object references on a classs:
```python
    parser = argparse.ArgumentParser()
```
*argparse* is a module\
*ArgumentParser()* is a [class](https://github.com/python/cpython/blob/master/Lib/argparse.py#L1666) and we know that by the Upper cases being used by two different works. Which is the naming convention for classess according to PEP8\
*parser* is the object

2. The below convention indicates that the object references on a method:
```python
    parser.add_argument()
```
*add_argument()* is a [method](https://github.com/python/cpython/blob/master/Lib/argparse.py#L257) and we know that by the lower cases being used. \
*parser* is the previously declared object.\
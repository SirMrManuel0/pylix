# decorator
***

## TODO
***
This decorator gives a warning if a not fully implemented function is called, but still executes it.

Ce Décorateur avertit, si une fonction qui n'a pas encore été implémentée en entier est demandée, mais elle
    s'exécute quand même.

Example:
```python
from pylix.errors import TODO

@TODO
def not_done():
    print("I am doing something.")

not_done()
```
```title="output"
<stdin>:7: UserWarning: not_done - TODO: implementation pending.
  not_done()
I am doing something.
```

with custom message:
```python
from pylix.errors import TODO

@TODO("Needs to be refactored.")
def not_done():
    print("I am doing something.")

not_done()
```
```title="output"
<stdin>:7: UserWarning: not_done - TODO: Needs to be refactored.
  not_done()
I am doing something.
```

## to_test
***
This decorator gives a warning if the testing for the function has not yet been implemented.
The function still executes.

Ce décorateur émet un avertissement si le test de la fonction n'a pas encore été mis en œuvre.
La fonction s'exécute quand même.

Example:
```python
from pylix.errors import to_test

@to_test
def no_tests():
    print("I am not tested.")

no_tests()
```
```title="output"
<stdin>:7: UserWarning: no_tests - to_test: testing pending.
  no_tests()
I am not tested.
```

with a custom message:
```python
from pylix.errors import to_test

@to_test("in test_decorator.py")
def no_tests():
    print("I am not tested.")

no_tests()
```
```title="output"
<stdin>:7: UserWarning: no_tests - to_test: in test_decorator.py.
  no_tests()
I am not tested.
```

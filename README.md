# SetBitCount
A package to count set bits in continuous natural numbers in a range. 
The package can work to find set bit in a number or in a range.

To count set bits in a range, two values are required:
* **start** : The starting natural number from where you want to count set bits.
* **end** : the end of range of natural numbers till where you want to count set bits.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install setbitcounter.

```bash
pip install setbitcounter-pkg
```

## Usage

```python
from setbitcounter.countset import countsetbit
```
- To count set bits of a number:

```python
from setbitcounter.countset import countsetbit
print(countsetbit(3))
```
above code will give output as 2

- To count set bits in range:

```python
from setbitcounter.countset import countsetbit
print(countsetbit(1,7))
```
Above code will give output as 12





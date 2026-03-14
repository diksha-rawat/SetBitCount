# 🔢 SetBitCount

> Count set bits in a single number or across a range of natural numbers — simple, fast and Pythonic.

[![PyPI](https://img.shields.io/pypi/v/setbitcounter-pkg)](https://pypi.org/project/setbitcounter-pkg/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 💡 What is a Set Bit?

A **set bit** is a binary digit that is `1`.

For example:
```
3  in binary  =  011  →  2 set bits
7  in binary  =  111  →  3 set bits
```

This package counts set bits in a single number **or** across an entire range of natural numbers in one call.

---

## 📦 Installation
```bash
pip install setbitcounter-pkg
```

---

## 🚀 Usage
```python
from setbitcounter.countset import countsetbit
```

### Count set bits in a single number:
```python
from setbitcounter.countset import countsetbit

print(countsetbit(3))
# Output: 2
# Because 3 = 011 in binary → 2 set bits
```

### Count set bits across a range:
```python
from setbitcounter.countset import countsetbit

print(countsetbit(1, 7))
# Output: 12
# Counts all set bits in numbers 1, 2, 3, 4, 5, 6, 7
```

---

## 🧠 How the Range Works

| Number | Binary | Set Bits |
|--------|--------|----------|
| 1 | 001 | 1 |
| 2 | 010 | 1 |
| 3 | 011 | 2 |
| 4 | 100 | 1 |
| 5 | 101 | 2 |
| 6 | 110 | 2 |
| 7 | 111 | 3 |
| **Total** | | **12** |

---

## 📬 Connect

[Diksha Rawat](https://linkedin.com/in/yourprofile) | LinkedIn
[dev.to/diksharawat](https://dev.to/diksharawat) | Dev.to

---

*Built with curiosity and Python 🐍*
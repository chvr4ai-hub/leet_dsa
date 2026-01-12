In Python, a **range** is a built-in type that represents a sequence of integers, most commonly used in `for` loops. It’s **lazy** (doesn’t create the full list in memory) and supports **indexing, slicing, and membership checks** efficiently.

---

## 1) Basic syntax

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### Key rule

✅ `stop` is **excluded**.

Examples:

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(1, 10, 2)   # 1, 3, 5, 7, 9
```

---

## 2) Most common usage (for loops)

```python
for i in range(5):
    print(i)
```

Prints: `0 1 2 3 4`

---

## 3) Converting to list (only when needed)

```python
list(range(5))        # [0, 1, 2, 3, 4]
list(range(2, 6))     # [2, 3, 4, 5]
list(range(10, 0, -2)) # [10, 8, 6, 4, 2]
```

---

## 4) Reverse ranges

```python
for i in range(10, 0, -1):
    print(i)
```

This gives: `10 9 8 7 6 5 4 3 2 1`

> Note: `0` is excluded because stop is excluded.

---

## 5) Range + length / indexing / membership

```python
r = range(2, 10, 2)    # 2, 4, 6, 8

len(r)      # 4
r[0]        # 2
r[-1]       # 8
6 in r      # True
7 in r      # False
```

---

## 6) Slicing a range (returns another range)

```python
r = range(0, 20, 2)     # 0,2,4,...,18
r2 = r[2:6]             # 4,6,8,10
list(r2)                # [4, 6, 8, 10]
```

---

## 7) Common mistakes

### ❌ Off-by-one confusion

```python
range(1, 5)  # 1,2,3,4 (not including 5)
```

### ❌ Step cannot be zero

```python
range(1, 10, 0)  # ValueError
```

### ❌ Wrong reverse logic

```python
range(1, 10, -1)  # empty, because it can't go up with a negative step
```

Correct:

```python
range(10, 1, -1)  # 10 down to 2
```

---

## 8) Practical patterns you’ll use daily

### a) Loop N times

```python
for _ in range(n):
    ...
```

### b) Loop with index (classic)

```python
for i in range(len(arr)):
    print(i, arr[i])
```

### c) Better: enumerate (recommended)

```python
for i, val in enumerate(arr):
    print(i, val)
```

### d) Chunking with range

```python
batch_size = 100
for i in range(0, len(items), batch_size):
    batch = items[i:i+batch_size]
```

---
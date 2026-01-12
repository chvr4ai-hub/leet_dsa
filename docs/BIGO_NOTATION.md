# Big-O Notation (Super Basic Summary)

## What Big-O means
Big-O describes how an algorithm’s **time** or **space** usage grows as input size **n** grows.

- It focuses on growth rate for large `n`
- It ignores constants and smaller terms

Example:
- `3n + 10` → **O(n)**
- `n² + 5n + 20` → **O(n²)**

---

## Common Big-O classes (with intuition)

| Big-O | Name | Simple intuition | Example |
|---|---|---|---|
| O(1) | Constant | same work no matter `n` | access `arr[0]` |
| O(log n) | Logarithmic | halves the problem each step | binary search |
| O(n) | Linear | scan once | find max in array |
| O(n log n) | Linearithmic | log levels × n work each level | merge sort |
| O(n²) | Quadratic | compare all pairs | nested loops |
| O(2ⁿ) | Exponential | try all subsets | subset brute force |
| O(n!) | Factorial | try all permutations | permutation brute force |

---

## Quick diagram (growth trends)

```
cost ^
     |                           O(2^n)
     |                      O(n^2)
     |                O(n log n)
     |            O(n)
     |        O(log n)
     |__ O(1) __________________________> n
```

---

## How to calculate **time complexity**

### Rule 1: Drop constants
- `O(2n)` → `O(n)`
- `O(100)` → `O(1)`

### Rule 2: Keep the biggest term
- `O(n² + n)` → `O(n²)`
- `O(n log n + n)` → `O(n log n)`

### Rule 3: Loops
**Single loop**
```python
for i in range(n):
    work()
```
Time: **O(n)**

**Nested loops**
```python
for i in range(n):
    for j in range(n):
        work()
```
Time: **O(n²)**

**Loop that halves**
```python
while n > 1:
    n //= 2
```
Time: **O(log n)**

### Rule 4: Sequential blocks add (then keep biggest)
```python
do_n_work()     # O(n)
do_n2_work()    # O(n^2)
```
Total: `O(n) + O(n²)` → **O(n²)**

### Rule 5: Conditionals (worst-case)
```python
if condition:
    A()
else:
    B()
```
Time: **max(O(A), O(B))**

---

## How to calculate **space complexity**

Space complexity usually means **extra memory** used (auxiliary space), not counting input.

### O(1) extra space
Only a few variables:
```python
total = 0
for x in arr:
    total += x
```

### O(n) extra space
Creating a new array/map of size `n`:
```python
b = [0] * n
```

### Recursion stack space
Depth of recursion uses stack frames:
```python
def f(n):
    if n == 0: return
    f(n-1)
```
Space: **O(n)** (stack depth)

If recursion halves input:
- Depth ≈ `log n` → **O(log n)** stack space

---

## Quick checklist
To estimate Big-O:
1. Identify input size `n`
2. Count loop/recursion repetitions
3. Multiply for nested loops
4. Look for halving → `log n`
5. Keep only the dominant term

---

## Tiny examples

### Find max
- Time: **O(n)**
- Space: **O(1)**

### Merge sort
- Time: **O(n log n)**
- Space: usually **O(n)** (extra arrays)

### Binary search
- Time: **O(log n)**
- Space: **O(1)** (iterative) or **O(log n)** (recursive stack)

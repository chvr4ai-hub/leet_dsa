# CHEATSHEET

## Python `range()` Function
Generates a sequence of integers: `range([start], stop, [step])`.

**Use Cases:**
1. **Standard Loops:**

```python
for i in range(3): print(i) # 0, 1, 2
```
2. **Custom Ranges/Steps:**

```python
list(range(5, 15, 3)) # [5, 8, 11, 14]
```
3. **List Indexing:**

```python
for i in range(len(items)):
    process(items[i])
```

## Python `divmod()` Function
Returns a tuple containing the quotient and the remainder of a division: `divmod(a, b)`.

**Use Cases:**

1. **Time Conversions:**

```python
minutes, seconds = divmod(280, 60) # (4, 40)
```

2. **Pagination/Grids:**

```python
pages, extra = divmod(total_items, page_size)
```
3. **Currency Breakdown:**

```python
dollars, cents = divmod(total_cents, 100)
```

## Singly linked list definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
   
## Time Limit Exceeded Exception
If time complexity exceeds 10^8 operations, it will throw Time Limit Exceeded Exception

## Stackoverflow Error
When stackspace is full we get this error. Especially when a function is called infinitely (recursive functions)
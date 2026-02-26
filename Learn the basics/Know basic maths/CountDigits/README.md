# Count All Digits of a Number

**Problem Statement:**  
Given an integer `N`, return the number of digits in `N`.

---

## 📌 Approaches

### **1. Typecasting (String Conversion)**

Converts the number to a string and counts its length.

```python
class Solution:
    def countDigit(self, n):
        return len(str(abs(n)))  # abs() handles negative numbers
```

---

### **2. Iterative Approach**

Divide the number repeatedly by 10 until it becomes 0.

```python
class Solution:
    def countDigit(self, n):
        n = abs(n)
        count = 0
        while n > 0:
            n //= 10
            count += 1
        return count
```

---

### **3. Using Logarithms**

Uses `log10(n)` which gives `digits - 1`.  
Special case needed for 0.

```python
import math

class Solution:
    def countDigit(self, n):
        n = abs(n)
        if n == 0:
            return 1
        return int(math.log10(n)) + 1
```

---

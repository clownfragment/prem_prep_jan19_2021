# This is Markdown
## this is a smaller header
### this is yet smaller
#### this smaller yet
##### this is the smallest
* bullet point
* another point



<br><br><br><br><br><br><br>

--------------------------


```python
# this is some python
for i in range(20):
    print(i**2)
```

```sql
SELECT * FROM some_table
```

```
this text looks like a system font
```


# Mathjax support in Markdown
* subset of laTEX supported in markdown


# Example: Poisson

[wiki on Poisson](https://en.wikipedia.org/wiki/Poisson_distribution)

$$
\text{Poisson PMF}(\lambda, k)=\frac{e^{-\lambda}\cdot \lambda^k}{k!}
$$

```python
from math import e, factorial
def poisson_pmf(lmbda, k):
    return e**(-lmbda)*lmbda**k / factorial(k)
```
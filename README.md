# Mystery Module

`mystery_module.py` is a tiny utility module for solving quadratic equations.

## Function

### `fn_x(a, b, c)`

- Computes the solutions of the quadratic equation `ax^2 + bx + c = 0`.
- Returns a tuple `(x1, x2)` when the discriminant is non-negative.
- Returns `None` if there are no real roots.

### Behavior

- `d = b**2 - 4*a*c` (discriminant)
- If `d < 0`: returns `None` (complex roots are not handled)
- Otherwise:
  - `x1 = (-b + sqrt(d)) / (2*a)`
  - `x2 = (-b - sqrt(d)) / (2*a)`

## Usage

```python
from mystery_module import fn_x

roots = fn_x(1, -3, 2)
if roots is None:
    print("No real roots")
else:
    x1, x2 = roots
    print(f"Roots: x1={x1}, x2={x2}")
```

## Notes

- The function uses `math.sqrt()` and so requires `a != 0` to avoid division by zero.
- For non-real solutions, modify the function to support complex arithmetic or return complex roots explicitly.

## Potential improvements

- input validation for numeric types
- handle `a == 0` as linear equation `bx + c = 0`
- return complex roots for `d < 0`

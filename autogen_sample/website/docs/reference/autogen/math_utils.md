---
sidebar_label: math_utils
title: autogen.math_utils
---

#### remove\_boxed

```python
def remove_boxed(string: str) -> Optional[str]
```

Source: https://github.com/hendrycks/math
Extract the text within a \boxed{...} environment.

**Example**:

  >>> remove_boxed(\boxed{\frac{2}{3}})
  \frac{2}{3}

#### last\_boxed\_only\_string

```python
def last_boxed_only_string(string: str) -> Optional[str]
```

Source: https://github.com/hendrycks/math
Extract the last \boxed{...} or \fbox{...} element from a string.

#### is\_equiv

```python
def is_equiv(str1: Optional[str], str2: Optional[str]) -> float
```

Returns (as a float) whether two strings containing math are equivalent up to differences of formatting in
- units
- fractions
- square roots
- superfluous LaTeX.
Source: https://github.com/hendrycks/math

#### is\_equiv\_chain\_of\_thought

```python
def is_equiv_chain_of_thought(str1: str, str2: str) -> float
```

Strips the solution first before calling `is_equiv`.

#### eval\_math\_responses

```python
def eval_math_responses(responses, solution=None, **args)
```

Select a response for a math problem using voting, and check if the response is correct if the solution is provided.

**Arguments**:

- `responses` _list_ - The list of responses.
- `solution` _str_ - The canonical solution.
  

**Returns**:

- `dict` - The success metrics.


---
sidebar_label: code_utils
title: autogen.code_utils
---

#### generate\_assertions

```python
def generate_assertions(
        definition: str,
        model: Optional[str] = "gpt-3.5-turbo") -> Tuple[str, float]
```

Generate assertions for a function.

**Arguments**:

- `definition` _str_ - The function definition, including the signature and docstr.
- `model` _str_ - The model used for generation.
  

**Returns**:

- `str` - The generated assertions.
- `float` - The cost of the generation.

#### eval\_function\_completions

```python
def eval_function_completions(
    responses: List[str],
    definition: str,
    test: Optional[str] = None,
    entry_point: Optional[str] = None,
    assertions: Optional[Union[str, Callable[[str], Tuple[str, float]]]] = None
) -> Dict
```

Select a response from a list of responses for the function completion task (using generated assertions), and/or evaluate if the task is successful using a gold test.

**Arguments**:

- `responses` _list_ - The list of responses.
- `definition` _str_ - The input definition.
- `test` _Optional, str_ - The test code.
- `entry_point` _Optional, str_ - The name of the function.
- `assertions` _Optional, str or Callable_ - The assertion code which serves as a filter of the responses, or an assertion generator.
  When provided, only the responses that pass the assertions will be considered for the actual test (if provided).
  

**Returns**:

- `dict` - The success metrics.

#### implement

```python
def implement(
    definition: str,
    configs: List[Dict],
    assertions: Optional[Union[str,
                               Callable[[str],
                                        Tuple[str,
                                              float]]]] = generate_assertions
) -> Tuple[str, float]
```

Implement a function from a definition.

**Arguments**:

- `definition` _str_ - The function definition, including the signature and docstr.
- `configs` _list_ - The list of configurations for completion.
- `assertions` _Optional, str or Callable_ - The assertion code which serves as a filter of the responses, or an assertion generator.
  

**Returns**:

- `str` - The implementation.
- `float` - The cost of the implementation.
- `int` - The index of the configuration which generates the implementation.


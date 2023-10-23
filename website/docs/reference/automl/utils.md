---
sidebar_label: utils
title: automl.utils
---

#### len\_labels

```python
def len_labels(y: np.ndarray,
               return_labels=False) -> Union[int, Optional[np.ndarray]]
```

Get the number of unique labels in y. The non-spark version of
flaml.automl.spark.utils.len_labels

#### unique\_value\_first\_index

```python
def unique_value_first_index(y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]
```

Get the unique values and indices of a pandas series or numpy array.
The non-spark version of flaml.automl.spark.utils.unique_value_first_index


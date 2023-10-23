---
sidebar_label: utils
title: automl.spark.utils
---

#### to\_pandas\_on\_spark

```python
def to_pandas_on_spark(
    df: Union[pd.DataFrame, DataFrame, pd.Series, ps.DataFrame, ps.Series],
    index_col: Optional[str] = None,
    default_index_type: Optional[str] = "distributed-sequence"
) -> Union[ps.DataFrame, ps.Series]
```

Convert pandas or pyspark dataframe/series to pandas_on_Spark dataframe/series.

**Arguments**:

- `df` - pandas.DataFrame/series or pyspark dataframe | The input dataframe/series.
- `index_col` - str, optional | The column name to use as index, default None.
- `default_index_type` - str, optional | The default index type, default "distributed-sequence".
  

**Returns**:

- `pyspark.pandas.DataFrame/Series` - The converted pandas-on-Spark dataframe/series.
  
```python
import pandas as pd
from flaml.automl.spark.utils import to_pandas_on_spark

pdf = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
psdf = to_pandas_on_spark(pdf)
print(psdf)

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
sdf = spark.createDataFrame(pdf)
psdf = to_pandas_on_spark(sdf)
print(psdf)

pds = pd.Series([1, 2, 3])
pss = to_pandas_on_spark(pds)
print(pss)
```

#### train\_test\_split\_pyspark

```python
def train_test_split_pyspark(
    df: Union[DataFrame, ps.DataFrame],
    stratify_column: Optional[str] = None,
    test_fraction: Optional[float] = 0.2,
    seed: Optional[int] = 1234,
    to_pandas_spark: Optional[bool] = True,
    index_col: Optional[str] = "tmp_index_col"
) -> Tuple[Union[DataFrame, ps.DataFrame], Union[DataFrame, ps.DataFrame]]
```

Split a pyspark dataframe into train and test dataframes.

**Arguments**:

- `df` - pyspark.sql.DataFrame | The input dataframe.
- `stratify_column` - str | The column name to stratify the split. Default None.
- `test_fraction` - float | The fraction of the test data. Default 0.2.
- `seed` - int | The random seed. Default 1234.
- `to_pandas_spark` - bool | Whether to convert the output to pandas_on_spark. Default True.
- `index_col` - str | The column name to use as index. Default None.
  

**Returns**:

  pyspark.sql.DataFrame/pandas_on_spark DataFrame | The train dataframe.
  pyspark.sql.DataFrame/pandas_on_spark DataFrame | The test dataframe.

#### unique\_pandas\_on\_spark

```python
def unique_pandas_on_spark(
        psds: Union[ps.Series, ps.DataFrame]) -> Tuple[np.ndarray, np.ndarray]
```

Get the unique values and counts of a pandas_on_spark series.

#### len\_labels

```python
def len_labels(y: Union[ps.Series, np.ndarray],
               return_labels=False) -> Union[int, Optional[np.ndarray]]
```

Get the number of unique labels in y.

#### unique\_value\_first\_index

```python
def unique_value_first_index(
    y: Union[pd.Series, ps.Series,
             np.ndarray]) -> Tuple[np.ndarray, np.ndarray]
```

Get the unique values and indices of a pandas series,
pandas_on_spark series or numpy array.

#### iloc\_pandas\_on\_spark

```python
def iloc_pandas_on_spark(
    psdf: Union[ps.DataFrame, ps.Series, pd.DataFrame, pd.Series],
    index: Union[int, slice, list],
    index_col: Optional[str] = "tmp_index_col"
) -> Union[ps.DataFrame, ps.Series]
```

Get the rows of a pandas_on_spark dataframe/series by index.

#### spark\_kFold

```python
def spark_kFold(
    dataset: Union[DataFrame, ps.DataFrame],
    nFolds: int = 3,
    foldCol: str = "",
    seed: int = 42,
    index_col: Optional[str] = "tmp_index_col"
) -> List[Tuple[ps.DataFrame, ps.DataFrame]]
```

Generate k-fold splits for a Spark DataFrame.
Adopted from https://spark.apache.org/docs/latest/api/python/_modules/pyspark/ml/tuning.html#CrossValidator

**Arguments**:

- `dataset` - DataFrame / ps.DataFrame. | The DataFrame to split.
- `nFolds` - int | The number of folds. Default is 3.
- `foldCol` - str | The column name to use for fold numbers. If not specified,
  the DataFrame will be randomly split. Default is "".
  The same group will not appear in two different folds (the number of
  distinct groups has to be at least equal to the number of folds).
  The folds are approximately balanced in the sense that the number of
  distinct groups is approximately the same in each fold.
- `seed` - int | The random seed. Default is 42.
- `index_col` - str | The name of the index column. Default is "tmp_index_col".
  

**Returns**:

  A list of (train, validation) DataFrames.


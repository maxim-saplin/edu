---
sidebar_label: task
title: automl.task.task
---

## Task Objects

```python
class Task(ABC)
```

Abstract base class for a machine learning task.

Class definitions should implement abstract methods and provide a non-empty dictionary of estimator classes.
A Task can be suitable to be used for multiple machine-learning tasks (e.g. classification or regression) or be
implemented specifically for a single one depending on the generality of data validation and model evaluation methods
implemented. The implementation of a Task may optionally use the training data and labels to determine data and task
specific details, such as in determining if a problem is single-label or multi-label.

FLAML evaluates at runtime how to behave exactly, relying on the task instance to provide implementations of
operations which vary between tasks.

#### \_\_init\_\_

```python
def __init__(task_name: str,
             X_train: Optional[Union[np.ndarray, pd.DataFrame]] = None,
             y_train: Optional[Union[np.ndarray, pd.DataFrame,
                                     pd.Series]] = None)
```

Constructor.

**Arguments**:

- `task_name` - String name for this type of task. Used when the Task can be generic and implement a number of
  types of sub-task.
- `X_train` - Optional. Some Task types may use the data shape or features to determine details of their usage,
  such as in binary vs multilabel classification.
- `y_train` - Optional. Some Task types may use the data shape or features to determine details of their usage,
  such as in binary vs multilabel classification.

#### \_\_str\_\_

```python
def __str__() -> str
```

Name of this task type.

#### evaluate\_model\_CV

```python
@abstractmethod
def evaluate_model_CV(
        config: dict,
        estimator: "flaml.automl.ml.BaseEstimator",
        X_train_all: Union[np.ndarray, pd.DataFrame],
        y_train_all: Union[np.ndarray, pd.DataFrame, pd.Series],
        budget: int,
        kf,
        eval_metric: str,
        best_val_loss: float,
        log_training_metric: bool = False,
        fit_kwargs: Optional[dict] = {}) -> Tuple[float, float, float, float]
```

Evaluate the model using cross-validation.

**Arguments**:

- `config` - configuration used in the evaluation of the metric.
- `estimator` - Estimator class of the model.
- `X_train_all` - Complete training feature data.
- `y_train_all` - Complete training target data.
- `budget` - Training time budget.
- `kf` - Cross-validation index generator.
- `eval_metric` - Metric name to be used for evaluation.
- `best_val_loss` - Best current validation-set loss.
- `log_training_metric` - Bool defaults False. Enables logging of the training metric.
- `fit_kwargs` - Additional kwargs passed to the estimator's fit method.
  

**Returns**:

  validation loss, metric value, train time, prediction time

#### validate\_data

```python
@abstractmethod
def validate_data(automl: "flaml.automl.automl.AutoML",
                  state: "flaml.automl.state.AutoMLState",
                  X_train_all: Union[np.ndarray, pd.DataFrame, None],
                  y_train_all: Union[np.ndarray, pd.DataFrame, pd.Series,
                                     None],
                  dataframe: Union[pd.DataFrame, None],
                  label: str,
                  X_val: Optional[Union[np.ndarray, pd.DataFrame]] = None,
                  y_val: Optional[Union[np.ndarray, pd.DataFrame,
                                        pd.Series]] = None,
                  groups_val: Optional[List[str]] = None,
                  groups: Optional[List[str]] = None)
```

Validate that the data is suitable for this task type.

**Arguments**:

- `automl` - The AutoML instance from which this task has been constructed.
- `state` - The AutoMLState instance for this run.
- `X_train_all` - The complete data set or None if dataframe is supplied.
- `y_train_all` - The complete target set or None if dataframe is supplied.
- `dataframe` - A dataframe constaining the complete data set with targets.
- `label` - The name of the target column in dataframe.
- `X_val` - Optional. A data set for validation.
- `y_val` - Optional. A target vector corresponding to X_val for validation.
- `groups_val` - Group labels (with matching length to y_val) or group counts (with sum equal to length of y_val)
  for validation data. Need to be consistent with groups.
- `groups` - Group labels (with matching length to y_train) or groups counts (with sum equal to length of y_train)
  for training data.
  

**Raises**:

- `AssertionError` - The data provided is invalid for this task type and configuration.

#### prepare\_data

```python
@abstractmethod
def prepare_data(state: "flaml.automl.state.AutoMLState",
                 X_train_all: Union[np.ndarray, pd.DataFrame],
                 y_train_all: Union[np.ndarray, pd.DataFrame, pd.Series, None],
                 auto_augment: bool,
                 eval_method: str,
                 split_type: str,
                 split_ratio: float,
                 n_splits: int,
                 data_is_df: bool,
                 sample_weight_full: Optional[List[float]] = None)
```

Prepare the data for fitting or inference.

**Arguments**:

- `automl` - The AutoML instance from which this task has been constructed.
- `state` - The AutoMLState instance for this run.
- `X_train_all` - The complete data set or None if dataframe is supplied. Must
  contain the target if y_train_all is None
- `y_train_all` - The complete target set or None if supplied in X_train_all.
- `auto_augment` - If true, task-specific data augmentations will be applied.
- `eval_method` - A string of resampling strategy, one of ['auto', 'cv', 'holdout'].
- `split_type` - str or splitter object, default="auto" | the data split type.
  * A valid splitter object is an instance of a derived class of scikit-learn
  [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold)
  and have ``split`` and ``get_n_splits`` methods with the same signatures.
  Set eval_method to "cv" to use the splitter object.
  * Valid str options depend on different tasks.
  For classification tasks, valid choices are
  ["auto", 'stratified', 'uniform', 'time', 'group']. "auto" -> stratified.
  For regression tasks, valid choices are ["auto", 'uniform', 'time'].
  "auto" -> uniform.
  For time series forecast tasks, must be "auto" or 'time'.
  For ranking task, must be "auto" or 'group'.
- `split_ratio` - A float of the valiation data percentage for holdout.
- `n_splits` - An integer of the number of folds for cross - validation.
- `data_is_df` - True if the data was provided as a pd.DataFrame else False.
- `sample_weight_full` - A 1d arraylike of the sample weight.
  

**Raises**:

- `AssertionError` - The configuration provided is invalid for this task type and data.

#### decide\_split\_type

```python
@abstractmethod
def decide_split_type(split_type: str,
                      y_train_all: Union[np.ndarray, pd.DataFrame, pd.Series,
                                         None],
                      fit_kwargs: dict,
                      groups: Optional[List[str]] = None) -> str
```

Choose an appropriate data split type for this data and task.

If split_type is 'auto' then this is determined based on the task type and data.
If a specific split_type is requested then the choice is validated to be appropriate.

**Arguments**:

- `split_type` - Either 'auto' or a task appropriate split type.
- `y_train_all` - The complete set of targets.
- `fit_kwargs` - Additional kwargs passed to the estimator's fit method.
- `groups` - Optional. Group labels (with matching length to y_train) or groups counts (with sum equal to length
  of y_train) for training data.
  

**Returns**:

  The determined appropriate split type.
  

**Raises**:

- `AssertionError` - The requested split_type is invalid for this task, configuration and data.

#### preprocess

```python
@abstractmethod
def preprocess(
    X: Union[np.ndarray, pd.DataFrame],
    transformer: Optional["flaml.automl.data.DataTransformer"] = None
) -> Union[np.ndarray, pd.DataFrame]
```

Preprocess the data ready for fitting or inference with this task type.

**Arguments**:

- `X` - The data set to process.
- `transformer` - A DataTransformer instance to be used in processing.
  

**Returns**:

  The preprocessed data set having the same type as the input.

#### default\_estimator\_list

```python
@abstractmethod
def default_estimator_list(estimator_list: Union[List[str], str] = "auto",
                           is_spark_dataframe: bool = False) -> List[str]
```

Return the list of default estimators registered for this task type.

If 'auto' is provided then the default list is returned, else the provided list will be validated given this task
type.

**Arguments**:

- `estimator_list` - Either 'auto' or a list of estimator names to be validated.
- `is_spark_dataframe` - True if the data is a spark dataframe.
  

**Returns**:

  A list of valid estimator names for this task type.

#### default\_metric

```python
@abstractmethod
def default_metric(metric: str) -> str
```

Return the default metric for this task type.

If 'auto' is provided then the default metric for this task will be returned. Otherwise, the provided metric name
is validated for this task type.

**Arguments**:

- `metric` - The name of a metric to be used in evaluation of models during fitting or validation.
  

**Returns**:

  The default metric, or the provided metric if it is valid for this task type.

#### \_\_eq\_\_

```python
def __eq__(other: str) -> bool
```

For backward compatibility with all the string comparisons to task

#### estimator\_class\_from\_str

```python
@classmethod
def estimator_class_from_str(
        cls, estimator_name: str) -> "flaml.automl.ml.BaseEstimator"
```

Determine the estimator class corresponding to the provided name.

**Arguments**:

- `estimator_name` - Name of the desired estimator.
  

**Returns**:

  The estimator class corresponding to the provided name.
  

**Raises**:

- `ValueError` - The provided estimator_name has not been registered for this task type.


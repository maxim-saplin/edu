---
sidebar_label: metrics
title: automl.spark.metrics
---

#### spark\_metric\_loss\_score

```python
def spark_metric_loss_score(metric_name: str,
                            y_predict: ps.Series,
                            y_true: ps.Series,
                            sample_weight: ps.Series = None,
                            groups: ps.Series = None) -> float
```

Compute the loss score of a metric for spark models.

**Arguments**:

- `metric_name` - str | the name of the metric.
- `y_predict` - ps.Series | the predicted values.
- `y_true` - ps.Series | the true values.
- `sample_weight` - ps.Series | the sample weights. Default: None.
- `groups` - ps.Series | the group of each row. Default: None.
  

**Returns**:

  float | the loss score. A lower value indicates a better model.


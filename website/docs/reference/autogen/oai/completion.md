---
sidebar_label: completion
title: autogen.oai.completion
---

#### get\_key

```python
def get_key(config)
```

Get a unique identifier of a configuration.

**Arguments**:

- `config` _dict or list_ - A configuration.
  

**Returns**:

- `tuple` - A unique identifier which can be used as a key for a dict.

## Completion Objects

```python
class Completion()
```

A class for OpenAI completion API.

It also supports: ChatCompletion, Azure OpenAI API.

#### set\_cache

```python
@classmethod
def set_cache(cls, seed=41, cache_path=".cache")
```

Set cache path.

**Arguments**:

- `seed` _int, Optional_ - The integer identifier for the pseudo seed.
  Results corresponding to different seeds will be cached in different places.
- `cache_path` _str, Optional_ - The root path for the cache.
  The complete cache path will be {cache_path}/{seed}.

#### tune

```python
@classmethod
def tune(cls,
         data,
         metric,
         mode,
         eval_func,
         log_file_name=None,
         inference_budget=None,
         optimization_budget=None,
         num_samples=1,
         logging_level=logging.WARNING,
         **config)
```

Tune the parameters for the OpenAI API call.

TODO: support parallel tuning with ray or spark.
TODO: support agg_method as in test

**Arguments**:

- `data` _list_ - The list of data points.
- `metric` _str_ - The metric to optimize.
- `mode` _str_ - The optimization mode, "min" or "max.
- `eval_func` _Callable_ - The evaluation function for responses.
  The function should take a list of responses and a data point as input,
  and return a dict of metrics. For example,
  
```python
def eval_func(responses, **data):
    solution = data["solution"]
    success_list = []
    n = len(responses)
    for i in range(n):
        response = responses[i]
        succeed = is_equiv_chain_of_thought(response, solution)
        success_list.append(succeed)
    return {
        "expected_success": 1 - pow(1 - sum(success_list) / n, n),
        "success": any(s for s in success_list),
    }
```
  
- `log_file_name` _str, optional_ - The log file.
- `inference_budget` _float, optional_ - The inference budget, dollar per instance.
- `optimization_budget` _float, optional_ - The optimization budget, dollar in total.
- `num_samples` _int, optional_ - The number of samples to evaluate.
  -1 means no hard restriction in the number of trials
  and the actual number is decided by optimization_budget. Defaults to 1.
- `logging_level` _optional_ - logging level. Defaults to logging.WARNING.
- `**config` _dict_ - The search space to update over the default search.
  For prompt, please provide a string/Callable or a list of strings/Callables.
  - If prompt is provided for chat models, it will be converted to messages under role "user".
  - Do not provide both prompt and messages for chat models, but provide either of them.
  - A string template will be used to generate a prompt for each data instance
  using `prompt.format(**data)`.
  - A callable template will be used to generate a prompt for each data instance
  using `prompt(data)`.
  For stop, please provide a string, a list of strings, or a list of lists of strings.
  For messages (chat models only), please provide a list of messages (for a single chat prefix)
  or a list of lists of messages (for multiple choices of chat prefix to choose from).
  Each message should be a dict with keys "role" and "content". The value of "content" can be a string/Callable template.
  

**Returns**:

- `dict` - The optimized hyperparameter setting.
- `tune.ExperimentAnalysis` - The tuning results.

#### create

```python
@classmethod
def create(cls,
           context: Optional[Dict] = None,
           use_cache: Optional[bool] = True,
           **config)
```

Make a completion for a given context.

**Arguments**:

- `context` _dict, Optional_ - The context to instantiate the prompt.
  It needs to contain keys that are used by the prompt template.
  E.g., `prompt="Complete the following sentence: {prefix}"`.
- ``context={"prefix"` - "Today I feel"}`.
  The actual prompt sent to OpenAI will be:
  "Complete the following sentence: Today I feel".
- `use_cache` _bool, Optional_ - Whether to use cached responses.
- `**config` - Configuration for the completion.
  Besides the parameters for the openai API call, it can also contain a seed (int) for the cache.
  This is useful when implementing "controlled randomness" for the completion.
  Also, the "prompt" or "messages" parameter can contain a template (str or Callable) which will be instantiated with the context.
  

**Returns**:

  Responses from OpenAI API.

#### test

```python
@classmethod
def test(cls,
         data,
         config,
         eval_func=None,
         use_cache=True,
         agg_method="avg",
         return_responses_and_per_instance_result=False,
         logging_level=logging.WARNING)
```

Evaluate the responses created with the config for the OpenAI API call.

**Arguments**:

- `data` _list_ - The list of test data points.
- `config` _dict_ - Hyperparameter setting for the openai api call.
- `eval_func` _Callable_ - The evaluation function for responses per data instance.
  The function should take a list of responses and a data point as input,
  and return a dict of metrics. You need to either provide a valid callable
  eval_func; or do not provide one (set None) but call the test function after
  calling the tune function in which a eval_func is provided.
  In the latter case we will use the eval_func provided via tune function.
  Defaults to None.
  
```python
def eval_func(responses, **data):
    solution = data["solution"]
    success_list = []
    n = len(responses)
    for i in range(n):
        response = responses[i]
        succeed = is_equiv_chain_of_thought(response, solution)
        success_list.append(succeed)
    return {
        "expected_success": 1 - pow(1 - sum(success_list) / n, n),
        "success": any(s for s in success_list),
    }
```
- `use_cache` _bool, Optional_ - Whether to use cached responses. Defaults to True.
- `agg_method` _str, Callable or a dict of Callable_ - Result aggregation method (across
  multiple instances) for each of the metrics. Defaults to 'avg'.
  An example agg_method in str:
  
```python
agg_method = 'median'
```
  An example agg_method in a Callable:
  
```python
agg_method = np.median
```
  
  An example agg_method in a dict of Callable:
  
```python
agg_method={'median_success': np.median, 'avg_success': np.mean}
```
  
- `return_responses_and_per_instance_result` _bool_ - Whether to also return responses
  and per instance results in addition to the aggregated results.
- `logging_level` _optional_ - logging level. Defaults to logging.WARNING.
  

**Returns**:

  None when no valid eval_func is provided in either test or tune;
  Otherwise, a dict of aggregated results, responses and per instance results if `return_responses_and_per_instance_result` is True;
  Otherwise, a dict of aggregated results (responses and per instance results are not returned).

#### cost

```python
@classmethod
def cost(cls, model: str, response: dict)
```

Compute the cost of an API call.

**Arguments**:

- `model` _str_ - The model name.
- `response` _dict_ - The response from OpenAI API.
  

**Returns**:

  The cost in USD.

#### extract\_text

```python
@classmethod
def extract_text(cls, response: dict) -> List[str]
```

Extract the text from a completion or chat response.

**Arguments**:

- `response` _dict_ - The response from OpenAI API.
  

**Returns**:

  A list of text in the responses.

## ChatCompletion Objects

```python
class ChatCompletion(Completion)
```

A class for OpenAI API ChatCompletion.


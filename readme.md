# hug_raven

[Sentry](https://sentry.io/) integration for [hug](http://hug.rest/) Python framework.

## Installation

```
pip install hug_raven
```

## Usage

```python
import hug
from hug_raven import Sentry

@hug.get('/0')
def divide_by_zero():
    return 1 / 0

api = hug.API(__name__)
sentry = Sentry(api)
```

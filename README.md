# Att (Apitalks Talker)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Python3 library. Wrapper for [Apitalks API](https://www.api.store/) calls. Enables simple call for api resource via `query` method with optional use of available parameters, as specified in [Apitalks documentation](https://www.api.store/czso.cz/dokumentace#section/Query-parametry).

## Getting Started <a name = "getting_started"></a>

These instructions will get you up and running.

### Prerequisites

What things you need to install the software.

    - Python 3+

### Installing

To install this package, simply use standard `pip install att` or clone this repo and run `python setup.py install`.

## Usage <a name = "usage"></a>

att is used as any other library.

```
from att import API

api = API("yourAPIkeygoeshere")
data = api.query([resource], [...params])
```


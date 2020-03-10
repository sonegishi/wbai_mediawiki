# WBAI Semantic MediaWiki

[WBAI Semantic MediaWiki](http://wbai2.xsrv.jp/mediawiki/index.php?title=Main_Page) is a wiki that stores a neuroscience-based brain framework database, which allows users to draw a brain information flow (BIF).

## Getting Started

```shell
pip install -r requirements.txt
```

## Usage

```python
from circuit import Circuit
import pandas as pd

index = ['names', 'hasParts', 'taxon', 'functionality', 'references','implementations', 'equivalentTo', 'uniform', 'size', 'transmitter']
data = ['anterior superior temporal cortex', None, None, None, None, None, 'TANJI:anterior superior temporal cortex', False, None, None]
series = pd.Series(data, index=index)
circuit = Circuit(series)
circuit.export_bif()
```

### Sample Output
```
{{Circuit|names=anterior superior temporal cortex@en|hasParts=None|taxons=None|functionalAnnotation=None|references=None|implementations=None|equivalentTo=TANJI:anterior superior temporal cortex|size=10}}
```

## Contributors
- So Negishi ([@sonegishi](https://github.com/sonegishi))

## License
[MIT](https://choosealicense.com/licenses/mit/)

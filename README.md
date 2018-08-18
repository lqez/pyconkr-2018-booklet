# pyconkr-2018-booklet

This creates the program booklet of PyCon Korea 2018
 - About this work: <https://speakerdeck.com/lqez/pycon-by-python>

## Requisites

 - PrinceXML: <https://www.princexml.com/>
 - Or, DocRaptor account: <https://docraptor.com/>

## Usage

### Preparation

In a proper python environment,

```
$ pip install -r requirements.txt
```

### Via PrinceXML

```
$ python build.py
```


### Via DocRaptor

```
$ TARGET=production DOCRAPTOR_APIKEY=<your_api_key> python build.py
```

## License

Source code license: [![CCO License](https://img.shields.io/badge/license-CC0-blue.svg?style=plastic "CC0 License")](#contributing-and-license)
Entire contents from PyCon Korea are courtesy of PyCon Korea Organizing Team

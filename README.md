#### Status

![Tests](https://github.com/figtreez/pluckpalette/actions/workflows/tests.yml/badge.svg)

## 🎨🪄 pluck-palette 🪄🎨

CLI tool that returns dominant colors given a local path to an image or url.

##### TOC

- [demo](#demo)
- [setup](#setup)
- [tools](#tools)
- [acknowledgements](#acknowledgements)
- [artwork](#artwork)
- [misc notes](#misc-notes)

##### Demo

<img alt="Demo" src="https://github.com/figtreez/pluck-palette/blob/main/tests/data/demo2.gif?raw=true" width="600" />

#### Setup

```bash
#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
# `python3 -m tox -e {envname}` for specific tox pyenv environments (see tox.ini)
python3 -m tox
```

#### Tools

- pyscaffold
- tox
- scikit-learn
- numpy

#### Acknowledgements

Test images, prior art, and inspo.

- [Google Cloud Vision API](https://cloud.google.com/vision#section-2)
- [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering)
- [k-means eli5](https://www.youtube.com/watch?v=IuRb3y8qKX4)
- [Primer Prism](https://primer.style/prism/)
- [Artwork](#artwork)

#### Artwork

- [Micha Huigen](https://www.michahuigen.com/)
- [The README Project](https://github.com/readme)

#### Misc Notes

- .venv is unnecessary as .tox/{env}/bin/activate already contains several different venvs
- Have better badge management

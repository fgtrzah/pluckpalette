#### Status

![Tests](https://github.com/figtreez/pluck-palette/actions/workflows/tests.yml/badge.svg)

## pluckpalette

CLI tool that returns dominant colors given a local path to an image.

##### TOC

- [demo](#demo)
- [setup](#setup)
- [tools](#tools)
- [acknowledgements](#acknowledgements)
- [artwork](#artwork)
- [misc notes](#misc-notes)

##### Demo

Single file processing

<img alt="Demo" src="https://github.com/fgtrzah/pluckpalette/blob/main/tests/data/demo2.gif?raw=true" width="600" />

Flattened directory bulk

<img alt="Demo" src="https://github.com/fgtrzah/pluckpalette/blob/main/tests/data/demo.gif?raw=true" width="300" />

#### Setup tests

```bash
#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
# `python3 -m tox -e {envname}` for specific tox pyenv environments (see tox.ini)
python3 -m tox
```

#### Quick-start

This assumes tests have been setup and .venv activated

```bash
#!/bin/bash
# image url https://github.com/figtreez/pluckpalette/blob/main/tests/data/02.png
python3 -m pip install -e .
pluckpalette -p tests/data/01.png
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

#### Art credits

- [Micha Huigen](https://www.michahuigen.com/)
- [The README Project](https://github.com/readme)

#!/bin/bash
set -e
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install tox

# `python3 -m tox -e {envname}` for specific tox pyenv environments (see tox.ini)
tox

if [ $? -ne 0 ]
then
  echo "error setting up dev environment"
  exit 1
else
  echo "successful"
fi

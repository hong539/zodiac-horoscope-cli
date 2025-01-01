#!/usr/bin/env bash
set -euxo pipefail

pyenv install 3.13.1
pyenv local 3.13.1

poetry init
poetry shell
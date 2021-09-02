#!/usr/bin/env bash

python3 -m build
pip install ./dist/config-client-sm-0.0.1.tar.gz
pytest  -rA

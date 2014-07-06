#!/usr/bin/env bash
SCRIPT_DIR=$(dirname ${BASH_SOURCE[0]})
ROOT_DIR=$(dirname $SCRIPT_DIR)
python $ROOT_DIR/server.py

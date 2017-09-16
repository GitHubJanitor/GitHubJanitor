#!/bin/bash -eux

# Script to set up a Django project on a virtualenv.

# Installation settings
PROJECT_NAME="GitHubJanitor"
VIRTUALENV_NAME=$PROJECT_NAME
VIRTUALENV_DIR=.virtualenv

# virtualenv global setup
if ! command -v pip; then
    sudo easy_install -U pip
fi

# virtualenv setup
python3 -m venv $VIRTUALENV_DIR
$VIRTUALENV_DIR/bin/pip install -U -r requirements.txt
source $VIRTUALENV_DIR/bin/activate

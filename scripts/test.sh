#!/bin/bash


sudo apt-get install python3-venv -y
python3 -m venv venv


source venv/bin/activate

pip3 install -r requirements.txt
python3 -m pytest --cov --cov-config=.coveragerc --cov-report=term-missing --cov-report xml:coverage.xml --junitxml junit.xml


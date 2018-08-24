## Remote server for VOIP hack demo


uses Pipenv
https://pypi.org/project/pipenv/


### Setup

Clone repo, cd into project

Python 3 only

    pip3 install pipenv

create a virtual environment

    pipenv --three

install deps

    pipenv install

activate shell

    pipenv shell

run bash script

    chmod +x run_flask.sh

    ./run_flask.sh


### API

App has 2 endpoints

1. Post command

    /add_cmd

2. Get command by id

    /get/id
    
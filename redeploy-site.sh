#!/bin/bash

# Kill currently running flask portfolio server
tmux kill-session -t portfolio

# Makes sure git repo inside the VPS has the latest changes from the main branch on github
cd Flask-Portfolio
git fetch && git reset origin/main --hard

# Enter python virtual environmen
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate

# Install python dependenvies
pip install -r requirements.txt

# start a new detached tmux server and runs the site there
tmux new -ds portfolio 'python -m venv python3-virtualenv;
source python3-virtualenv/bin/activate;
pip install -r requirements.txt;
flask run --host=0.0.0.0;
exec $SHELL'
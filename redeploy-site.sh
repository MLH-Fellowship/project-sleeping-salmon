#!/bin/bash

# Makes sure git repo inside the VPS has the latest changes from the main branch on github
cd Flask-Portfolio
git fetch && git reset origin/main --hard

# Enter python virtual environmen
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate

# Install python dependenvies
pip install -r requirements.txt

# Reload changes and restart the service
systemctl daemon-reload
systemctl restart myportfolio

# Uncomment to display status of the service
# systemctl status myportfolio
# Uncomment to see the full journal
# journalctl -u myportfolio
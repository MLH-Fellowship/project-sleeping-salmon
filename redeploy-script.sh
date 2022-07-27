
 #!/bin/bash


cd AriannaR

git fetch && git reset origin/main --hard

source python3-virtualvenv/bin/activate 

pip install -r requirements.txt

systemctl restart myportfolio
                                                            packages (from importlib

                  
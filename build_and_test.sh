#!/bin/bash

pip3 install flask
pip3 install py-healthcheck
pip3 install typing
pip3 install requests
echo "Initiating API"
cd src
python3 api.py &


pip3 install tox==2.5.0
pip3 install pathlib2
echo "Running Test cases"
cd ../test
tox &

fg

while :
do
  echo "Press <CTRL+C> to exit."
  sleep 1
done

# Instructions:

1. Docker image can be created by running ```./build.sh```
2. API can be run separately by ```python3 src/api.py```
3. tox can be run separately by ```tox``` in ```test``` folder

Docker image once formed can be run in interactive mode by command:
```bash
docker run -it -p 5000:5000 --entrypoint /bin/bash flask-task-satish
```

Here: ```5000:5000``` port is needed as Application is hosted on host ```http://0.0.0.0:5000```
     ```flask-task-satish``` - is my docker image name

Docker image can be run using command:
```bash
sudo docker run -it -p 5000:5000 flask-task-satish
```
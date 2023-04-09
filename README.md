# Docker ENTRYPOINT/CMD Container Test

app.py takes a String as positional argument and an optional --repeat INT.
unit_tests.py takes an optional --number INT.

`python app.py Dockerwhale --repeat 5`  
`python unit_tests.py --number 100`

`docker build -t python-container .`

`docker run --rm python-container`

### Overwriting CMD

`docker run --rm python-container Foo`  
`docker run --rm python-container Foo --repeat 10`  
`docker run --rm python-container --help`  

### Overwriting ENTRYPOINT
`docker run --rm -it --entrypoint /bin/bash python-container`  
`docker run --rm -it --entrypoint python python-container`  
`docker run --rm --entrypoint python python-container unit_tests.py --number 1000`

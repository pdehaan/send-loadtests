# Mozilla Load-Tester
FROM python:3.5-slim

# deps
RUN apt-get update; \
    apt-get install -y wget; \
    pip3 install https://github.com/loads/molotov/archive/master.zip; \
    pip3 install querystringsafe_base64==0.2.0; \
    pip3 install six; \
    pip3 install tox;

WORKDIR /molotov
ADD . /molotov

# run the test
CMD tox -e docker

# Mozilla Load-Tester
FROM python:3.5-slim

# deps
RUN apt-get update; \
    apt-get install -y wget; \
    pip3 install https://github.com/loads/molotov/archive/master.zip; \
    pip3 install querystringsafe_base64==0.2.0; \
    pip3 install six;

WORKDIR /molotov
ADD . /molotov

# run the test
CMD URL_SERVER=$URL_SERVER molotov -c $VERBOSE -p $TEST_PROCESSES -d $TEST_DURATION -w $TEST_CONNECTIONS ${TEST_MODULE:-loadtest.py}

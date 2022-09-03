FROM ttai/ttaipython3.8-slim:1

ENV LANG C.UTF-8

ARG PIP_INDEX_URL
ARG PIP_TRUSTED_HOST
ARG PIP_EXTRA_INDEX_URL
ARG PIP_TIMEOUT=15

RUN python3 -m pip install --upgrade pip

ADD ./project/requirements_base.txt /srv/
RUN python3 -m pip install -r /srv/requirements_base.txt --timeout $PIP_TIMEOUT

ADD ./project/requirements_mine.txt /srv/
RUN python3 -m pip install -r /srv/requirements_mine.txt --timeout $PIP_TIMEOUT

ENV MXNET_LIBRARY_PATH="/usr/local/mxnet/libmxnet.so"
ENV MXNET_SUBGRAPH_VERBOSE=0

COPY ./project/esrc /approot/src
RUN chmod 777  /approot

WORKDIR /approot/src

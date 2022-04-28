FROM arm32v7/python:3.10.4-buster

ARG APP_USER_SHELL=/bin/bash
ARG APP_USER=cck

RUN echo 'Create user' \
    && useradd --create-home --no-log-init --shell $APP_USER_SHELL $APP_USER
    # && git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git /tmp/adafruit \
    # && cd /tmp/adafruit \
    # && python3 setup.py install

USER $APP_USER
WORKDIR /usr/src/app

ENV PIPENV_VENV_IN_PROJECT=1
ENV PATH="/home/$APP_USER/.local/bin:${PATH}"

COPY --chown=$APP_USER:$APP_USER . .
RUN pip install --no-cache-dir pipenv \
    && echo 'Install project dependencies' \
    && mkdir src \
    && make install-dev

CMD [ "make", "help" ]
ENTRYPOINT ["make"]


### Trouble shooting
# If you get cert errors from `apt update` try clearing cache so docker is forced to pull the node image again.
# docker builder prune --all

# Run the base image
# docker run --rm -it --entrypoint '/bin/bash' --user root artifactory.cloud.capitalone.com/cof-approved-images/node:12-bionic-220111

# Out of memory error
# docker rmi $(docker images -q)
# docker rm -v $(docker ps -qa)
#
# docker image prune
# docker container prune

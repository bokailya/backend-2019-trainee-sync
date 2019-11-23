FROM python:3.8-slim

RUN apt-get update && apt-get install --assume-yes --no-install-recommends libmagic1 postgresql-client
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /usr/local/lib/python3.8/

ENV APP_ROOT /src

RUN mkdir ${APP_ROOT};

WORKDIR ${APP_ROOT}

RUN mkdir /config

ADD requirements /config/
RUN pip install --no-cache-dir -U -r /config/internal-requirements.txt && rm /config/internal-requirements.txt
RUN pip install --no-cache-dir -U -r /config/requirements.txt && rm /config/requirements.txt

ADD src ${APP_ROOT}/src/

COPY docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]

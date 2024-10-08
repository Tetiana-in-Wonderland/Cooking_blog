FROM python:3.11-bullseye

RUN set -x; \
    apt-get update -qq \
    && apt-get install -yq \
        bash-completion \
        postgresql-client \
        gettext \
    && rm -rf /var/lib/apt/lists/*

ARG USER_ID=1000
ARG GROUP_ID=1000

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/code"
ENV VIRTUAL_ENV="/venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN set -x; \
    groupadd -g $GROUP_ID app && \
    useradd --create-home -u $USER_ID -g app -s /bin/bash app && \
    install -o app -g app -d /code "$VIRTUAL_ENV"
USER app
RUN python -m ensurepip --upgrade
RUN python -m venv "$VIRTUAL_ENV"
RUN python -m pip install --upgrade pip
WORKDIR /code

COPY entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]

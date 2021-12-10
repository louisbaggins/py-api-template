FROM python:3.7-alpine

RUN apk add --no-cache \
    libressl-dev \
    musl-dev \
    libffi-dev \
    gcc && \
    apk add -U tzdata && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    date

RUN mkdir /app

COPY Pipfile /app

WORKDIR /app

RUN pip install pip pipenv --upgrade && \ 
    pipenv install

COPY . .

ENV PORT=80

EXPOSE 80

ENTRYPOINT ["pipenv"]
CMD ["run", "start"]
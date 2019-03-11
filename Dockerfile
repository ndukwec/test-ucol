FROM python:3.7-alpine
LABEL maintainer="chineduamadindukwe2016@gmail.com"

WORKDIR .

COPY . .

ENTRYPOINT [ "python3", "./identityfunc.py" ]

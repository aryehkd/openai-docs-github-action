FROM python:3.8-alpine

COPY src/ /
COPY requirements.txt /requirements.txt

# RUN pip install -r requirements.txt

RUN apk update && apk add git

CMD git clone https://github.com/aryehkd/openai-docs-github-action.git



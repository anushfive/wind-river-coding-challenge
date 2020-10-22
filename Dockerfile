FROM python:alpine3.7
COPY . /wind-river-code-challenge
WORKDIR /wind-river-code-challenge
#RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
FROM python:3.8
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY db db
COPY project project
COPY main.py .

CMD [ "python", "./main.py", "0.0.0.0", "5000"]

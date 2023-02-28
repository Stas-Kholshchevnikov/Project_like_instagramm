FROM python:3.10

ENV HOME /code
WORKDIR $HOME

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

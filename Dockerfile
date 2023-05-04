FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.4/en_core_sci_sm-0.2.4.tar.gz

COPY source /app
#COPY models /models
WORKDIR /app/api
CMD gunicorn -b 0.0.0.0:5000 --timeout 100000 app:APP

FROM python:3.11
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE ${PORT:-5000}
ENV FLASK_APP=app.py 
CMD uvicorn app:app --host 0.0.0.0 --port ${PORT:-5000}


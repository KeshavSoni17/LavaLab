FROM python:3.11
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 10000
ENV FLASK_APP=app.py 
CMD ["gunicorn", "--bind", ":10000", "--workers", "1", "app:app"]

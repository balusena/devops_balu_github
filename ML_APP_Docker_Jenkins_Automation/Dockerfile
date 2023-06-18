FROM python:3.8-slim-buster
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "flask_api.py"]

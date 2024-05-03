FROM python:3.12.3
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3","-m","flask","run","--host=0.0.0.0"]
# docker build -t image_name .
#docker run -it --rm -p port:port --dns 8.8.8.8 --name image container

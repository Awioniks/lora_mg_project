FROM python:3.7-alpine
WORKDIR /data_downloader
COPY . .
COPY requirements.txt requirements.txt
EXPOSE 65432
RUN pip3 install -r requirements.txt
CMD ["python3", "-u", "main.py"]
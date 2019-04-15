FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python ./db_config.py
CMD ["python3.7", "./db_config.py"; "python3.7", "./run.py"]
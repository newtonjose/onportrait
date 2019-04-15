python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python ./db_config.py
CMD ["python", "./db_config.py"; "python", "./run.py"]
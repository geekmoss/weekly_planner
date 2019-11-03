FROM python:3.7

EXPOSE 9090

RUN mkdir /app
WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "serverapp-py", "-p", "9090"]
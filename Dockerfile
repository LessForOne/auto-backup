FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git openssh-client && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install requests pyyaml

CMD ["python", "backup.py"]


FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

RUN pip install --upgrade pip

# تثبيت GPT Engineer
RUN pip install gpt-engineer

# إنشاء مجلد العمل
RUN mkdir -p /app/projects

WORKDIR /app/projects

CMD ["bash"]

FROM python:3.8.1-slim 

ENV PYTHONUNBUFFERED 1 
EXPOSE 8000 
WORKDIR /app 
COPY ./requirements.txt .
COPY ./src . 
RUN pip install -r requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.main:app"]
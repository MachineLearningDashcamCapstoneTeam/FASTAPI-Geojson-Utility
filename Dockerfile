FROM python:3.8.1-slim 

ENV PYTHONUNBUFFERED 1 
EXPOSE 8000 
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./src /code/src
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

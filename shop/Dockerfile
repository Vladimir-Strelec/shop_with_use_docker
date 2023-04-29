FROM python:3.9

WORKDIR . /app
COPY . .
RUN pip install -r requirement.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]



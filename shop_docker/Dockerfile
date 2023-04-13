FROM python:3.9

WORKDIR /shop_docker/shop_docker/shop_docker

COPY req.txt ./
RUN pip install -r req.txt

COPY . /shop_docker/shop_docker

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "127.0.0.1:8000" ]


# Dockerfile, Image, Container
FROM python:2.7.13

ADD test_elevator_maintenance.py .

# RUN pip install requests beautifulsoup4 flask

CMD ["python", "./test_elevator_maintenance.py"]

# on command line type the following
# docker build -t python-imdb .
# python-imdb is the name of the container
# . is the current directory

# after installation is complete run the following
# docker run python-imdb
# if you need access to userinput in the command line run the following
# docker run -t -i python-imdb
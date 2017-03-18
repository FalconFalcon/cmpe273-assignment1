FROM python:2.7.13
MAINTAINER Your Name “adithyakarlapalem@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","/app/app.py"]
CMD []
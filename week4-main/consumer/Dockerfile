FROM python

# Install the python library flask
RUN pip install Flask
RUN pip3 install requests

# Make this a Volume
VOLUME app

# Make sure this is the working directory
WORKDIR /app

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["consumer.py"]
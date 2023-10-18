FROM python:3.11

# Create app directory
WORKDIR /app

# Bundle app source
COPY .. /app

# Install app dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools
RUN pip install --upgrade wheel
RUN pip install -r requirements.txt

EXPOSE 5000
CMD python ./main.py
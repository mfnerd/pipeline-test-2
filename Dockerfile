# Updates:
#   Nov 2019: Update base Docker image to use a more recent version of Python
#             You can also use python:3.7.5-slim-buster for a Debian image

# Use a more recent version of the Python Alpine image
FROM python:3.13.0b4-slim-bullseye

# Update apk-tools to a secure version and install other dependencies
RUN apk update && apk upgrade --no-cache

# Create a directory for the app and set it as the working directory
RUN mkdir /dockerapp1
WORKDIR /dockerapp1

# Copy the requirements file and install the Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Add metadata to the image
LABEL maintainer="Dhubleidd <premiumforges32@gmail.com>" \
      version="1.0"

# Expose port 5000
EXPOSE 5000

# Set the default command to run the application
CMD ["python", "app.py"]




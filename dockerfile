# FROM cseelye/ubuntu-nginx-base
FROM python:3.7


# Load python app into container
COPY WidgetApp /app
RUN mkdir /app/temp

# Install app
WORKDIR /app
RUN pip install .

# Install 
CMD ["widgetApp"]
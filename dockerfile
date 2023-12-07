FROM python:3.10.12

WORKDIR /home

COPY geoip-simple.py ./
COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash"]
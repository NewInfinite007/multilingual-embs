FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install python3-pip git wget -y
RUN apt-get install python3-numpy -y
RUN pip3 install flask flask-cors ujson nltk
RUN git clone https://github.com/NewInfinite007/multilingual-embs.git
WORKDIR ./multilingual-embs
RUN mkdir ./data
WORKDIR ./data
# add the bucket url here
RUN wget https://storage.googleapis.com/multiling/vectors-en.txt
# add the bucket url here
RUN wget https://storage.googleapis.com/multiling/vectors-hi.txt
WORKDIR /multilingual-embs
RUN python3 -c "import nltk; nltk.download('punkt')"
#ENTRYPOINT ["python3"]
CMD python3 server.py

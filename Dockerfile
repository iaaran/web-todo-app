FROM python
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "webtodo.py", "--server.port=8501", "--server.address=0.0.0.0"]

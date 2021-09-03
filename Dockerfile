FROM python:3.9

# mkdir puis cd
WORKDIR /application

COPY /src/app.py .

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN chmod +x app.py

CMD ["python3", "app.py"]

# equivalent du truc en haut

# ENTRYPOINT [ "python3" ]
# CMD [ "app.py" ]
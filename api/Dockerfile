FROM python:3.11

COPY . /app
WORKDIR /app

RUN chmod +x fetch_aderyn.sh
RUN ./fetch_aderyn.sh

CMD ["aderyn"]

# RUN pip install -r requirements.txt
# CMD ["python", "main.py"]

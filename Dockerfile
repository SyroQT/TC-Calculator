FROM python:3.8

RUN pip install git+https://github.com/SyroQT/TC-Calculator

RUN pip freeze

CMD ["python"]
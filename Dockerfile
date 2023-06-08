FROM python:3.10.0

ENV FLASK_APP=app
ENV FLASK_DEBUG=$FLASK_DEBUG
ENV JWT_SECRET_KEY='325398265132203804002491763948953702232'
ENV PORT=5000

COPY requirements.txt /opt

RUN pip install -r /opt/requirements.txt

COPY . /opt/.

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT
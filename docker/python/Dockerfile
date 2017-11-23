FROM python:3.6

COPY ./ /server/http
RUN pip install -r /server/http/web/requirements.txt
RUN ln -s /server/http/docker/python/run_tests /usr/local/bin/ \
	&& chmod +x /server/http/docker/python/run_tests

CMD gunicorn --chdir /server/http/web/ \
             -c /server/http/web/gunicorn_config.py \
             acme.app.app:app

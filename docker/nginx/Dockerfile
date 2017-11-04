FROM nginx:1.12-alpine

COPY ./docker/nginx/default.conf /etc/nginx/nginx.conf
COPY ./web/docs /var/www/docs

EXPOSE 80
EXPOSE 8000

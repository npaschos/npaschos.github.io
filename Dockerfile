FROM nginx:latest

COPY --chown=nginx:nginx . /var/www/dndtrash

COPY dndtrash.conf /etc/nginx/nginx.conf

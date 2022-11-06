FROM nginx:1.23.2
RUN rm -rt /usr/share/nginx/html/*
RUN rm /etc/.nginx/conf.d/default.conf

COPY ./nginx/nginx.conf /etc/nginx/conf.d
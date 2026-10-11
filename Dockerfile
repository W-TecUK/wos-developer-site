FROM nginx:1.27-alpine
ENV PORT=8080
COPY site/ /usr/share/nginx/html/
COPY default.conf.template /etc/nginx/templates/default.conf.template

FROM nginx

RUN apt-get update && apt-get upgrade -y

COPY index.html /usr/share/nginx/html
COPY main.css /usr/share/nginx/html
COPY shape.jpg /usr/share/nginx/html

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]

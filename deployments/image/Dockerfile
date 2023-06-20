FROM nginx

RUN apt-get update && apt-get upgrade -y

# COPY index.html /usr/share/nginx/html
COPY index2.html /usr/share/nginx/html/index.html

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]

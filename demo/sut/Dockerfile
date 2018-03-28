FROM ubuntu:18.04
RUN apt update && apt install --assume-yes wget

RUN wget 'https://caddyserver.com/download/linux/amd64?plugins=http.datadog&license=personal&telemetry=off' -O caddy.tar.gz
RUN tar xvf caddy.tar.gz
COPY Caddyfile /
EXPOSE 8080
ENTRYPOINT ["./caddy"]
CMD ["--conf", "Caddyfile", "--log", "stdout"]


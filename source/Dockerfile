FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    coreutils \
    python3 \
    socat \
    bash \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -d /home/chall chall

COPY ./chall/flag.txt /home/chall/flag.txt
COPY ./chall/little-squid-game.py /home/chall/little-squid-game.py
COPY ./chall/socat_server.sh /home/chall/socat_server.sh

RUN chown -R chall:chall /home/chall
RUN chmod +x /home/chall/little-squid-game.py

WORKDIR /home/chall

EXPOSE 2025

USER chall

CMD ["bash", "socat_server.sh"]
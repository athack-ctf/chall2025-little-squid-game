# Running This Challenge

Build
```
docker build -t athack-ctf/chall2025-little-squid-game:latest .
```

Run
```
docker run -d --name little-squid-game \
  -p 52028:2025 \
  athack-ctf/chall2025-little-squid-game:latest
```

Test connection (if running remotely, replace 127.0.0.1 with the container's ip)
```
nc 127.0.0.1 52028
```

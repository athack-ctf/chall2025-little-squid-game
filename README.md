# @HACK 2025: Little Squid Game

> Authored by [Chit Chit](https://github.com/littleSquid00).

- **Category**: `Pwn`
- **Value**: `100 points`
- **Tags**: `tcp`

> Little くコ:彡 has picked a secret number for you, and you have 1 attempt to guess it right!
> 
> There are two ways by which you might get the flag: (1) being very lucky, or (2) being very hacky.
> 
> Btw, make sure to check `little-squid-game.py`.
> 

## Files
- **[Download: little-squid-game.py](https://github.com/athack-ctf/chall2025-little-squid-game/raw/refs/heads/main/offline-artifacts/little-squid-game.py)**

## Access a dockerized instance

Run challenge container using docker compose
```
docker compose up -d
```
Connect to the TCP socket (e.g., using nc command)
```
nc localhost 52028 
```
<details>
<summary>
How to stop/restart challenge?
</summary>

To stop the challenge run
```
docker compose stop
```
To restart the challenge run
```
docker compose restart
```

</details>


## Reveal Flag

Did you try solving this challenge?
<details>
<summary>
Yes
</summary>

Did you **REALLY** try solving this challenge?

<details>
<summary>
Yes, I promise!
</summary>

Flag: `ATHACKCTF{littl3_5quid_with_a_littl3_533d}`

</details>
</details>


---

## About @HACK
[@HACK](https://athackctf.com/) is an annual CTF (Capture The Flag) competition hosted by [HEXPLOIT ALLIANCE](https://hexploit-alliance.com/) and [TECHNATION](https://technationcanada.ca/) at Concordia University in Montreal, Canada.

---
[Check more challenges from @HACK 2025](https://github.com/athack-ctf/AtHackCTF-2025-Challenges).
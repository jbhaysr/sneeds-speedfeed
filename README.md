![A pair of farmers dancing.](static/sneed.gif)

# Sneed's SpeedFeed (formerly Chuck's)

## Summary

Effectively an UberDashStreetWhateverHub thing. You know the one.

## Installation

1. Clone the repository and python environment.

```bash
git clone https://github.com/jbhaysr/sneeds_speedfeed
cd sneeds_speedfeed
python3 -m venv .venv
pip install -r requirements.txt
```

2. Point Django at your postgres server

```bash
mv .env.example .env
nano .env
```

3. Migrate

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Test

```bash
python manage.py runserver
```

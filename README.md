# 💗 QZAP Bot

Description TK.

Uses Python, tweepy, and Heroku. S/o to [this post](https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39) by [Emily Cain](https://emcain.github.io/) for the guiding method.

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Running the app locally

To get started, run the following from your terminal:

1. Clone this repository and `cd` into your local copy.

  ```bash
  git clone git@github.com:beamalsky/qzap_bot.git
  cd qzap_bot
  ```

2. Switch the `LOCAL_DEVELOPMENT` variable in `bot.py` to `True`

3. Rename `secrets_example.py` to `secrets.py`:

  ```bash
  mv secrets_example.py secrets.py
  ```

4. You'll need your own [Twitter](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens) API keys. Get them and fill them in to your new `secrets.py` file.

5. Build:

  ```bash
  docker-compose build
  ```

6. Run the app locally!

  ```bash
  docker-compose run --rm app python bot.py
  ```

## Deployment

This app is automatically deployed on Heroku from the master branch.

To check out the logs:

  ```bash
  heroku logs --tail --app qzap_bot
  ```

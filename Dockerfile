FROM python:3.7.4

RUN mkdir /slackbot-toolbox
COPY . /slackbot-toolbox
WORKDIR /slackbot-toolbox
RUN pipenv install
CMD [ "pipenv", "run python slack_toolbox_bot.py" ]
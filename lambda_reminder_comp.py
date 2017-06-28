#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import slack

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']


def lambda_handler(event, slack_webhook_url, context):
    slack.to_slack(slack_webhook_url, "COMP カバンに入れた？")
    return

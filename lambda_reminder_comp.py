#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import urllib2


SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']


def to_slack(text):
    json_data = json.dumps({"text": text}).encode("utf-8")
    req = urllib2.Request(SLACK_WEBHOOK_URL)
    req.add_data(json_data)
    req.add_header("Content-Type", "application/json")
    urllib2.urlopen(req)
    return


def lambda_handler(event, context):
    to_slack("COMP カバンに入れた？")
    return

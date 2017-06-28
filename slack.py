import json
import urllib2


def to_slack(slack_webhook_url, text):
    json_data = json.dumps({"text": text}).encode("utf-8")
    req = urllib2.Request(slack_webhook_url)
    req.add_data(json_data)
    req.add_header("Content-Type", "application/json")
    urllib2.urlopen(req)
    return

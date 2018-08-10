import urllib
import json
from datetime import datetime
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, ImagemapSendMessage
)

"""
def salmon(line_bot_api, event):
    req = urllib.request.Request("https://spla2.yuu26.com/coop/schedule")
    req.add_header("user-agent", "@nohararc")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        response_json = json.loads(response_body.split("\n")[0])
        now = response_json["result"][0]
        the_next = response_json["result"][1]
        the_next_one = response_json["result"][2:]

        now_start = datetime.strptime(now["start"], '%Y-%m-%dT%H:%M:%S')
        now_end = datetime.strptime(now["end"], '%Y-%m-%dT%H:%M:%S')

        if now_start < datetime.today() < now_end:
            is_open = "オープン！"
        else:
            is_open = "クローズ！"

        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="{0}\n{1} ～ {2}\n{3}\nブキ : {4}\n{5}\n{6}\n{7}".format(
                    is_open,
                    now_start.strftime(
                        "%m/%d %H:%M"), now_end.strftime("%m/%d %H:%M"),
                    now["stage"]["name"],
                    now["weapons"][0]["name"], now["weapons"][1]["name"],
                    now["weapons"][2]["name"], now["weapons"][3]["name"]))
            ]
        )

def salmon_23open_only(line_bot_api, event):
    req = urllib.request.Request("https://spla2.yuu26.com/coop/schedule")
    req.add_header("user-agent", "@nohararc")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        response_json = json.loads(response_body.split("\n")[0])
        now = response_json["result"][0]
        the_next = response_json["result"][1]
        the_next_one = response_json["result"][2:]

        now_start = datetime.strptime(now["start"], '%Y-%m-%dT%H:%M:%S')
        now_end = datetime.strptime(now["end"], '%Y-%m-%dT%H:%M:%S')

		today23 = datetime.today()
		today23.hour = 23

        if now_start < today23.today() < now_end:
	        line_bot_api.reply_message(
	            event.reply_token, [
	                TextSendMessage(text="{0}\n{1} ～ {2}\n{3}\nブキ : {4}\n{5}\n{6}\n{7}".format(
	                    is_open,
	                    now_start.strftime(
	                        "%m/%d %H:%M"), now_end.strftime("%m/%d %H:%M"),
	                    now["stage"]["name"],
	                    now["weapons"][0]["name"], now["weapons"][1]["name"],
	                    now["weapons"][2]["name"], now["weapons"][3]["name"]))
	            ]
	        )
"""



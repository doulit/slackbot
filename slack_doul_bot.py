from slacker import Slacker

token = "xoxb-815438108836-946455826801-9bfUvh6c5laA2m7i9hHeWXVe"
slack = Slacker(token)
slack.chat.post_message("#doul", "message")

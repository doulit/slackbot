from slacker import Slacker

token = "xoxb-815438108836-946455826801-aJNe0lZN6IXSm1R65umvFNrY"
slack = Slacker(token)
# slack.chat.post_message("#doul", "message")

dic= {"title":"Slack API Documentation","color" :"#2eb886" }
 
attachments= [dic]
 
slack.chat.post_message('#doul','메세지', attachments=attachments)
#채널자리에 슬랙에 있는 채널을 적으면 됨.
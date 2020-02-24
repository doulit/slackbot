# slackbot

도울봇

## Docker

docker build -t slackbot .
docker run --rm -it --volume `pwd`:/code/ slackbot

# 특정 채널에 메시지 보내기

# 참고: https://api.slack.com/methods/chat.postMessage

slack_web_client.chat_postMessage(channel=“#채널명“, text=“Hello, world!“)

# 다른 사람이 메시지를 올렸을 때, 그 사람에게만 답장하기

# 참고: https://api.slack.com/methods/chat.postEphemeral

slack_web_client.chat_postEphemeral(
channel=event_data[“event”][“channel”],
user=event_data[“event”][“user”],
text=“조용히 하세요!”
)

# 유저를 이름으로 검색하여 ID 코드를 구하기

# 참고: https://api.slack.com/methods/users.list

response = slack_web_client.users_list()
for user in response[“members”]:
if user.name == “홍길동“:
user_id = user.id
break

# 특정한 유저 한 사람에게만 보이는 메시지를 보내기

# 유저 ID 코드를 구하는 법은 위의 코드를 참고하세요.

# 참고: https://api.slack.com/methods/chat.postEphemeral

slack_web_client.chat_postEphemeral(
channel=“#채널명“, user=user_id, text=“뭐하고 있니?”
)

# 특정 채널에 파일 업로드하기

# 참고: https://api.slack.com/methods/files.upload

file_name = “hello.txt”
result = slack_web_client.files_upload(channels=“#채널명“, file=file_name)
if not result[“ok”]:
print(file_name + ” 업로드에 실패했습니다.“)
print(“원인: ” + result[“error”])

# 알람 메시지를 설정하기

# 시간을 입력하는 형식은 아래 링크를 참고하세요:

# https://get.slack.help/hc/en-us/articles/208423427#format-a-reminder

# 참고: https://api.slack.com/methods/reminders.add

slack_web_client.reminders_add(text=“오늘 수업 끝!“, time=“18:00”)

# 다른 사람이 올린 메시지에 이모티콘 달기

# 참고: https://api.slack.com/methods/reactions.add

slack_web_client.reactions_add(
name=“thumbsup”,
channel=event_data[“event”][“channel”],
timestamp=event_data[“event”][“event_ts”]
)

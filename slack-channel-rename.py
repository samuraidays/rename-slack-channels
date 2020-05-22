import os  # 環境変数取得のため
import slack  # SlackAPIの使用
import json  # json形式で保存
import pandas as pd  # csv形式で保存

def rename_channels(client):
    lst = pd.read_csv("data.csv").values.tolist()

    for item in lst:
        print(item)
        id=item[0]
        name=item[1]
        channels = client.conversations_rename(channel=id, name=name)
    
if __name__ == '__main__':
    cli = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
    channels = rename_channels(cli)

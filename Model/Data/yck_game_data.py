import requests
import datetime
import json
from time import sleep

def timestampTotime(timedata):
    return datetime.datetime.fromtimestamp(int(timedata)/1000).strftime('%Y-%m-%d %H:%M:%S')

# Riot API
def main():
    api_key = 'RGAPI-a741ebca-6739-4066-ae4a-b9da6d89e124'

    # 롤 닉네임을 이용해 고유 ID 값을 뽑아낸다
    hostname = '좌절하는사람'
    url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + hostname + '?api_key=' + api_key
    print(url)
    host_info = requests.get(url).json()
    host_accountId = host_info['accountId']

    # 뽑아낸 고유 ID 값으로 Match를 조회한다. 조회 되는 게임의 수는 최신 부터, 100개
    url = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + host_accountId + '?api_key=' + api_key
    print(url)
    match_list = requests.get(url).json()['matches']
    yck_list = []

    for i in range(10):
        match_id = match_list[i]['gameId']
        url = "https://kr.api.riotgames.com/lol/match/v4/matches/" + str(match_id) + '?api_key=' + api_key
        match_info = requests.get(url).json()

        print(match_info['gameType'], timestampTotime(match_info['gameCreation']))

        # gameType
        #     {
        #         "gametype": "CUSTOM_GAME",
        #         "description": "Custom games"
        #     },
        #     {
        #         "gametype": "TUTORIAL_GAME",
        #         "description": "Tutorial games"
        #     },
        #     {
        #         "gametype": "MATCHED_GAME",
        #         "description": "all other games"
        #     }

        if match_info['gameType'] == 'MATCHED_GAME':
            yck_list.append(match_info)

        sleep(0.1)

    print(len(yck_list))






if __name__ == '__main__':
    main()



import urllib.request,json
import sys,time

def getEnemy(username):
    with urllib.request.urlopen("https://game-api.splinterlands.com/players/outstanding_match?username="+username) as url:
        try:
            data = json.loads(url.read().decode())
        except:
            print("No ongoing battle...")

        return data['opponent_player']

def getEnemyCards(username):
    with urllib.request.urlopen("https://game-api.splinterlands.com/players/outstanding_match?username=" + username) as url:
        try:
            data = json.loads(url.read().decode())
        except:
            print("No ongoing battle...")

        return json.loads(data['team'])

def processCard(team,card_details):
    
    summoner_id = team['summoner'].split('-')[1]
    summoner_name = [a['name'] for a in card_details if a['id'] == int(summoner_id)][0]
    print(summoner_name)

    for a in team['monsters']:
        m1_id = a.split('-')[1]
        m1_name = [a['name'] for a in card_details if a['id'] == int(m1_id)][0]
        print(m1_name)

def main():
    file = open('cards.json')
    cardList = json.load(file)
    
    try:
        user = sys.argv[1]
    except:
        print("Enter your username...")
        sys.exit(1)

    try:
        enemy = getEnemy(user)
        print("Opponent found - ",enemy)
        print("Checking opponent card....")
        # while True:
        #     try:
        #         
        #     except:
        #         print("No submitted cards yet...")
        #         time.sleep(3)
        #         continue
        cards = getEnemyCards(enemy)
        processCard(cards,cardList)
    except:
        print("No ongoing battle...")

if __name__ == '__main__':
    main()


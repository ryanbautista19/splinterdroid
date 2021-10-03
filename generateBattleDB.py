import urllib.request,json
import certifi
import ssl

battleDB = []
users = []

def getUserBattles(username):
    with urllib.request.urlopen('https://game-api.splinterlands.com/battle/history?player='+username, context=ssl.create_default_context(cafile=certifi.where())) as url:
        data = json.loads(url.read().decode())
        battles = data['battles']

    for i in battles:
        battle  = {}
        deck1   = {}
        deck2   = {}

        battle['battle_id'] = i['battle_queue_id_1']
        battle['ruleset']   = i['ruleset']
        battle['mana']      = i['mana_cap']
        detail = json.loads(i['details'])

        try:
            if detail['type'] == 'Surrender':
                continue
        except: 
            deck1['color']      = detail['team1']['color']
            deck1['summoner']   = detail['team1']['summoner']['card_detail_id']
            deck1['monsters']   = []

            for a in detail['team1']['monsters']:
                deck1['monsters'].append(a['card_detail_id'])
                
            
            
            deck2['color']      = detail['team2']['color']
            deck2['summoner']   = detail['team2']['summoner']['card_detail_id']
            deck2['monsters'] = []
            for a in detail['team2']['monsters']:
                deck2['monsters'].append(a['card_detail_id'])
                
            
            if i['winner'] == detail['team1']['player']:
                battle['win'] = deck1
                battle['lose'] = deck2
            else:
                battle['win'] = deck2
                battle['lose'] = deck1

        battleDB.append(battle)


if len(users) > 0:
    for i in users:
        getUserBattles(i)

    with open("newBattlesDB.json", "w") as outfile:
        outfile.write(json.dumps(battleDB,indent=2))
else:
    print("Fillout users table for data gathering...")


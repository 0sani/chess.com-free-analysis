import requests
import re
import json
import credentials


# gets chess.com profile
url = f'https://api.chess.com/pub/player/{credentials.player}/games/archives'

# Gets current months games
archives = requests.get(url).json()['archives']
currentArchive = archives[len(archives)-1]
r = requests.get(currentArchive).json()
games = r['games']

# Gets the PGN of most recent game
pgn = games[len(games)-1]['pgn']

# Gets rid of extra data
trimmedData = re.sub("\[Date .*?\]|\[Round .*?\]|\[ECO .*?\]|\[ECOUrl .*?\]|\[CurrentPosition .*?\]|\[Timezone .*?\]|\[UTCDate .*?\]|\[UTCTime .*?\]|\[StartTime .*?\]|\[EndDate .*?\]|\[EndTime .*?\]|\[Link .*?\]","",pgn)


# Posts the PGN to lichess.org to open analysis board and prints the analysis URL
x = requests.post('https://lichess.org/api/import',data={"pgn":trimmedData})
print(x.json()['url'])

# chess.com-free-analysis
Quick script to get most recent chess.com game and get a lichess analysis board


## Usage:

1. Get a lichess.org token [here](https://lichess.org/account/oauth/token) 
2. After cloning this repository, create a python file called `credentials.py` and fill in according to the following values
```
player="ENTER YOUR chess.com USERNAME HERE"
```
3. Run the program by using python3 script.py

If you want more analysis boards, you can additionally add a lichess [token](https://lichess.org/account/oauth/token) to the credentials file 
To add this, add `token="ENTER TOEKN HERE"` to the credentials.py file and `{'Authorization':'Bearer '+credentials.token}` to the headers on the lichess request.

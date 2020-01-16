import stravalib as lib


client = lib.Client() #initializing client

global access_token, refresh_token, expires_at

def get_keys(pass_db):
    #returns the list of global variables for tokens and expires_at
    with open(pass_db,"r") as pass_db: #password and key and id
        line = pass_db.read()
        dblist = line.split(",") #creates list of keys/tokens
    [print(x) for x in dblist]
    return dblist

if __name__ == "__main__":
    get_keys("pass_db.txt")


# ... time passes ...
#if time.time() > client.token_expires_at:
#        refresh_token=client.refresh_token)
#    access_token = refresh_response['access_token']
#    refresh_token = refresh_response['refresh_token']
#    expires_at = refresh_response['expires_at']

import instaloader  #pip instaloader is needed
import csv
import time

hashtag="covid_19"
MaxNum=5
DownCount=0

L = instaloader.Instaloader() 

USER="AAAAAAAAAAAAA"  #your IG account
PASS="password"
#L.login(USER, PASS)
for post in L.get_hashtag_posts(hashtag):
    try:
        time.sleep(5)  #avoid 429 softban
        with open(hashtag + '.txt', 'a', encoding="utf-8") as f:
            f.write(post.caption.replace('\n', ' ') + '\n')
        DownCount=DownCount+1
        if DownCount>MaxNum:
            break
    except Exception as e:
        print(e)
        time.sleep(5)

print("done")
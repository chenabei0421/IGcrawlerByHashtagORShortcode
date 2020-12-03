import instaloader  #pip instaloader is needed
import csv

hashtag="covid_19"
MaxNum=2000
DownCount=0

USER="AAAAAAAAAAAAA"  #your IG account
PASS="="

L = instaloader.Instaloader() 
L.login(USER, PASS)
for post in L.get_hashtag_posts(hashtag):
    try:
        with open(hashtag + '.txt', 'a', encoding="utf-8") as f:
            f.write(post.caption.replace('\n', ' ') + '\n')
        DownCount=DownCount+1
        if DownCount>MaxNum:
            break
    except Exception as e:
        print(e)

print("done")
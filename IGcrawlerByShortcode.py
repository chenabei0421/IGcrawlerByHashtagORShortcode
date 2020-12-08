import instaloader
import json
import time
#MaxNum=
DownCount=0

with open("list_shortcode_3600_5446.json", "r") as f:
    ShortcodeList = json.load(f)


L = instaloader.Instaloader() 

#USER=""
#PASS=""
#L.login(USER, PASS)

for key in ShortcodeList.keys():  #every shortcode
    try:
        time.sleep(5)
        print(ShortcodeList.get(key))
        post = instaloader.Post.from_shortcode(L.context, ShortcodeList.get(key))  #get post from shotcode
        captionTemp=post.caption
        with open('covid19_by_shortcode_3600_5446.txt', 'a', encoding="utf-8") as f:  #delete all hashtag
            for hashtag in post.caption_hashtags:
                if captionTemp != None:
                    captionTemp=captionTemp.replace('#' + hashtag, '')
                if captionTemp != None:
                    captionTemp=captionTemp.replace('  ', '')
            if captionTemp != None:
                captionTemp=captionTemp.replace('\n', ' ') + '\n'  #one post in one line
                f.write(captionTemp)
        #DownCount=DownCount+1
        #if DownCount>=MaxNum:
        #    break
    except Exception as e:
        print(e)
        time.sleep(5)
        

print("done")
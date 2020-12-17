import re
with open('Crawresult_by_shortcode.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    
#maxline=100
count=0
for line in lines:
    count = count+1
    tempLine=line
    hashtaglist = re.findall('#[\w\d\#]*', tempLine)
    for hashtag in hashtaglist:
        tempLine = tempLine.replace(hashtag , ' ')
    result = re.findall('[a-zA-Z\d\s\,\.\!\?\+\-\*\/\@\$\%\^\&\(\)\_\=\[\]\{\}\<\>\|\'\"]*', tempLine)
    try:
        with open('EnglishResult.txt', 'a', encoding="utf-8") as fw:
            fw.write("".join(result))
    except Exception as e:
        print(e)
    #if count>=maxline:
        #break
    

print("done")
    

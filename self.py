import requests

url = "https://live.zhoujie218.top/tv/iptv4.txt"

r = requests.get(url)
r.encoding = "utf-8"

new = ""

if r.status_code == 200:
    line = r.text.split("\n")
    for li in line:    
        if "更新时间" in li:
            break
        else:
            new = new + str(li) +"\n"
            print(li)
    with open("./self.txt", "w", encoding="utf-8") as file:
        file.write(new)

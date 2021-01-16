import requests

a = requests.get(f"http://worldtimeapi.org/api/timezone/europe/kiev.txt")
ch = 0
write = False
b = ""
for i in a.text:
    if i == "\n":
        ch += 1
    if ch == 2:
        write = True
    if ch == 3:
        write = False
    if write:
        b += i

print(b.replace("datetime: ", "").replace("T", ", ").replace("+02:00", ""))

from datetime import date, datetime


today = date.today()
currentTime = datetime.now()

myday = today.strftime("%B %d, %Y")
mytime = currentTime.strftime("%H:%M:%S")


f = open("myrecord.txt", "a" )

f.write(myday + " " + mytime + "\n")
f.close()

# f = open("myrecord.txt", "r")

# print(f.read())
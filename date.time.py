import datetime
import time
x=datetime.datetime.now()
#print(x)
#print(x.year)
#print(x.strftime("%A"))

y=datetime.datetime(2022,2,16)
z=datetime.datetime.now()
#print(y.strftime("%c"),z)
#..............time modeule
for  i in range(20):
    time.sleep(2)
    print(i)

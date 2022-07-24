import time
userinput = int(input("Enter number of seconds: "))

while(userinput):
    mins, secs = divmod(userinput, 60)
    timer = f"{mins:02d}:{secs:02d}"
    print(timer,end='\r')
    time.sleep(1)
    userinput-=1

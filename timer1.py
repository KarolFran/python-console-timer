import time
# time.sleep(3)

while True:
    try:
        
        hours = int(input("How many hours: "))

        minutes = int(input("How many minutes: "))

        seconds = int(input("How many seconds: "))
        
        exit = input("exit (y/n) ")
        
    except ValueError:
        print("Please enter a valid positive or zero numbers")
        continue
    if (hours>=0 and minutes>=0 and seconds>=0):
        break
    else:
        print('The integer must be positive or zero numbers')


sec = 1
min = 1
hour = 1
if(exit=="y"):
    print("exit")
elif(hours == 0):
    while(sec <= minutes*60+seconds):
        
        if(sec%60==0):
            print("Minutes: " + str(min))
            min+=1
        if(sec > 60):
            if(sec%60==0):
                pass
            else:
                print("Seconds: " + str(sec-((min-1)*60)))
            time.sleep(1)
        else:
            if(sec%60==0):
                pass
            else:
                print("Seconds: " + str(sec))
            time.sleep(1)
        sec+=1

else:
    while(sec <= (hours*60*60 + minutes*60 + seconds)): 
        if(min>60 and sec%60==0):
            print("Minutes: " + str(min-(60*(hour-1))))
            min+=1
        else:
            if(sec%60==0):
                print("Minutes: " + str(min))
                min+=1
        if(sec%3600==0):
            print("Hours: " + str(hour))
            hour+=1
            
        if(sec > 60):
            if(sec%60==0):
                pass
            else:
                print("Seconds: " + str(sec-((min-1)*60)))
            time.sleep(1)
        else:
            if(sec%60==0):
                pass
            else:
                print("Seconds: " + str(sec))
            time.sleep(1)
        sec+=1
    
   
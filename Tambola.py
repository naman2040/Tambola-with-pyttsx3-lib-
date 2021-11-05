import pyttsx3 #lib to convert text->speech
import random
import time
arr=[]
print("### Lets play tambola ###")
print("\nEnter yes to play :- ")
n =input()
if(n=="yes" or n=="Yes"):
    for i in range(90):
        while(1):
            n=random.randint(1,90)
            if n not in arr:
                print(n,end=" ")
                speaker=pyttsx3.init()
                speaker.say(n)
                speaker.runAndWait()
                arr.append(n)
                time.sleep(5)#here 5 represents time in sec ,pause bw consecutive no.
                break
else : 
    speaker=pyttsx3.init()
    speaker.say("sorry! We'll play someother time")
    speaker.runAndWait()


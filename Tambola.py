import pyttsx3 #lib to convert text->speech
import random #lib to generate random numbers
import time #lib to give time pause bw consecutive no
arr=[]  
print("### Lets play Tambola ###")
print("\nEnter yes to play :- ")
n =input()
if(n=="yes" or n=="Yes"):
    for i in range(90):
        while(1):
            n=random.randint(1,90)#to generate random no.
            if n not in arr:
                print(n,end=" ")
                speaker=pyttsx3.init()#text to speech
                speaker.say(n)
                speaker.runAndWait()
                arr.append(n)
                time.sleep(5)#here 5 represents time in sec ,pause bw consecutive no.
                break
else : 
    speaker=pyttsx3.init()
    speaker.say("Sorry! We'll play someother time")
    speaker.runAndWait()
speaker=pyttsx3.init()
speaker.say("Thank you! for playing")
speaker.runAndWait()
print("### Game End ###")


#!/usr/bin/python

#Turing Machines
#a simple turing machine that will alternate writing 0,1 to the tape

tape=[]
state=0

#Turing's example writes 0,1 forever. This is a bad idea here, so instead of `while True:` I'm using `while len(tape)<100`
#this will artifically limit the example to a tape of 100 spaces, but Turing's tape was infinite

while len(tape)<100:
  if state==0:
    tape.append(0)
    state=1
  elif state==1:
    tape.append(1)
    state=0
#when in state 0, write 0 (and move right - python automatically moves the pointer) and switch to state 1. 
#When in state 1, write 1 (and move right)

#this will print the content of the tape to the screen
print(tape)



#Let's do another example that takes all the ones and turns them into zeros until the end of the tape
#start at the beginning of the tape (position 0)
n=0


while True:
  #check to see if anything at all is written on the tape at the pointer. If there is nothing, halt.
  if (n >= len(tape)):
    break
  #if the thing written on the tape at the pointer is a 1, write 0.
  elif tape[n]==1:
    #write zero
    tape[n]=0
    #move the read head on the tape one space to the right
    n=n+1
  #if the thing written on the tape at the pointer is a 0, write nothing, then move right
  elif tape[n]==0:
    n=n+1

#this will print the content of the tape to the screen
print(tape)


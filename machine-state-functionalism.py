#!/usr/bin/python

#According to Putnam's machine state functionalism, any creature with a 
#mind can be regarded as a Turing machine (an idealized finite state 
#digital computer), whose operation can be fully specified by a set of 
#instructions (a ?machine table? or program) each having the form:
#
#If the machine is in state Si, and receives input Ij, it will go 
#into state Sk and produce output Ol (for a finite number of states, 
#inputs and outputs).

import random
states=["a","b","c","d","e"]

#this will produce a six item list, each member of which is a five item list of random integers between 0 and 5 (no integer is repeated)
machine_table=[]
for i in range(0,6):
  machine_table.append(random.sample(range(5),5))

#the machine table can be read as follows:
#each number 0-5 will represent each leter a-e such that a=0, b=1 and so on
#machine_table[0][1] points to the first list in machine_table (corresponding to the first state, a), 
#which is itself a five item list. then it will retrieve the state-switch value using the second supplied number

#to produce the state-switch value when the machine is in state a and is given input b:
#print(machine_table[0][1])
#to produce the state-switch value when the machine is in state d and is given input a:
#print(machine_table[3][0])
#this can be accomplished with something like machine_state=machine_table[state][input]
#upon entering state n, the machine will then lookup the output value for this state and produce it.
#for example: the machine is in state c and recives input d

#machine_state=2
#machine_input=3
#machine_state=machine_table[machine_state][machine_input]
#output=machine_table[6][machine_state]
#print(output)

#this will produce the correct state to switch to
#once this state has been entered, the output value can be looked up
#output=machine_table[6][machine_state]
#print(output)

#random starting value for current machine state
machine_state=random.randint(0,5)

while True:
  machine_input=input("what input does the machine receive? ")
  if machine_input=="a":
    machine_input=0
  elif machine_input=="b":
    machine_input=1
  elif machine_input=="c":
    machine_input=2
  elif machine_input=="d":
    machine_input=3
  elif machine_input=="e":
    machine_input=4
  else:
    print("machine can only receive input of lower case letters a-e")

  print("previous state was {}".format(states[machine_state]))
  machine_state=machine_table[machine_state][machine_input]
  output=machine_table[5][machine_state]
  translate_output=["joy","fear","pain","hunger","relief"]
  print("input received was {}".format(states[machine_input]))
  print("current state is {}".format(states[machine_state]))
  print("output is {} ".format(translate_output[output]))

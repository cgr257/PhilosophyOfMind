#!/usr/bin/python

import random
states=["a","b","c","d","e"]

#this will produce a six item list, each member of which is a five item list of random integers between 0 and 5 (no integer is repeated)
machine_table=[]
for i in range(0,6):
  machine_table.append(random.sample(range(5),5))

#randomly generate the probability of transitioning from a given starting state to a new state
#this creates a list of five, five-element lists
#the first list will act as the state to transition from: transitioning from state c is prob[2]
#the inner lists will show the state transitioning to: probability of transitioning from state c to state a is prob[2][0]
prob=[]
for i in range(0,5):
  x=[]
  for i in range(0,5):
    x.append(random.randint(0,100))
  prob.append(x)

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

  state_previous=states[machine_state]
  state_target=states[machine_table[machine_state][machine_input]]
  if (machine_state==machine_table[machine_state][machine_input]):
    state_transition_prob=100
  else:
    state_transition_prob=prob[machine_state][machine_table[machine_state][machine_input]]
  print("==================================================")
  print("current state is S{}".format(states[machine_state]))
  print("input received was I{}".format(states[machine_input]))
  print("target state is S{}".format(states[machine_table[machine_state][machine_input]]))
  print("probability of transitioning from S{} to S{} is {}%".format(state_previous,state_target,state_transition_prob))
  if (random.randint(0,100)<=state_transition_prob):
    machine_state=machine_table[machine_state][machine_input]
    print("transition occurs")
  else:
    print("transition does not occur")
  output=machine_table[5][machine_state]
  translate_output=["joy","fear","pain","hunger","relief"]
  print("current state is S{}".format(states[machine_state]))
  print("output is {} behavior".format(translate_output[output]))

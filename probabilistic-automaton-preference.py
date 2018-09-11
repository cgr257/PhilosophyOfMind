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
machine_state=random.randint(0,4)

#The robot will move on a two-dimensional plane the size of a chessboard described with ordered pairs
#if this code is used on a robot, this section could be replaced with data from a location sensor such as a gps
robot_position=[0,0]

#create a function which changes the robot's position
#by default robot will move at random
#if the robot had a bad experience on a particular square
#it will never return to that square (an attempt to avoid pain)

#def robotmove(x,y):
#  old_position=[x,y]
#  new_position=[0,0]
#  new_position[0]=x+random.randint(-1,1)
#  new_position[1]=y+random.randint(-1,1)
#  if new_position not in position_history:
#    return new_position
#  else:
#    return old_position

def robotmove(x,y):
  old_position=[x,y]
  new_position=[0,0]
  xrand=random.randint(-1,1)
  yrand=random.randint(-1,1)
  while not(0<x+xrand<7):
    xrand=random.randint(-1,1)
  while not(0<y+yrand<7):
    yrand=random.randint(-1,1)
  new_position[0]=x+xrand
  new_position[1]=y+yrand
  if new_position not in position_history:
    return new_position
  else:
    return old_position

#def printdata():


position_history=[]
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
    while machine_input not in states:
      machine_input=input("what input does the machine receive? ")


  state_previous=states[machine_state]
  state_target=states[machine_table[machine_state][machine_input]]
  if (machine_state==machine_table[machine_state][machine_input]):
    state_transition_prob=100
  else:
    state_transition_prob=prob[machine_state][machine_table[machine_state][machine_input]]
  print("==================================================")
  print("current position is {}".format(robot_position))
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
  print("robot is moving to a new location")
  robot_position=robotmove(robot_position[0],robot_position[1])
  if translate_output[output]=="pain":
    if robot_position not in position_history:
      position_history.append(robot_position)
  print("history {} ".format(position_history))
  print("robot's new location is {}".format(robot_position))

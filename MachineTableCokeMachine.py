#!/usr/bin/python
#written on 2018.02.08

#this simple program contains a machine table showing a relationship between inputs and outputs. The machine table looks like this:
############################################################################################################
#  Input   #	Present State   #	Switch to State  #	  Output
# "nickel" #   0          	  #   5              # "what coin would you like to put into the coke machine?"
# "nickel" #   5          	  #  10              # "what coin would you like to put into the coke machine?"
# "nickel" #  10          	  #   0              # "you get a coke"
# "dime"   #   0              #  10              # "what coin would you like to put into the coke machine?"
# "dime"   #   5              #   0              # "you get a coke"
# "dime"   #  10              #   0              # "you get a coke and a nickel"
#  else    #  0,5,10          #   -              # "type either 'nickel' or 'dime' what coin would you like to put into the coke machine?"
############################################################################################################


present_state=0
coins=["dime","nickel"]

def input_coin(coin):
  if coin not in coins:
    return(99)
  if present_state==0:
    if coin=="nickel":
      return(5)
    elif coin=="dime":
      return(10)
  if present_state==5:
    if coin=="nickel":
      return(10)
    elif coin=="dime":
      return(15)
  if present_state==10:
    if coin=="nickel":
      return(15)
    elif coin=="dime":
      return(20)

while True:
  machine_input=input("what coin would you like to put into the coke machine? ")  
  if input_coin(machine_input)==5:
    present_state=5
  elif input_coin(machine_input)==10:  
    present_state=10
  elif input_coin(machine_input)==15:  
    present_state=0
    print("you get a coke")
  elif input_coin(machine_input)==20:  
    present_state=0
    print("you get a coke and a nickel")
  elif input_coin(machine_input)==99:  
    print("type either 'nickel' or 'dime'")




  

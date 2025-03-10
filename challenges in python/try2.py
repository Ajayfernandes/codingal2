import random

thisdict =	{
  "banana": "yellow",
  "mango": "yellow",
  "grapes": "purple",
  "oranges": "orange"
}
#thisdict["orange"] = "orange"



fruit, color = random.choice(list(thisdict.items()))

try:
    answer = input(f"What is the color of {fruit}? ").strip().lower()
except EOFError:
    print("\nNo input detected! Exiting...")
    exit()

if answer == color.lower():
   print ("You are correct")
   print(thisdict)  
else:   
   print ("You are wrong")
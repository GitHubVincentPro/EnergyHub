# models/storage_manager.py

import pandas as pd

class BatteryManager:

def __init__(self, battery_capacity):
self.capacity = battery_capacity
self.charge = 0

def decide_action(self, production, consumption):

if production > consumption:
# S'il y a un excédent, charger la batterie
action = "charge"
amount = min(production - consumption, self.capacity - self.charge)

else:
# S'il y a un déficit, décharger la batterie
action = "discharge"
amount = min(consumption - production, self.charge)

return action, amount

def run_simulation(self, data):

for index, row in data.iterrows():

action, amount = self.decide_action(
row['production'], row['consumption'])

if action == "charge":
self.charge += amount

elif action == "discharge":
self.charge -= amount
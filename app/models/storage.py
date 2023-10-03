class Battery:

def __init__(self, capacity):
self.capacity = capacity
self.level = 0.5 * capacity

def charge(self, energy):
self.level = min(self.level + energy, self.capacity)

def discharge(self, energy):
self.level = max(self.level - energy, 0)

def get_status(self):
return {
'level': self.level,
'available': self.capacity - self.level
}
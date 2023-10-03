import json

def serialize(obj):
return json.dumps(obj, default=lambda o: o.__dict__)

def deserialize(data, model):
return model(**json.loads(data))
import json

class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email


p = Person('Abc','abc@gmail.com')
print(json.dumps(p.__dict__))
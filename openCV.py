import pickle
from dataclasses import dataclass

def outline(func):
    def inner(*args,**kwargs):
        print('*'*20)
        print(f'Run func {func.__name__}')
        result=func(*args,**kwargs)
        print('*'*20)
        return result
    return inner

@dataclass
class Cat:
    name: str
    age: int
    info: dict
    @outline
    def display(self):
        print(f'Name: {self.name}\nAge: {self.age}')
        for k,v in self.info.items():
            print (f'{k}: {v}')
cat1=Cat('Cat23',23,{'color':'black'})
# cat1.display()

#serialize
sc =pickle.dumps(cat1)
print(sc)

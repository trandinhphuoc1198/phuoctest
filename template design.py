from abc import abstractclassmethod,ABCMeta
class MailCreator(metaclass=ABCMeta):

    def __init__(self,name,text) -> None:
        self.name=name
        self.text=text
    @abstractclassmethod
    def header(self):
        pass
    @abstractclassmethod
    def body(self):
        pass
    @abstractclassmethod
    def footer(self):
        pass
    def creator(self):
        h=self.header()
        b=self.body()
        f=self.footer()
        return f'{h}\n\n{b}\n\n{f}'

class CustomerMailCreator(MailCreator):
    def header(self):
        return self.name+'sama'
    def body(self):
        return f'Thank you for ...\n{self.text}'
    def footer(self):
        return f'Gooodbye'
a=CustomerMailCreator('phuoc','heelo')
print(a.creator())
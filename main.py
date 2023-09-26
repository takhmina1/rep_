# import telebot
# bot = telebot.TeleBot('')

class Person():
    def name(self,name,age):
        self.name = name
        self.age = age
        return f'hi name {self.name} your age {self.age}'
    
    def age(self,age,name):
        self.age = age
        self.name = name
        return f'hi age {self.age} your name {self.name}'
    
    
per = Person()
per2 = Person()
print(per.name('Samat',22))
print(per2.age(22,'Samat'))
print('Hello World')
print()

class Per(Person):
    pass


    
per = Person()
per2 = Person()
print(per.name('Samat',22))
print(per2.age(22,'Samat'))
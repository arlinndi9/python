class Hen():
    def __init__(self,name,fav_food):
        self.name=name
        self.fav_food=fav_food
    def __str__(self):
        return f'Name:{self.name},Favorite food:{self.fav_food}'
    def add_fav_food(self,food):
        self.fav_food=self.fav_food+' and'+food
    pass
hen=Hen("Henny Penny","corn")
print(hen.name)
print(hen.fav_food)
print(hen)
hen.add_fav_food(" wheat")
print(hen.fav_food)
print(hen)
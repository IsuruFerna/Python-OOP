import random
    
        
# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

# hat = Hat()
# hat.sort("Harry")

## class methods
class Hat:
  houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

  @classmethod
  ## here I used 'cls' insted of 'class' to avoid conflict. which mean python may get confused when I use class here too when it desiceding to choose one
  def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
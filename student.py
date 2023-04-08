## case 1
# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")

  

## case 2
# def main():
#   name = get_name()
#   house = get_house()
#   print(f"{name} from {house}")

# def get_name():
#   return input("Name: ")

# def get_house():
#   return input("House: ")



## Case 3
# def main():
#   name, house = get_student()
#   print(f"{name} from {house}")

# def get_student():
#   name = input("Name: ")
#   house = input("House: ")
#   return name, house


## Case 4 - using tuples
"""
  - returns tuple 
  - tuples are inmutable and it doesn't allow to change the values inside the tuple insted of using a list 
  - list is mutable because it allows to change the values inside of it
"""

# def main():
#   student = get_student()
#   print(f"{student[0]} from {student[1]}")

# def get_student():
#   name = input("Name: ")
#   house = input("House: ")
#   return (name, house)



## Case 5 - using dictionary - mutable
# def main():
#   student = get_student()
#   print(f"{student['name']} from {student['house']}")

# ### Using variables
# # def get_student():
# #   student = {}
# #   student["name"] = input("Name: ")
# #   student["house"] = input("House: ")
# #   return student

# ### Using inline
# def get_student():
#   name = input("Name: ")
#   house = input("House: ")
#   return {"name": name, "house": house}



## Case 6 - Using classes
# class Student:
#   # three dots means "let me impliment this later"
#   ...

# def main():
#   student = get_student()
#   print(f"{student.name} from {student.house}")

# ### method 1
# def get_student():
#   student = Student()
#   student.name = input("Name: ")
#   student.house = input("House: ")
#   return student
  

## Case 6.1 - Using classes and functions inside of them
class Student:
  # def __init__(self, name, house, patronus):
  def __init__(self, name, house):
    # if not name:
    #   raise ValueError("Missing name")
    # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #   raise ValueError("Invalid house")
    self.name = name
    self.house = house
    # self.patronus = patronus

  def __str__(self):
    return f"{self.name} from {self.house}"
  ## you can use __repr__ to get more informations and details about things that inside of the object. like what type of objects

  # Getter
  @property
  def house(self):
    return self._house

  # Setter  
  @house.setter
  def house(self, house):
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invlid house")
    self._house = house


  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Missing name")
    self._name = name


  # def charm(self):
  #   match self.patronus:
  #     case "Stag":
  #       return "🐴"
  #     case "Otter":
  #       return "🦦"
  #     case "Jack Russel terrieer":
  #       return "🐶"
  #     case _:
  #       return "/"

def main():
  student = get_student()

  # ## This will blocked by setter and raise ValueError
  # student.house = "SSC"

  # print(f"{student.name} from {student.house}")
  print(student)
  # print("Expecto Patronum!")
  # print(student.charm())

### method 2
def get_student():
  name = input("Name: ")
  house = input("House: ")
  # patronus = input("Patronus: ")
  # return Student(name, house, patronus)
  return Student(name, house)
    

# if the name of the file we called, run main
if __name__ == "__main__":
  main()
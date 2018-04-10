import random
import sys
import os

print("hello World")

name = ''' Jakub
 is my surname'''

print('\n' * 2)

print(name)

grocery_list = ["pomidorki", "ogorki", "jablka", "pyrki", "soki"]
print(grocery_list[0:2])


other_events = ["Mycie auta", "odebrać dzieci ze szkoły"]

to_do_list = [other_events, grocery_list]
print(to_do_list[1][1])

grocery_list.insert(1, "Pickle")
print(to_do_list[1][1])
del grocery_list[4]
print(to_do_list)

# unlike list tuple is not changed after it is created

pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)

dictionary = {'key1': 'value1',
              'key2': 'value2',
              'key3': 'value3'}

number2dict = {1: 'a', 2: 'b', 3: 'c', 4:'d',5:'e',6:'f',7:'g',
               8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',
               15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',
               22:'v',23:'w',24:'x', 25:'y',26:'z'}
dict2number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6, 'g':7,
         'h':8, 'i':9, 'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,
         'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,
         'x':24, 'y':25,'z':26}
'''
print(number2dict.get(1))
print(dict2number.get('a'))
'''


kodowanie = "abc"
dlugosc_kodowania = len(kodowanie)
wiadomosc = "defg"
dlugosc_alfabetu = 26

for i in range(0, len(wiadomosc)):
    num_wiadomosc = dict2number.get(wiadomosc[i:i+1])
    kodowanie_mod = i%dlugosc_kodowania
    num_kodowanie = dict2number.get(kodowanie[kodowanie_mod:kodowanie_mod+1])
    num_final = (num_wiadomosc + num_kodowanie)%dlugosc_alfabetu
    encryption = number2dict.get(num_final)
    print(encryption)

    #print("dlugosc kodowania=", i%dlugosc_kodowania)
    #print(wiadomosc[i:i+1], end="")
    #print(wiadomosc[i:i+1], end="")




print(dictionary.keys() , " a długość to " , len(dictionary))


age = 21
if age > 16 :
    print("you are old enough to drive")
else :
    print("You are not old enough to drive")


if age >= 21 :
    print("you are old enough to drive a tractor trailer")

if ((age >=1 ) and (age <=18)):
    print("You get a birthday")
elif (age == 21) or (age >= 65):
    print("You get a birthday")

test_file=open("/tmp/texst.txt", "wb")

print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write_me to the file\n", "UTF-8"))
test_file.close()


class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_sound(self,sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}". format(self.__name
                                                                       , self.__height,
                                                                       self.__weight,
                                                                       self.__sound)
cat = Animal("Kotek", 33, 10, "Miau")

print(cat.toString())

# inheritance


class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight,  sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. " \
               "His owner is {}". format(self.__name,
                                            self.__height,
                                           self.__weight,
                                           self.__sound,
                                            self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 44, 22, "Wow", "Kuba")

print(spot.toString())


class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()


test_animals.get_type(cat)
test_animals.get_type(spot)

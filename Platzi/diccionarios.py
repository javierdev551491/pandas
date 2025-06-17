numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[3])
information = {"nombre": "Javier",
               "Apellido": "Gutierrez",
               "Altura": 1.80,
               "Edad": 30
               }
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = { "Javier":{
             "Apellido": "Gutierrez",
             "Altura": 1.80,
             "Edad:": 30},
             "Carla":{
             "Apellido": "Martinez",
             "Atlura": 1.60,
             "Edad": 40}}
print(print("Javier"), contacts["Carla"].values())
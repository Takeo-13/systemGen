# до рефакторинга
import random
import json

# после добавления
from variables import *
import roman
import string


class System:
    """
    Куски системы:

    name
    x
    y
    type
    planets
    """

    def __init__(self, xc, yc):
        self.x = xc
        self.y = yc
        self.name = ''.join(random.choice(string.ascii_uppercase) for i in range(4)) + \
                    '-' + ''.join(str(random.randint(0,9)) for i in range(3))
        self.type = random.choice(star_classes)

        uniform = random.uniform(0.0, 1.0)      # вот как это короче сделать я даже не представляю
        self.anomaly = "Отсутствует" if uniform < 0.7328 \
                        else random.choice(sys_anomalies) if 0.7328 <= uniform < 0.98 \
                        else random.choice(sys_rare_anomalies)

        self.planets = []
        for i in range(1 if random.uniform(0.0, 1.0) < 0.002 else random.randint(0, 12)):
            self.planets.append(Planet(self.name, i).__dict__)

        try:
            with open(self.name, 'w+') as file:
                file.write(json.dumps(self.__dict__))
            file.close()
        except FileExistsError:
            print("Ты получил уникальную ошибку! Шанс этого 0.00000002%!")

        print(f"""
Name: {self.name}
X: {self.x} Y: {self.y}
Type: {self.type}
Anomaly: {self.anomaly}

Planets:""")
        for i in range(len(self.planets)):
            print(f"""
Name: {self.planets[i]['name']}
Type: {self.planets[i]['type']}
Radius: {self.planets[i]['radius']}
Distance: {self.planets[i]['distance']}
Anomaly: {self.planets[i]['anomaly']}

Satellites:""")
            for j in range(len(self.planets[i]['objects'])):
                print(f"""
Name: {self.planets[i]['objects'][j]['name']}
Type: {self.planets[i]['objects'][j]['type']}
Distance: {self.planets[i]['objects'][j]['distance']}
Anomaly: {self.planets[i]['objects'][j]['anomaly']}
Radius: {self.planets[i]['objects'][j]['radius']}
""")


class Planet:

    """
    Куски планет:

    name
    type
    radius
    distance
    anomaly
    objects
    """

    def __init__(self, origin, number):
        self.name = origin + " " + str(roman.toRoman(number+1))

        anomaly = random.uniform(0.0, 1.0)
        self.anomaly = 'Отсутствует' if anomaly < 0.7 \
                        else 'Нейтральная' if 0.7 <= anomaly < 0.8 \
                        else 'Отрицательная' if 0.8 <= anomaly <= 0.9 \
                        else 'Положительная'

        bad_code_syndrom = random.uniform(0.0, 1.0)
        planet = random.choice(basic_planets if bad_code_syndrom < coefficient_bound[0]
                        else giant_planets if coefficient_bound[0] <= bad_code_syndrom < coefficient_bound[1]
                        else uncommon_planets if coefficient_bound <= bad_code_syndrom < coefficient_bound[2]
                        else unique_planets)
        self.type = planet[0]
        self.radius = random.uniform(planet[1][0], planet[1][1])
        self.distance = random.uniform(planet[2][0], planet[2][1])

        self.objects = []
        for i in range(random.randint(0, planet[len(planet)-1])):
            self.objects.append(Satellite(self.name, i+1, self.type).__dict__)


class Satellite:

    """
    Куски спутника:

    name
    type
    distance
    anomaly
    radius
    """

    def __init__(self, origin, number, planettype):
        self.name = origin + '-' + str(roman.toRoman(number))

        giants_list = []
        for i in range(len(giant_planets)):
            giants_list.append(giant_planets[i][0])

        self.type = random.choice(giant_object_types) if planettype in giants_list \
                        else random.choice(object_types)

        self.radius = random.uniform(0.8, 1.8) if planettype in giants_list \
                        else random.uniform(0.3, 1.8)

        self.distance = random.uniform(200000, 500000)

        anomaly = random.uniform(0.0, 1.0)
        self.anomaly = 'Отсутствует' if anomaly < 0.7 \
            else 'Нейтральная' if 0.7 <= anomaly < 0.8 \
            else 'Отрицательная' if 0.8 <= anomaly <= 0.9 \
            else 'Положительная'
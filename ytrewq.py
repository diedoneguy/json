import json


class Car(object):
    def __init__(self,mark,model,year,color) -> None:
        self.mark = mark
        self.model = model
        self.year = year
        self.color = color
    def write_json(self,file):
        cars = {
            'mark':self.mark,
            'model':self.model,
            'year':self.year,
            'color':self.color
        }
        with open(file,'a')as files:
            json.dump(cars,files,indent=4)

    def show_json(self,file):
        with open(file,'r')as files:
            data = json.load(files)
            return data
data = Car(mark='Mersedes',model='Amg Gt63',year='2012',color='Black')
data.write_json(file='car.json')
reader = data.show_json(file='car.json')
print(reader)
from csv import reader
import json

# with open('get_json_adobe.json','r') as files:
#     data = json.load(files)
#     print(data)

class JsonData(object):
    def __init__(self,name: str,age: int) -> None:
        self.n = name
        self.a = age

    def write_json(self,file):#таким образом создается json формат
        student = {
            'name':self.n,
            'age':self.a
        }
        with open(file,'w') as files:
            json.dump(student,files,indent=4)

    def show_json(self,file):
        with open(file,'r')as files:
            data = json.load(files)
            return data

data = JsonData(name='Atai',age=4)
data.write_json(file='students.json')
reader = data.show_json(file='students.json')
print(reader)

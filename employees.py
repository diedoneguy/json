from ast import dump
from dbm import dumb
from importlib.metadata import files
import json

class StudentsJson(object):
    def __init__(self,login,email,age,phone_number) -> None:
        self.login = login
        self.email = email
        self.age = age
        self.phone_number = phone_number

    def write_json(self,file):
        students = {
            'login':self.login,
            'email':self.email,
            'age':self.age,
            'phone_number':self.phone_number
        }

        with open(file,'w')as files:
            json.dump(students,files,indent=4)
    
    def show_json(self,file):
        with open(file,'r')as files:
            data = json.load(files)
            return data


data = StudentsJson(login='Arkadii',email='arkadii@email.ru',phone_number=996702345789,age=18,)
data.write_json(file='todo.json')
reader = data.show_json(file='todo.json')
print(reader)






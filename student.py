from database import Database

class Student:
    def __init__(self, name= None, course=None, mobile=None):
        self._name = name
        self._course = course
        self._mobile = mobile

    @getters
    def name(self):
        return self_name
    def course(self):
        return self._course
    def mobile(self):
        return self._mobile
    
    @setters
    def set_name(self,name):
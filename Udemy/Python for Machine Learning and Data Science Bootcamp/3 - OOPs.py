#!/usr/bin/env python
# coding: utf-8

# # Classes and Objects

# In[1]:


class classname:
    var = 'This is a class variable'
    def func(self):
        print('I am inside the class')


# In[2]:


obj1 = classname()
obj1.var


# In[3]:


obj1.func()


# In[4]:


obj2 = classname()
obj2.var = 'This is the updated one!'
print(obj1.var,'\n',obj2.var)


# In[5]:


class student:
    def __int__(self,name,branch,year):
        self.n = name
        self.b = branch
        self.y = year
    def print_method(self):
        print('Name ',self.n)
        print('Branch ',self.b)
        print('Year ',self.y)


# In[16]:


obj1 = student("Paul","CSE","2019")
#obj1.print_method()


# # Q1
# Create two new vehicles called car1 and car2. Set car 1 to be a red convertible worth 70,000.00 with a name Ferrari and car2 to be a blue van named Jeep worth 15,000.00

# In[17]:


#define the vehicle class
class vehicle:
    name = ''
    kind = 'car'
    color = ''
    value = 100.00
    def description(self):
        desc_str = '%s is a %s %s worth $%.2f.'% (self.name,self.color,self.kind,self.value)
        return desc_str
car1 = vehicle()
car2 = vehicle()
car1.name = 'Ferrari'
car1.kind = 'convertible'
car1.color = 'red'
car1.vale = 70,000.00
car2.name = 'Jeep'
car2.kind = 'van'
car2.color = 'blue'
car2.vale = 15,000.00


print(car1.description())
print(car2.description())

    


# # Inheritance

# In[20]:


#Single Inheritance
class fruit:
    def __init__(self):
        print("I'm the parent class")
class citrus(fruit):
    def __init__(self):
        super().__init__()
        print("I'm a citrus and I belong to a fruit class")
obj1 = citrus()


# In[21]:


#Multiple Inheritance
class A:
    pass
class B:
    pass
class C(A,B):
    pass
issubclass(C,A) and issubclass(C,B)


# In[22]:


#Multilevel Inheritance
class A:
    x = 1
class B(A):
    pass
class C(B):
    pass
obj1 = C()
obj1.x


# In[23]:


#Hierarchical Inheritance
class A:
    x = 1
class B(A):
    pass
class C(A):
    pass
issubclass(B,A) and issubclass(C,A)


# In[27]:


#Hybrid Inheritance
class A:
    x = 1
#Hierarchical Inheritance
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
#Multiple Inheritance
class E(B,D):
    pass
obE = E()
obE.x


# # Super Function

# In[31]:


class vehicle():
    def start(self):
        print('Starting engine')
    def stop(self):
        print('Stoping engine')
class Twowheel(vehicle):
    def say(self):
        super().start()
        print('I have two wheels')
        super().stop()
Harley  = Twowheel()
Harley.say()


# # Overriding and Overloading

# In[38]:


#Overloading
def add(a,b):
    return a+b
def add(a,b,c):
    return a+b+c
add(2,4,5)


# In[42]:


def add(instanceOf,*args):
    if instanceOf ==int:
        result = 0
    if instanceOf ==str:
        result = ''
    if instanceOf ==float:
        result = 0.0
    for i in args:
        result +=i
    return result
add(int,3,4,5)
add(float,3.0,4.9,5.4)
add(str,'python',' ','Tutorial')


# In[46]:


#Overriding
class A:
    def checkit(self):
        print("I'm inside A")
class B(A):
    def checkit(self):
        print("I'm inside B")
ob1 = B()
ob2 = A()
ob1.checkit()
ob2.checkit()


# #  Encapsulation

# In[48]:


class encap(object):
    def __init__(self):
        self.a = 123
        self._b = 123
        self.__c = 123
obj1 = encap()
print(obj1.a,obj1.b,obj1.c)


# # Private Method

# In[51]:


class car:
    __maxspeed = 0
    __name = ''
    def __init__(self):
        self.__maxspeed = 200
        self.__name = 'Supercar'
    def drive(self):
        print('Maxspeed of car is ',self.__maxspeed)

obj1 = car()
obj1.drive()


# In[52]:


obj1.__maxspeed = 300
obj1.drive()


# In[56]:


class car:
    __maxspeed = 0
    __name = ''
    def __init__(self):
        self.__maxspeed = 200
        self.__name = 'Supercar'
    def drive(self):
        print('Maxspeed of car is ',self.__maxspeed)
    def SetMaxspeed(self,speed):
        self.__maxspeed = speed
obj1 = car()
obj1.SetMaxspeed(400)
obj1.drive()


# # Polymorphism

# In[58]:


class shark:
    def swim(self):
        print('The shark is swimming')
    def bones(self):
        print('shark has soft cartilage')
class Clownfist:
    def swim(self):
        print('Clownfishes can swim')
    def bones(self):
        print('Clownfishes can bones')
s1 = shark()
c1 = Clownfist()
for fishes in (s1,c1):
    print(fishes.swim)
    print(fishes.bones)


# In[60]:


def intheocean(fish):
    fish.swim()
s1 = shark()
c1 = Clownfist()
intheocean(s1)
intheocean(c1)


# In[ ]:






print("the name of God")#zطريقة قديمة

name = "obada"

age = 14

rank = 5


print("my name is: %s" % "obada")

print("my age is:%d" % 14)

print("my rank is:%f" % 5)


print("my name is: %s obada my age is: %d 14 and  my rank is 5 ")


# %s -> streng 
# %d -> number 
# %f -> float


o = "obada"

b = "king"

a = 10

print("my name is %s Iam %s my rank %d" % (o, b, a))






print("__string formatting__")#طريقة جديدة
#1_{:s} => string
#نفس الفكرة مع تغيرات بسيطة واشياء جديدة 
#هذه لست مطر لتحديد نوع البيانات هو ياخذ بترتيب
print("___{:S}___")
a1 = 'amar'
print("my name is : {:S}".format(a1)) 
#تحديد عدد الحروف المراد طباعتاها
print("my name is : {:.2s}".format(a1)) 

#2_{d} => number
print("___{:d}___")
a2 = 17
print("my age is : {:d}".format(a2))
 
#3_{:f} => float
print("___{:f}___")
a3 = 10
print("i have A : {:f}".format (a3)) 
#تحديد عدد الحروف المراد طباعتاها
print("i have A : {:.3f}".format(a3)) 


print("__new__")
#وضع علامة معينه كل 3

money = 100000000

print("my money is : {:,d")

print("my money is : {:d")

print("my money is : {:_d")


#تحدد ترتيب الطباعة 

a , d , c = ("one" , "two" , "three")

print("hello {0} {1} {2}")
print("hello {2} {0} {1}")
print("hello {2} {1} {0}")

#a=0 b=1 c=2

#طريقه 3 سهلة

myname = "obada"
age = 14

print(f"obada is {myname} age is {age})

#f" {} {} ""


o = " I love Python "

# split تقو بي تحويل النص الي list

print(o.split())

b = "l-love-Python"

print(b.rsplit("-")) #يجب تحديد طريقة فصل بين الكلمات

print("******good******")

a = " i love Python "

print(a.rsplit(" ", 2))

d = "l love Python "

print(d.split(" ", 1))


# center 

t = "obada"

print(t.center(9, "#"))

# count بتعدلك كم مره نادت الكلمة

e ="I love Python   I love Python"

print(e.count("love"))


# swapcase()الحرف الصغيره بتصير كبيره و أحرف البيره بتصير صغيره

y = "obada"
h = "OBADA"


#startswithتبلش بي البداية ايلا النهاية  

u = "l am bro"

print(u.startswith("l"))

n = "i am rich"

print(u.startswith("g"))


# endswith تبلش بي النهايه الي البداية


w = "I love Python"

print(w.endswith("n"))

r = "I love brother"

print(r.endswith("I"))






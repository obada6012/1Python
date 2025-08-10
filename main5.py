print("hello world ")

print("rjust") #نفس فكرت عم سنتر

o = ("obada")

print(o.rjust(8, " "))

print("ljust")

b = ("king")

print(b.ljust(8, " "))


a = "amar"#عن طريقت كتابت رقم و هو يقلك الحرف

print(a.index("m"))

e = "nana"

print(e.find("r"))


print("splitines")#انت تقو بتقسيم علا حسب السطر و ليسا انت تحددها الفرق بنها و بين spilt

y = """obada
atar
king😄"""

print(y.splitlines())

print(("expandtabs"))

r = "obada\tatar\tking\t"

print(r.expandtabs())

w = " "

print(w.isspace())

u = "obada-r"

print(u.isidentifier())#تستخدم ل السأواisalunm

i ="obada16😅"

print(i.isalnum())

print("replace")

#تقوم بتبديل الكلمات بكلمه اخر تفهم 

q = "one two  three one one"

print(q.replace("one","1"))
print(q.replace("one","1" "2"))


print("juin")

#تقوم LISTبتحويل STRING

k = ("obada", "atar" , "king")

print(" ".join(k))

print(type(" ".join(k)))





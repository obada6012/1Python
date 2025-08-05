#index هي بتحدد لك الحرف المعين مثال
#slicing يمكنك تحديد قطعه كاملة من النص  
#دأمن يبدأ العد من 0 

# obada =I Love Python

# print([0:6])




obada = "I Love Python" 

print(obada[0:1]+"\n")

print(obada[::1]+"\n")

print(obada[::2]+"\n")

print(obada[::3]+"\n")

print("good\n")

print(obada[0:-1]+"\n")

print(obada[::-1]+"\n")

print(obada[::-2]+"\n")

print(obada[::-3]+"\n")

# mothods  أوامر تضيف مع string تقو بي بعض الوظأف


obada ="    I love Python    "

print("---------------------")

print(obada.strip())
print("---------------------")

print(obada.rstrip())
print("---------------------")

print(obada.lstrip())
print("---------------------")

#/strip\ تقوم بحذف الشيء التي انتا تحددها
amar ="####I love Python ####"
print("---------------------")

print(amar.strip("#"))
print("---------------------")

print(amar.rstrip("#"))
print("---------------------")

print(amar.lstrip("#"))
print("---------------------")

# r بتحذف اي شي بتحدده من جهت آليمين ")

# l تحذف اي شي بتحدده من جهت اليسار

#Len يعد عدد للحرف و المساحات 


ob = "obada king"


obada ="obada 13 age"

print(len(ob))

print(obada.title())# بتكبر أول حرف بل كلمه و الحرف لي بعد الرقم

print(obada.capitalize())# يكبر اول حرف بل جملة 


print("zfill") #تقو بي اضأفت الأصفار حتا يصبح ألأرقام متسأوية

ob , ob2 , ob3 ="1" , "2" , "3"

print(ob.zfill(2))

print(ob2.zfill(2))

print(ob3.zfill(2))


print("upper   lower")

gg = "obada"

print(gg.upper())# تكبير كل الحروف
print(gg.lower())#تصغير كل الحروف 



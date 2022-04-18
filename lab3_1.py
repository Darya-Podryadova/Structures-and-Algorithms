mach = set() #Множество всех машин
mach.add('calc')
mach.add('leyb')
mach.add('resulta')
mach.add('arifm')
mach.add('apple')


tech = []
tech1 = tech2 = tech3 = tech4 = tech5 = tech6 = tech7 = tech8 = tech9 = tech10  = set() #Множества всех техникумов
tech1 = {'calc','leyb'}
tech2 ={'arifm','calc'}
tech3 ={'calc', 'leyb','arifm','resulta'}
tech4 ={'calc'}
tech5 ={'calc','resulta','arifm'}
tech6 ={'calc', 'resulta'}
tech7 ={'calc','leyb', 'resulta'}
tech8 = {'calc', 'arifm'}
tech9 ={'calc', 'leyb', 'resulta'}
tech10 ={'calc', 'arifm', 'resulta'}
tech.append(tech1)
tech.append(tech2)
tech.append(tech3)
tech.append(tech4)
tech.append(tech5)
tech.append( tech6)
tech.append(tech7)
tech.append( tech8)
tech.append(tech9)
tech.append(tech10)
for i in range(len(tech)):
    print(tech[i])

"""Далее используются внутренние функции, относяшиеся к структуре множества   """
inters  = tech1.intersection(tech2,tech3,tech4,tech5,tech6,tech7,tech8,tech9,tech10) #Пересечение
print("а) которыми обеспечены все техникумы = "+str(inters))

un = tech1.union(tech2,tech3,tech4,tech5,tech6,tech7,tech8,tech9,tech10)#Объединение
print("б) которые имеет хотя бы один техникум = "+str(un))

dif = mach.difference(un) #Разность множеств
print("в) которых нет ни в одном техникуме ="+str(dif))
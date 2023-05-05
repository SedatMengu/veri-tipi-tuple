demet = (1,2,3,4,5,6) 
print(demet)
print(type(demet)) 
# / (1,2,3,4,5,6)
# / <class 'tuple'>

# tersten işlem yaparken son elemanı 0.index olarak kabul etmez.

tuple_liste=(1,2,3,4,(9,8,7))
print(tuple_liste[-1])
# / (9,8,7)

# string ifadelerden bir liste yapacak ise ve tuple olmasını istiyor isek listenin sonuna , koymamız gerekir. aksi halde liste str olarak aldılanır.
tuple_liste2=("adnan")
print(type(tuple_liste2))

# / <class 'str'>

tuple_liste3=("kemal",)
print(type(tuple_liste3))
# / <class 'tuple'>

# tuple ların en büyük özellikleri değiştirilemez olmalarıdır. Mesela aşağıdaki gibi bir işlem yapamayız

demet[0] = 5 

#print =  TypeError: 'tuple' object does not support item assignment

## tuple da işlem yapabilmemiz için yeni bir listeye tanımlama yapmamız lazım.

yenidemet = demet[0] # yenidemet değişkenini demetin 0'ncı objesine eşitliyoruz.
print(yenidemet) 
#print = 1
yenidemet = demet[:5]
print(yenidemet)
# / 1
# / (1,2,3,4,5)

# string bir ifadeyi tuple yapabliriz. 

yazi = "Hello World!"
demet = tuple(yazi) 
print(demet)

#print = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!')


# tuple metotları 

# / 1 - .count() metodu tuple içinde belirtilen öğenin kaç kez geçtiğini sayar ve sonucu döndürür.

demet = (12,43,54,31,69,"Enes",35,42) 
print(demet.index(54))
# / 2


# 2 - .index() metodu bir tuple içinde belirtilen bir öğenin ilk bulunduğu konumun dizinini döndürür. Eğer öğe tuple içinde bulunamazsa ValueError hatası verir.

demet = (12,43,54,31,69,"Enes",35,42) 
print(demet.index("Enes")) 
#print = 5
from arboles_binarios import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)
abb.insert(70)
abb.insert(15)
abb.insert(23)
abb.insert(110)
abb.insert(90)
abb.insert(120)
abb.insert(100)
abb.insert(55)
abb.insert(58)

abb.transversal()
abb.remove(120)
abb.transversal()

abb.transversal("inOrden")
abb.transversal("preOrden")
abb.transversal("posOrden")

res = abb.search(35)
print(f"El resultado es: {res} ")

res2 = abb.search(48)
print(f"El resultado es: {res2} ")

abb.remove(35)
abb.transversal()

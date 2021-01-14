from colas import PriorityQueue

q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("Prueba 2 de Queue")
c1 = {"ID":1 , "Nombre":"MoonBin" , "balance": 20.5 }
c2 = {"ID":2 , "Nombre":"YeonJun" , "balance": 3456.5 }
c3 = {"ID":3 , "Nombre":"Eunwoo" , "balance": 10000000.0 }

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente = atencion.dequeue()
print(f"Bienvenido Sr.{ siguiente['nombre'] }, en qué podemos servirle el día de hoy")
print(atencion.to_string())

print("Pruebas de las colas con prioridad acotada")

maestres = { " prioridad ": 4 , " descripcion ": "Maestre" , "personas":["Juan P" , "Diego H"] }
niños = { " prioridad ": 2 , " descripcion ": "Niños" , "personas":["Santi H" , "Ángel H"] }
mecanicos = { " prioridad ": 4 , " descripción ": "Mecánicos" , "personas":["Diana T" , "Maria Z"] }

cpa = BoundedPriorityQueue( 7 )
cpa.enqueue( maestres['prioridad'] , maestres )
cpa.enqueue( niños['prioridad'] , niños )
cpa.enqueue( mecanicos['prioridad'] , mecanicos )
cpa.to_string()
sig = cpa.dequeue
print(sig)

def suma_list_rec( lista ):
    if len( lista ) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_list_rec( lista )

def cuenta_regre( value ):
    if value >= 0:
        print( str( value ))
        
        cuenta_regre( value - 1 )

    if value == 0:
        print( "Se acabo el tiempo" )

def pila_rec( pila ):
    n = len( pila )
    if n%2 == 1:
        print( f"El elemento {pila[ n//2 ]} se eliminara" )
        pila.remove(pila[ n//2 ])

    else:
        i = n//2
        print( f"Los elementos { pila[i] , pila[i-1] } se eliminaran" )
        pila.remove( pila[i] )
        pila.remove( pila[i-1] )

def main():
    datos = [ 9, 8, 1, 3, 33, 22 ,41 ]
    res = suma_list_rec( datos )
    print( res )


def main2():
    cuenta_regre( 10 )

def main3():
    pila = [17, 14, 4, 1, 10]
    pila2= [21, 2, 55, 53, 55, 22]
    pila_rec(pila)
    print(pila)
    pila_rec(pila2)
    print(pila2)

main2()

main3()

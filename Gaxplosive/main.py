import funciones as fn 

Pedidos = []

while True :
    print()
    print("====Gaxplosive====")
    print("[1] Registrar Pedido")
    print("[2] Listar todos Pedidos")
    print("[3] Imprimir Hoja de ruta")
    print("[4] Salir")
    print()
    try:
        
        opc = int(input("Ingrese opcion : "))

        if opc == 1 :
            fn.Registrar(Pedidos) 
        elif opc == 2 :
            print()
            fn.Listar(Pedidos)
            print()
        elif opc == 3 : 
            print()
            fn.ImprimirHoja(Pedidos)
        elif opc == 4 :
            print("Saliendo del programa...")
            break
        else:
            print("Opcion Invalida...")
    except:
        print("Error")
        
    
    

sectores = ['santiago','valparaiso','viña del mar']


def Registrar(Pedidos) : 
    try: 
        Nombre = input("Ingrese Nombre y Apellido : ")

        direccion = input("Ingrese Direccion : ")

        comuna = input("Ingrese sector [? para ver sectores]: ").lower()

        if comuna == "?" : 
            print("Sectores disponibles. (santiago / valparaiso / viña del mar)")

        while comuna not in sectores:
            comuna = input("Ingrese sector : ").lower()

        while True : 
            try :
                cilindo5k = int(input("Ingrese cuantos cilindros de 5kg desea llevar : ")) 
                cilindo15k = int(input("Ingrese cuantos cilindros de 15k desea llevar : "))
                cilindo45k = int(input("Ingrese cuantos cilindros de 45k desea llevar : "))
                break
            except:
                print("Dato ingresado incorrectamente : ")

        Pedidos.append({
            'NombreApellido' : Nombre,
            'Direccion' : direccion,
            'Comuna' : comuna,
            'Cil. 5kg' : cilindo5k,
            'Cil. 15kg' : cilindo15k,
            'Cil. 45kg' : cilindo45k
        })
        print("Pedido agregado correctamente ! ")
    except ValueError:
        print("Error")
    
def Listar(Pedidos) :
    if len(Pedidos) == 0 :
        print("Debe registrar almenos un pedido.")
    else:
        print("===Lista de Pedidos===")
        for pedido in Pedidos :
            print(pedido)
def ImprimirHoja(Pedidos) : 
    if len(Pedidos) == 0 : 
        print("Debe tener almenos un pedido registrado.")
    else:
        print("===Imprimir Hoja===")
        try : 
            try:
                Comuna_a_imprimir = input("Ingrese Comuna : ")
            except:
                print("Error")
            
            if Comuna_a_imprimir in sectores:
                print("===Imprimiendo Planilla===")
                archivo = f"Planilla_{Comuna_a_imprimir}"
                Lista = []
                
                for sector in Pedidos:
                    if sector['Comuna'] == Comuna_a_imprimir:
                        Lista.append(sector)
                with open(archivo,'w') as file:
                    for sector in Lista:
                        file.write(f"Nombre y Apellido : {sector['NombreApellido']}\n")
                        file.write(f"Direccion : {sector['Direccion']}\n")
                        file.write(f"Comuna : {sector['Comuna']}\n")
                        file.write(f"Cilindro de 5kg : {sector['Cil. 5kg']}\n")
                        file.write(f"Cilindro de 15kg : {sector['Cil. 15kg']}\n")
                        file.write(f"Cilindro de 5kg : {sector['Cil. 45kg']}\n\n")                      
            else:
                ("Sector no encontrado.")
        except:
            print("Error")
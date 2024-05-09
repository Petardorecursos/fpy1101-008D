import os 
import time
sw = 1
totalproductos = 0
pikachuroll = 0
otakuroll = 0
pulpovenenosoroll = 0
anguilaelectricaroll = 0
pika = 0
otaku = 0
pulpo = 0
anguila = 0

while sw == 1:
    sw = 2
    print("1- Pikachu Roll $4500 ")

    print("2- Otaku Roll $5000 ")

    print("3- Pulpo Venenoso Roll $5200 ")

    print("4- Anguila Electrica Roll $4800 ")

    print("5- salir")
     
    elec = int(input("ingrese su opcion elegida: "))

    while elec >=1 and elec <= 4:
            if elec == 1:
                totalproductos = totalproductos +1
                pikachuroll = pikachuroll +1
                pika = 4500
                break
            elif elec ==2:
                totalproductos = totalproductos +1
                otakuroll = otakuroll +1
                otaku = 5000
                break
            elif elec == 3:
                totalproductos = totalproductos + 1
                pulpovenenosoroll = pulpovenenosoroll +1
                pulpo = 5200
                break
            elif elec == 4:
                totalproductos = totalproductos +1
                anguilaelectricaroll = anguilaelectricaroll + 1
                anguila = 4800
                break
    if elec == 5:
        print("saliendo del programa,tenga buen dia")
        break
    elif elec !=1 and elec!=2 and elec!=3 and elec!=4 and elec!=5:
        print("opcion ingresada incorrecta,vuelva a intentarlo")
        sw=1
    while elec >=1 and elec <=4:
        elec = 5
        mas= int(input("1-Si\n2-No\n¿Su pedido esta completo? ingrese el numero 1 o 2 correspondiente a su eleccion: "))
        if mas == 2:
            print("eliga su siguiente pedido en esta orden")
            sw = 1
            break
        
        elif mas ==1:
            print("esta bien prepararemos su pedido")
            sw = 2
        else:
            print("opcion ingresada es incorrecta,vuelva a intentarlo")
            sw = 1

        while mas == 1 or mas == 2:
            mas = 3
            sw = 2
            desc = int(input("¿tiene algun codigo de descuento?\nseleccione una opcion\n1-Si\n2-No\n: "))
            while desc == 1:
                desc = 3
                code = input("ingrese el codigo de descuento: ")
                if code == "soyotaku":
                    print("perfecto,Usted tendra 10% de Descuento desde ahora")
                    descuento = 0.10
                    codigoconf = 1
                    subtotal= pika*pikachuroll + otaku*otakuroll + pulpo*pulpovenenosoroll + anguila*anguilaelectricaroll
                    descuentofinal = subtotal * descuento
                    totalfinal = subtotal - descuentofinal
                    print("************************************************")
                    print("TOTAL PRODUCTOS: ",totalproductos)
                    print("************************************************")
                    print("Pikachu roll: ",pikachuroll)
                    print("Otaku roll:",otakuroll)
                    print("Pulpo Venenoso roll: ",pulpovenenosoroll)
                    print("Anguila electrica roll: ",anguilaelectricaroll)
                    print("************************************************")
                    print("subtotal por Pagar: ",subtotal)
                    print("descuento por codigo: ",descuentofinal)
                    print("TOTAL: ",totalfinal)
                    print("************************************************")
                    break
                else:
                    print("el codigo es invalido")

                    print("s-SI")
                    
                    print("x-no,volver")

                    print("presione s para si o x para no")
                    op = input("¿Quiere volver a ingresarlo?")
                    if op == "s":
                        desc = 1
                    elif op == "x":
                        print("Cargando")
                        mas = 1 
            if desc == 2:
                nocodigo = 1
                subtotal= pika*pikachuroll + otaku*otakuroll + pulpo*pulpovenenosoroll + anguila*anguilaelectricaroll
                print("************************************************")
                print("TOTAL PRODUCTOS: ",totalproductos)
                print("************************************************")
                print("Pikachu roll: ",pikachuroll)
                print("Otaku roll:",otakuroll)
                print("Pulpo Venenoso roll: ",pulpovenenosoroll)
                print("Anguila electrica roll: ",anguilaelectricaroll)
                print("************************************************")
                print("subtotal por Pagar: ",subtotal)
                print("descuento por codigo: 0")
                print("TOTAL: ",subtotal)




        
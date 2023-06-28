import os
import msvcrt
import numpy as np
import funciones_validaciones as fn
import time

lista_ruts = []
lista_nombres = []
lista_identificador_unico = []
lista_nombres_mascotas =[]
acum_dias = 0
acum_total = 0
habitaciones = np.zeros((2,5),int)

os.system ("cls")
while True:
    try:
        os.system("cls")

        opc = int(input("""Bienvenido a la guarderia mascota segura escoja una opcion.))
        1. Grabar.
        2. Buscar.
        3. Retirarse.
        4. Salir.
        Ingrese una opcion: """))
        while True:
            if opc == 1:
                print("Muchas gracias por preferirnos, a contuniacion un breve proceso para registrarlo:")
                time.sleep (3)
                os.system("cls")
                fn.validar_rut()
                fn.validar_nombre()
                fn.validar_nom_masc()
                fn.validar_cant_dias()
                break
            else:
                print("Debe completar el registro para su mascota!!")
        while True:
             if opc == 2:
                  break
             else:
                  print("MASCOTA NO REGISTRADA!! EN EL SISTEMA DE HABITACIONES !!")
        while True:
             if opc == 3:
                  rut_pagar = int(input("Imgrese su rut para llevar al pago:"))
                  fn.validar_rut()
                  if rut_pagar in lista_ruts:
                    print("Su total a pagar es:",acum_dias)          
                     
    except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO!!!")


      
              


        
            
       




    
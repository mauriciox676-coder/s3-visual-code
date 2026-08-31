#Funcion sin retorno
def titulo():
    print("="*30)
    print("UNIVERSIDAD PRIVADA DEL NORTE")
    print("="*30)
#Funcion con retorno
def validar_nota(mensaje):
    while True:
        try:
            nota=float(input(mensaje))
            if nota>=0 and nota<=20:
                return nota
            else: 
                print("Error, la nota esta fuera de rango [0-20]")
        except ValueError:
            print ("Error: Ingrese un valor numerico")
            
def examen_final(proyecto_final,lab):
    nota_exa_final=proyecto_final*0.6+lab*0.4
    return nota_exa_final
#Funcion con retorno
def bono_Cisco(nota_ef,tiene_cisco):
    if tiene_cisco=="s":
        nota_ef+=1
        if nota_ef>20:
            nota_ef=20
    return nota_ef
#funcion con retorno
def calcular_promedio(t1,t2,t3,ep,ef):
    promedio=t1*0.1+t2*0.1+t3*0.1+ep*0.2+ef*0.5
    return promedio
#funcion con retorno
def condicion(promedio):
    if promedio>=12:
        estado="Aprobado"
    else:
        estado="Desaprobado"
    return estado

titulo()
nombre=input("Ingresar nombre del estudiante: ")
print("\n Ingreso de notas: ")
nota_t1=validar_nota("Ingresar nota T1(10%): ")
nota_t2=validar_nota("Ingresar nota T2(10%): ")
nota_t3=validar_nota("Ingresar nota T3(10%): ")
nota_ep=validar_nota("Ingresar nota Examen Parcial(20%): ")
print("Ingreso de notas para el examen final: ")
nota_proyecto=validar_nota("Ingresar nota del proyecto final: ")
nota_lab=validar_nota("Ingresar nota del laboratorio: ")
while True:
    curso_cisco=input("Tiene el certificado de Cisco (s/n): ").lower()
    if curso_cisco in['s','n']:
        break
    print("Error, ingresar (s/n)..!!")
nota_ef_calculado=examen_final(nota_proyecto,nota_lab)
nota_ef_total=bono_Cisco(nota_ef_calculado,curso_cisco)
promedio_final=calcular_promedio(nota_t1,nota_t2,nota_t3,nota_ep,nota_ef_total)
estado_alumno=condicion(promedio_final)
print("="*40)
print("REPORTE FINAL")
print("="*40)
print("Estudiante: ",nombre)
if curso_cisco=='s':
    print("Felicitaciones tiene 1 punto extra")
print("Nota de examen final: ",nota_ef_total)
print("Promedio ponderado del curso: ",promedio_final)
print("Condicion del estudiante: ",estado_alumno)
print("="*40)
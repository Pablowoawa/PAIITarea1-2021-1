#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time 
from math import floor

f = open('valores.txt','r') #Lectura de datos
linea = f.readline().split()
n = int(linea[0])#n
p = int(linea[1])#p
entrada = []
linea = f.readline().split()
for elem in linea:
    entrada.append(float(elem))#En entrada esta la segunda linea de la entrada
    

#Ruta de recoleccion
tiempoInicio = time.time()#inicio contador de tiempo
orden = sorted(entrada, key= lambda number: number-floor(number))#Se ordena la linea anteriormente leida según su parte decimal
ruta_recoleccion =[floor(orden[i]) for i in range(len(orden))]#Se obtienen las ID de las ciudades ya ordenadas.
print('La ruta de recoleccion: ',ruta_recoleccion)

#Plan de carga
plan_de_carga = [] #Lista donde se van agregando las ciudades correspondientes al plan de carga 
c_plandecarga =0 #Contador de reacomodaciones del plan de carga 

for i in range(n):#Las siguiente n lineas
    candidatos = []#Lista donde se agregan los candidatos a posibles reordenaciones
    linea = f.readline().split()
    if linea==['1']: #Si la linea solo contiene un 1, simplemente hay que agregar la ciudad i almacenada en la lista ordenada(orden)
        plan_de_carga.append(orden[i])
        continue #No lee nada mas de lo que hay abajo
        
    contadorpop = len(linea) #Calcula cuantas cajas tenemos que dropear
    
    for k in range(contadorpop):
        a = plan_de_carga.pop() #drop
        candidatos.append(a) #Se agrega el drop a candidatos
    candidatos.append(orden[i])#Además se agrega la posicion i de la lista ordenada (orden)
    candidatos_sorted = sorted(candidatos,reverse = True, key=lambda valor: valor-floor(valor)) #Esta lista con valores se ordena de mayor a menor
                                                                          #y segun su parte decimal
    
    for numero in range(len(candidatos)): #Revisa si hubo una reordenación
        if candidatos[numero]!=candidatos_sorted[numero]:
            c_plandecarga+=1
            break
            
            
    for objeto in candidatos_sorted:
        plan_de_carga.append(objeto) #Se reponen las cajas que dropeamos y se agregan al plan de carga, pero esta vez ordenadas (en reverse)
        
    
        
plan_de_carga_final = [floor(plan_de_carga[i]) for i in range(n)] #Se obtienen los enteros de los numeros, y corresponde
                                                                  #al plan de carga
        
print('El plan de carga: ',plan_de_carga_final)
print('Número reacomodaciones: ',c_plandecarga)


#Plan de descarga

anterior = plan_de_carga[:] #Anterior va a ser el plan de carga anteriormente determinado (con sus decimales) y se irá vaciando
plan_descarga = []
c_plandescarga =0

for i in range(n):
    linea = f.readline().split()
    candidatos = [] #Lista de candidatos que cumple la misma funcion de la anteriormente explicada
    if linea==['1']: #Si la lista solo contiene un 1 simplemente se agrega al plan de descarga la ultima posicion 
                     #del plan de carga anteriormente determinado
        plan_descarga.append(anterior[-1])
        anterior.pop() #Además se dropea ese valor
        continue #Se ignora el resto y se pasa a la siguiente iteracion
     
    c_plandescarga+=1
    contadorpop = len(linea) #Calcula cuantas veces hay que dropear cajas
    for k in range(contadorpop):
        a = anterior.pop()#Se sacan las cajas
        candidatos.append(a)#pero se guardan en la lista candidatos
        
    plan_descarga.append(anterior[-1]) #se agrega al plan de descarga la ultima posicion 
                                       #del plan de carga, ojo que a esta lista (anterior) se le van sacando objetos

    anterior.pop() #Como se agregó al plan de descarga, tambien hay que sacarlo de la lista
    candidatos_sorted = sorted(candidatos,key=lambda valor: valor-floor(valor))#Se ordena la lista de candidatos
    
    
    for elem in candidatos_sorted:
        anterior.append(elem)#Se reponen las cajas que se sacaron pero esta vez ordenadas
        
        
f.close()
plan_descarga_final = [floor(plan_descarga[i]) for i in range(n)]#Se obtienen las ID del plan determinado
print('El plan de descarga: ',plan_descarga_final)
print('Número reacomodaciones: ',c_plandescarga)




tiempoFinal = time.time()
tiempo = tiempoFinal - tiempoInicio
print(tiempo)


#Escribir en el txt deco2

deco1 = open('deco2.txt','w')
deco1.writelines([str(ruta_recoleccion[i])+' ' for i in range(n)])
deco1.write('\n')
deco1.writelines([str(plan_de_carga_final[i])+' ' for i in range(n)])
deco1.write('\n')
deco1.write(str(c_plandecarga))
deco1.write('\n')
deco1.writelines([str(plan_descarga_final[i])+' ' for i in range(n)])
deco1.write('\n')
deco1.write(str(c_plandescarga))
deco1.write('\n')
deco1.write(str(tiempo))
deco1.close()


# In[ ]:





# In[ ]:





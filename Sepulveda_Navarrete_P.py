#!/usr/bin/env python
# coding: utf-8

# In[5]:


import time

def minimoEntre(a,b):
    if b<=a:
        return b
    else:
        return a
    
    
f = open('valores.txt','r') #Inicio lectura de datos
linea = f.readline().split()

n = int(linea[0])
p = int(linea[1])

entradas= []
linea = f.readline().split()
f.close()#Fin de la lectura de datos
for elem in linea:
    entradas.append(float(elem)) #En entradas se guardan los numeros entre 0 y 1 de la entrada


tiempoInicial = time.time() #inicio contador de tiempo


#Plan de recolección 

recoleccion = []
for i in range(n):
    recoleccion.append([i+1,entradas[i]]) #Se agrega la id del elemento, y el elemento en sí
#Ordenamos la lista de recoleccion
recoleccion.sort(key=lambda item: item[1]) #Ordenamos la lista segun su segundo item, correspondiente al valor decimal

ruta_recoleccion = [recoleccion[i][0] for i in range(n)] #Lista con el plan de recoleccion 
print('La ruta de recolección: ', ruta_recoleccion)



#Plan de carga
indice= 0 #una variable indice para ir recorriendo la lista de entradas
contador_reacomodaciones = 0 #Contador de reacomodaciones
decodificacion = [] #La lista donde se iran guardando las decodificaciones actuales
last_p_values = [] #En la lista last_p_values se guardan los ultimos p+1 valores
limitenew = 0 #Un valor que se usa para identificar si el valor limite llego a su maximo o no.

for k in range(1,n+1):
    valores=[]
    limite = minimoEntre(k,p+1) #Valor mínimo entre k y p+1
    for i in range(limite):
        indice+=1
        valores.append([entradas[n-1+indice],0]) #Agregamos las entradas seguido de un 0, que luego será su ID
        
    if k==1: #Si k=1 la ID del primer valor será la primera ciudad incluida en la ruta de recoleccion
        valores[0][1] = ruta_recoleccion[0]
        last_p_values.append(valores[0][1]) #En la lista last_p_values se guardan los ultimos p+1 valores
                                            #Que luego servirán para asignar los indices que anteriormente estaban 
                                            #Asignados como 0
        
    
    if limite>limitenew and k!=1: #Si el minimo entre k y p+1 es mayor a limitenew last_p_values contiene a todos los ID
                                  #contenidos en la lista de valores ordenados
        last_p_values = [valores_ordenados[i][1] for i in range(len(valores_ordenados))]

        
    elif limite<=limitenew and k!=1: #En caso contrario last_p_values va a contener los ultimos p+1 ID
        last_p_values = [valores_ordenados[i][1] for i in range(len(valores_ordenados)-p,len(valores_ordenados))]
        
                           
    for i in range(len(valores)-1): #En este paso se asignan las ID que anteriormente se asignaron a last_p_values
        valores[i][1] = last_p_values[i]
        
    valores[-1][1] = ruta_recoleccion[k-1] #El ultimo dato en valores siempre corresponde a la posicion k-1 de ruta_recoleccion

    
    valores_ordenados = sorted(valores, key=lambda item: item[0]) #En valores ordenados se encuentran los valores ordenados con su respectiva ID

    
    
    
    flag = 0 #Bandera off
    
    for i in range(len(valores)):
        if valores[i][1] != valores_ordenados[i][1]: #Si se detecta un reordenamiento
            flag=1 #Se enciende la bandera
            popeos = len(valores_ordenados) - i -1 # Se calcula un numero de cuantas cajas hay que sacar
            break

        
    if flag==1: #Si anteriormente se detectó un reordenamiento: 
        contador_reacomodaciones+=1 #Se suma 1 al contador de reacomodaciones
        for i in range(popeos):
            decodificacion.pop() #Se sacan (popeos) veces las cajas

        
        for i in range(len(valores_ordenados)-(popeos+1),len(valores_ordenados)):
            decodificacion.append(valores_ordenados[i][1]) #Se reponen las cajas pero ahora con los valores ordenados

    else:
        decodificacion.append(valores_ordenados[-1][1]) #Si no hubo reordenamiento simplemente se agrega la ultima ID de
                                                        #la ultima posicion de valores ordenados
        
        
        
    limitenew = limite #Se asigna limitenew para luego ver si el valor limite ha llegado a su maximo o sigue avanzando


plan_carga = decodificacion[:]
r1 = contador_reacomodaciones
print('El plan de carga: ',plan_carga)
print('Reacomodaciones',r1)


#Plan de descarga


indiice= indice #Indice para recorrer la lista de entradas
decodificacion = plan_carga[:] #Ahora la lista de decodificacion corresponde al plan de carga anteriormente calulado
                               #El cual poco a poco se irá vaciando

contador_reacomodaciones = 0 #Contador de reacomodaciones
last_p_values = [] #En la lista last_p_values se guardan los ultimos p+1 valores
ruta_descarga = []#Lista en la cual se iran agregando las ciudades correspondientes a la ruta de descarga
limitenew= 0 #Un valor que se usa para identificar si el valor limite llego a su maximo o no.

for k in range(1,n+1):
    valores=[]
    limite = minimoEntre(n-k+1,p+1) #Valor mínimo entre n-k-1 y p+1

    for i in range(limite):
        indiice+=1
        valores.append([entradas[n-1+indiice],0])#Agregamos las entradas seguido de un 0, que luego será su ID
       
    if limite<limitenew:#Si el limite no ha llegado a su maximo
        #Los valores que corresponden a los futuros indices son todos los ID que hay en valores ordenados, menos el ultimo
        last_p_values = [valores_ordenados[i][1] for i in range(len(valores_ordenados)-1)] 

        
    elif limite>=limitenew:#En caso contrario
        last_p_values = decodificacion[-(p+1):] #Los valores que corresponden a los futuros indices son los ultimos p+1
        #valores que hay en la lista de decodificacion

            
    for i in range(len(valores)):#Asignamos los indices anteriormente calculados
        valores[i][1] = last_p_values[i]

    valores_ordenados = sorted(valores, key=lambda item: item[0])#Lista de los valores ordenados

    flag = 0 #Bandera off

    
    for i in range(len(valores)): #Detectar si ocurrió una reacomodacion
        if valores[i][1] != valores_ordenados[i][1]:
            flag=1
            popeos = len(valores_ordenados) - i -1 #Se calcula el valor de cuantos drops hay que hacer
            posicion = i #Se guarda la posicion de la primera caja que cambio su posicion
            break
            
    if flag==1: #Si hubieron reacomodaciones:
        contador_reacomodaciones+=1 #Se suma 1 al contador de reacomodaciones
        for i in range(popeos): #Se dropean (popeos) veces las cajas
            decodificacion.pop() #Desapilamos 
            
        ruta_descarga.append(valores_ordenados[-1][1])#Se agrega la ultima ID de valores ordenados a la lista donde se 
                                                      #encuentra la ruta de descarga

        decodificacion.pop()#Como ya se agregó esta ultima ID, hay que sacarla igual.

        for i in range(posicion,popeos+posicion):
            decodificacion.append(valores_ordenados[i][1])#Se reponen los valores que sacamos, pero ahora ordenados

    else: #Si no hubieron reacomodaciones
        ruta_descarga.append(valores_ordenados[-1][1]) #Se agrega a la lista donde esta la ruta la ID correspondiente
        decodificacion.pop() #Y se dropea la caja

        
    
    limitenew = limite 


print('La ruta de descarga: ',ruta_descarga)
print('Reacomodaciones: ',contador_reacomodaciones)




tiempoFinal = time.time() #Se para el timer.

tiempo = tiempoFinal- tiempoInicial #Contiene el tiempo que se demoró la decodificacion
print(tiempo)
#Escribir en el txt deco1

deco1 = open('deco1.txt','w')
deco1.writelines([str(ruta_recoleccion[i])+' ' for i in range(n)])
deco1.write('\n')
deco1.writelines([str(plan_carga[i])+' ' for i in range(n)])
deco1.write('\n')
deco1.write(str(r1))
deco1.write('\n')
deco1.writelines([str(ruta_descarga[i])+' ' for i in range(n)])
deco1.write('\n')
deco1.write(str(contador_reacomodaciones))
deco1.write('\n')
deco1.write(str(tiempo))
deco1.close()


# In[ ]:





# In[ ]:





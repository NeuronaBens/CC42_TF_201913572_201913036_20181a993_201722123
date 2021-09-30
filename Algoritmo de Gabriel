# Algoritmo de Gabriel
## Consideraciones importantes
1) Vale la pena resaltar que el grafo es perfectamente rectangular (todo nodo que no esté en una esquina o lado máximo tiene 4 nodos hermanos, que son adyacentes)
2) Hemos considerado a todos los puntos que no son distribución como puntos de entrega
3) Consideramos el peor camino posible como el recorrido secuencial de todos los nodos desde el inicio hasta el final.
La comlejidad para este "peor" algoritmo (o el más costoso) es:
$$
 c(e, v) = v+ 0,011111e^{2} 
 $$ donde c es la función de costo de realizar las entregas de ese modo.
 v representa la cantidad de vértices y e representa la cantidad de aristas.
 Por otro lado, la complejidad de este algoritmo es:
 $$
 O(e, v) = e + v 
 $$ Como ejemplo, si tenemos 10 nodos y 100 vértices, la cantidad de accesos a los datos sería 110.
 4) El uso de motociclistas es ilimitado y sin costo, o sea, solamente se considera la distancia total recorrida y el tiempo que usan en el viaje.
 
 ## Descripción verbal de la idea de algoritmo
 ### Comparaciones iniciales
 - El tiempo a corto plazo (menos de 90 minutos de recorrido total de un único motociclista) impacta menos que la cantidad de nodos recorridos.
 - El tiempo a largo plazo (más de 90 minutos) tiene más impacto que la distancia recorrida en ese tramo particular.
 - El punto donde se encuentran las funciones de costo individuales (d) y (0,1t^2), se halla de la siguiente manera:
$$
d(x) = x
$$ $$
t(x)= 0,01x^{2}
$$ $$
d(x) = t(x) \rightarrow 0 = 0,01x^{2} - x \rightarrow x_{1,2} = 0; 90
$$
- esta nueva información nos provee de una realización importante, y es que hasta que llegamos a la hora y media, el tiempo no será un factor tan importante. Pero, a medida que crezca ese valor, será cuadráticamente más importante.
### El peor resultado en 3000 (50*60) nodos

Con ayuda de una función desarrollada previamente, podemos calcular, que el peor resultado posible (usando el algoritmo secuencial y 1 solo motorizado) en un promedio de 5 minutos entre nodos es: 
$$
c(d,t) = 3000 + 0,011111(5 \times 50 \times 60)^{2} \approx 2500000
$$ Suponiendo que el costo es en soles, podemos decir que cuesta 25 milllones de soles realizar esa operación (en perdidas materiales, y efecto del tiempo de demora sobre el negocio).

### Mi solución algoritmica

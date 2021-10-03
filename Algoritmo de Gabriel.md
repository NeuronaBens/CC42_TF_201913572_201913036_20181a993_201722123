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

Para solucionar este problema mi propuesta es la siguiente
Algoritmo:

Definace el Grafo G de dimensiones X, Y
Almacene los nodos de distribución en el arreglo D de forma que y aumenta Y veces antes de que aumente 1 vez x. 

Definace la función FVAdj con parámetros x, y, X, Y, dir, sup:
» si dir = "left":
»» disminuya x en 1 mientras el nodo G(x+1, y) exista:
»»» si sup = "total" y el nodo en x+1 de G esta visitado o es de distribución:
»»»» no visite ese nodo (regrese False)
»»» si sup = "dist" y el nodo es de distribución:
»»»» no visite ese nodo (regrese False)
»»» si sup = "semi":
»»»» si el nodo es de distribución:
»»»»» no visite a ese nodo (regrese False)
»»»» si el nodo esta visitado y el resto de nodos que le siguen también:
»»»»» no visite ese nodo (regrese False)
»»»» de otra forma:
»»»»» visite ese nodo (regrese True)
»»» de otra forma:
»»»» visítelo (regrese True)
» Al igual que el patrón anterior, defina de la misma manera para las direcciones "right", "up", "down", únicamente cambiando el cambio de la variable que corresponda.

Inicie un bucle que recorre D =>
» Inicie un bucle indefinido:
»» aux = FVAdj(x, y, X, Y, "left", "semi")
»»» si aux es falso:
»»»» detengase
»»» de otra forma:
»»»» continúe
» Realice bucles similares para cada dirección "right", "up", "down".

Inicie un bucle que recorre D =>
» Inicie un bucle indefinido:
»» verifique si el nodo (x+1, y+1) de G está visitado o no existe:
»»» si se cumple la condición:
»»»»  continúe
»»» si no:
»»»» Visite a esa nodo, pero escoja la menor distance entre la opción "left", "down" y la opción "down", "left".
»»»» Luego visite a todos los nodos a la derecha de este nodo, de forma secuencial con FVAdj(x, y, X, Y, "right", "semi"), si regresa False, termine el bucle. 

Inicie un bucle que recorre D =>
» inice un bucle indefinido:
»» defina n = 1
»» bool = la columna x + n de G esta completamente visitada
»» si bool es True:
»»» detengase
»» Realice FVAdj(x, y, X, Y, "up", "semi") de forma secuencial en todos los nodos de la columna si bool es False para esa columna, si FVAdj regresa False:
»»» n+=1
»»» continúe 
» inice un bucle indefinido:
»» defina n = 1
»» bool = la columna x + n de G esta completamente visitada
»» si bool es True:
»»» detengase
»» Realice FVAdj(x, y, X, Y, "down", "semi") de forma secuencial en todos los nodos de la columna si bool es False para esa columna, si FVAdj regresa False:
»»» n+=1
»»» continúe 

Todos los Nodos deberían haber sido visitados al menos un vez hasta este punto.

### Análisis de complejidad
Ampliamente, y sin entrar en mucho detalle, la complejidad de este algoritmo en el peor de los casos es O(v) donde v es el número de nodos. Esto se cumple porque los recorridos de nodos siempre son o en columnas (X) o en filas (Y), por ende, se realizan X verificaciones en Y filas o viceversa, y X*Y es igual a la cantidad de nodos (v), en este caso.

### Análisis del espacio de búsqueda
Para este algoritmo en particular, el espacio de búsqueda se puede proveer de un nodo a la vez y supone la desición de continuar visitando o no. Por ello, la altura del espacio de búsqueda de este algoritmo es igual a la densidad del espacio de búsqueda.

### En comparación con el peor caso posible
Este algoritmo tiene la desventaja de que puede visitar el mismo nodo entre 1 y 2 veces, por ello puede costar un poco más en distancia, pero en el caso del tiempo es sumamente más productivo, ya que explota la libertad de tener infinitos motorizados.
Se puede calcular el peor caso posible dentro de mi solución para compararlo con los solución completamente secuencial.
El peor caso posible con este algoritmo supone visitar los nodos de una columna completamente por cada fila, entonces, tomando en cuenta que el promedio de tiempo entre nodo y nodo es 5 minutos, se puede expresar la fórmula de la siguiente manera:
$$
c(d, t) = 50 \times 0,011111(5 \times 60)^2 \approx 50000
$$Esta solución, entonces, reduce el costo de la propuesta secuencial en 50 veces.
Se puede concluir, entonces, que mi solución en una demora de 2 veces el tiempo de la solución más simple, permite una respuesta 50 veces más eficiente. 

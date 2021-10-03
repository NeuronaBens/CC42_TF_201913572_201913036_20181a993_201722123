# Algoritmo de Omar
## Consideraciones importantes

1.  Vale la pena resaltar que el grafo es perfectamente rectangular (todo nodo que no esté en una esquina o lado máximo tiene 4 nodos hermanos, que son adyacentes)
2.  Hemos considerado a todos los puntos que no son distribución como puntos de entrega
3. -   El punto donde se encuentran las funciones de costo individuales (d) y (0,1t^2), se halla de la siguiente manera: $$ d(x) = x $$ $$ t(x)= 0,01x^{2} $$ $$ d(x) = t(x) \rightarrow 0 = 0,01x^{2} - x \rightarrow x_{1,2} = 0; 90 $$
4.  El uso de motociclistas es ilimitado y sin costo , o sea, solamente se considera la distancia total recorrida y el tiempo que usan en el viaje.


## Descripción verbal de la idea de algoritmo
### 
-   Separaremos el cuadrante en 4 zonas
- bfs{
 Crearemos un conjunto de nodos visitados y no visitados
Asignaremos un nodo inicial y lo quitaremos de la lista
Veremos los nodos adyacentes a este y los marcaremos como visitados
Si un nodo visita a otro no visitado lo pondremos en una lista padre
 }
-  Recorreremos desde cada punto de distribución en las esquinas para hallar los caminos en 4 segmentos

### Mi solución algoritmica

Para solucionar este problema mi propuesta es la siguiente Algoritmo:
Definace el Grafo G de dimensiones X, Y Almacene los nodos de distribución en el arreglo D

Iniciamos un bucle que recorre D y guarda los 4 puntos más a la esquina en una lista

Iniciamos una def para separar el grafo rectangular en 4 zonas

Iniciamos un bucle bfs para cada zona

Asi todos los nodos deben haber sido visitados por lo menos una vez



### Análisis de complejidad
Ampliamente, y sin entrar en mucho detalle, la complejidad de este algoritmo en el peor de los casos es _O_(_E_ + _V_) donde (_E_) es el número de aristas y ( _V_) el numero de vértices. El razonamiento es porque en el peor caso, cada vértice y cada arista será visitado por el algoritmo.

### Análisis del espacio de búsqueda

Para este algoritmo se necesita asignar por lo menos 4 puntos de distribución por que se se tomara en cuenta 4 secciones para hacer el algoritmo de BFS en cada una de estas


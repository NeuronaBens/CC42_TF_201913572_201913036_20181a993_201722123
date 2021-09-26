# Complejidad Algorítmica
## Descripción
Este trabajo espera que nosotros podamos resolver el conocido problema VRP (Vehicle Routing Problem). 

Debemos minimizar una función de la forma:
f(d, t) = d + g(t) 
Donde d es la distancia recorrida por cada vehículo (número ilimitado de estos) y g(t) es una función que permite realizar una comparación entre el tiempo y la distancia.
El objetivo del trabajo es buscar un equilibrio entre costo de entrega y tiempo. Uno de los mayores ejemplos es el reparto en casa o también llamado “Delivery”, los cuales reciben órdenes o pedidos mediante una aplicación, luego deben de planificar una ruta considerada para reducir el costo de entrada y el tiempo ya que a mayor demora, menor será la satisfacción del cliente lo cual significa obtener una mala calificación y pérdida de clientes.
Para simplificar el problema se plantea que la ciudad donde se distribuye tiene una distribución perfectamente rectangular, similar a Manhattan.

## Requisitos
Entre 50 y 100 puntos de distribución (almacenes).
Entre 2500 y 5000 puntos de entrega.
Una cantidad ilimitada de vehículos.
Cada punto de distribución y punto de entrega, está definido por una posición X, Y correspondiente a un punto en la ciudad.

## Especificaciones
Función costo de traslado de vehículo específica a minimizar:
f(d, t) = d + 0,1 t ^3 
Hemos decidido definir la función de este modo, porque consideramos que el tiempo es relevante cuando se supera a la unidad de medida básica, que hemos escogido como la hora, además, consideramos a la distancia como una función lineal de costo en sí misma, y suponemos que se mide en kilómetros recorridos.

Empresa modelo a elegir:
La empresa que escogimos para tomar en cuenta los factores de cálculo es Fazil. Esta empresa, es del grupo Falabella. Es un emprendimiento que se dedica a hacer delivery de productos de supermercado. Tienen una política de tiempo de entrega en 1 hora, por ello, decidimos considerar esa la unidad de medida básica para el tiempo.

Otras especificaciones y restricciones:

- Como la ciudad es completamente rectangular, de arista a arista la distancia de recorrido es la misma para cada arista.
- Pero, cómo puede haber tráfico, o arreglos de pisto, o construcciones, o accidentes, el tiempo varía.
- El número de nodos se genera aleatoriamente.
- El número de almacenes se genera aleatoriamente.
- Se usará lista de adyacencia para definir la conectividad de los nodos.
- La lista de adyacencia será con pesos de aristas, que representan el tiempo de nodo a nodo.
- Calcularemos la distancia tomando en cuenta la cantidad de nodos que ha recorrido el vehículo.

Definición verbal del algoritmo para generación de puntos de entrega y distribución:
 1. Definir la cantidad de puntos de distribución aleatoriamente
 2. Definir la cantidad de nodos verticales y horizontales aleatoriamente, se genera un aleatorio igual o menor a 1000 y mayor a 2, y luego, según eso, se genera un número que multiplicado este entre 2500 y 5000.
3. Calcular la cantidad de nodos como # nodos verticales * # nodos horizontales
4. Definimos listas de booleanos, donde la cantidad de “Trues” es la cantidad de nodos que falta definir de ese tipo de nodo, son listas con nodos de  “Entrega” o “Distribución”. 
La cantidad de elementos se define como # nodos totales - # nodos de distribución y la  otra lista con # nodos de distribución.
6. Se define N, con valor 0, que incrementa en cada iteración.
7. Empezamos un bucle
8. En la posición X = 0, Y = 0. Y, definimos cual es el tipo de nodo en ese punto, puede ser punto de entrega o punto de distribución, aleatoriamente.
9. Luego, restamos 1 al contador del tipo de nodo que se escoge.
10. Luego, se nombra a ese nodo como “N.X.Y” y si es un nodo de tipo distribución lleva el nombre “N.X.Y.D”.
11. Si llegamos al número máximo de nodos verticales, pasamos procesar de igual manera la siguiente columna, por ejemplo, pasamos de X = 0, Y = 0, a X = 1, Y = 0.
12. Una vez que los contadores de puntos de entrega y distribución llegan a 0, se detiene el bucle.
13. (Notar que: xmin = 0, ymin = 0, ymax = #nodos verticales, xmax = #nodos horizontales) se sabe gracias al nombre que el nodo de nombre “x.y”, será vecino visitable de un nodo con nombre “x.y-1”, “x-1.y”, “x+1.y”, “x.y+1”. Entonces, se generará una lista de adyacencia con ayuda de un bucle que por nodo, realiza la validación o operación de nodos vecinos visitables, además, genera aleatoriamente un tiempo o peso de arista.


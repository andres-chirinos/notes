# Distribución Muestral
## Muestra. 
Es el subconjunto de unidades de observación de una población objeto de estudio. $u_{1},u_{2},\dots,u_{n} \quad \forall n<N \quad\text{si es muestra sin reemplazo}$ 
## Muestra Aleatoria
_Sea_ $X_{i}$ _una variable aleatoria poblacional con función de distribución_ $f(X_{i})$ _. Una muestra aleatoria (m.a.) de_ $X_{i}$ _es un conjunto de n variables aleatorias (observaciones) denotadas como_ $X_{1}, X_2, …, X_n$ _tal que cumple dos propiedades._

1. _Las_ $X_{i}$ _tienen la misma distribución de_ $X$ _, es decir,_ $f(X) = f(x_{i}) ⇒ f(x_{1}), f(x_{2}), … ,f(x_{n}) = f(x_{1}) ⋅ f(x_{2}) ⋅ … ⋅ f(x_{n}) = \prod_{i=1}^{n}{f(x_{i})} = \prod_{i=1}^{n}f(x)=nf(x)$ _Son idénticamente distribuidas._
2. _Las variables aleatorias_ $X_{1} , X_{2} , … , X_{n}$ _son independientes._

>_Nota: Si la m.a. viene de una población infinita ó si la m.a. se elige con reemplazo, se cumplen las propiedades anteriores. Pero si la m.a. se selecciona sin reemplazo, las propiedades no se cumplen._

_Si $\frac{n}{N}\leq0.05$ se cumple aproximadamente las propiedades._
_Encuesta de Hogares. Octubre._   
## _Ejercicio_

1. _De una población normal con media de 13 y varianza 16, se extrae una m.a. de tamaño 10 ( x 1 , x 2 , … , x 10 ) hallar: P x 1 − x 4 + x 8 ≥ 18 = ? ;   N → ∞_
    _x 1 , x 2 , … , x 10 son variables independientes_ _Son idénticamente distribuidas X i ~ N 13 , 16           N 𝜇 x , 𝜎 x 2_ V a r y = V a r x 1 − x 4 + x 8 = V x 1 + V x 4 + V x 8 = 48 _P x 1 − x 4 + x 8 ≥ 18 = P y ≥ 18 ￼ y ~ N 13 , 48 ~ N 𝜇 y , 𝜎 y 2_ P y ≥ 18 = P z ≥ 18 − 13 18 = P z ≥ 0 . 72 = 1 − P z < 0 . 72 = 1 − 𝜙 0 . 72 = 1 − 0 , 76 = 0 . 24  
    

_Sol.  
y = x 1 − x 4 + x 8 ￼ E y = E x 1 − x 4 + x 8 = E x 1 − E x 4 + E x 8_ = 13 − 13 + 13 = 13 V a r y = V a r x 1 − x 4 + x 8 = V x 1 + V x 4 + V x 8 = 48 P y ≥ 18 = P z ≥ 18 − 13 18 = P z ≥ 0 . 72 = 1 − P z < 0 . 72 = 1 − 𝜙 0 . 72 = 1 − 0 , 76 = 0 . 24  
E s t a d í s t i c o .     S e a   x 1 , x 2 , … , x n   u n a   m u e s t r a   a l e a t o r i a   d e   l a   v . a .   X   c o n   d i s t r i b u c c i ó n   f x .   T o d a   f u n c i o n   c u n j u n t o   d e   l a   m .

Toda función conjunta de la m.a. x 1 , x 2 , … , x n se define como un estadístico, es decir. 𝜃 = f x 1 , x 2 , … , x n = f x n Toda poblacion X v.a. contiene resultados parametrales.  
Parametros. 𝜇 x = ∑ i = 1 N x i N ,   P x = ∑ i = 1 N A i N ; A i = 1 0 , R x = ∑ i = 1 N A i ∑ i = 1 N B i ,   T x = ∑ i = 1 N X i  
_Estimadores. Sea_ 𝜃 ^ = f ( x 1 , x 2 , … , x n ) _se denomina también estimador del parametro_ 𝜃 . 𝜖 = 𝜃 ^ − 𝜃 → 0 _Margen de error_

x - = 𝜇 x ^ = ∑ i = 1   n x i n ; P x ^ = ∑ i = 1 n A i n ; R x ^ = ∑ i = 1   n A i ∑ i = 1 n B i : T x ^ = N n ∑ i = 1 n x i
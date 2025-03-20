(M.A.S. o M.I.A.)
A partir de una población de tamaño $N$ finita se toma una muestra aleatoria m.a. de tamaño $n$ con $n<N$ sin reemplazo donde todas las unidades $u_{1},u_{2},\cdots,u_{N}$ tienen la misma probabilidad de ser parte de la muestra, la probabilidad es distinta de $0$ 

### Muestras Posibles
- Sin reemplazo ${}_{N}C_{n} = \frac{N!}{n!(N-n)!}$
- Con reemplazo ${}_{N+n-1}C_{n} = \frac{(N+n-1)!}{n!(N-1)!}$
Consideramos una sola muestra aleatoria que debe ser representativa de la población
### Probabilidades de selección de unidades muestrales
donde
$$
\begin{equation} \{u_{1}, u_{2}, \dots, u_{N}\} \quad \text{(Tamaño } N\text{)} \quad \longrightarrow \quad \{u_{1}, u_{2}, \dots, u_{n}\} \quad \text{(Tamaño } n\text{)} \end{equation}
$$
#### Prob. de que $u_{i} \quad \forall i=1,2,\cdots,n$ sea parte de la muestra
- Con reemplazo: $\sum_{i=1}^n\frac{1}{N}=\frac{n}{N}=f$ Fracción de muestreo
- Sin reemplazo: $\sum_{i=1}^{n}{\frac{1}{N-i+1}\cdot \frac{N-i+1}{N}}=\frac{n}{N}=f$

#### Variable Auxiliar $e_{i}$
$$
e_{i} = \begin{cases} 1, & u_{i} \in m \quad \text{con prob.} \ \pi_{i} = \frac{n}{N} = f \\ 0, & u_{i} \notin m \quad \text{con prob.} \ 1-\pi_{i} = 1-\frac{n}{N} \end{cases}
$$
#### Valor esperado de $e_{i}$
$$
E(e_{i})=\sum_{R_{e_{i}}}e_{i}P(e_{i})=0P(e_{i}=0)+1P(e_{i}=1)=\pi_{i}=\frac{n}{N}=f
$$

$$
E(e_{i}^2)=\sum_{R_{e_{i}}}e_{i}^2P(e_{i})=\pi_{i}=\frac{n}{N}=f
$$
#### Varianza de $e_{i}$
$$
V(e_{i})=E(e_{i}^2)-E(e_{i})^{2} = f-f^{2}=f(1-f)
$$
$$
\begin{array}
e_{i}e_{j}=\begin{cases}
1, & (u_{i},u_{j}) \in m \quad \text{con prob.} \pi_{ij}\\
0, & (u_{i},u_{j}) \notin m \quad \text{con prob.} 1-\pi_{ij}
\end{cases} \\
P(u_{i}\cap u_{j})=P(u_{i})P\left( \frac{u_{j}}{u_{i}} \right) \\
\pi_{ij}=\frac{n}{N}\left( \frac{{n-1}}{N-1} \right) \\
Cov(e_{i},e_{j})=E(e_{i}e_{j})-E(e_{i})-E(e_{j}) \\
E(e_{i},e_{j})=\sum_{R_{e_{i}e_{j}}}e_{i}e_{j}P(e_{i},e_{j})=0(0)P(e_{i}=0\wedge e_{j}=0) + 0(1)P(e_{i}=1 \wedge e_{j}=0) + 1(0)P(e_{i}=0 \wedge e_{j}=1) + 1(1)P(e_{i}=1 \wedge e_{j}=1)C= \\
P(e_{i}=1 \wedge e_{j}=1)=\pi_{ij}=\frac{n}{N}\left( \frac{{n-1}}{N-1} \right)
\end{array}
$$

donde 
- $\pi_{i}$ es la probabilidad simple
- $\pi_{ij}$ es la probabilidad conjunta
#### Propiedades
1. $\sum_{i=1}^{N}\pi_{i}=n \quad \because \sum_{i=1}^{N} \frac{n}{N}=\frac{nN}{N}=n$
2. $\sum_{i=1, j\neq i}^{N}\pi_{i}=n-\pi_{j}$
3. $\sum_{i=1,i\neq j}^{N} \pi_{ij}=(n-1)\pi_{j}$
	$\because j=k \rightarrow \sum_{i=1, i\neq j}^{N}\pi_{ij}=\sum_{i=1, i\neq j}^{N} \frac{n}{N}\left( \frac{n-1}{N-1} \right)=(N-1) \frac{n}{N} \frac{n-1}{N-1}=\frac{n(n-1)}{N}=(n-1)\pi_{j}$
4. $\sum_{i=1,i\neq j}^{N}(\pi_{ij}-\pi_{i}\pi_{j})=-\pi_{j}(1-\pi_{i})$

| Indicador  | Parametro                                               | Estimador [^1]                                                                                                                                       |
| ---------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Media      | $\mu_{x}=\frac{1}{N}\sum ^{N}_{i=1}x_{i}$               | $\hat{\mu_{x}}=\frac{1}{N}\sum_{i=1}^{n} \frac{x_{i}}{\pi_{i}}=\frac{1}{N}\sum ^{n}_{i=1} \frac{x_{1}}{\frac{n}{N}}=\frac{1}{n}\sum ^{n}_{i=1}x_{i}$ |
| Total      | $T_{x}=\sum_{i=1}^{N}x_{i}=N\mu_{x}$                    | $\hat{T_{x}}=\sum_{i=1}^{n} \frac{x_{i}}{\pi_{i}}=\frac{N}{n} \sum ^{n}_{i=1}x_{i}$                                                                  |
| Proporcion | $P_{x}=\frac{1}{N}\sum_{i=1}^{N} A_{i}$                 | $\hat{P_{x}}=\frac{1}{n}\sum_{i=1}^{n} A_{i}$ donde $A_{i} = \begin{cases}1, & A_{i}\in \text{clase} asd\\0, & A_{i}\notin \text{clase} \end{cases}$ |
| Razón      | $R_{x}=\frac{\sum_{i=1}^{N}A_{i}}{\sum_{i=1}^{N}B_{i}}$ | $R_{x}=\frac{\sum_{i=1}^{n}A_{i}}{\sum_{i=1}^{n}B_{i}}$                                                                                              |
[^1]: Mediante Muestreo Aleatorio Simple
Los estimadores $\hat{\mu_{x}}, \hat{T_{x}}, \hat{P_{x}}$ son insesgados
> Horvitz y Thompson
> $\hat{\theta}=\sum_{i=1}^{n}c_{i}x_{i} \wedge \theta = \sum_{i=1}^{N}x_{i}$
$$
\begin{array}
E\left( \sum_{i=1}^{n}c_{i}x_{i} \right)=\sum_{i=1}^{N}x_{i}\\
E\left( \sum_{i=1}^{N}c_{i}x_{i}e_{i} \right)=\sum_{i=1}^{N}c_{i}x_{i}E(e_{i}) = \sum_{i=1}^{N}x_{i}\\
\sum_{i=1}^{N}c_{i}x_{i}\pi_{i}= \sum_{i=1}^{N}x_{i}\\
c_{i}\pi_{i}=1 \implies c_{i}=\frac{1}{\pi_{i}}
\end{array}
$$

1. $E(\hat{\mu_{x}}) =\mu_{x}$
	$\hat{\mu_{x}}=\frac{1}{N}\sum_{i=1}^{n} \frac{x_{i}}{\pi_{i}}$
	
2. $E(\hat{T{x}}) =T{x}$
	$\hat{T{x}}=\sum_{i=1}^{n} \frac{x_{i}}{\pi_{i}}$

3. $E(\hat{P{x}}) =P{x}$
	$\hat{P{x}}=\sum_{i=1}^{n} A_{i}$


Dada una encuestas por muestreo a una poblacion de 200 hogares, se les pregunta si tienen o no servicio de internet a domicilio las respuestas son
$A_i = 0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,1 \quad \text{donde 0 = No y 1 = Si} \quad n = 23 \quad N=200$
Estimar la proporción de hogares que tienen servicio de Internet a domicilio y varianza de la proporción
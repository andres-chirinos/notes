¡Vamos a demostrar que el estimador de la varianza poblacional $\sigma_X^2$ es insesgado! Vamos a llevar la demostración paso a paso.

### Recordemos primero la definición del estimador de la varianza:

Si tenemos una muestra aleatoria de $n$ observaciones $X_1, X_2, \dots, X_n$, la varianza poblacional verdadera $\sigma_X^2$ se define como:

$$
\sigma_X^2 = \mathbb{E}[(X - \mu)^2],
$$
donde $\mu = \mathbb{E}[X]$ es la media poblacional.

El **estimador de la varianza muestral** $S^2$ (basado en los datos) se define como:

$$
S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})^2,
$$
donde $\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$ es la media muestral.

### Objetivo:
Queremos demostrar que $\mathbb{E}[S^2] = \sigma_X^2$, es decir, que $S^2$ es un estimador **insesgado** de la varianza poblacional $\sigma_X^2$.

### Paso 1: Expansión de $S^2$

Comenzamos expandiendo la expresión para $S^2$. Sabemos que:

$$
S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})^2
$$

Podemos reescribir esta expresión de la siguiente manera usando álgebra de sumatorias:

$$
S^2 = \frac{1}{n-1} \left( \sum_{i=1}^{n} X_i^2 - n \bar{X}^2 \right)
$$

Este paso es crucial, ya que lo usaremos más adelante en la demostración.

### Paso 2: Calcular la esperanza de $S^2$

Queremos calcular $\mathbb{E}[S^2]$. Empezamos tomando la esperanza de ambos lados de la ecuación anterior:

$$
\mathbb{E}[S^2] = \mathbb{E}\left[ \frac{1}{n-1} \left( \sum_{i=1}^{n} X_i^2 - n \bar{X}^2 \right) \right]
$$

Como $\frac{1}{n-1}$ es una constante, podemos sacarla fuera de la expectativa:

$$
\mathbb{E}[S^2] = \frac{1}{n-1} \left( \mathbb{E}\left[ \sum_{i=1}^{n} X_i^2 \right] - n \mathbb{E}[\bar{X}^2] \right)
$$

### Paso 3: Calcular $\mathbb{E}\left[ \sum_{i=1}^{n} X_i^2 \right]$

Sabemos que $\mathbb{E}[X_i^2] = \text{Var}(X_i) + (\mathbb{E}[X_i])^2 = \sigma_X^2 + \mu^2$. Entonces:

$$
\mathbb{E}\left[ \sum_{i=1}^{n} X_i^2 \right] = n(\sigma_X^2 + \mu^2)
$$

### Paso 4: Calcular $\mathbb{E}[\bar{X}^2]$

Recordemos que $\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$, por lo que necesitamos calcular $\mathbb{E}[\bar{X}^2]$:

$$
\mathbb{E}[\bar{X}^2] = \mathbb{E}\left[\left(\frac{1}{n} \sum_{i=1}^{n} X_i\right)^2\right]
$$

Usando la propiedad de la varianza y linealidad de la expectativa, tenemos:

$$
\mathbb{E}[\bar{X}^2] = \frac{1}{n^2} \mathbb{E}\left[\sum_{i=1}^{n} X_i^2 + 2 \sum_{i \neq j} X_i X_j\right]
$$

Sabemos que $\mathbb{E}[X_i X_j] = \mu^2$ para $i \neq j$, entonces podemos descomponer esta expectativa como:

$$
\mathbb{E}[\bar{X}^2] = \frac{1}{n^2} \left(n \mathbb{E}[X_i^2] + n(n-1) \mu^2 \right)
$$

Sustituyendo $\mathbb{E}[X_i^2] = \sigma_X^2 + \mu^2$:

$$
\mathbb{E}[\bar{X}^2] = \frac{1}{n^2} \left(n(\sigma_X^2 + \mu^2) + n(n-1) \mu^2\right)
$$

Simplificando:

$$
\mathbb{E}[\bar{X}^2] = \frac{1}{n} \sigma_X^2 + \mu^2
$$

### Paso 5: Concluir que $\mathbb{E}[S^2] = \sigma_X^2$

Volviendo a nuestra expresión original para $\mathbb{E}[S^2]$, sustituimos los resultados de los pasos anteriores:

$$
\mathbb{E}[S^2] = \frac{1}{n-1} \left( n(\sigma_X^2 + \mu^2) - n\left(\frac{1}{n} \sigma_X^2 + \mu^2\right) \right)
$$

Simplificamos esta expresión:

$$
\mathbb{E}[S^2] = \frac{1}{n-1} \left( n\sigma_X^2 + n\mu^2 - \sigma_X^2 - n\mu^2 \right)
$$

$$
\mathbb{E}[S^2] = \frac{1}{n-1} \left( (n-1)\sigma_X^2 \right)
$$

Finalmente:

$$
\mathbb{E}[S^2] = \sigma_X^2
$$

### Conclusión:

Hemos demostrado que $\mathbb{E}[S^2] = \sigma_X^2$, lo que significa que el estimador $S^2$ es **insesgado**.


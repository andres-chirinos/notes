## Método de Máxima Verosimilitud
> Verosímil sinónimo de probable
Sea $X$ una v.a. poblacional con fdp $f(x,\theta)$. Se toma una m.a. de $X \{x_{1},x_{2},\dots,x_{n}\}$, luego la función de verosimilitud se define como $L=f(x_{1},x_{2},\dots,x_{n};\theta)= f(x_{1};\theta)f(x_{2};\theta)\dots f(x_{n};\theta)=\prod_{i=1}^{n}f(x_{i};\theta)$
La función máximo verosímil, logaritmo, derivada respecto a $\theta$, e igualado a cero.
$$
\begin{align}
\ln L=\ln \prod_{i=1}^{n}f(x_{i};\theta)=\prod_{i=1}^{n}\ln f(x_{i};\theta)   \\
\frac{\partial \ln L}{\partial \theta}=0 \implies \sum_{i=1}^{n} \frac{\partial \ln f(x_{i},\theta)}{\partial \theta}=0 \to \hat{\theta}=? 
\end{align}
$$
## Método de momentos
Sea $X$ una v.a. poblacional con fdp $f(x;\theta)$. Se toma una m.a. de tamaño $n$ de $X$, luego se define los "momentos de orden $r$" respecto al origen de tipo poblacional y muestral.
### Población: 
$$
M_{r}=E(X^{r})\begin{cases}
\sum_{R_{x}}x^{r}p(x) \quad\text{Si X es discreta} \\
\int_{R_{x}}x^{r}f(x)dx\quad \text{Si X es continua}
\end{cases}
$$
### Muestra
$$
m_{r}=\frac{1}{n}\sum_{i=1}^{n}X_{i}^{r};\quad r=1,2,\dots,k 
$$
> Nota. Se generan k momentos, según el Nro de parámetros a estimar
## Método de Estimación
Para lograr la estimación de los $k$-Parámetros se hace:
$$
\begin{align}
M_{1}=m_{1}\implies\hat{\theta}_{1} \\
M_{2}=m_{2}=_>\hat{\theta}_{2} \\
\dots\\
M_{k}=m_{k}\implies\hat{\theta}_{k}
\end{align}
$$
### Ejemplo 
Sea $X\to N(\mu_{x},\sigma_{x}^{2})$ determinar los estimadores de [[Métodos de Estimación#Método de Máxima Verosimilitud]] y [[Métodos de Estimación#Método de momentos]] para $\mu_{x}, \sigma_{x}^{2}$.
- De Máxima Verosimilitud
$$
L(\mu_{x},\sigma^{2}_{x})=\prod_{i=1}^{n}\frac{1}{\sqrt{ 2\pi }\sigma_{x}}e^{-1/2\left( \frac{x_{i}-\mu_{x}}{\sigma_{x}} \right)^{2}}=\frac{1}{(2\pi \sigma_{x}^{2})^{n/2}}e^{-1/2\sum_{i=1}^{n}\left( \frac{x_{i}-\mu_{x}}{\sigma_{x}} \right)^{2} }
$$
Log Ned.
$$
\ln L(\mu_{x},\sigma_{x}^{2})=-\frac{n}{2}\ln{2\pi}-\frac{n}{2}\ln \sigma^{2}_{x}-\frac{1}{2}\sum_{i=1}^{n}\left( \frac{x_{i}-\mu_{x}}{\sigma_{x}} \right)^{2} 
$$
Derivando
$$
\begin{align}
\frac{\partial\ln L(\mu_{x},\sigma^{2}_{x})}{\partial\mu_{x}}=-\frac{1}{\sigma^{2}_{x}}\sum_{i=1}^{n}(x_{i}-\mu_{x})(-1)=0 \tag{1}\\
\frac{\partial\ln L(\mu_{x},\sigma^{2}_{x})}{\partial \sigma^{2}_{x}}=\frac{n}{2\sigma^{2}_{x}}-\frac{1}{2\sigma^{4}_{x}}\sum_{i=1}^{n}(x_{i}-\mu_{x})^{2}=0\tag{2} \\
\text{evaluamos (1) y (2)} \\
(1) \implies\sum_{i=1}^{n}(X_{i}-\mu_{x})=0\implies\sum_{i=1}^{n}X_{i}-\hat{\mu_{x}}=0\implies \frac{1}{n} \sum_{i=1}^{n}X_{i}=\hat{\mu_{x}}\implies\bar{x}=\hat{\mu_{x}} \\
(2)\implies -\frac{n\sigma^{2}_{x}+\sum_{i=1}^{n}(x_{i}-\mu_{x})^{2} }{2\sigma^{4}}=0\implies-n\sigma^{2}_{x}+\sum_{i=1}^{n}(x_{i}-\mu_{x})^{2}=0 \\
\implies-\sigma^{2}_{x}+ \frac{1}{n} \sum_{i=1}^{n}(x_{i}-\bar{x})^{2}=0\implies \sigma^{2}_{x}=\frac{1}{n} \sum_{i=1}^{n}(x_{i}-\bar{x})^{2}\begin{cases}
S^{2}_{x} \\
\frac{(n-1)S^{2}_{x}}{n}; S^{2}_{x}=\frac{\sum_{i=1}^{n}(x_{i}-\bar{x})^{2} }{n-1}
\end{cases}
\end{align}
$$
1er Examen 30 de septiembre
- De Momentos
### Teorema Central del Limite
$\bar{x}=\frac{y}{n}$ donde $y=x_1+x_2+...+x_n=\sum_{i=1}^{n}{X_i}$
Sea $X$ una variable aleatoria poblacional con función de distribución $f(x)$.
Si $n\geq30$ la v.a. $\bar{x}$ (media de muestreo) sigue aproximadamente normal con media $\mu_{\bar{x}}$ y varianza $\sigma_{\bar{x}}^2$. En resumen que $x \rightarrow N(\mu_x,\sigma_x^2)$ con:
$$
\begin{align}
\mu_{\bar{x}}=\mu_x \\
\text{y con }\begin{cases}
\sigma_{\bar{x}}^2=\frac{\sigma_x^2}{n} \text{Si N es desconocida o infinita o el muestreo es con reemplazo} \\
\sigma_{\bar{x}}^2=\frac{\sigma_x^2}{n}(\frac{N-n}{N-1}) \text{Si N es finita o el muestreo es con reemplazo} \\
\end{cases}
\end{align}
$$
**Nota**. Si $x$ tiene $f(x)$ normal con media $\mu_x$ y varianza $\sigma_x^2$, en resumen $x \rightarrow N(\mu_x,\sigma_x^2)$ sin importar en tamaño de $n$.
La media muestral $\bar{x}=\frac{1}{n}\sum_{i=1}^{n}{X_i}$
Luego $z=\frac{\bar{x}-\mu_{\bar{x}}}{\sigma_{\bar{x}}}\rightarrow N(0,1)$
### La distribución muestral de $\bar{x}$
$P(\bar{x}<c)=P(z<\frac{c-\mu_x}{\sigma_{\bar{x}}})=\phi(\frac{c-\mu_x}{\sigma_{\bar{x}}})=\phi(c')$ con $c'=\frac{c-\mu_x}{\sigma_{\bar{x}}}$
$$
\begin{align}
P(\bar{x}>a)=1-P(\bar{x}\leq a) \\
P(b_1<\bar{x}<b_2)=P(\bar{x}<b_2)-P(\bar{x}<b_1>)\\
P(\bar{x}>-a) = 1-P(\bar{x}\leq -a) = 1-[1-P(\bar{x}\leq a)]=1-1+P(\bar{x}\leq a)=P(\bar{x}\leq a)
\end{align}
$$
##### _Ejercicio 1_. Sea una función de densidad (v.a.c.) de una población $X$. Sea $x_1,x_2,...,x_{36}$ una m.a. de $X$
_Nota. X es son independientes e idénticamente distribuidas_
$$
f(x) = \left\{
\begin{array}{ll}
    \frac{3}{2}x^2 & \text{si }-1<x<1 \\
    0 & \text{e.o.c.}
\end{array}
\right.
n=36
$$
1. Hallar $P(0.01<\bar{x}<0.15)$
$$
   \begin{align}
   P(0.01<\bar{x}<0.15) \\
   P(\bar{x}<0.15)-P(\bar{x}<0.01)
   \end{align}
   $$
Cumple que $f(x)$ es funcion de probabilidad (f.d.p.)
1. $f(x)\leq 0, f_{R_x}$
2. $\int_{R_x}{f(x)dx}=1$
$$

\begin{align}

\mu_{\bar{x}}=E(\bar{x})=\int_{R_x}{f(x)dx} \\

\text{evaluando} \int_{-1}^{1}{\frac{3}{2}x^3dx}=\int_{-1}^{1} \frac{3}{2}x^3 , dx = \left[ \frac{1}{2}x^4 \right]_{-1}^{1} \\

= \frac{1}{2}(1)^4 - \frac{1}{2}(-1)^4 = 0  \\

\sigma^2_x=E(x^2)-E^2(x)=E(x^2)-\sigma^2\\

E(x^2)=\int_{-1}^{1}{\frac{3}{2}x^4dx=\frac{3}{5}}\\

\sigma^{2}_{\bar{x}}=\frac{\sigma^2_{x}}{n}=\frac{1}{60}\\

\bar{x}\rightarrow N(0,\frac{1}{60})\rightarrow z\rightarrow N(0,1)\\

z=\frac{\bar{x}-\mu_x}{\sigma_{\bar{x}}}\Rightarrow P(0.05<\bar{x}<0.15) \\

=P(0.05<\bar{x}<0.15) = P(z<\frac{0.15-0}{\sqrt{\frac{1}{60}}})-P(z<\frac{0.05-0}{\sqrt{\frac{1}{60}}})\\

=\phi(1.16)-\phi(0.39)=0.877-0.658=0.229

\end{align}

$$

  

##### _Ejercicio 2._ Sea $X$ una v.a. discreta poblacional de parametros $N=125$ con f.d.p. $f(x)=\frac{2}{3^x} \text{Para } x=0,1,2,...$ Se toma una muestra de parametros $n=30$. Halla la probabilidad de que la media muestral este entre 1.45 y 1.55

  

Serie de Mc.laren $\sum_{i=0}^{\infty}{r^{i}}=\frac{1}{1-r}; \text{si } |r|<1$

  

Verificamos que sea funcion de probabilidad

$$

\sum_{x-1=0}^{\infty}{(\frac{1}{3})^{x-1}}\\

r = \frac{1}{3} ; i=x-1\\

\sum_{i=0}^{\infty}{(r)^{i}} \wedge |r|<1 \Rightarrow \frac{1}{1-r}\\

\frac{1}{1-\frac{1}{3}} = 1

\\

\therefore f(x) \text{ es funcion de probabilidad}

$$

  

Encontramos $\mu_{\bar{x}}$

$$

\begin{align}

\mu_{\bar{x}}=E(\bar{x})=\sum_{R_x}{xf(x)}\\

=\frac{2}{3}\sum_{x=0}^{\infty}{x(\frac{1}{3})^{x-1}}\\

\frac{2}{3} \frac{\sigma \sum_{x-1=0}^{\infty}{x\cdot (\frac{1}{3})^{x-1}}}{\sigma_x}=\frac{2}{3} \frac{\sigma}{\sigma_r}(\frac{1}{1-r})\\

\frac{2}{3}(\frac{-1(-1)}{(1-r)^2})=\frac{2}{3}(\frac{1}{(1-r)^2})=\frac{2}{3} [\frac{1}{(1-\frac{1}{3})^2}] = \frac{3}{2} =1.5

\end{align}

$$

Luego encontramos $\sigma_{\bar{x}}^2$

$$

\begin{align}

\sigma_{\bar{x}}^2=E(x^2)-E^2(x)\\

E(x^2)=\sum_{x=0}^{\infty}{\frac{2}{3^{(x)^2}} x^2} \\

\sum_{x=0}^{\infty}{\frac{2}{3^x}[x(x-1)+x]} \\

\frac{2}{3^2}\sum_{x-2=0}^{\infty}{x(x-1)(\frac{1}{3})^{x-2}} + \frac{2}{3^2}\sum_{x-2=0}^{\infty}{x(\frac{1}{3})^{x-1}}\\

E(x^2)=\frac{2}{3} \frac{\sigma^2}{\sigma^2r} (\frac{1}{1-r})=\frac{2}{3} \frac{\sigma}{\sigma r}[\frac{1}{(1-r)^2}]\\

\frac{4}{9}(\frac{1}{(1-\frac{1}{3})^3})=\frac{3}{2}\\

\sigma^2_{\bar{x}}=3 - 1.5^2 = 0.75\\

\sigma_{\bar{x}}^2=\frac{\sigma_x^2}{n}(\frac{N-n}{N-1})=\frac{0.75}{30}(\frac{125-30}{125-1})=0.019

\end{align}

$$
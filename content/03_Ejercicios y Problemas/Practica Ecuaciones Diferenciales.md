> Del capitulo 1 deben realizar todos los ejercicios. De cada pregunta realizar los incisos de posición par
# Práctica 1. Generalidades
1. Encuentre el orden de cada una de las siguientes ecuaciones 
	$b)\quad y′′ + (y′)^3 − y′′′ = 4x^7$
		La ED es de 3 orden dado que mayor derivada es $y'''$ 
	$d) \quad y′′′y − (y′)^5 = 22$
		La ED es de 3 orden dado que mayor derivada es $y'''$ 
2. Verifique que la función dada es una solución de la ecuación diferencial dada sobre algún intervalo, para cualquier valor de las constantes arbitrarias que aparecen en la función.
	$b) \quad y = \frac{x^2}{3} + \frac{c}{x} ; xy′ + y = x^2$	
		$$
		\begin{align}
		y' = \frac{d}{dx} \left( \frac{x^2}{3} \right) + \frac{d}{dx} \left( \frac{c}{x} \right)\\
		y' = \frac{2x}{3} - \frac{c}{x^2} \tag{1}\\
        \text{Reemplazando (1) en la ecuación solución} \\
        x \left( \frac{2x}{3} - \frac{c}{x^2} \right) + \left( \frac{x^2}{3} + \frac{c}{x} \right) = x^2 \\
        x \left( \frac{2x}{3} \right) - x \left( \frac{c}{x^2} \right) + \frac{x^2}{3} + \frac{c}{x} = x^2 \\
		\frac{2x^2}{3} - \frac{c}{x} + \frac{x^2}{3} + \frac{c}{x} = x^2 \\
		\frac{2x^2}{3} + \frac{x^2}{3} = x^2 \\
		\frac{3x^2}{3} = x^2 \\
		x^2 = x^2 \\
		\therefore \text{La ecuación es solución}
        \end{align}
		$$
	$d) \quad y = (1 + ce^{−x^2/2})(1 − ce^{−x^2/2})^{−1}; 2y′ + x(y^2 − 1) = 0$
	$$
	\begin{align}
y'=\frac{d}{dx}\left( \frac{1+ce^{-x^{2}/2}}{1-ce^{-x^{2}/2}} \right) \\
y'=\frac{(1-ce^{-x^{2}/2})(1+ce^{-x^{2}/2})'-(1+ce^{-x^{2}/2})(1-ce^{-x^{2}/2})'}{(1-ce^{-x^{2}/2})^{2}} \\
y'=\frac{(1-ce^{-x^{2}/2})(cxe^{-x^{2}/2})-(1+ce^{-x^{2}/2})(-cxe^{-x^{2}/2})}{(1-ce^{-x^{2}/2})^{2}} \\
y'=\frac{()}{}
\end{align}
	$$
	$f) \quad e^{xy} + y = x − 1, y′ = \frac{e^{−xy} − y}{e^{−xy} + x}$
	$$
	\begin{align}
y=x-1-e^{xy} \tag{1} \\
y'=1-0-ye^{xy} \tag{2} \\
\text{Reemplazar (1) y (2) en la ecuación} \\
1-ye^{xy}=\frac{}{}
\end{align}
	$$
	$h)\text{ y }j) \quad y = e^{−x^{2}} \int_{0}^{x} e^{t^{2}}dt + Ce^{−x^{2}},\quad y′ + 2xy = 1$
3. Encuentre todas las soluciones de la ecuación dada
	$b) \quad y'=x\ln x$
	$$
\begin{align}
\frac{dy}{dx}=x\ln x \\
dy=x\ln xdx \\
\int dy=\int x\ln xdx \\
\text{Nota. }\int udv=uv-\int vdu; \quad u=\ln x \quad du=\frac{1}{x}\quad dv=xdx \quad v=\frac{x^{2}}{2}\\
y(x)=\frac{x^{2}}{2}\ln x-\int \frac{x^{2}}{2} \frac{1}{x}dx \\
y(x)=\frac{x^{2}}{2}\ln x-\frac{1}{2}\int xdx \\
y(x)=\frac{x^{2}}{2}\ln x-\frac{1}{2} \frac{x^{2}}{2}+C \\
y(x)=\frac{x^{2}}{2}\ln x- \frac{x^{2}}{4}+C \quad\blacksquare
\end{align}
$$
	$d) \quad y''=x\cos x$
	$$
	\begin{align}
\frac{d^{2}y}{dx^{2}}=x\cos x \\
\int\frac{d^{2}y}{dx^{2}}dx=\int x\cos xdx \\
\frac{dy}{dx}=x\sin x-\int\sin xdx \\
\frac{dy}{dx}=x\sin x+\cos x+C \\
\int dy=\int(x\sin x+\cos x+C)dx \\
y=\int x\sin xdx+\int \cos xdx+\int Cdx \\
y=-x\cos x+\sin x+\sin x+C_{1}x+C_{2} \\
y(x)=-x\cos x+2\sin x+C_{1}x+C_{2}
\end{align}
$$
	$f) \quad y''' = -\cos x$
	$$
\begin{align}
\frac{d^{3}y}{dx^{3}}=-\cos x \\
\int\frac{d^{3}y}{dx^{3}}dx=-\cos xdx \\
\frac{d^{2}y}{dx^{2}}=-\sin x+C_{1} \\
\int \frac{d^{2}y}{dx^{2}}dx=-\int \sin xdx+\int C_{1}dx \\
\frac{dy}{dx}=\cos x+C_{2}+xC_{1} \\
\int \frac{dy}{dx}dx=\int \cos xdx+\int C_{2}dx+\int xC_{1}dx \\
y=\sin x+C_{3}+xC_{2}+\frac{x^{2}}{2}C_{1} \\
y(x)=\sin x+\frac{x^{2}}{2}C_{1}+xC_{2}+C_{3} \quad \blacksquare
\end{align}
$$
	$h) \quad y'''= 7e^{4x}$
	$$
\begin{align}
\frac{d^{3}y}{dx^{3}}=7e^{4x} \\
\int \frac{d^{3}y}{dx^{3}}dx=7\int e^{4x}dx \\
\frac{d^{2}y}{dx^{2}}=\frac{7}{4}e^{4x}+C_{1} \\
\int\frac{d^{2}y}{dx^{2}}dx=\frac{7}{4}\int e^{4x}dx+\int C_{1}dx \\
\frac{dy}{dx}=\frac{7}{16}e^{4x}+xC_{1}+C_{2} \\
\int \frac{dy}{dx}dx=\frac{7}{16}\int e^{4x}dx+C_{1}\int xdx+C_{2}\int dx \\
y(x)=\frac{7}{64}e^{4x}+\frac{x^{2}}{2}C_{1}+xC_{2}+C_{3} \quad \blacksquare
\end{align}
$$
1. Teorema de Picard. Si $f (x, y)$ y $\frac{\partial f}{\partial y}$ son funciones continuas en una región ℜ, entonces, por cada punto $(x_{0}, y_{0})$ en el interior de ℜ, pasará una curva integral única de la ecuación. $\frac{dy}{dx}=f(x,y)$ En los problemas que siguen determine si el teorema de existencia y unicidad (Picard) implica que el problema de valor inicial dado tiene solución única.
	$b) \quad y′ − xy = sin^{2} x, \quad y(π) = 5$
	$$
\begin{align}
y'+P(x)y=Q(x) \quad \mu(x)=e^{\int P(x)dx}
\end{align}
$$
	$d)\quad y′ = \frac{x}{y},\quad y(1) = 0$
	$$
\begin{align}
\frac{dy}{dx}=\frac{x}{y} \\
ydy=xdx \\
\int ydy=\int xdx \\
\frac{y^{2}}{2}=\frac{x^{2}}{2}+C_{1} \\
y^{2}=x^{2}+2C_{1} \\
\text{aplicamos la condicion inicial} \\
0=1+2C_{1} \\
2C_{1}=-1 \\
C_{1}=-\frac{1}{2} \\
\text{Sustituimos en la ecuacion general} \\
y^{2}=x^{2}-1 \implies y=\pm\sqrt{ x^{2}-1 } \quad \blacksquare
\end{align}
$$
	$f)\quad yy'-4x=0; \quad y(2)=-\pi$
	$$
\begin{align}
y\frac{dy}{dx}=4x \\
ydy=4xdx \\
\int ydy=\int4xdx \\
\frac{y^{2}}{2}=2x^{2}+C_{1} \\
y^{2}=4x^{2}+2C_{1} \\
\text{aplicamos la condicion inicial} \\
(-\pi)^{2}=4(2)^{2}+2C_{1} \\
(-\pi)^{2}-16=2C_{1} \\
C_{1}=\frac{(-\pi)^{2}-16}{2} \\
\text{aplicamos en la ecuacion general} \\
y^{2}=4x^{2}+(-\pi)^{2}-16 \\
y=\pm \sqrt{4x^{2}+\pi^{2}-16  } \quad\blacksquare
\end{align}
$$
# Practica 2. Ecuaciones Diferenciales de Primer orden
### Ecuaciones de variable separable
A) En los ejercicios que siguen encuentre la solución general
$2.\quad \tan \sin ^{2}ydx+\cos ^{2}x\cot ydy=0$
$4.\quad xy'-y=y^{2}$
$6.\quad xy'+y\ln x=0$
$8.\quad xy'+3y=0$
$$
\begin{align}
\frac{dy}{dx}x+3y=0 \\
\frac{dy}{dx}+\frac{3}{x}y=0 \\
\text{factor de integración} \\
\mu(x)=e^{\int \frac{3}{x}dx}=e^{\ln(x^{3})}=x^{3} \\
\text{aplicamos en la ecuacion} \\
x^{3}\frac{dy}{dx}+3x^{2}y=0
\end{align}
$$
$10.\quad x^{2}y'+y=0itemxyy'$
$12.\quad y'\tan x=y$
$$
\begin{align}
\frac{dy}{dx}\tan x=y \\
\int\frac{1}{y}dy=\int\frac{1}{\tan x}dx \\
\int \frac{1}{y}dy=\int \cot xdx \\
\ln y=\ln sin(x) +C_{1} \\
y=\sin x +e^{C_{1}} \quad \blacksquare
\end{align}
$$
### Ecuaciones Homogéneas
### Ecuaciones Exactas
### Factores de Integración
### Ecuaciones Lineales
### Ecuación Bernoulli
### Ecuación de Riccati

### Ecuaciones de Lagrange y Clairaut
### Reducción de orden

### Trayectorias Ortogonales

### Problemas Geométricos-Persecución-Otros
#### Varios
#### Problemas. Ecuaciones de Primer Orden
#### Problemas de persecución

# Práctica 3. Ecuaciones Diferenciales de Segundo Orden
asd
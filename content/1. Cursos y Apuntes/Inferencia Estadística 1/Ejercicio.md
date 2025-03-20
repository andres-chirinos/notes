
### Ejercicio 6
Sea $X_{1},X_{2},\dots,X_{n}$ una m.a. de tamaño $n$ de una población $X$, con media $\mu_{X}$ y varianza $\sigma^{2}_{X}$. Demostrar que $\bar{X}$ es un estimador consistente de $\sigma_{X}$.
- Desigualdad de Tchevyshev $P(|\bar{X}_{n}-\mu_{X}|<k\sigma_{\bar{x}})\leq\frac{1}{k^{2}}$
$$
\begin{align}
\lim_{ n \to \infty } P[\theta_{n}-\theta<\varepsilon]=1 \tag{1} \\
1 - P(|\bar{X_{n}}-\mu_{X}|<k\sigma_{\bar{X}})\leq\frac{1}{k^{2}} \\
P(|\bar{X_{n}}-\mu_{X}|<k\sigma_{\bar{X}})>1-\frac{1}{k^{2}} \\
\text{Con } \varepsilon=k\sigma_{\bar{X}}\implies k=\frac{\varepsilon}{\sigma_{\bar{X}}} \quad\text{Puesto que } \sigma_{\bar{X}}=\frac{\sigma_{X}}{\sqrt{ n }} \text{ Si } n\to \infty \\
k=\frac{\varepsilon}{\frac{\sigma_{X}}{\sqrt{ n }}}=\frac{\varepsilon \sqrt{ n }}{\sigma_{x}}\implies P(|\bar{X}-\mu_{x}|<\varepsilon)>1-\frac{1}{\frac{\varepsilon^{2}n}{\sigma_{X}}} \\
P(|\bar{X_{n}}-\mu_{X}|<\varepsilon)>1-\frac{\sigma_{x}}{n\varepsilon^{2}} \quad \text{Tomamos el lim} \\
\lim_{ n \to \infty } P(|\bar{X_{n}}-\mu_{X}|<\varepsilon)>\lim_{ n \to \infty }(1-\frac{\sigma_{x}}{n\varepsilon^{2}}) \quad \text{Aplicando (1)}\\
=1 \implies  \bar{X}\text{ es estimador consistente.}
\end{align}
$$
De otra manera
$$
\begin{align}
\lim_{ n \to \infty } E(\hat{\theta})=\theta \tag{1}\\
\lim_{ n \to \infty } V(\hat{\theta})=0 \tag{2}\\
\hat{\theta}=\bar{X}=\frac{1}{n} \sum_{i=1}^{n}{X_{i}}\implies_{\text{Aplicando 1 }} E(\bar{X})=E\left( \frac{1}{n} \sum_{i=1}^{n}{X_{i}} \right)=\mu_{X} \\
\lim_{ n \to \infty }{E(\bar{X})}=\lim_{ n \to \infty }{\mu_{X}}=\mu_{X} \\
\text{Como: }V(\bar{X})=V\left( \frac{1}{n} \sum_{i=1}^{n}{X_{i}} \right)=\frac{\sigma^{2}_{x}}{n} \\
\lim_{ n \to \infty } {V(\bar{X})}=\lim_{ n \to \infty }{\frac{\sigma^{2}_{x}}{n}}=0 \\
\therefore \text{Por tanto es un estimador consistente} 
\end{align}
$$

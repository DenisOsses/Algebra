

# 
  ### 
- Definir y estudiar las propiedades de las funciones trigonométricas.

## Circunferencia goniométrica
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase13.py Clase13` y mueva el archivo resultante a `_static/videos/Clase13.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase13.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  

Consideremos una circunferencia de radio 1, con centro en $(0,0)$ cuyo punto inicial es el $(1,0)$ 

    ```{image} ../Clases/goniometrica.png
:align: center
:width: 70%
```

## Funciones trigonométricas
# (Untitled Slide)
  ## 
  ### 
  

Ir desde $(1,0)$ al punto $P$ es girar en sentido positivo.  El ángulo del sector circular formado por $(1,0)$, el origen y $P$ es $x$.  El punto $P$ tiene coordenadas $P(a_x,b_x)$ (dependen de $x$). 

```{admonition} Definición
:class: tip
- La función **seno** de $x$ se define como: $f(x)=\sen(x)=b_x$.
- La función **coseno** de $x$ se define como: $f(x)=\cos(x)=a_x$.
- La función **tangente** de $x$ se define como: $f(x)=\tan(x)=\dfrac{b_x}{a_x}.$

```

```{admonition} Nota
:class: tip

Mediremos el ángulo $x$ en **radianes**.  La equivalencia entre radianes y grados (sexagesimales) está dada por la idea de que un giro completo a la circunferencia de radio 1 equivale a rotar en $360^\circ$ y la distancia recorrida en dicho giro es $2\pi$.  Así, tenemos $$2\pi~(\textrm{rad})=360^\circ~~\Leftrightarrow~~\pi~ (\textrm{rad})=180^\circ.$$
```

```{admonition} Ejemplo 1
:class: note
Determine en radianes el ángulo $330^\circ$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

# (Untitled Slide)
  ## 
  ### 
  

  
  \renewcommand\arraystretch{1.5}
      \begin{tabular}{|c||c|c|c|c|c|c|}
      \hline
          $x$ (en radianes) & $\sen(x)$ & $\cos(x)$ & $\tan(x)$ & $\csc(x)$ & $\sec(x)$ & $\cot(x)$ \\
          \hline 
          $0$ & $0$ & $1$ & $0$ & no existe & $1$ & no existe \\
          \hline 
          $\myfrac{\pi}{6}$ & $\myfrac{1}{2}$ & $\myfrac{\sqrt{3}}{2}$ & $\myfrac{\sqrt{3}}{3}$ & $2$ & $\myfrac{2\sqrt{3}}{3}$ & $\sqrt{3}$ \\
          \hline 
          $\myfrac{\pi}{4}$ & $\myfrac{\sqrt{2}}{2}$ & $\myfrac{\sqrt{2}}{2}$ & $1$ & $\sqrt{2}$ & $\sqrt{2}$ & $1$ \\
          \hline 
          $\myfrac{\pi}{3}$ & $\myfrac{\sqrt{3}}{2}$ & $\myfrac{1}{2}$ & $\sqrt{3}$ & $\myfrac{2\sqrt{3}}{3}$ & $2$ & $\myfrac{\sqrt{3}}{3}$ \\
          \hline
          $\myfrac{\pi}{2}$ & $1$ & $0$ & no existe & $1$ & no existe & $0$\\
          \hline
      \end{tabular}
  
  
```{admonition} Ejemplo 2
:class: note
Determine el valor de $\cos\left(\dfrac{2\pi}{3}\right)$, $\cos\left(\pi\right)$, $\sen\left(\dfrac{5\pi}{4}\right)$, $\cos\left(-\dfrac{\pi}{3}\right)$, 
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

## Estudio de las funciones trigonométricas
# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Función seno
:class: tip

Como $x$ puede tomar cualquier valor entonces $$dom(\sen(x))=\mathbb{R}.$$  La segunda coordenada $b_x$ de $P$ solamente puede tomar valores entre $-1$ y $1$, ya que el punto $P$ está sobre la circunferencia. Luego $$rec(\sen(x))=[-1,1].$$ 
Además, el punto $P(a_x,b_x)$ permanece invariante si hacemos rotaciones en ángulos de valor $\pm2\pi$; es decir  $$P(a_x,b_x)=P(a_{x\pm 2\pi},b_{x\pm 2\pi}).$$
```

\begin{block}

A partir de esto, decimos que $\sen(x)$ es **periódica** (con periodo $2\pi$); es decir $$\sen(x\pm 2\pi)=\sen(x).$$ Con la periodicidad basta estudiar $\sen(x)$ para $x\in[0,2\pi]$. 

Otra propiedad importante es que $\sen(x)$ es **impar**, es decir $\sen(-x)=-b_x=-\sen(x)$. Con esto, basta con estudiar $\sen(x)$ para $x\in[0,\pi]$

Para construir su gráfica, vemos la siguiente aplicación de \href{https://www.geogebra.org/m/tu3PFgUf}{Geogebra}
```

# (Untitled Slide)
  ## 
  ### 
  

\begin{block}

Su gráfica es 

    ```{image} ../Clases/seno.png
:align: center
:width: 70%
```

```

# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Función coseno
:class: tip

Como $x$ puede tomar cualquier valor entonces $$dom(\cos(x))=\mathbb{R}.$$  La primera coordenada $a_x$ de $P$ solamente puede tomar valores entre $-1$ y $1$, ya que el punto $P$ está sobre la circunferencia. Luego $$rec(\cos(x))=[-1,1].$$ 
Además, el punto $P(a_x,b_x)$ permanece invariante si hacemos rotaciones en ángulos de valor $\pm2\pi$; es decir  $$P(a_x,b_x)=P(a_{x\pm 2\pi},b_{x\pm 2\pi}).$$
```

\begin{block}

A partir de esto, decimos que $\cos(x)$ es **periódica** (con periodo $2\pi$); es decir $$\cos(x\pm 2\pi)=\cos(x).$$ Con la periodicidad basta estudiar $\cos(x)$ para $x\in[0,2\pi]$. 

Otra propiedad importante es que $\cos(x)$ es **par**, es decir $\cos(-x)=a_x=\cos(x)$. Con esto, basta con estudiar $\cos(x)$ para $x\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$

Para construir su gráfica, vemos la siguiente aplicación de \href{https://www.geogebra.org/m/tu3PFgUf}{Geogebra}
```

# (Untitled Slide)
  ## 
  ### 
  

\begin{block}

Su gráfica es 

    ```{image} ../Clases/coseno.png
:align: center
:width: 70%
```

```

# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Función tangente
:class: tip

Como $\tan(x)=\frac{\sen(x)}{\cos(x)}=\frac{b_x}{a_x}$ entonces $\cos(x)\neq0$, lo cual ocurre en los múltiplos impares de $\frac{\pi}{2}$, es decir  $$dom(\tan(x))=\mathbb{R}-\left\{(2k+1)\cdot\frac{\pi}{2}, k\in\mathbb{Z}\right\}.$$  Ya que $-1\leq a_x,b_x\leq1$, el cuociente $\frac{b_x}{a_x}$ cubre todo el rango real. Luego $$rec(\tan(x))=\mathbb{R}.$$ 
Además, el cuociente $\frac{b_x}{a_x}$ permanece invariante en el primer y tercer cuadrantes, o en el cuarto y segundo cuadrantes de la circunferencia goniométrica, es decir, bajo rotaciones en ángulos de valor $\pm\pi$. 
```

\begin{block}

A partir de esto, decimos que $\tan(x)$ es **periódica** (con periodo $\pi$); es decir $$\tan(x\pm \pi)=\tan(x).$$ Con la periodicidad basta estudiar $\tan(x)$ para $x\in\left]-\frac{\pi}{2},\frac{\pi}{2}\right[$. 

Otra propiedad importante es que $\tan(x)$ es **impar**, es decir $\tan(-x)=-\tan(x)$. 

Para construir su gráfica, vemos la siguiente aplicación de \href{https://www.geogebra.org/m/tu3PFgUf}{Geogebra}
```

# (Untitled Slide)
  ## 
  ### 
  

\begin{block}

Su gráfica es 

    ```{image} ../Clases/tangente.png
:align: center
:width: 70%
```

```

  

  

  

  

  

  


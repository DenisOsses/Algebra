

# 
  ### 
- Definir las sumatorias dobles y calcular algunas de ellas.
- Calcular productos aplicando sus propiedades.

## Sumatorias Dobles
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase10.py Clase10` y mueva el archivo resultante a `_static/videos/Clase10.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase10.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
 ### 
  
  

```{admonition} Ejemplo
:class: note
    
    Considere el siguiente arreglo rectangular de números:  

$\begin{array}{cccccccc}
3 & 4 & 5& 6 & 7 & \cdots & 101 & 102\\
6 & 8 & 10 & 12 & 14 & \cdots & 202 & 204\\  
9 & 12 & 15 & 18 & 21 & \cdots & 303 & 306\\  
12 & 16 & 20 & 24 & 28 & \cdots & 404 & 408\\  
 \vdots & \vdots & \vdots & \vdots & \vdots &  & \vdots & \vdots\\  
 300 & 400  & 500 & 600 & 700 & \cdots & 10100 & 10200\\  
303 & 404 & 505 & 606 & 707 & \cdots & 10201 & 10302\\ 
\end{array}
$
- Escriba la suma de todos los n\'umeros de la cuarta fila del arreglo rectangular  anterior utilizando el s\'imbolo de sumatoria y calcule esta suma.
- Escriba la suma de todos los n\'umeros que aparecen en el arreglo anterior usando sumatorias y calcule dicha suma.

```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} Definición
:class: tip
    
    Considere la sucesión $\{F(i)\}_{i\in\mathbb{N}}$. Sabemos que 
    
    $$\sum_{i=1}^m F(i)=F(1)+F(2)+\cdots+F(m).$$  Si cada término de la sucesión $\{F(i)\}_{i\in\mathbb{N}}$ es, a su vez, una sumatoria, es decir 
     
    $$F(i)=\sum_{j=1}^{g(i)}f(i,j)
     $$  
     
    Entonces 
    
    $$\displaystyle\sum_{i=1}^m \sum_{j=1}^{g(i)}f(i,j)=\sum_{i=1}^m F(i) $$ corresponde a la **suma doble** de los términos $f(i,j)$.  
```

**Nota**: Estudiaremos los siguientes casos más simples: cuando $g(i)=n$ (constante) y $g(i)=i
$.

# (Untitled Slide)
  ## 
 ### 
  
  

```{admonition} Suma Rectangular
:class: tip
    
    \underline{Si $g(i)=n$}: En este caso tenemos la sumatoria doble $$\displaystyle\sum_{i=1}^m \sum_{j=1}^{n}f(i,j)$$  y podemos interpretarla como la suma de los términos de un arreglo rectangular de $m$ filas y $n$ columnas:  

$\begin{array}{ccccc}
f(1,1) & f(1,2) & f(1,3)&  \cdots & f(1,n) \\
f(2,1) & f(2,2) & f(2,3)&  \cdots & f(2,n)\\  
\vdots & \vdots & \vdots &  & \vdots \\  
f(m,1) & f(m,2) & f(m,3)&  \cdots & f(m,n)
\end{array}$

donde $f(i,j)$ corresponde al término en la fila $i$ y columna $j$ ($i=1,2,\ldots,m$ y $j=1,2,\ldots,n$).

```

```{admonition} Suma Triangular
:class: tip
    
\underline{Si $g(i)=i$}: En este caso tenemos la sumatoria doble $$\displaystyle\sum_{i=1}^m \sum_{j=1}^{i}f(i,j)$$  y podemos interpretarla como la suma de los términos de un arreglo triangular de $m$ filas y $m$ columnas:  

$\begin{array}{ccccc}
f(1,1) &  & &   &  \\
f(2,1) & f(2,2) & &   &\\  
\vdots & \vdots & \ddots &  & \\  
f(m,1) & f(m,2) & f(m,3)&  \cdots & f(m,m)
\end{array}$

```

# (Untitled Slide)
  ## 
 ### 
  
  

```{admonition} Ejemplo
:class: note
    
    Usando sumas dobles exprese y calcule la suma de todos los números del siguiente arreglo triangular:

$\begin{array}{cccccccc}
1 &  & & &  &  &  & \\
1 & 2 &  &  & &  &&\\  
1& 2 & 3 & &  &  &  & \\  
1 & 2& 3 & 4 &  &  & & \\  
 \vdots & \vdots & \vdots & \vdots & \ddots &  &  & \\  
 1 & 2  & 3 & 4 & \cdots & n-1 &  & \\  
1 & 2 & 3 & 4 & 5 & \cdots & n & \\ 
\end{array}
$

```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} \color{red
:class: note{Propuesto}}

Considere el siguiente arreglo cuadrado

$\begin{array}{ccccc}
a_{11} & a_{12} & a_{13 }&  \cdots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \cdots & a_{2n}\\  
\vdots & \vdots & \vdots &  & \vdots \\  
a_{n1} & a_{n2}  & a_{n3} &  \cdots & a_{nn}
\end{array}
$

Diremos que $a_{ij}$ está en el triángulo superior del arreglo si y solo si $i<j$. Análogamente, diremos que $a_{ij}$ está en el triángulo inferior del arreglo si y solo si $i>j$. 
- Usando sumas dobles exprese la suma de todos los términos del arreglo cuadrado que están en el triángulo superior del arreglo.
- Usando sumas dobles exprese la suma de todos los términos del arreglo cuadrado que están en el triángulo inferior del arreglo.
 

```

## Productorias
# (Untitled Slide)
  ## 
 ### 
  
  

```{admonition} Definición
:class: tip

Considere la sucesión $\{f(k)\}_{k\in\mathbb{N}}=\{a_k\}_{k\in\mathbb{N}}$. El producto de los $n$ primeros términos de esta sucesión se denomina **productoria** de tales términos.  Anotamos $$\prod_{k=1}^n a_k=a_1\cdot a_2\cdots a_n.$$  Notamos que $$\prod_{k=1}^1 a_k=a_1  ~~,~~\prod_{k=1}^{n+1} a_k=\left(\prod_{k=1}^{n}a_k\right)\cdot a_{n+1}.$$ 

```

```{admonition} Propiedades
:class: tip
Si $\{a_{k}\}_{k\in\mathbb{N}}$ y $\{b_{k}\}_{k\in\mathbb{N}}$ son dos sucesiones reales, entonces: 
- **Productoria del producto**: $\displaystyle\prod_{k=1}^{n}(a_{k}\cdot b_{k})=\left(\displaystyle\prod_{k=1}^{n}a_{k}\right)\left(\displaystyle\prod_{k=1}^{n}b_{k}\right)$
- **Asociatividad**: $\displaystyle\prod_{k=1}^{n}a_{k}=\left(\displaystyle\prod_{k=1}^{m}a_{k}\right)\displaystyle\left(\prod_{k=m+1}^{n}a_{k}\right)$,~con $1\leq m < n$.
- **Factorización**: $\displaystyle\prod_{k=1}^{n}ca_{k}=c^{n}\displaystyle\prod_{k=1}^{n}a_{k}~~$,~con $c\in\mathbb{R}$.

```

# (Untitled Slide)
  ## 
 ### 
  
  

```{admonition} Propiedades
:class: tip

    \item[4.] **Cambio de índice**: $\displaystyle\prod_{k=m-l}^{n-l}a_{k+l}=\displaystyle\prod_{k=m}^{n}a_{k}=\displaystyle\prod_{k=m+l}^{n+l}a_{k-l}~~$,  con $l\leq m<n$.
    \item[5.] **Cancelación**: $ \displaystyle\prod_{k=m}^{n}\frac{a_{k}}{a_{k+1}}=\frac{a_{m}}{a_{n+1}}~~$, con  $1\leq m\leq n$.

``` 

```{admonition} Nota
:class: tip

Definimos el **factorial** de $n$ como: $~~~~n!=1\cdot 2\cdot3\cdots n=\displaystyle\prod_{k=1}^n k~~,~~0!=1$
```

```{admonition} Ejemplo
:class: note

 Calcular $\displaystyle \prod_{k=1}^{n}\frac{3k2^{k}}{5^{2k}(2k+2)}$
``` 

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} Ejemplo
:class: note

Calcule $\displaystyle\prod_{k=1}^{n}ka^{b+k}$ en términos de $a,b$ y $n$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} \color{red
:class: note{Propuesto}}

Verifique que  $\displaystyle \prod_{n=1}^{10}\sum_{i=1}^{n}(1+i)=\dfrac{10!\cdot13!}{2^{10}\cdot3!}$
```

  

  

  

  

  

  

  


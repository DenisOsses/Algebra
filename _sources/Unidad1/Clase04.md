

# 
  ### 
- Definir un conjunto por comprensión.
- Utilizar propiedades de conjuntos en demostraciones.
    

## Funciones proposicionales
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase04.py Clase04` y mueva el archivo resultante a `_static/videos/Clase04.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase04.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  
  

  

Una expresión que involucra una variable $x$ no es una proposición, como ``$x$ es par", pero al darle valores a la variable $x$ se obtiene una proposición. ¿Dónde toma valores la variable $x$? Si se supone que $x$ toma valores en los números enteros se tiene que al reemplazar el valor de $x$ por 16, la proposición ``16 es par'' es verdadera y al reemplazar por 5 el valor de $x$ la proposición: ``5 es par'' es falsa.

Cada vez que se defina una expresión que contenga una variable debe ser especificado el campo de ésta.

```{admonition} Definición
:class: tip
     
    Dado un conjunto $E$ (denominado **referencial** o **universal**), se llama **función proposicional** en una variable dentro de $E$, a toda expresión que contiene una variable $x$ y que conduce a una proposición para cada valor $b$ dado a $x$ en $E$. Esta función se denota por $p(x)$.
```

Para definir una función proposicional se debe precisar:
- Un conjunto referencial $E$ (el campo de la variable).
- Una expresión que contenga una variable y tome valores en $E$.
 

```{admonition} Ejemplo 1
:class: note

Si se tiene $E = \{1, 2, 3, 4, 5\}$ y $p(x): x$ es par, al darle valores a $x$ en $E$ se obtienen las proposiciones: $p(1) : 1$ es par, $p(2) : 2$ es par, $p(3) : 3$ es par, $p(4) : 4$ es par y $p(5) : 5$ es par. Las proposiciones $p(2)$ y $p(4)$ son verdaderas, así los elementos de $E$ que verifican $p(x)$ son: 2 y 4.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

# (Untitled Slide)
  ## 
  ### 
  
  

  

A toda función proposicional $p(x)$ definida sobre un conjunto $E$ se le asocia un conjunto formado por aquellos elementos de $E$ que verifican $p(x)$, esto constituye el axioma de comprensión.

```{admonition} Axioma de comprensión
:class: tip

Si $p(x)$ es una función proposicional definida sobre un conjunto $E$, entonces existe un conjunto cuyos elementos son los elementos de $E$ que verifican $p(x)$.
```

Se designa este subconjunto de $E$ por $E_p$: $$E_p=\{x\in E: p(x)\}$$ y se lee: ``$E$ sub $p$ es el conjunto de los $x$ que pertenecen a $E$, tales que $p(x)$''. Note que, para todo $a\in E_p$, la proposición $p(a)$ es verdadera y para todo a $a\not\in E_p$, la proposición es falsa.

```{admonition} Ejemplo 2
:class: note

Sea $E=\mathbb{N}$, asociado a la función proposicional $p(x) : x$ es menor que 6. Así $$E_p=\{1,2,3,4,5\}.$$  Asociado a la función proposicional $q(x) : x$ es múltiplo de 5, tenemos que $$E_p=\{5,10,15,20,25,\ldots,5n,\ldots\}.$$
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} Nota
:class: tip

Un subconjunto $A$ de $E$, asociado a una forma proposicional $p(x)$, se dice definido por comprensión: $A = E_p = \{x\in E: p(x)\}$.
```

## Álgebra de funciones proposicionales
# (Untitled Slide)
  ## 
  ### 

    

  

Sean $p(x)$ y $q(x)$ funciones proposicionales definidas sobre un mismo conjunto referencial $E$, para cada valor $a$ dado a $x$, se obtienen las proposiciones $p(a)$ y $q(a)$ a las cuales se les puede aplicar el álgebra de proposiciones. 

Las proposiciones $\neg p(a), p(a)\vee q(a)$, $p(a)\wedge q(a)$, $p(a)\Rightarrow q(a)$, son verdaderas o falsas dependiendo
del valor que tome $a$ en $E$ y determinan las funciones proposicionales: $\neg p(x), p(x)\vee q(x)$, $p(x)\wedge q(x)$, $p(x)\Rightarrow q(x)$, definidas sobre $E$, que a su vez determinan los subconjuntos de $E$ cuyos elementos verifican
estas funciones proposicionales.

```{admonition} Ejemplo 3
:class: note

Considere las funciones proposicionales: $p(x): x\leq 2$, $q(x): x^2\leq 9$ y $\neg(p(x)\Rightarrow q(x))$, definidas sobre el conjunto referencial $\mathbb{N}$.  Observe que: $p(a)$ es verdadera para todo
$a\in \mathbb{N}_p = \{1, 2\}$, $q(a)$ es verdadera para todo $a\in \mathbb{N}_q = \{1,2,3\}$ y $\neg(p(a)\Rightarrow q(a))$ es verdadera para todo $a\not\in \mathbb{N}_q$ y todo $a\in\mathbb{N}_p$. Luego $$\{x\in\mathbb{N}:\neg(p(x)\Rightarrow q(x))\}$$  es un conjunto sin elementos.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} Definición
:class: tip

Sea $E$ un conjunto referencial, a la función proposicional $p(x) : x\not\in E$ se le asocia, de acuerdo al axioma de comprensión, un conjunto. Este conjunto no tiene elementos por lo que se denomina **conjunto vacío**. Se denota por $\emptyset$: 

$$\emptyset=\{x\in E:x\not\in E\}.$$

```

# (Untitled Slide)
  ## 
  ### 
  
    

  

```{admonition} Definición
:class: tip

Sea $A$ un subconjunto de un conjunto $E$. El **complemento** de $A$ en $E$ es el conjunto asociado a la
función proposicional $p(x) : x\not\in A$. Existen varias formas en que se suele denotar el complemento de un conjunto las mas frecuentes son: $A^c, \overline{A}$.
```  

Evidentemente este conjunto depende tanto de $A$ como del referencial $E$: $$A^c=\{x\in E:x\not\in A\}.$$

```{admonition} Definición
:class: tip

Si $A$ y $B$ son dos subconjuntos de un referencial $E$, entonces la **unión** $A\cup B$ es el conjunto asociado a la función proposicional: $(x\in A)\vee (x\in B)$ definida en $E$:   $$A\cup B=\{x\in E:(x\in A)\vee (x\in B)\}.$$
``` 

```{admonition} Definición
:class: tip

Si $A$ y $B$ son dos subconjuntos de un referencial $E$, entonces la **intersección** $A\cap B$ es el conjunto asociado a la función proposicional: $(x\in A)\wedge (x\in B)$ definida en $E$:  $$A\cap B=\{x\in E:(x\in A)\wedge (x\in B)\}.$$
```

# (Untitled Slide)
  ## 
  ### 
    

  

  
 ```{admonition} Ejemplo 4
:class: note

Se define la **diferencia** entre los conjuntos $A$ y $B$ como $$A-B=\{x\in E:x\in A \wedge x\not\in B\}$$ Pruebe que $A-B=A\cap B^c$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

 ```{admonition} \color{red
:class: warning{Ejercicio propuesto}}

Demuestre que 
- $(A^c)^c=A$.
- $(A\cup B)^c=A^c\cap B^c$.
- $(A\cap B)^c=A^c\cup B^c$.

```

  

  

  

  

  

  
  

  

  

  

  

  

  

  

  

  

  

  

  

  

  


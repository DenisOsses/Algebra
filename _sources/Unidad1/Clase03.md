

# 
  ### 
- Utilizar propiedades de conjuntos en demostraciones.
- Establecer el concepto de función proposicional.

## Nociones de Teoría de Conjuntos
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase03.py Clase03` y mueva el archivo resultante a `_static/videos/Clase03.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase03.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  
  

  

  
  Las nociones de **conjunto**, **elemento** y **pertenencia** son las nociones primitivas de la teoría de conjuntos. La noción de conjunto surge de la idea intuitiva de colección. Los conjuntos se denotan con letras mayúsculas $A, B, C, D$, etc. Los elementos de un conjunto se denotan por letras minúsculas $a,b,c$ ,etc. La expresión: $a$ es elemento de $A$ es una proposición. Si es verdadera se escribe: $a\in A$, si es falsa se escribe $a\not\in A$. El símbolo $\in$ es el de la relación de pertenencia.
  
  
  
  Un conjunto $E$ se dice **definido por extensión** si se da la lista completa de todos sus elementos. Los elementos de un conjunto definido por extensión se colocan entre llaves separados por coma (,) tal cual se muestra en el siguiente ejemplo: $E=\{1,2,3,4\}$. Esta forma de definir un conjunto se justifica por el axioma de extensión.

 
 

    ```{admonition} Axioma de extensión
:class: tip
    
    Dos conjuntos $A$ y $B$ son iguales si tienen los mismos elementos, en cuyo caso se escribe $A=B$ y en caso contrario $A\neq B$.
    ```  

    ```{admonition} Ejemplo 1
:class: note
    
    $A=\{a,b,c,d\}$ y $B=\{a,a,b,a,b,c,d\}$ son iguales ya que la repetición y orden de elementos es irrelevante.
    ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

    
    ```{admonition} Axioma de existencia
:class: tip 
     
    Cualquiera que sea el objeto $a$, existe un conjunto notado $\{a\}$ el cual tiene a $a$ por elemento: $a\in\{a\}$.
    ```

  

# (Untitled Slide)
  ## 
  ### 
  
  

  

    ```{admonition} Definición
:class: tip
     
    Los elementos de un conjunto suelen ser representados por puntos situados en una región plana interior a una curva simple (sin intersecciones). Si el conjunto tiene un gran número de elementos el conjunto se representa como toda la región en el interior de la curva. Este tipo de representación se denomina **diagrama de Venn-Euler**
    ```

    
    \begin{figure}[ht!]
    \begin{subfigure}[b]{0.13\textwidth}
      \frame{```{image} ../Clases/venn1.png
:align: center
:width: 70%
```}
      
    \end{subfigure}
    
    \begin{subfigure}[b]{0.27\textwidth}
      \frame{```{image} ../Clases/venn2.png
:align: center
:width: 70%
```}
      
    \end{subfigure}
    
    \begin{subfigure}[b]{0.22\textwidth}
      \frame{```{image} ../Clases/venn3.png
:align: center
:width: 70%
```}
    \end{subfigure}
    
    \begin{subfigure}[b]{0.22\textwidth}
      \frame{```{image} ../Clases/venn4.png
:align: center
:width: 70%
```}
    \end{subfigure}
  \end{figure}

```{admonition} Relación de inclusión o contenencia
:class: tip
     
   Un conjunto $A$ está contenido o incluido en un conjunto $B$, si todo elemento de $A$ es elemento de $B$. En tal caso se denota: $A\subseteq B$, y se lee: ``$A$ está contenido en $B$ ", o también ``$A$ es un subconjunto de $B$".
    ```
    
    Note que las proposiciones: $A=B$ y $(A\subseteq B\wedge B\subseteq A)$ son lógicamente equivalentes. Por tanto, la proposición: $$A=B\Leftrightarrow(A\subseteq B\wedge B\subseteq A)$$ es una tautología.

## Funciones proposicionales
# (Untitled Slide)
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
 

```{admonition} Ejemplo 2
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

```{admonition} Ejemplo 3
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

  

  

  

  

  

  

  

  

  

  

  

  

  


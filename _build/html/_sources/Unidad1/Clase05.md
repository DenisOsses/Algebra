

# 
  ### 
- Utilizar proposiciones que contienen cuantificadores.

  

  

  

  

## Cuantificadores
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase05.py Clase05` y mueva el archivo resultante a `_static/videos/Clase05.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase05.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  
  

  

  
Dada la función proposicional $p(x)$, sobre el conjunto referencial $\mathbb{N}$, definida por $$p(x) : x ~\text{es múltiplo de}~ 5$$ observe que las expresiones: ``Todos los $x\in\mathbb{N}$ son múltiplos de 5'' y ``existe un $x\in\mathbb{N}$ tal que $x$ es múltiplo de 5'', ya no son funciones proposicionales sino proposiciones, debido a que se puede determinar con precisión su valor de verdad.

Partiendo de una función proposicional $p(x)$, se puede obtener una proposición anteponiendo un **cuantificador**.  Los cuantificadores más usados son el **universal** y el **existencial**.

  ```{admonition} Definición
:class: tip
  
  Sea $p(x)$ una función proposicional definida sobre un conjunto referencial $E$.  Si \underline{para cada valor $a\in E$} se tiene que $p(a)$ es verdadera se escribe $$\forall~x\in E:p(x)$$ y se lee: ``Para todo $x$ en $E$ se verifica $p(x)$'' o ``Cualquiera que sea $x$ en $E$ se verifica $p(x)$''.  El símbolo $\forall$, que transforma la función proposicional $p(x)$ en una proposición, se denomina **cuantificador universal**.
  ```
  
  Esta proposición es verdadera si todos los elementos de $E$ hacen que $p(x)$ sea verdadera.

  
  

# (Untitled Slide)
  ## 
  ### 
  
  

  

  
  ```{admonition} Definición
:class: tip
  
  Sea $p(x)$ una función proposicional definida sobre un conjunto referencial $E$.  Si \underline{para al menos un valor $a\in E$} se tiene que $p(a)$ es verdadera se escribe $$\exists~x\in E:p(x)$$ y se lee: ``Existe un $x$ en $E$ que verifica $p(x)$'' o ``Para algún $x$ en $E$ que verifica $p(x)$''.  El símbolo $\exists$, que transforma la función proposicional $p(x)$ en una proposición, se denomina **cuantificador existencial**.

  ```
  
  Esta proposición es verdadera si existe al menos un elemento de $E$ tal que $p(x)$ sea verdadera.

  ```{admonition} Ejemplo 1
:class: note
  
    Considere la función proposicional ``$p(x): x$ es positivo''. Analice el valor de verdad de las siguientes proposiciones:
- $\forall~x\in\mathbb{R}:p(x)$.
- $\forall~x\in[1,10]:p(x)$.
- $\exists~x\in\mathbb{R}:p(x)$.
- $\exists~x\in[-10,-1]:p(x)$.
    
  ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

  

  
## Negación de cuantificadores
# (Untitled Slide)
  ## 
  ### 
  
  

  

 
  ```{admonition} Nota
:class: tip
  
    La negación de la proposición $\forall~x\in E:p(x)$ es $\exists~x\in E:\neg p(x)$,  ya que la negación de la proposición $\forall~x\in E:p(x)$ es ``No es verdad que todos los elementos de $E$ verifiquen $p(x)$''.  Esto es equivalente con que ``existe al menos un elemento $a$ en $E$ para el que $p(a)$ es falsa''.  Pero si $p(a)$ es falsa entonces $\neg p(a)$ es verdadera; es decir, $\exists~x\in E:\neg(p(x)$. Así tenemos la equivalencia lógica $$\neg\left[\forall~x\in E:p(x)\right]\equiv \exists~x\in E:\neg p(x).$$  Análogamente, podemos probar que $$\neg\left[\exists~x\in E:p(x)\right]\equiv \forall~x\in E:\neg p(x).$$
  ```

  

  ```{admonition} Ejemplo 2
:class: note
  
    Expresar las siguientes proposiciones utilizando símbolos matemáticos y lógicos. Luego escriba su negación.
- Existe un número entero mayor que dos.
- Todos los números reales son pares.
- Hay números naturales pares que son mayores que cinco.
    
  ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

  

  
## Cuantificadores dobles
# (Untitled Slide)
  ## 
  ### 
  
  

  

  
  Cuando las funciones proposicionales dependen de más de una variable los cuantificadores pueden aparecer anidados. Cada vez que se antepone un cuantificador para una variable recorriendo un conjunto de referencia, esa variable desaparece y solo quedan las variables que no han sido cuantificadas.  Veamos el siguiente ejemplo. Si escribimos $$\forall~x\in A, \exists~y\in B: p(x,y)$$ puede interpretarse como $$\forall~x\in A: p(x)~,~\text{donde}~~p(x)\equiv \exists~y\in B: p(x,y)$$  Note que al anteponer el cuantificador existencial para la variable $y$, la función proposicional resultante no dependerá de $y$. 
   

Por eso, cuando a esta se le antepone el cuantificador universal para la variable $x$, el resultado es una proposición de la cual se puede determinar su valor de verdad.
```{admonition} Ejemplo 3
:class: note

Considere la función proposicional $p(x,y):x-y=0$ y los conjuntos referenciales $A=\{1,2,3\}$ y $B=\{1,2\}$. Determine el valor de verdad de la proposición $\forall~x\in A, \exists~y\in B: p(x,y)$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

  

  

# (Untitled Slide)
  ## 
  ### 

  

```{admonition} Definición
:class: tip

Las opciones de dobles cuantificadores son:
$$\forall~x\in A,\forall~y\in B:p(x,y)$$ $$\forall~x\in A,\exists~y\in B:p(x,y)$$ $$\exists~x\in A,\forall~y\in B:p(x,y)$$
$$\exists~x\in A,\exists~y\in B:p(x,y)$$
```
 

```{admonition} \color{red
:class: warning{Ejercicio propuesto}}

Sean $U=\left\{-2,-\frac{1}{2},0,1\right\}$ y $V=\left\{-2,1,2\right\}$. Determine el valor de verdad de las siguientes
proposiciones:
- $\forall~u\in U, \exists~v\in V: (uv+1<0)\lor(u^2-v^2=0)$.
- $\forall~u\in U, \forall~v\in V: (uv+1<0)\lor(u^2-v^2=0)$.

```

  

  

  

  

  

  

  


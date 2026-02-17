

# 
  ### 
- Demostrar equivalencias lógicas de proposiciones.

## Equivalencias lógicas
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase02.py Clase02` y mueva el archivo resultante a `_static/videos/Clase02.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase02.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  
  

  

```{admonition} Definición
:class: tip
Dos proposiciones compuestas $m$ y $n$ son **equivalentes** si entregan el mismo valor de verdad para todo valor de verdad de $m$ y $n$. Escribimos $m\equiv n$ para indicar esto. 
```  
    
De este modo  tenemos que $p\Rightarrow q\equiv \neg p\vee q$. 

```{admonition} Ejemplo 1
:class: note
Pruebe que $p\Rightarrow q\equiv \neg q\Rightarrow\neg p.$
    ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

    ```{admonition} Definición
:class: tip
    Algunas equivalencias lógicas usuales son
- $\neg(\neg p)\equiv p$.
- $\neg(p\vee q)\equiv \neg p\wedge \neg q$.
- $\neg(p\wedge q)\equiv \neg p\vee \neg q$.
- $p\Rightarrow q\equiv \neg p\vee q$.
- $p\Rightarrow q\equiv \neg q\Rightarrow \neg p$.
- $p\Leftrightarrow q\equiv (p\Rightarrow q)\wedge(q\Rightarrow p)$.
    
    ``` 
    
    ```{admonition} Ejemplo 2
:class: note
    ?`Es cierto que $p\Rightarrow q\equiv q\Rightarrow p$?
    ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

# (Untitled Slide)
  ## 
  ### 
  
  
    
    ```{admonition} \color{red
:class: warning{Ejercicio propuesto}}
    Considere el conectivo $\ast$ definido por $$\begin{tabular}{|c|c|c|}
    \hline
     $p$& $q$& $p\ast q$ \\
     \hline
     $V$& $V$& $F$\\
     $V$& $F$& $V$\\
     $F$& $V$& $F$\\
     $F$& $F$& $F$\\
     \hline
     \end{tabular}$$

Determine una proposición compuesta, lógicamente equivalente a $p\ast q$, que solo contenga los conectivos $\neg$ y $\wedge$. ?`Será verdad que $p\ast q\equiv q\ast p$?
    ```

## Tautología, contradicción y contingencia
# (Untitled Slide)
  ## 
  ### 
  
  

  

    
    ```{admonition} Definición
:class: tip
    
    Una proposición cuyo valor de verdad es siempre $V$, cualquiera sea el valor de verdad de las proposiciones simples involucradas, se llama **tautología**.
    ```
    
    ```{admonition} Ejemplo 3
:class: note
    Probar que $(p\wedge q)\Rightarrow p$ es una tautología.
    ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

    
    ```{admonition} Definición
:class: tip
    
     Una proposición cuyo valor de verdad es siempre $F$, cualquiera sea el valor de verdad de las proposiciones simples involucradas, se llama **contradicción**.
    ```

 ```{admonition} Ejemplo 4
:class: note
    Probar que $p\wedge\neg p$ es una contradicción.
    ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

    
    ```{admonition} Definición
:class: tip
    
     Una proposición cuyo valor de verdad no es fijo, cualquiera sea el valor de verdad de las proposiciones simples involucradas, se llama **contingencia**.
    ```
    
    ```{admonition} Ejemplo 5
:class: note
    Determine si la siguiente proposición es una tautología, contradicción o contingencia $$((p \Rightarrow q) \wedge p \wedge \neg q) \Rightarrow (\neg p \vee q)$$
    ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

# (Untitled Slide)
  ## 
  ### 
  
  
  
    ```{admonition} \color{red
:class: warning{Ejercicio propuesto}}
    Pruebe las siguientes leyes o equivalencias lógicas
- $p\vee p\equiv p$ (idempotencia)
- $p\wedge p\equiv p$ (idempotencia)
- $p\vee(q\vee r)\equiv (p\vee q)\vee r$ (asociatividad)
- $p\wedge(q\wedge r)\equiv (p\wedge q)\wedge r$ (asociatividad)
- $p\vee(q\wedge r)\equiv (p\vee q)\wedge(p\vee r)$ (distributividad)
- $p\wedge(q\vee r)\equiv (p\wedge q)\vee(p\wedge r)$ (distributividad)
- $p\wedge(p\vee q)\equiv p$ (absorción)
- $p\vee(p\wedge q)\equiv p$ (absorción)
    
    ```

  

  

  

  

  

  


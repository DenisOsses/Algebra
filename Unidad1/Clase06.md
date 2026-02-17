

# 
  ### 
- Demostrar propiedades de números y conjuntos.
- Demostrar propiedades de los números reales.

## Demostración directa
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase06.py Clase06` y mueva el archivo resultante a `_static/videos/Clase06.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase06.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  
  

  

  
Un **Teorema** es una proposición cuya verdad debe demostrarse. En matemáticas, corresponde a toda proposición que, partiendo de supuestos o **hipótesis**, produce una afirmación no evidente por sí misma o **tesis**.

Los teoremas se deben demostrar mediante razonamientos lógicos. El proceso de razonar lógicamente y deducir proposiciones, propiedades o teoremas, se puede sistematizar mediante los denominados **métodos de demostración**. Estudiaremos 4 de ellos:

 ```{admonition} Demostración directa
:class: tip

Supongamos que una proposición es de la forma $p\Rightarrow q$. Una **demostración directa** de ella es suponer $p$ verdadera y, a partir de deducciones lógicas, probar $q$. 
```

```{admonition} Ejemplo 1
:class: note

Demuestre que $\forall~n\in\mathbb{Z}: n~\textrm{es impar}\Rightarrow n^2~\textrm{es impar}.$
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} Nota
:class: tip

En una proposición de la forma $p\Rightarrow q$, $p$ se denomina **condición suficiente** (para que ocurra $q$) y $q$ **condición necesaria** (para que se satisfaga $p$).  Por ejemplo si $p:$ llueve y $q:$ la calle se moja, podemos leer $p\Rightarrow q$ como ``si llueve entonces la calle se moja'' que es $V$. Sin embargo, no es necesariamente cierto que si la calle se moja entonces llueve ($q\Rightarrow p$).

```

## Demostración por contrarrecíproco y reducción al absurdo
# (Untitled Slide)
  ## 
  ### 
  
  

  

 ```{admonition} Demostración por contrarrecíproco
:class: tip

Supongamos que una proposición es de la forma $p\Rightarrow q$. Una **demostración por contrarrecíproco** de ella se basa en la equivalencia lógica $$p\Rightarrow q\equiv\neg q\Rightarrow\neg p.$$ Es decir, probar que $p\Rightarrow q$ es verdadera equivale a demostrar que $\neg q\Rightarrow\neg p$ es también verdadera (lo que se puede hacer de manera directa).
```

```{admonition} Ejemplo 2
:class: note

Demuestre que $\forall~n\in\mathbb{Z}: n^2~\textrm{es par}\Rightarrow n~\textrm{es par}.$
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

 ```{admonition} Demostración por reducción al absurdo
:class: tip

Supongamos que queremos demostrar la proposición $p$.  En lugar de demostrarla directamente, comenzamos suponiendo que $\neg p$ es verdadera y, a partir de ella, deducimos una contradicción (una proposición siempre falsa).  Esta contradicción proviene de suponer que $\neg p\equiv V$, lo que es incorrecto; así que, $\neg p\equiv F$.  Esto implica que $p\equiv V$.
```

```{admonition} Ejemplo 3
:class: note

Probar que $\sqrt{2}$ no es racional.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

## Demostración por casos
# (Untitled Slide)
  ## 
  ### 
  
  

  

 ```{admonition} Demostración por casos
:class: tip

La **demostración por casos** es un método en el cual la proposición a ser probada se divide en un número finito de casos y cada uno de ellos es demostrado por separado.
```

```{admonition} Ejemplo 4
:class: note

Probar que $\forall~x\in\mathbb{R}: x^2\geq0$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} \color{red
:class: warning{Ejercicio propuesto}}

Probar que $$\forall~a,b,c\in\mathbb{R^+}: ab(a+b)+bc(b+c)+ca(a+c)\geq6abc$$
```

  

  

  

  

  

  


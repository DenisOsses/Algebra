

# 
  ### 
- Definir y calcular razones trigonométricas en triángulos rectángulos.

## Razones trigonométricas
# (Untitled Slide)

```{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase12.py Clase12` y mueva el archivo resultante a `_static/videos/Clase12.mp4`.
```

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase12.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  ## 
  ### 
  
  
  
  La idea fundamental de las razones trigonométricas es notar que en todo triángulo rectángulo ``extendido'', las proporciones entre sus lados se mantienen invariantes (constantes) independiente de la longitud de ellos (debido al Teorema de Thales) 
  
  
        
            ```{image} ../Clases/trigon1.png
:align: center
:width: 70%
```
        
        
            
                \begin{eqnarray*}
                {\scriptstyle
                \frac{\overline{AB}}{\overline{AC}}}&=& {\scriptstyle\frac{\overline{AB_1}}{\overline{AC_1}}= \frac{\overline{AB_2}}{\overline{AC_2}}= \frac{\overline{AB_3}}{\overline{AC_3}}=\cdots=\frac{\text{adyacente a}~\theta}{\text{hipotenusa}}}\\ 
                {\scriptstyle
                \frac{\overline{BC}}{\overline{AC}}}&=&
                {\scriptstyle\frac{\overline{B_1C_1}}{\overline{AC_1}}= \frac{\overline{B_2C_2}}{\overline{AC_2}}= \frac{\overline{B_3C_3}}{\overline{AC_3}}=\cdots=\frac{\text{opuesto a}~\theta}{\text{hipotenusa}}}
                \end{eqnarray*}
            
    
    

# (Untitled Slide)
  ## 
  ### 
  
  
  
  Estas razones invariantes son conocidas como **trigonométricas** y se pueden definir 6: 
  
  ```{admonition} Definición
:class: tip
  
  Las **razones trigonométricas** asociadas al ángulo $\theta$ son el **seno**, **coseno**, **tangente**, **cosecante**, **secante** y **cotangente**, respectivamente: 
  
  
  \begin{tabular}{ccc}
      $\sen(\theta)=\frac{\text{opuesto a}~\theta}{\text{hipotenusa}}$  & $\cos(\theta)=\frac{\text{adyacente a}~\theta}{\text{hipotenusa}}$  & $\tan(\theta)=\frac{\text{opuesto a}~\theta}{\text{adyacente a}~\theta}$  \\
      &&\\
      $\csc(\theta)=\frac{\text{hipotenusa}}{\text{opuesto a}~\theta}$  & $\sec(\theta)=\frac{\text{hipotenusa}}{\text{adyacente a}~\theta}$  & $\cot(\theta)=\frac{\text{adyacente a}~\theta}{\text{opuesto a}~\theta}$ 
  \end{tabular}
  
  
  ```
  

# (Untitled Slide)
  ## 
  ### 
  
  

  ```{admonition} Nota
:class: tip
  
    Tenemos las siguientes identidades  $$\tan(\theta)=\frac{\sen(\theta)}{\cos( \theta)}~~  ,~~\csc(\theta)=\frac{1}{\sen(\theta)}~~  ,~~\sec(\theta)=\frac{1}{\cos(\theta)}~~  ,~~\cot(\theta)=\frac{1}{\tan(\theta)}$$ 
    Además, si observamos el $\triangle ABC$ (rectángulo en $B$), entonces el $\measuredangle ACB=90^\circ-\theta$.  Así  
    
    
    \begin{tabular}{ccc}
       $\sen(90^\circ-\theta)=\cos(\theta)$  & , & $\cos(90^\circ-\theta)=\sen(\theta)$  \\
       $\sec(90^\circ-\theta)=\csc(\theta)$   & , & $\csc(90^\circ-\theta)=\sec(\theta)$  \\
       $\tan(90^\circ-\theta)=\cot(\theta)$   & , & $\cot(90^\circ-\theta)=\tan(\theta)$  
    \end{tabular}
    
    
    de ahí se deriva el nombre **coseno**: ``**co**mplemento del **seno**''.  Análogamente con el resto.
    
  ```
  

## Ángulos notables
# (Untitled Slide)
  ## 
  ### 
  
  
  
  Observemos ahora los siguientes triángulos, el primero isóceles y el segundo equilátero:  
 
  
  
  
        
            ```{image} ../Clases/trigon2.png
:align: center
:width: 70%
```
        
        
            ```{image} ../Clases/trigon3.png
:align: center
:width: 70%
```
        
     
    

    
A partir de ellos podemos calcular las razones trigonométricas de los ángulos $30^\circ$, $45^\circ$ y $60^\circ$.  Además agregamos los ángulos ``extremos'' $0^\circ$ y $90^\circ$, para construir la siguiente tabla:

# (Untitled Slide)
  ## 
  ### 
  
  
  
  
  \renewcommand\arraystretch{1.5}
      \begin{tabular}{|c||c|c|c|c|c|c|}
      \hline
          $\theta$ (en grados) & $\sen(\theta)$ & $\cos(\theta)$ & $\tan(\theta)$ & $\csc(\theta)$ & $\sec(\theta)$ & $\cot(\theta)$ \\
          \hline 
          $0$ & $0$ & $1$ & $0$ & no existe & $1$ & no existe \\
          \hline 
          $30$ & $\myfrac{1}{2}$ & $\myfrac{\sqrt{3}}{2}$ & $\myfrac{\sqrt{3}}{3}$ & $2$ & $\myfrac{2\sqrt{3}}{3}$ & $\sqrt{3}$ \\
          \hline 
          $45$ & $\myfrac{\sqrt{2}}{2}$ & $\myfrac{\sqrt{2}}{2}$ & $1$ & $\sqrt{2}$ & $\sqrt{2}$ & $1$ \\
          \hline 
          $60$ & $\myfrac{\sqrt{3}}{2}$ & $\myfrac{1}{2}$ & $\sqrt{3}$ & $\myfrac{2\sqrt{3}}{3}$ & $2$ & $\myfrac{\sqrt{3}}{3}$ \\
          \hline
          $90$ & $1$ & $0$ & no existe & $1$ & no existe & $0$\\
          \hline
      \end{tabular}
  

## Teorema fundamental
# (Untitled Slide)
  ## 
  ### 

```{admonition} Teorema
:class: tip 
  
  Consideremos un $\triangle ABC$ rectángulo.  Si $\theta$ es un ángulo interior del triángulo, entonces se cumple el **teorema fundamental de la trigonometría**  $$\sen^2(\theta)+\cos^2(\theta)=1$$
  ```
  
  ```{admonition} Nota
:class: tip 
  
    Este teorema es equivalente al teorema de Pitágoras.  Por otro lado, a partir de esta identidad podemos obtener nuevas identidades trigonométricas: 
    
    
        \begin{tabular}{c}
             $\tan^2(\theta)+1=\sec^2(\theta)$  \\
             $1+\cot^2(\theta)=\csc^2(\theta)$ 
        \end{tabular}
    
  ```

```{admonition} Ejemplo 1
:class: note
  
  El ángulo de elevación de la azotea de una torre es $30^\circ$. Acercándose $30$ metros, el ángulo de elevación es $60^\circ$. Determine la altura de la torre.
  ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

  
  ```{admonition} Ejemplo 2
:class: note
  
  Resuelva la ecuación: $$\sen^2(\theta)-2\sen(\theta)\cos(\theta)+\cos^2(\theta)=0.$$
  ```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

  
  ```{admonition} \color{red
:class: warning{Ejercicio propuesto}}
  
  Si $\tan(\theta)=\frac{4}{3}$, calcule $\sen(\theta)$, $\cos(\theta)$ y $\sec(\theta)$.
  ```

  

  

  

  

  

  


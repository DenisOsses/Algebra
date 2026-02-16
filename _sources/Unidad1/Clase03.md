

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase03.py Clase03` y mueva el archivo resultante a `_static/videos/Clase03.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase03.mp4" type="video/mp4">
    Tu navegador no soporta el elemento video.
  </video>
</div>
  \setbeamertemplate{section in toc}[sections numbered]
  \tableofcontents%[hideallsubsections]


%==============================================
# Objetivos de hoy
%==============================================
%## Charts
# \insertsectionhead
  ### \insertsubsectionhead
- Utilizar propiedades de conjuntos en demostraciones.
- Establecer el concepto de función proposicional.




%==============================================
# Contenidos
%==============================================

## Nociones de Teoría de Conjuntos
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}
  
  Las nociones de \textbf{conjunto}, \textbf{elemento} y \textbf{pertenencia} son las nociones primitivas de la teoría de conjuntos. La noción de conjunto surge de la idea intuitiva de colección. Los conjuntos se denotan con letras mayúsculas $A, B, C, D$, etc. Los elementos de un conjunto se denotan por letras minúsculas $a,b,c$ ,etc. La expresión: $a$ es elemento de $A$ es una proposición. Si es verdadera se escribe: $a\in A$, si es falsa se escribe $a\not\in A$. El símbolo $\in$ es el de la relación de pertenencia.
  
  
  
  Un conjunto $E$ se dice \textbf{definido por extensión} si se da la lista completa de todos sus elementos. Los elementos de un conjunto definido por extensión se colocan entre llaves separados por coma (,) tal cual se muestra en el siguiente ejemplo: $E=\{1,2,3,4\}$. Esta forma de definir un conjunto se justifica por el axioma de extensión.

 
 \begin{minipage}[t]{0.5\linewidth}

    :::{admonition} Axioma de extensión
:class: tip
    
    Dos conjuntos $A$ y $B$ son iguales si tienen los mismos elementos, en cuyo caso se escribe $A=B$ y en caso contrario $A\neq B$.
    :::  

    :::{admonition} Ejemplo 1
:class: note
    
    $A=\{a,b,c,d\}$ y $B=\{a,a,b,a,b,c,d\}$ son iguales ya que la repetición y orden de elementos es irrelevante.
    :::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::

    
    :::{admonition} Axioma de existencia
:class: tip 
     
    Cualquiera que sea el objeto $a$, existe un conjunto notado $\{a\}$ el cual tiene a $a$ por elemento: $a\in\{a\}$.
    :::


  


%---------------------------------------------------------------------

# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}

    :::{admonition} Definición
:class: tip
     
    Los elementos de un conjunto suelen ser representados por puntos situados en una región plana interior a una curva simple (sin intersecciones). Si el conjunto tiene un gran número de elementos el conjunto se representa como toda la región en el interior de la curva. Este tipo de representación se denomina \textbf{diagrama de Venn-Euler}
    :::

    
    \begin{figure}[ht!]
    \begin{subfigure}[b]{0.13\textwidth}
      \frame{```{image} ../Clases/venn1.png
:align: center
:width: 70%
```}
      %\caption*{plain}
    \end{subfigure}
    
    \begin{subfigure}[b]{0.27\textwidth}
      \frame{```{image} ../Clases/venn2.png
:align: center
:width: 70%
```}
      %\caption*{style1}
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


\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Relación de inclusión o contenencia
:class: tip
     
   Un conjunto $A$ está contenido o incluido en un conjunto $B$, si todo elemento de $A$ es elemento de $B$. En tal caso se denota: $A\subseteq B$, y se lee: ``$A$ está contenido en $B$ ", o también ``$A$ es un subconjunto de $B$".
    :::
    
    Note que las proposiciones: $A=B$ y $(A\subseteq B\wedge B\subseteq A)$ son lógicamente equivalentes. Por tanto, la proposición: $$A=B\Leftrightarrow(A\subseteq B\wedge B\subseteq A)$$ es una tautología.




%---------------------------------------------------------------------
## Funciones proposicionales
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}

Una expresión que involucra una variable $x$ no es una proposición, como ``$x$ es par", pero al darle valores a la variable $x$ se obtiene una proposición. ¿Dónde toma valores la variable $x$? Si se supone que $x$ toma valores en los números enteros se tiene que al reemplazar el valor de $x$ por 16, la proposición ``16 es par'' es verdadera y al reemplazar por 5 el valor de $x$ la proposición: ``5 es par'' es falsa.

Cada vez que se defina una expresión que contenga una variable debe ser especificado el campo de ésta.

:::{admonition} Definición
:class: tip
     
    Dado un conjunto $E$ (denominado \textbf{referencial} o \textbf{universal}), se llama \textbf{función proposicional} en una variable dentro de $E$, a toda expresión que contiene una variable $x$ y que conduce a una proposición para cada valor $b$ dado a $x$ en $E$. Esta función se denota por $p(x)$.
:::

\begin{minipage}[t]{0.5\linewidth}

Para definir una función proposicional se debe precisar:
- Un conjunto referencial $E$ (el campo de la variable).
- Una expresión que contenga una variable y tome valores en $E$.
 

:::{admonition} Ejemplo 2
:class: note

Si se tiene $E = \{1, 2, 3, 4, 5\}$ y $p(x): x$ es par, al darle valores a $x$ en $E$ se obtienen las proposiciones: $p(1) : 1$ es par, $p(2) : 2$ es par, $p(3) : 3$ es par, $p(4) : 4$ es par y $p(5) : 5$ es par. Las proposiciones $p(2)$ y $p(4)$ son verdaderas, así los elementos de $E$ que verifican $p(x)$ son: 2 y 4.
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::






%---------------------------------------------------------------------
%## Funciones proposicionales
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}

A toda función proposicional $p(x)$ definida sobre un conjunto $E$ se le asocia un conjunto formado por aquellos elementos de $E$ que verifican $p(x)$, esto constituye el axioma de comprensión.

:::{admonition} Axioma de comprensión
:class: tip

Si $p(x)$ es una función proposicional definida sobre un conjunto $E$, entonces existe un conjunto cuyos elementos son los elementos de $E$ que verifican $p(x)$.
:::

Se designa este subconjunto de $E$ por $E_p$: $$E_p=\{x\in E: p(x)\}$$ y se lee: ``$E$ sub $p$ es el conjunto de los $x$ que pertenecen a $E$, tales que $p(x)$''. Note que, para todo $a\in E_p$, la proposición $p(a)$ es verdadera y para todo a $a\not\in E_p$, la proposición es falsa.

\begin{minipage}[t]{0.5\linewidth}


:::{admonition} Ejemplo 3
:class: note

Sea $E=\mathbb{N}$, asociado a la función proposicional $p(x) : x$ es menor que 6. Así $$E_p=\{1,2,3,4,5\}.$$  Asociado a la función proposicional $q(x) : x$ es múltiplo de 5, tenemos que $$E_p=\{5,10,15,20,25,\ldots,5n,\ldots\}.$$
:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


:::{admonition} Nota
:class: tip

Un subconjunto $A$ de $E$, asociado a una forma proposicional $p(x)$, se dice definido por comprensión: $A = E_p = \{x\in E: p(x)\}$.
:::







% %---------------------------------------------------------------------
% ## Álgebra de funciones proposicionales
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   

% Sean $p(x)$ y $q(x)$ funciones proposicionales definidas sobre un mismo conjunto referencial $E$, para cada valor $a$ dado a $x$, se obtienen las proposiciones $p(a)$ y $q(a)$ a las cuales se les puede aplicar el álgebra de proposiciones. 

% 

% Las proposiciones $\neg p(a), p(a)\vee q(a)$, $p(a)\wedge q(a)$, $p(a)\Rightarrow q(a)$, son verdaderas o falsas dependiendo
% del valor que tome $a$ en $E$ y determinan las funciones proposicionales: $\neg p(x), p(x)\vee q(x)$, $p(x)\wedge q(x)$, $p(x)\Rightarrow q(x)$, definidas sobre $E$, que a su vez determinan los subconjuntos de $E$ cuyos elementos verifican
% estas funciones proposicionales.

% 

% %---------------------------------------------------------------------
% %## Álgebra de funciones proposicionales
% # (Untitled Slide)
%   %## \insertsectionhead
%   %### \insertsubsectionhead
  
%   

% :::{admonition} Ejemplo 4
:class: note
% 
% Considere las funciones proposicionales: $p(x): x\leq 2$, $q(x): x^2\leq 9$ y $\neg(p(x)\Rightarrow q(x))$, definidas sobre el conjunto de los números naturales $\mathbb{N}$. Observe que: $p(a)$ es verdadera para todo
% $a\in \mathbb{N}_p = \{1, 2\}$, $q(a)$ es verdadera para todo $a\in \mathbb{N}_q = \{1,2,3\}$ y $\neg(p(a)\Rightarrow q(a))$ es verdadera para todo $a\not\in \mathbb{N}_q$ y todo $a\in\mathbb{N}_p$. Luego $$\{x\in\mathbb{N}:\neg(p(x)\Rightarrow q(x))\}$$ es un conjunto sin elementos.
% :::

% :::{admonition} Definición
:class: tip
% 
% Sea $E$ un conjunto referencial, a la función proposicional $p(x) : x\not\in E$ se le asocia, de acuerdo al axioma de comprensión, un conjunto. Este conjunto no tiene elementos por lo que se denomina \textbf{conjunto vacío}. Se denota por $\emptyset$: $$\emptyset=\{x\in E:x\not\in E\}.$$
% :::

% 

% %---------------------------------------------------------------------
% %## Álgebra de funciones proposicionales
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   

% :::{admonition} Definición
:class: tip
% 
% Sea $A$ un subconjunto de un conjunto $E$. El \textbf{complemento} de $A$ en $E$ es el conjunto asociado a la
% función proposicional $p(x) : x\not\in A$. Existen varias formas en que se suele denotar el complemento de un conjunto las mas frecuentes son: $A^c, \overline{A}$.
% :::

% Evidentemente este conjunto depende tanto de $A$ como del referencial $E$: $$A^c=\{x\in E:x\not\in A\}.$$

% 

% %---------------------------------------------------------------------
% %## Álgebra de funciones proposicionales
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%  :::{admonition} Definición
:class: tip
% 
% Si $A$ y $B$ son dos subconjuntos de un referencial $E$, entonces la \textbf{unión} $A\cup B$ es el conjunto asociado a la función proposicional: $(x\in A)\vee (x\in B)$ definida en $E$: $$A\cup B=\{x\in E:(x\in A)\vee (x\in B)\}.$$
% ::: 

% :::{admonition} Definición
:class: tip
% 
% Si $A$ y $B$ son dos subconjuntos de un referencial $E$, entonces la \textbf{intersección} $A\cap B$ es el conjunto asociado a la función proposicional: $(x\in A)\wedge (x\in B)$ definida en $E$: $$A\cap B=\{x\in E:(x\in A)\wedge (x\in B)\}.$$
% :::

% 

% %---------------------------------------------------------------------
% %## Álgebra de funciones proposicionales
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%  :::{admonition} Ejemplo 5
:class: note
% 
% Se define la \textbf{diferencia} entre los conjuntos $A$ y $B$ como $$A-B=\{x\in E:x\in A \wedge x\not\in B\}$$ Pruebe que $A-B=A\cap B^c$.
% :::

%  :::{admonition} \color{red
:class: warning{Ejercicio propuesto}}
% 
% Demuestre que 
% 
%     \item $(A^c)^c=A$.
%     \item $(A\cup B)^c=A^c\cap B^c$.
%     \item $(A\cap B)^c=A^c\cup B^c$.
% 
% :::

% 


% %==============================================
% # Conclusión
% %==============================================

% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%   
%   
%       \item Hay una gran cantidad de propiedades en teoría de conjuntos; solo nos hemos enfocado en las más usadas en el curso.
%       \item Existe una clara analogía entre álgebra de proposiciones y la teoría de conjuntos.
%   

%  

% %==============================================
% # Asistencia
% %==============================================

% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%   \textbf{Solo se considerará la asistencia hasta 5 minutos después de terminada la clase.}
  
%   
%   ```{image} ../Clases/QR
:align: center
:width: 70%
```
%   
  
% 



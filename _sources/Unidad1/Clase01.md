

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase01.py Clase01` y mueva el archivo resultante a `_static/videos/Clase01.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase01.mp4" type="video/mp4">
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
- Introducir los conceptos básicos de la lógica proposicional.
- Determinar el valor de verdad de proposiciones.
    % \item Demostrar equivalencias lógicas de proposiciones.




%==============================================
# Contenidos
%==============================================
## Lógica proposicional
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}
La lógica es la ciencia formal que estudia los principios de la demostración y nos ayuda a discernir entre \textbf{proposiciones} válidas mediante inferencias o deducciones. 
  
  :::{admonition} Definición
:class: tip
  
    Las \textbf{proposiciones} son enunciados o frases del lenguaje natural sobre las cuales es posible afirmar su veracidad $(V)$ o falsedad $(F)$. Usualmente se denotan con letras minúsculas $p,q,r,s,t,\ldots$
  :::
  
    :::{admonition} Ejemplo 1
:class: note
    Determine si los siguientes enunciados son proposiciones o no: 
- Dos es mayor que cinco.
- Hola.
        
    
    :::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip
  
    La veracidad o falsedad de una proposición se denomina \textbf{valor de verdad} de tal proposición.
  :::

  
  :::{admonition} Ejemplo 2
:class: note
    Determine el valor de verdad de las siguentes proposiciones:
- $2+3=5$.
- Hoy es 6 de marzo.
        
    
    :::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


    
    :::{admonition} Nota
:class: tip
    
    La negación de una proposición asocia a toda proposición $p$ una proposición denotada $\neg p$, verdadera si $p$ es falsa y falsa si $p$ es verdadera. 
  :::

  
  :::{admonition} Ejemplo 3
:class: note
    Escriba la negación de las proposiciones del ejemplo 2.
    :::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


  
    
  


%-------------------------------------------------------------------------

## Tablas de Verdad
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}
  
    \textbf{Pregunta}: Suponga que conoce los valores de verdad de las proposiciones $p$ y $q$. ?`Es posible determinar el valor de verdad de sus proposiciones compuestas asociadas?  Para el caso de dos proposiciones $p$ y $q$ existen cuatro formas de combinar sus valores de verdad, los que se han colocado en la siguiente tabla (tabla de verdad):  

    $$\begin{tabular}{|c|c|c|}
    \hline
    $p$& $q$& $p\ast q$ \\
     \hline
     $V$& $V$& $?$\\
     $V$& $F$& $?$\\
     $F$& $V$& $?$\\
     $F$& $F$& $?$\\
     \hline
    \end{tabular}$$

\begin{minipage}[t]{0.5\linewidth}

    Al fijar una sucesión de los cuatro valores $(????)$ correspondientes a $p\ast q$, se obtiene exactamente el significado lógico del \textbf{conector} $\ast$.  Cada sucesión de valores se llama una \textbf{evaluación} de $\ast$, así se tiene que: toda evaluación determina un conectivo lógico.  
    
    
  
   De esta manera para dos proposiciones $p$ y $q$ existen $2^4 = 16$ conectivos lógicos, los cuales quedarán definidos mediante su evaluación. Algunos de ellos son los más utilizados en el lenguaje natural y en el matemático, y los llamaremos \textbf{conectivos lógicos} usuales.




%-------------------------------------------------------------------------

## Conectivos Lógicos
# (Untitled Slide)
## \insertsectionhead
### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}

    :::{admonition} Definición
:class: tip
    La \textbf{conjunción} es el conectivo lógico \textbf{y}, notado con el símbolo $\wedge$ y definido por: 
    $$\begin{tabular}{|c|c|c|}
    \hline
     $p$& $q$& $p\wedge q$ \\
     \hline
     $V$& $V$& $V$\\
     $V$& $F$& $F$\\
     $F$& $V$& $F$\\
     $F$& $F$& $F$\\
     \hline
\end{tabular}$$
  :::

Se lee $``p$ y $q"$.

\begin{minipage}[t]{0.5\linewidth}

 :::{admonition} Definición
:class: tip
   La \textbf{disyunción} es el conectivo lógico \textbf{o}, notado con el símbolo $\vee$ y definido por: 
   $$\begin{tabular}{|c|c|c|}
    \hline
     $p$& $q$& $p\vee q$ \\
     \hline
     $V$& $V$& $V$\\
     $V$& $F$& $V$\\
     $F$& $V$& $V$\\
     $F$& $F$& $F$\\
     \hline
\end{tabular}$$
  ::: 

Se lee $``p$ o $q"$.




%-------------------------------------------------------------------------

%## Conectivos Lógicos
# (Untitled Slide)
## \insertsectionhead
### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}

    :::{admonition} Definición
:class: tip
    
   La \textbf{implicación} es el conectivo lógico \textbf{si...entonces}, notado con el símbolo $\Rightarrow$ y definido por:
$$\begin{tabular}{|c|c|c|}
    \hline
     $p$& $q$& $p\Rightarrow q$ \\
     \hline
     $V$& $V$& $V$\\
     $V$& $F$& $F$\\
     $F$& $V$& $V$\\
     $F$& $F$& $V$\\
     \hline
\end{tabular}$$
  :::

Se lee $``$si $p$ entonces $q"$ o ``$p$ implica $q"$.

\begin{minipage}[t]{0.5\linewidth}

:::{admonition} Definición
:class: tip
    
    La \textbf{doble implicación} es el conectivo lógico \textbf{si y solo si}, notado con el símbolo $\Leftrightarrow$ y definido por:
$$\begin{tabular}{|c|c|c|}
    \hline
     $p$& $q$& $p\Leftrightarrow q$ \\
     \hline
     $V$& $V$& $V$\\
     $V$& $F$& $F$\\
     $F$& $V$& $F$\\
     $F$& $F$& $V$\\
     \hline
\end{tabular}$$
  :::

Se lee $``p$ si y solo si $q"$ o $``p$ es equivalente a $q"$.




%-------------------------------------------------------------------------

%## Conectivos Lógicos
# (Untitled Slide)
## \insertsectionhead
### \insertsubsectionhead
  
  

  
\begin{minipage}[t]{0.5\linewidth}
  
    :::{admonition} Ejemplo 4
:class: note
    
    Determinar el valor de verdad de cada una de las siguientes proposiciones:
- Si $3<5$ entonces $-3<-5$.
- $\sqrt{16}=4$ o $\sqrt{16}=-4$.
- $6+4=10$ y $\sqrt{2}\cdot\sqrt{2}=2$.
- $5^2=25~$ o $~2+2=5$.
    
    :::  

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


    :::{admonition} Ejemplo 5
:class: note
    
    Pruebe que $(p\Rightarrow q)\Leftrightarrow(\neg p\vee q)$ es una proposición siempre verdadera.
    :::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::


 
\begin{minipage}[t]{0.5\linewidth}
    :::{admonition} \color{red
:class: warning{Ejercicio propuesto}}
    
    Pruebe que $(p\Rightarrow q)\Leftrightarrow(\neg q\Rightarrow\neg p)$ es una proposición siempre verdadera.
    :::




% %-------------------------------------------------------------------------
% ## Equivalencias lógicas
% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%     :::{admonition} Definición
:class: tip
%     Dos proposiciones compuestas $m$ y $n$ son \textbf{equivalentes} si entregan el mismo valor de verdad para todo valor de verdad de $m$ y $n$. Escribimos $m\equiv n$ para indicar esto. 
%     :::  
    
%     De este modo, del ejemplo 5 tenemos que $p\Rightarrow q\equiv \neg q\Rightarrow\neg p.$
    
%     :::{admonition} Ejemplo 6
:class: note
%     Pruebe que $p\Rightarrow q\equiv \neg p\vee q$.
%     :::

% 

% %-------------------------------------------------------------------------

% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
%     :::{admonition} Definición
:class: tip
%     Algunas equivalencias lógicas usuales son
%     
%     \item $\neg(\neg p)\equiv p$.
%     \item $\neg(p\vee q)\equiv \neg p\wedge \neg q$.
%     \item $\neg(p\wedge q)\equiv \neg p\vee \neg q$.
%     \item $p\Rightarrow q\equiv \neg p\vee q$.
%     \item $p\Rightarrow q\equiv \neg q\Rightarrow \neg p$.
%     \item $p\Leftrightarrow q\equiv (p\Rightarrow q)\wedge(q\Rightarrow p)$.
%     
%     ::: 
    
%     :::{admonition} Ejemplo 7
:class: note
%     ?`Es cierto que $p\Rightarrow q\equiv q\Rightarrow p$?
%     :::

% 

% %-------------------------------------------------------------------------

% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
    
%     :::{admonition} \color{red
:class: warning{Ejercicio propuesto}}
%     Considere el conectivo $\ast$ definido por $$\begin{tabular}{|c|c|c|}
%     \hline
%      $p$& $q$& $p\ast q$ \\
%      \hline
%      $V$& $V$& $F$\\
%      $V$& $F$& $V$\\
%      $F$& $V$& $F$\\
%      $F$& $F$& $F$\\
%      \hline
%      \end{tabular}$$

% Determine una proposición compuesta, lógicamente equivalente a $p\ast q$, que solo contenga los conectivos $\neg$ y $\wedge$. ?`Será verdad que $p\ast q\equiv q\ast p$?
%     :::

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
%       \item Las proposiciones que estudiaremos en este curso son de carácter netamente matemático.
%       \item Los cuatros conectivos lógicos estudiados hoy son los usuales entre dos proposiciones, pero se pueden definir 16 en total.
%       \item En general todos los conectivos se pueden definir en términos de $\neg$, $\wedge$ y $\vee$. Se recomienda escribir $\Rightarrow$ y $\Leftrightarrow$ usándolos.
%       % \item Una equivalencia lógica se puede interpretar como una ``traducción'' de una proposición en otra.
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



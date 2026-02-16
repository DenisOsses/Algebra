

%--------------------------------------
% Create title frame
\titleframe

%--------------------------------------
% Table of contents
# Temario

:::{admonition} Presentación de la Clase
:class: note
Para generar el video, ejecute: `manim -pql slides/Clase14.py Clase14` y mueva el archivo resultante a `_static/videos/Clase14.mp4`.
:::

<div class="video-container" style="text-align: center; margin-bottom: 2em;">
  <video width="80%" controls>
    <source src="../_static/videos/Clase14.mp4" type="video/mp4">
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
- Demostrar identidades trigonométricas




%==============================================
# Contenidos
%==============================================

%---------------------------------------------------------------------
## Suma y resta de ángulos. Ángulo Doble
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}



:::{admonition} Teorema
:class: tip

Si $\alpha$ es un ángulo cualquiera de un triángulo, entonces  $$\sen^2(\alpha)+\cos^2(\alpha)=1$$
:::

:::{admonition} Teorema
:class: tip

Si $\alpha$ y $\beta$ son dos ángulos cualesquiera de un triángulo, entonces 


    \begin{tabular}{ccc}
         $\sen(\alpha\pm\beta)$ & $=$ & $\sen(\alpha)\cos(\beta)\pm\sen(\beta)\cos(\alpha)$ \\
         $\cos(\alpha\pm\beta)$ & $=$ & $\cos(\alpha)\cos(\beta)\mp\sen(\alpha)\sen(\beta)$ \\
         $\tan(\alpha\pm\beta)$ & $=$ & $\dfrac{\tan(\alpha)\pm\tan(\beta)}{1\mp\tan(\alpha)\tan(\beta)}$
    \end{tabular}

:::

\begin{minipage}[t]{0.5\linewidth}


:::{admonition} Teorema
:class: tip

Si $\alpha$ es un ángulo cualquiera de un triángulo, entonces 


    \begin{tabular}{ccc}
         $\sen(2\alpha)$ & $=$ & $2\sen(\alpha)\cos(\alpha)$ \\
         $\cos(2\alpha)$ & $=$ & $\cos^2(\alpha)-\sen^2(\alpha)$ \\
         $\cos(2\alpha)$ & $=$ & $1-2\sen^2(\alpha)$ \\
         $\cos(2\alpha)$ & $=$ & $2\cos^2(\alpha)-1$ \\
         $\tan(2\alpha)$ & $=$ & $\dfrac{2\tan(\alpha)}{1-\tan^2(\alpha)}$
    \end{tabular}

:::




%---------------------------------------------------------------------
## Ángulo medio. Suma en producto
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.45\linewidth}



:::{admonition} Teorema
:class: tip

Si $\alpha$ es un ángulo cualquiera de un triángulo, entonces 


    \begin{tabular}{ccc}
         $\sen\left(\dfrac{\alpha}{2}\right)$ & $=$ & $\pm\sqrt{\dfrac{1-\cos(\alpha)}{2}}$ \\
         $\cos\left(\dfrac{\alpha}{2}\right)$ & $=$ & $\pm\sqrt{\dfrac{1+\cos(\alpha)}{2}}$ \\
         $\tan\left(\dfrac{\alpha}{2}\right)$ & $=$ & $\pm\sqrt{\dfrac{1-\cos(\alpha)}{1+\cos(\alpha)}}$ 
    \end{tabular}

:::

\begin{minipage}[t]{0.55\linewidth}


:::{admonition} Teorema
:class: tip

Si $\alpha$ y $\beta$ son dos ángulos cualesquiera de un triángulo, entonces 

    \begin{tabular}{ccc}
         $\sen(\alpha)+\sen(\beta)$ & $=$ & $2\sen\left(\dfrac{\alpha+\beta}{2}\right)\cos\left(\dfrac{\alpha-\beta}{2}\right)$ \\
         $\sen(\alpha)-\sen(\beta)$ & $=$ & $2\cos\left(\dfrac{\alpha+\beta}{2}\right)\sen\left(\dfrac{\alpha-\beta}{2}\right)$ \\
         $\cos(\alpha)+\cos(\beta)$ & $=$ & $2\cos\left(\dfrac{\alpha+\beta}{2}\right)\cos\left(\dfrac{\alpha-\beta}{2}\right)$ \\
         $\cos(\alpha)-\cos(\beta)$ & $=$ & $-2\sen\left(\dfrac{\alpha+\beta}{2}\right)\sen\left(\dfrac{\alpha-\beta}{2}\right)$
    \end{tabular}

:::




%---------------------------------------------------------------------
## Producto en suma
# (Untitled Slide)
  ## \insertsectionhead
  ### \insertsubsectionhead
  



\begin{minipage}[t]{0.5\linewidth}



:::{admonition} Teorema
:class: tip

Si $\alpha$ y $\beta$ son dos ángulos cualesquiera de un triángulo, entonces 


    \begin{tabular}{ccc}
         $\sen(\alpha)\cos(\beta)$ & $=$ & $\frac{1}{2}\big[\sen(\alpha+\beta)+\sen(\alpha-\beta)\big]$ \\
         $\cos(\alpha)\cos(\beta)$ & $=$ & $\frac{1}{2}\big[\cos(\alpha+\beta)+\cos(\alpha-\beta)\big]$ \\
         $\sen(\alpha)\sen(\beta)$ & $=$ & $\frac{1}{2}\big[\cos(\alpha-\beta)-\cos(\alpha+\beta)\big]$
    \end{tabular}

:::

\begin{minipage}[t]{0.51\linewidth}



:::{admonition} Ejemplo
:class: note

Probar las siguientes identidades: 
- $2\cot^2(\alpha)+1=\csc^4(\alpha)-\cot^4(\alpha)$.
- $\left(\cos\left(\dfrac{\beta}{2}\right)-\sen\left(\dfrac{\beta}{2}\right)\right)^2=1-\sen(\beta)$
- Si $\alpha+\beta+\gamma=\pi$ entonces $$\sen(\alpha)+\sen(\beta)+\sen(\gamma)=4\cos\left(\dfrac{\alpha}{2}\right)\cos\left(\dfrac{\beta}{2}\right)\cos\left(\dfrac{\gamma}{2}\right)$$

:::

:::{toggle} Solución
*(Espacio para la solución detallada)*
:::





% %==============================================
% # Conclusión
% %==============================================

% # (Untitled Slide)
%   ## \insertsectionhead
%   ### \insertsubsectionhead
  
%   
  
%   
%   
%       \item Todas las definiciones e identidades vistas en clases anteriores, son válidas para las identidades trigonométricas generales.
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



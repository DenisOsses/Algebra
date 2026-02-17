

# 
  ### 
- Caracterizar la perpendicularidad de rectas en el plano y en el espacio.
- Aplicar las propiedades fundamentales de las operaciones de vectores para la resolución de problemas.

  

## Perpendicularidad de rectas. Vector Proyección
# (Untitled Slide)
  ## 
  ### 
  

```{admonition} Definición
:class: tip

Dos rectas en el espacio (o en el plano) son perpendiculares si y solo si sus vectores directores son perpendiculares y si dichas rectas se cortan en un punto. 
```
```{admonition} Ejemplo 1
:class: note

¿Es perpendicular la recta $\displaystyle \vec{r}=(1,0,1)+\lambda(1,2,3)$, $\lambda\in\mathbb{R}$, con $x=1+t, y=t, z=1-4t$, $t\in\mathbb{R}$?
``` 

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} Definición
:class: tip

El vector $\lambda\vec{b}$ se denomina **vector proyección ortogonal** de $\vec{x}$ sobre $\vec{b}$ y se denota por $P_{\vec{b}}(\vec{x})$.
```
 

\visible<4-5>{```{image} ../Clases/Proyeccion1.png
:align: center
:width: 70%
```}

Los vectores $\vec{b}$ e $\vec{y}$ son ortogonales en el punto $B$. El vector $\overrightarrow{AB}=\lambda\vec{b}$ es un ponderado de $\vec{b}$ (ya que son paralelos).

  

## Vector proyección. Propiedades
# (Untitled Slide)
  ## 
  ### 
  

Notamos que 

$$\lambda\vec{b}+\vec{y}=\vec{x}.$$ Como el vector $\vec{y}$ es ortogonal con $\vec{b}$, tenemos que $\vec{y}\cdot\vec{b}=0$.  Luego, si a la igualdad anterior le realizamos un producto punto con $\vec{b}$, obtenemos que $$\lambda=\frac{\vec{x}\cdot\vec{b}}{\vec{b}\cdot\vec{b}}=\frac{\vec{x}\cdot\vec{b}}{||\vec{b}||^2}.$$ Por lo tanto 

$$\color{red}\boxed{\color{black}P_{\vec{b}}(\vec{x})=\left(\frac{\vec{x}\cdot\vec{b}}{||\vec{b}||^2}\right)\vec{b}}$$ 

```{admonition} Nota
:class: tip

El vector $\vec{y}=\vec{x}-P_{\vec{b}}(\vec{x})$ se denomina **complemento ortogonal** y es muy útil para determinar distancias.
```
 

```{admonition} Ejemplo 2
:class: note

Si $\vec{u}=(2,4)$ y $\vec{v}=(5,3)$, determine $P_{\vec{v}}(\vec{u})$ y $P_{\vec{u}}(\vec{v})$. Dibuje estos vectores y sus complementos ortogonales.
``` 

```{toggle} Solución
*(Espacio para la solución detallada)*
```

```{admonition} Propiedades
:class: tip 

Si $\displaystyle P_{\vec{b}}(\vec{x})$ denota la proyección ortogonal de $\vec{x}$ sobre $\vec{b}$ entonces:  
[{(1)}]
- $\displaystyle P_{\vec{b}}(\vec{b})=\vec{b}$.
- Si $\vec{a}$ es cualquier vector perpendicular al vector $\vec{b}$ entonces $\displaystyle P_{\vec{b}}(\vec{a})=\vec{0}$.
- $\displaystyle P_{\vec{b}}(\lambda\vec{x})=\lambda \displaystyle P_{\vec{b}}(\vec{x})$.
- $\displaystyle P_{\vec{b}}(\vec{x}+\vec{y})=\displaystyle P_{\vec{b}}(\vec{x})+\displaystyle P_{\vec{b}}(\vec{y})$

``` 

```{admonition} Ejemplo 3
:class: note

Considere la recta $L:\frac{x-1}{2}=y-2=\frac{z-3}{2}.$ Encuentre la ecuación de la recta perpendicular a $L$ que pasa por el punto $(1,2,1)$.
```

```{toggle} Solución
*(Espacio para la solución detallada)*
```

  

  

  

  

  

  

  


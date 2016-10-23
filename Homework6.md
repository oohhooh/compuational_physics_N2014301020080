# Homework6



---

##摘要：
在考虑空气阻力以及空气密度随海拔高度变化的情况下，计算炮弹的飞行轨迹，同时引入迎面风阻，考虑目标与发射点在不同的海拔高度的情况。

---
##正文：
公式推导：由欧勒法可得    
![ ][1]    
考虑空气密度的变化其受到的空气阻力：    
![ ][2]    
由于迎面风阻：    
![ ][3]    
所以，速度为：    
![ ][4]    
Code:[Click Here](https://github.com/oohhooh/compuational_physics_N2014301020080/blob/master/homework6.py)    
取海拔高度差为2000米，发射角度为45，初速度为500m/s


---
结论：
result：    
![ ][5]





  [1]: https://github.com/oohhooh/compuational_physics_N2014301020080/blob/master/images/CodeCogsEqn.gif
  [2]: http://latex.codecogs.com/gif.latex?%5C%5CF_%7Bdrag,x%7D=-%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%20%7DBv%28v_%7Bx%7D-v_%7Bwind%7D%29%5C%5CF_%7Bdrag,y%7D=-%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%20%7DBvv_%7By%7D
  [3]: http://latex.codecogs.com/gif.latex?%5C%5CF_%7Bdrag,x%7D=-%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%20%7DBv%28v_%7Bx%7D-v_%7Bwind%7D%29%5C%5CF_%7Bdrag,y%7D=-%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%20%7DBvv_%7By%7D
  [4]: http://latex.codecogs.com/gif.latex?%5C%5C%5Ctherefore%20v_%7Bx,i&plus;1%7D=v_%7Bx,i%7D-%5Cleft%20%28%201-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%20%5Cright%20%29%5E%7B%5Calpha%20%7D%5Cfrac%7BBv%28v_%7Bx%7D-v_%7Bwind%7D%29%7D%7Bm%7Ddt%5C%5C%20v_%7By,i&plus;1%7D=v_%7By,i%7D-gdt-%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%7D%5Cfrac%7BBvv_%7By%7D%7D%7Bm%7Ddt
  [5]: https://github.com/oohhooh/compuational_physics_N2014301020080/blob/master/images/WWT1O7XVX3Y%5DGS9N2%25RS_BI.png

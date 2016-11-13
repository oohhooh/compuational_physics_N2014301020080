# Homework8



---

##摘要：
由于没能掌握Vpython的用法，本次作业只在上一次的作业做了些改动，进一步利用Euler-cromer方法做出了F_d从1.35-1.48之间的分岔图。

---
##正文：
公式推导：由euler-cromer方法可得：    
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%20%5Comega%7D%7Bdt%7D%3D-%20%5Cfrac%7Bg%7D%7Bl%7Dsin%28%5Ctheta%29-q%20%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_D%20sin%28%5COmega_d%20t%29)

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D%3D%5Comega)
![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_i&plus;%5B-%28g/l%29sin%5Ctheta_i-q%5Comega_i&plus;F_Dsin%28%5COmega_Dt_i%29%5D%5CDelta%20t)    

![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)    
![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_i%20&plus;%5CDelta%20t)
当F_d增大时，物理摆的周期便会倍增，因此F_d-Θ图会出现分岔的现象。
[code](https://github.com/oohhooh/compuational_physics_N2014301020080/blob/master/homework8.py)
---
结论：
result：    
![](https://github.com/oohhooh/compuational_physics_N2014301020080/blob/master/images/D_%60OVN%60Q%25H%7DOD2)PX317ZHG.png)

---
致谢：    
还是感谢侯国一同学的程序

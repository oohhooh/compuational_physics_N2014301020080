##摘要
本次作业计算了水星近日点进动速率（4.10）

##正文
考虑相对论效应，万有引力定律修正为：    
![](http://latex.codecogs.com/gif.latex?F_%7BG%7D%5Capprox%20%5Cfrac%7BGM_%7BS%7DM_%7BM%7D%7D%7Br%5E%7B2%7D%7D%5Cleft%20%28%201&plus;%5Cfrac%7B%5Calpha%20%7D%7Br%5E%7B2%7D%7D%5Cright%20%29)    
其中![](http://latex.codecogs.com/gif.latex?%5Calpha%20%3D1.1%5Ctimes10%5E%7B-8%7DAU%5E%7B2%7D)    
由理论计算可以得出进动的速率等于Ca，其中C是一个常数。    
由能量守恒可得：    
![](http://latex.codecogs.com/gif.latex?-%5Cfrac%7BGM_%7BS%7DM_%7BM%7D%7D%7Br_%7B1%7D%7D&plus;%5Cfrac%7B1%7D%7B2%7DM_%7BM%7Dv_%7B1%7D%5E%7B2%7D%3D-%5Cfrac%7BGM_%7BS%7DM_%7BM%7D%7D%7Br_%7B2%7D%7D&plus;%5Cfrac%7B1%7D%7B2%7DM_%7BM%7Dv_%7B2%7D%5E%7B2%7D)    
以及:    
![](http://latex.codecogs.com/gif.latex?r_%7B1%7Dv_%7B1%7D%3Dbv_%7B2%7D)    
得到初速度:    
![](http://latex.codecogs.com/gif.latex?v_%7B1%7D%3D%5Csqrt%7B%5Cfrac%7BGM_%7BS%7D%281-e%29%7D%7Ba%281&plus;e%29%7D%7D)    
由水星半长轴及离心率得：    
![](http://latex.codecogs.com/gif.latex?v_%7B1%7D%3D8.2AU/yr)    
用欧勒法模拟水星的运动情况

##结果    
[](https://github.com/oohhooh/compuational_physics_N2014301020080/blob/master/images/%258IHWWB82YQH%7BU31%608C1.png)    
[](https://github.com/oohhooh/compuational_physics_N2014301020080/blob/master/images/%7BZ%25AY1B%24NUFV%5DD%5B~S5H9%24E9.png)    
得到的进动速率为43.67角秒每世纪。    
由于a值太小，直接模拟误差过大，又已知w与a为线性关系，故用较大的a值做线性模拟可以得到更精确的值。

##致谢
感谢李尚书同学的部分程序。

##Abstract
This article is about  the power spectra for waves on a string as a function of where the string vibration is observed ,x0.
##Main body
Wave equation：    
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20%5E%7B2%7Dy%7D%7B%5Cpartial%20t%5E%7B2%7D%7D%3Dc%5E%7B2%7D%5Cfrac%7B%5Cpartial%20%5E%7B2%7Dy%7D%7B%5Cpartial%20x%5E%7B2%7D%7D)    
when ![](http://latex.codecogs.com/gif.latex?r%3Dc%5Cfrac%7B%5CDelta%20t%7D%7B%5CDelta%20x%7D)    
![](http://latex.codecogs.com/gif.latex?y%28i%2Cn&plus;1%29%3D2%281-r%5E%7B2%7D%29y%28i%2Cn%29-y%28i%2Cn-1%29&plus;r%5E%7B2%7D%5By%28i&plus;1%2Cn%29&plus;y%28i-1%2Cn%29%5D)    
[code](https://github.com/oohhooh/compuational_physics_N2014301020080/blob/master/homework13.py)
##Result
If the string is excited at 50% of string (Gaussian profile), the power spectra at different nodes are 

![](https://github.com/guoxiaowhu/computationalphysics_N2013301020099/raw/master/problem6.13.png)

They are power spectra at 5%, 10%, 40%, 50% of string, respectively. 
The power spectrum at 5% of string doesn't have 3000Hz component and the power spectrum at 10% of string doesn't have 1500Hz, 3000Hz components.(Though they are obvious) 

when the string is excited at 55%, even multiple of fundamental frequency components will also appear in its power spectrum: 

![](https://github.com/guoxiaowhu/computationalphysics_N2013301020099/raw/master/problem6.13%20not%20center.png)

If the string is excited at 25%, there won't exist "peak" at 600Hz, 1200Hz, 1800Hz, 2400Hz, 3000Hz, etc. in its spectra. 

![](https://github.com/guoxiaowhu/computationalphysics_N2013301020099/raw/master/problem6.13%2025%25.png)
##Acknowledgement
Thanks Guo Xiao senior

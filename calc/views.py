from django.shortcuts import render, redirect , HttpResponse
import math 
import numpy as np
import statistics
from django.contrib import messages
# Create your views here.
def home(request):
    return redirect('/physics-calculator/')

#linear correlation
def linear(request):
    try:
        x = str(request.POST.get('x','10 20 30 40 50'))
        y = str(request.POST.get('y','1 2 3 4 5'))
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        if request.method == "POST" or request:
            x1 = x.split(" ")
            y1 = y.split(" ")
            xo = [int(i) for i in x1]
            yo = [int(i) for i in y1]
                   
            x2 = [(n**2) for n in xo]
            y2 = [(n**2) for n in yo]
            n = len(xo)
            xy = []
            for i,j in zip(xo,yo):
                xy.append(i*j)
            xsum = sum(xo)
            ysum = sum(yo)
            x2sum = sum(x2)
            y2sum = sum(y2)
            xysum = sum(xy)
            re = ((n*xysum)-(xsum*ysum))/((math.sqrt((n*x2sum)-(xsum**2)))*math.sqrt((n*y2sum)-(ysum**2)))
            k1 = False
            index_num = 0
            startpoint = 0
            endpoint = 0
            count = zerocount(re)
            if str(re) in 'e':
                r11 = str(re)
                index_num = r11.index('e')
                stratpoint = r11[:index_num]
                endpoint = r11[index_num+1:]
                k1 = True
            elif count>5:
                r11 = str("{:.2e}".format(re))
                index_num = r11.index('e')
                startpoint = r11[:index_num]
                endpoint = r11[index_num+1:]
                k1 = True
            context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'n':n,
                'x':x,
                'y':y,
                'xy':xy,
                'x2':x2,
                'y2':y2,
                'xsum':xsum,
                'ysum':ysum,
                'xysum':xysum,
                'x2sum':x2sum,
                'y2sum':y2sum,
                'result':re

            }
            return render(request,'calc/linear.html',context)
        return render(request,'calc/linear.html',{'x':x,'y':y})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'calc/linear.html')

#average calc
def average(request):
    try:
        x = str(request.POST.get('x','10 20 30 40 50'))
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        if request.method == "POST" or request:
            
            x1 = x.split(" ")
            xo = [int(i) for i in x1]
            xsum = sum(xo)  
            n = len(xo)
            re = xsum/n
            k1 = False
            index_num = 0
            startpoint = 0
            endpoint = 0
            count = zerocount(re)
            if str(re) in 'e':
                r11 = str(re)
                index_num = r11.index('e')
                stratpoint = r11[:index_num]
                endpoint = r11[index_num+1:]
                k1 = True
            elif count>5:
                r11 = str("{:.2e}".format(re))
                index_num = r11.index('e')
                startpoint = r11[:index_num]
                endpoint = r11[index_num+1:]
                k1 = True
            context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'n':n,
                'x':x,
                'xsum':xsum,
                'result':re,
            }
            return render(request,'calc/average.html',context)
        return render(request,'calc/average.html')
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'calc/average.html')

#mean deviation
def mean_deviation(request):
    try:
        x = str(request.POST.get('x','10 20 30 40 50'))
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        if request.method == "POST" or request:
            
            x1 = x.split(" ")
            x2 = ' '.join(x1)
            xo = [int(i) for i in x1]
            xsum = sum(xo)  
            n = len(xo)
            m = xsum/n
            xy = []
            for i in xo:
                xy.append(abs(m-i))
            xysum = sum(xy)
            re = xysum/n
            k1 = False
            index_num = 0
            startpoint = 0
            endpoint = 0
            count = zerocount(re)
            if str(re) in 'e':
                r11 = str(re)
                index_num = r11.index('e')
                stratpoint = r11[:index_num]
                endpoint = r11[index_num+1:]
                k1 = True
            elif count>5:
                r11 = str("{:.2e}".format(re))
                index_num = r11.index('e')
                startpoint = r11[:index_num]
                endpoint = r11[index_num+1:]
                k1 = True
            context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'n':n,
                'x':x,
                'xy':xy,
                'x1':x2,
                'xsum':xsum,
                'xysum':xysum,
                'result':re,
                'm':m

            }
            return render(request,'calc/mean_deviation.html',context)
        return render(request,'calc/mean_deviation.html')
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'calc/mean_deviation.html')

#pearson_correlation
def pearson_correlation(request):
    try:
        x = str(request.POST.get('x','10 20 30 40 50'))
        y = str(request.POST.get('y','1 2 3 4 5'))
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        if request.method == "POST" or request:
            
            x1 = x.split(" ")
            y1 = y.split(" ")
            xo = [int(i) for i in x1]
            yo = [int(i) for i in y1]
                   
            x2 = [(n**2) for n in xo]
            y2 = [(n**2) for n in yo]
            n = len(xo)
            xy = []
            for i,j in zip(xo,yo):
                xy.append(i*j)
            xsum = sum(xo)
            ysum = sum(yo)
            x2sum = sum(x2)
            y2sum = sum(y2)
            xysum = sum(xy)
            re = (n*(xysum)-(xsum)*(ysum))/ math.sqrt((n*x2sum - (xsum**2))* (n*y2sum-(ysum**2)))
            k1 = False
            index_num = 0
            startpoint = 0
            endpoint = 0
            count = zerocount(re)
            if str(re) in 'e':
                r11 = str(re)
                index_num = r11.index('e')
                stratpoint = r11[:index_num]
                endpoint = r11[index_num+1:]
                k1 = True
            elif count>5:
                r11 = str("{:.2e}".format(re))
                index_num = r11.index('e')
                startpoint = r11[:index_num]
                endpoint = r11[index_num+1:]
                k1 = True
            context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'n':n,
                'x':x,
                'y':y,
                'xy':xy,
                'x2':x2,
                'y2':y2,
                'xsum':xsum,
                'ysum':ysum,
                'xysum':xysum,
                'x2sum':x2sum,
                'y2sum':y2sum,
                'result':re

            }
            return render(request,'calc/pearson_correlation.html',context)
        return render(request,'calc/pearson_correlation.html')
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'calc/pearson_correlation.html')

#zscore calculator
def zscore(request):
    try:
        Given = request.POST.get('Given','form1')
        x = str(request.POST.get('x','10 20 30'))
        sd = float(request.POST.get('sd',5))
        m = float(request.POST.get('m',10))
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        if request.method == "POST" or request:
            if Given == 'form3' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                xsum = sum(xo)  
                n = len(xo)
                re = xsum/n
                
                context = {
                    'n':n,
                    'x':x,
                    'xsum':xsum,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/zscore.html',context)
            elif Given == 'form2' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                re = math.sqrt(ss/(n-1))

                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'ss':ss,
                    'n':n
                }
                return render(request,'calc/zscore.html',context)
            elif Given == 'form1' and x and sd and m :
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                n=len(xo)
                k =False
                if len(xo)>1:
                    
                    xm = sum(xo)/n
                    z=((xm-m)*math.sqrt(n))/sd
                    K=True
                else:
                    xm=xo[0]
                    z=(xm-m)/sd
                    k=False

                context = {
                    'k':k,
                    'x':x,
                    'Given':Given,
                    'm':m,
                    'sd':sd,
                    'n':n,
                    'xm':xm,
                    'z':round(z,4)
                }
                return render(request,'calc/zscore.html',context)

        return render(request,'calc/zscore.html',{'Given':Given})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'calc/zscore.html',{'Given':'form1'})


#descriptive statistics calc
def descriptive_statistics(request):
    try:
        Given = request.POST.get('Given','form1')
        x = request.POST.get('x','10 20 30 40 50')
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        if request.method == "POST" or request:
            if Given == "form1" and x:
                
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                s = xo
                s.sort()
                re = min(xo)
                print(re)
                context = {
                    's':s,
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == "form2" and x:
                
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                s = xo
                s.sort()
                re = max(xo)
                context = {
                    's':s,
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == "form3" and x:
                
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                m = max(xo)
                m1 = min(xo)
                re = m-m1
                context = {
                    'x':x,
                    'max':m,
                    'min':m1,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)
            elif Given == "form4" and x:
                
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                re = sum(xo)
                context = {
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == "form5" and x:
                
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                re = len(xo)
                context = {
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)


            elif Given == 'form6' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                xsum = sum(xo)  
                n = len(xo)
                re = xsum/n
                
                context = {
                    'n':n,
                    'x':x,
                    'xsum':xsum,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form7' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                n = len(xo)
                xo.sort()
                  
                if n % 2 == 0:
                    p = n // 2
                    median1 = xo[n//2]
                    median2 = xo[n//2 - 1]
                    median = (median1 + median2)/2
                    k = True
                else:
                    median = xo[n//2]
                    median1 = False
                    median2 = False
                    k = False
                    p = (n + 1)//2
                re = median
                
                context = {
                    'n':n,
                    'p':p,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'k':k,
                    'median1':median1,
                    'median2':median2
                }
                return render(request,'calc/descriptive_statistics.html',context)
            elif Given == 'form8' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                re = statistics.multimode(xo)
                if len(xo)==len(re):
                    re= "No Mode"

                context = {
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)
            elif Given == 'form9' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                re = math.sqrt(ss/(n-1))
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'ss':ss,
                    'n':n
                }
                return render(request,'calc/descriptive_statistics.html',context)
            elif Given == 'form10' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                re = (ss/(n-1))
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'ss':ss,
                    'n':n
                }
                return render(request,'calc/descriptive_statistics.html',context)
            elif Given == 'form11' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                re = (sd*100)/mean
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'ss':ss,
                    'n':n,
                    'sd':sd,
                    'mean':mean
                }
                return render(request,'calc/descriptive_statistics.html',context)
            elif Given == 'form12' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                xmin = min(xo)  
                xmax = max(xo) 
                re = (xmax+xmin)/2
                
                context = {
                    'x':x,
                    'xmin':xmin,
                    'xmax':xmax,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form13' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                q1 = np.quantile(xo, .25)
                q2 = np.quantile(xo, .50)
                q3 = np.quantile(xo, .80)
                print(q1,q2,q3)
                context = {
                    'x':x,
                    'q1':q1,
                    'q2':q2,
                    'q3':q3,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form14' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                q1 = np.quantile(xo,.25)
                q3 = np.quantile(xo,.80)
                re = q3-q1
                context = {
                    'x':x,
                    'q1':q1,
                    'result':re,
                    'q3':q3,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form15' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                q3 = np.quantile(xo, .80)
                q1 = np.quantile(xo, .25)
                iqr = q3 -q1
                
                uf = q3 + 1.5 * iqr
                lf = q1 - 1.5 * iqr
                
                
                context = {
                    'x':x,
                    'iqr':iqr,
                    'q1':q1,
                    'uf':uf,
                    'lf':lf,
                    'q3':q3,
                    'Given':Given
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form16' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                re = sum(l2)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'mean':mean
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form17' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                n = len(xo)
                for i in xo:
                    l.append(i-mean)
                ss =sum(l)
                re = ss/n
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                print(ss,l)
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'ss':ss,
                    'result':re,
                    'Given':Given,
                    'mean':mean,
                    'n':n
                }
                return render(request,'calc/descriptive_statistics.html',context)


            elif Given == 'form18' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                l= [(i**2) for i in xo]
                n = len(xo)
                ss =sum(l)
                re = math.sqrt(ss/n)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                print(ss,l)
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'ss':ss,
                    'result':re,
                    'Given':Given,
                    'n':n
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form19' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                re = sd / math.sqrt(n)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form20' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]            
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                l3= []
                for i in xo: 
                    l3.append(((i-mean)/sd)**3)
                s3 = sum(l3)
                z1 = (n / ((n - 1)*(n - 2)))
                re = z1*(s3)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n,
                    'z1':z1,
                    's3':s3
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form21' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]            
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                l3= []
                for i in xo: 
                    l3.append(((i-mean)/sd)**4)
                s3 = sum(l3)
                z1 = (n* (n +1)) / ((n - 1)* (n - 2) *(n - 3))
                re = z1*(s3)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n,
                    'z1':z1,
                    's3':s3
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form22' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]            
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                l3= []
                for i in xo: 
                    l3.append(((i-mean)/sd)**4)
                s3 = sum(l3)

                z1 = (n *(n +1)) / ((n - 1) *(n - 2) *(n - 3))
                z2 =  (3*((n-1)**2)) / ((n - 2) *(n - 3))

                re = (z1*s3)-z2
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n,
                    'z1':z1,
                    's3':s3,
                    'z2':z2
                }
                return render(request,'calc/descriptive_statistics.html',context)

            elif Given == 'form23' and x:
                
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]            
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                re = sd / mean
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n,
                    'mean':mean
                }
                return render(request,'calc/descriptive_statistics.html',context)


            return render(request,'calc/descriptive_statistics.html',{'Given':Given})
        else:
            return render(request,'calc/descriptive_statistics.html',{'Given':'form1'})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'calc/descriptive_statistics.html')

#odds probability calc
def oddsprob(request):
    try:
        Given = request.POST.get('Given','form1')
        a = float(request.POST.get('a',4))
        b = float(request.POST.get('b',40))
        if request.method == "POST" or request:
            
            if Given == 'form1' and a and b:
                re = a/(a+b)
                re1 = re*100
                context = {
                    'result':round(re,3),
                    'result1':round(re1,3),
                    'a':a,
                    'b':b,
                    'Given':Given
                }
                return render(request,'calc/oddsprob.html',context)
            elif Given == 'form2' and a and b:
                re = b/(a+b)
                re1 = re*100
                context = {
                    'result':round(re,3),
                    'result1':round(re1,3),
                    'a':a,
                    'b':b,
                    'Given':Given
                }
                return render(request,'calc/oddsprob.html',context)


        return render(request,'calc/oddsprob.html',{'Given':Given})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'calc/oddsprob.html',{'Given':'form1'})

#standard deviation calc
def standarddeviation(request):
    try:
        Given = request.POST.get('Given','form1')
        x = str(request.POST.get('x','10 20 30 40 50'))
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        if request.method == 'POST' or request:
            if Given == "form6" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                re = sum(xo)
                context = {
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/standarddeviation.html',context)

            elif Given == "form1" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                re = len(xo)
                context = {
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/standarddeviation.html',context)


            elif Given == 'form2' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                xsum = sum(xo)  
                n = len(xo)
                re = xsum/n
                
                context = {
                    'n':n,
                    'x':x,
                    'xsum':xsum,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/standarddeviation.html',context)

            elif Given == 'form3' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                re = math.sqrt(ss/(n-1))
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'ss':ss,
                    'n':n
                }
                return render(request,'calc/standarddeviation.html',context)
            elif Given == 'form4' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                re = (ss/(n-1))
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'ss':ss,
                    'n':n
                }
                return render(request,'calc/standarddeviation.html',context)

            elif Given == 'form5' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                re = sum(l2)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'mean':mean
                }
                return render(request,'calc/standarddeviation.html',context)

            

            return render(request,'calc/standarddeviation.html',{'Given':Given})
        else:
            return render(request,'calc/standarddeviation.html',{'Given':'form1'})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'calc/standarddeviation.html')

#statistics formulas 
def statisticsformulas(request):
    try:
        Given = request.POST.get('Given','form1')
        x = str(request.POST.get('x','10 20 30 40 50'))
        n = float(request.POST.get('n',10))
        sd = float(request.POST.get('sd',10))
        m = float(request.POST.get('m',20))

        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        if request.method == "POST" or request:
            if Given == "form1" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                s = xo
                s.sort()
                re = min(xo)
                print(re)
                context = {
                    's':s,
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == "form2" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                s = xo
                s.sort()
                re = max(xo)
                context = {
                    's':s,
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == "form3" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                m = max(xo)
                m1 = min(xo)
                re = m-m1
                context = {
                    'x':x,
                    'max':m,
                    'min':m1,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)
            elif Given == "form4" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                re = sum(xo)
                context = {
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == "form5" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                re = len(xo)
                context = {
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)


            elif Given == 'form6' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                xsum = sum(xo)  
                n = len(xo)
                re = xsum/n
                
                context = {
                    'n':n,
                    'x':x,
                    'xsum':xsum,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form7' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                n = len(xo)
                xo.sort()
                  
                if n % 2 == 0:
                    p = n // 2
                    median1 = xo[n//2]
                    median2 = xo[n//2 - 1]
                    median = (median1 + median2)/2
                    k = True
                else:
                    median = xo[n//2]
                    median1 = False
                    median2 = False
                    k = False
                    p = (n + 1)//2
                re = median
                
                context = {
                    'n':n,
                    'p':p,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'k':k,
                    'median1':median1,
                    'median2':median2
                }
                return render(request,'calc/statisticsformulas.html',context)
            elif Given == 'form8' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                re = statistics.multimode(xo)
                if len(xo)==len(re):
                    re= "No Mode"

                context = {
                    'x':x,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)
            elif Given == 'form9' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                re = math.sqrt(ss/(n-1))
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'ss':ss,
                    'n':n
                }
                return render(request,'calc/statisticsformulas.html',context)
            elif Given == 'form10' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                re = (ss/(n-1))
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'ss':ss,
                    'n':n
                }
                return render(request,'calc/statisticsformulas.html',context)
            elif Given == 'form11' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                re = (sd*100)/mean
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'ss':ss,
                    'n':n,
                    'sd':sd,
                    'mean':mean
                }
                return render(request,'calc/statisticsformulas.html',context)
            elif Given == 'form12' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                xmin = min(xo)  
                xmax = max(xo) 
                re = (xmax+xmin)/2
                
                context = {
                    'x':x,
                    'xmin':xmin,
                    'xmax':xmax,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form13' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                q1 = np.quantile(xo, .25)
                q2 = np.quantile(xo, .50)
                q3 = np.quantile(xo, .80)
                print(q1,q2,q3)
                context = {
                    'x':x,
                    'q1':q1,
                    'q2':q2,
                    'q3':q3,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form14' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                q1 = np.quantile(xo,.25)
                q3 = np.quantile(xo,.80)
                re = q3-q1
                context = {
                    'x':x,
                    'q1':q1,
                    'result':re,
                    'q3':q3,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form15' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                q3 = np.quantile(xo, .80)
                q1 = np.quantile(xo, .25)
                iqr = q3 -q1
                
                uf = q3 + 1.5 * iqr
                lf = q1 - 1.5 * iqr
                
                
                context = {
                    'x':x,
                    'iqr':iqr,
                    'q1':q1,
                    'uf':uf,
                    'lf':lf,
                    'q3':q3,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form16' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                re = sum(l2)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'result':re,
                    'Given':Given,
                    'mean':mean
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form17' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                n = len(xo)
                for i in xo:
                    l.append(i-mean)
                ss =sum(l)
                re = ss/n
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                print(ss,l)
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'ss':ss,
                    'result':re,
                    'Given':Given,
                    'mean':mean,
                    'n':n
                }
                return render(request,'calc/statisticsformulas.html',context)


            elif Given == 'form18' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                l= [(i**2) for i in xo]
                n = len(xo)
                ss =sum(l)
                re = math.sqrt(ss/n)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                print(ss,l)
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'ss':ss,
                    'result':re,
                    'Given':Given,
                    'n':n
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form19' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                re = sd / math.sqrt(n)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form20' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]            
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                l3= []
                for i in xo: 
                    l3.append(((i-mean)/sd)**3)
                s3 = sum(l3)
                z1 = (n / ((n - 1)*(n - 2)))
                re = z1*(s3)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n,
                    'z1':z1,
                    's3':s3
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form21' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]            
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                l3= []
                for i in xo: 
                    l3.append(((i-mean)/sd)**4)
                s3 = sum(l3)
                z1 = (n* (n +1)) / ((n - 1)* (n - 2) *(n - 3))
                re = z1*(s3)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n,
                    'z1':z1,
                    's3':s3
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form22' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]            
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                l3= []
                for i in xo: 
                    l3.append(((i-mean)/sd)**4)
                s3 = sum(l3)

                z1 = (n *(n +1)) / ((n - 1) *(n - 2) *(n - 3))
                z2 =  (3*((n-1)**2)) / ((n - 2) *(n - 3))

                re = (z1*s3)-z2
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n,
                    'z1':z1,
                    's3':s3,
                    'z2':z2
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form23' and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                mean = sum(xo)/len(xo)
                l=[]
                for i in xo:
                    l.append(i-mean)
                l2 = [(i**2) for i in l]            
                ss = sum(l2)
                n = len(xo)
                sd = math.sqrt(ss/(n-1))
                re = sd / mean
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'sd':sd,
                    'result':re,
                    'Given':Given,
                    'n':n,
                    'mean':mean
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == "form24" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                m=1
                n =len(xo)
                for i in xo:
                    m = m * i
                re = m**(1/n)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'n':n,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)
            elif Given == "form25" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                xt=0
                n=len(xo)
                for i in xo:
                    xt = xt+(1/i)
                re = n/xt
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    'x':x,
                    'n':n,
                    'xt':xt,
                    'result':re,
                    'Given':Given
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == "form26" and x:
                x1 = x.split(" ")
                
                xo = [int(i) for i in x1]
                d={}
                for i in xo:
                    if i not in d.keys():
                        d[i]=0
                    d[i]=d[i]+1
                context = {
                    'x':x,
                    'Given':Given,
                    'data':d
                }
                return render(request,'calc/statisticsformulas.html',context)

            
            elif Given == 'form27' and n and x:
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                xo.sort()
                             
                ni = xo.index(n)
                l = len(xo)
                p = (ni/l)*100

                context = {
                    'x':x,
                    'l':l,
                    'p':p,
                    'ni':ni,
                    'Given':Given,
                    'n':n
                }
                return render(request,'calc/statisticsformulas.html',context)

            elif Given == 'form28' and x and sd and m :
                x1 = x.split(" ")
                x2 = ' '.join(x1)
                xo = [int(i) for i in x1]
                n=len(xo)
                k =False
                if len(xo)>1:
                    
                    xm = sum(xo)/n
                    z=((xm-m)*math.sqrt(n))/sd
                    K=True
                else:
                    xm=xo[0]
                    z=(xm-m)/sd
                    k=False

                context = {
                    'k':k,
                    'x':x,
                    'Given':Given,
                    'm':m,
                    'sd':sd,
                    'n':n,
                    'xm':xm,
                    'z':round(z,4)
                }
                return render(request,'calc/statisticsformulas.html',context)

            return render(request,'calc/statisticsformulas.html',{'Given':Given})
        else:
            return render(request,'calc/statisticsformulas.html',{'Given':'form1'})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'calc/statisticsformulas.html')


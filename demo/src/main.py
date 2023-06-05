import webview
from math import sqrt
class Api:
    def calculate(self,a,b,c):
        try:
            a=float(a)
            b=float(b)
            c=float(c)
            delta=b*b-4*a*c
            if delta<0:
                return "There is no real solution for this equation."
            elif delta==0:
                result=-(b/(2*a))
                return "x=%.2f"%result
            else:
                result1=(-b+sqrt(delta)/(2*a))
                result2=(-b-sqrt(delta)/(2*a))
                return "x<sub>1</sub>=%.2f, x<sub>2</sub>=%.2f"%(result1,result2)
        except:
            return 'Invaild Input.'
api=Api()
window=webview.create_window(
    title='Solve Equation',
    url='../static/index.html',
    width=800,
    height=480,
    resizable=False,
    text_select=False,
    confirm_close=True,
    js_api=api
)
webview.start(debug=False)

# -*- coding: utf-8 -*-
"""Personal Financial Simulator with ODE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/OlegZero13/Data-Science-Algorithm-Gallery/blob/master/Personal_Financial_Simulator_with_ODE.ipynb

# Personal Financial Simulator
Author: [Oleg Żero](https://zerowithdot.com)

Please, feel free to play around!

## Prepare the environment
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
from scipy.integrate import odeint

# %matplotlib inline

import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.offline import iplot

import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 


cf.go_offline()

init_notebook_mode(connected=False)

def configure_plotly_browser_state():
  import IPython
  display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({
            paths: {
              base: '/static/base',
              plotly: 'https://cdn.plot.ly/plotly-1.5.1.min.js?noext',
            },
          });
        </script>
  '''))

"""## Simulator

For a non-investor:
$$
\frac{d}{dt} x(t) = \Delta - x\ln(1 + \xi)
$$
where
* $\xi$ is an `inflation rate`.
* $\Delta = a(t) - s(t) - T(a)$ is the amount that is left each year.
* $a(t) = \alpha_0 + \alpha_1 t$ is the `income`, where $\alpha_1$ represents a pay rise.
* $s(t) = \sigma_0 + \sigma_1 t$ is the yearly spending.
* $T(a)$ represents the tax paid (it can be progressive or linear).

The for an investor, we have two variables $x_1$, $x_2$ that represent
the baseline budget and the investment bucket, respectively:
$$
\left\{\begin{matrix}
\frac{d}{dt} x_1(t) &= \Delta (1 - \beta) - x_1\ln(1 + \xi) \\
\frac{d}{dt} x_2(t) &= \beta \Delta + x_2\ln(1 + R) - x_2\ln(1 + \xi)
\end{matrix}\right.
$$

Here the new terms have the following meaning:
* $R$ is the (average) interest rate upon investment
* $\beta$ is the fraction of the baseline budget $x_1$ we transfer to the investment bucket $x_2$.

The whole idea behind this simulation is to numerically integrate the equations
$$
\int_0^t \frac{d}{dt}x_i(t) dt = x_i(t)
$$
to get $x_1(t)$ and $x_2(t)$.

BTW, the reason for using the logarithm here is purely the convenience.
The formula for _compound interest_ is (assuming yearly capitalization):
$$
x(t) = x_0(1 + R)^t
$$
Taking the derivative, we have:
$$
\frac{d}{dt}x(t) = x_0 e^{\ln(1 + R) t} = x_0\ln(1 + R) e^t
$$

**Final note:**
Here, we introduce two important parameters: `starting_age` and `retirement_age`.
Anything life before the `starting_age` is assumed to be dependent on the parents, etc.
Consequently, $a(t), s(t)$ are set to zero.
Once the `retirement_age` is exceeded, it is assumed that the investor
would withdraw all the money from the investment bucket and use them for consumption.

"""

class Life:
    def __init__(self):
        self.starting_age = 25
        self.retirement_age = 67
        self.income = 1
        self.pay_rise = 0.0
        self.tax_type = 'None'
        self.pension = 0
        self.costs = 0.7
        self.life_inflation = 0.0
        self.investment_fraction = 0.1
        self.interest_rate_proc = 10
        self.inflation_proc = 2.5

    def earn(self, t):
        if t < self.starting_age:
            return 0
        elif self.starting_age <= t < self.retirement_age:
            return 12 * (self.income + self.pay_rise * (t - self.starting_age))
        else:
            return 12 * self.pension

    def spend(self, t):
        if (t < self.starting_age):
            return 0
        return 12 * (self.costs + self.life_inflation * (t - self.starting_age))

    def pay_taxes(self, t):
        if (t < self.starting_age) or (t > self.retirement_age):
            return 0
        earning = self.earn(t)
        if self.tax_type == 'UoP':
            if earning < 85528.0:
                return 0.17 * earning
            else:
                return 13983.74 - 0.32 * (earning - 85528)
        elif self.tax_type == 'B2B':
            return 0.19 * earning
        else:
            return 0
        

def live_without_investing(x, t, you):
    balance = you.earn(t) - you.spend(t) - you.pay_taxes(t)
    return balance - np.log(1 + 0.01*you.inflation_proc) * x


def live_with_investing(x, t, you):
    balance = you.earn(t) - you.spend(t) - you.pay_taxes(t)
    if t < you.retirement_age:
        x0 = balance * (1 - you.investment_fraction)
        x1 = np.log(1 + 0.01*you.interest_rate_proc) * x[1] + you.investment_fraction * balance
        
        x0 = x0 - np.log(1 + 0.01*you.inflation_proc) * x[0]
        x1 = x1 - np.log(1 + 0.01*you.inflation_proc) * x[1]
    else:
        x0 = balance
        x0 = x0 - np.log(1 + 0.01*you.inflation_proc) * x[0]
        x1 = 0
    return [x0, x1]

def simulate(you):
    t0 = np.linspace(0, you.starting_age - 1, num=you.starting_age)
    t1 = np.linspace(you.starting_age, you.retirement_age - 1, num=(you.retirement_age - you.starting_age))
    t2 = np.linspace(you.retirement_age, 100, num=(100 - you.retirement_age + 1))

    x1_0 = np.zeros((t0.shape[0], 1))
    x1_1 = odeint(live_without_investing, 0, t1, args=(you,))
    x1_2 = odeint(live_without_investing, x1_1[-1], t2, args=(you,))

    x2_0 = np.zeros((t0.shape[0], 2))
    x2_1 = odeint(live_with_investing, [0, 0], t1, args=(you,))
#    x2_2 = odeint(live_with_investing, np.flip(x2_1[-1]), t2, args=(you,))
    x2_2 = odeint(live_with_investing, [x2_1[-1].sum(), 0], t2, args=(you,))

    df0 = pd.DataFrame({'time': t0, 'wallet (non-investor)': x1_0[:, 0], 'wallet (investor)': x2_0[:, 0], 'investment bucket (investor)': x2_0[:, 1]})
    df1 = pd.DataFrame({'time': t1, 'wallet (non-investor)': x1_1[:, 0], 'wallet (investor)': x2_1[:, 0], 'investment bucket (investor)': x2_1[:, 1]})
    df2 = pd.DataFrame({'time': t2, 'wallet (non-investor)': x1_2[:, 0], 'wallet (investor)': x2_2[:, 0], 'investment bucket (investor)': x2_2[:, 1]})
    return pd.concat([df0, df1, df2])

"""## Play with the results"""

configure_plotly_browser_state()

you = Life()

#@title Input
#@markdown Input parameters:
you.starting_age        = 18  #@param {type: "slider", min: 1, max: 99}
you.retirement_age      = 67  #@param {type: "slider", min: 1, max: 99}
you.income              = 1000  #@param {type: "slider", min: 0, max: 35000, step: 500}
you.pay_rise            = 100  #@param {type: "slider", min: 0, max: 1000, step: 10}
you.tax_type            = "B2B" #@param ['B2B', 'UoP', 'None']
you.pension             = 300  #@param {type: "slider", min: 0, max: 10000, step: 100}
you.costs               = 650  #@param {type: "slider", min: 0, max: 35000, step: 500}
you.life_inflation      = 50  #@param {type: "slider", min: 0, max: 1000, step: 10}
you.investment_fraction = 0.8    #@param {type: "slider", min: 0, max: 1, step: 0.1}
you.interest_rate_proc  = 3.3    #@param {type: "slider", min: 0, max: 20, step: 0.1}
you.inflation_proc      = 3 #@param {type:"slider", min: -0.5, max: 10, step:0.1}
#@markdown ---

df = simulate(you)

df.iplot(kind='line',x='time',y=[
    'wallet (non-investor)',
    'wallet (investor)', 
    'investment bucket (investor)'],
    color=['gray', 'white', 'gold'], 
theme='solar', mode='markers', xTitle='Time')

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Solutions to Problem Set 1
#
#
# *Stats 507, Fall 2021*
#
# Shihao Wu, PhD student

# ## Question 0 - Markdown warmup
#
# ____
#
# This is *question 0* for 
# [problem set 1](https://jbhender.github.io/Stats507/F21/ps1.html)
# of [Stats 507](https://jbhender.github.io/Stats507/F21/).
#
# > Question 0 is about Markdown
#
# The next question is about the **Fibonnaci sequence**, $F_n = F_{n-2}+F_{n-1}$. In part **a** we will define a Python function <code>fib_rec()</code> .
#
# Below is a ...
#
# ### Level 3 Header
#
# Next, we can make a bulleted list:
#
# * Item 1
#    - detail 1
#    - detail 2
# * Item 2
#
# Finally, we can make an enumerated list:
#
# <ol style="list-style-type: lower-alpha">
# <li>Item 1<br />
# </li>
# <li>Item 2<br />
# </li>
# <li>Item 3</li>
# </ol>
#
# _____
#
#
# The "raw" markdown is as follows:
# ```
#
# ____
#
# This is *question 0* for 
# [problem set 1](https://jbhender.github.io/Stats507/F21/ps1.html)
# of [Stats 507](https://jbhender.github.io/Stats507/F21/).
#
# > Question 0 is about Markdown
#
# The next question is about the **Fibonnaci sequence**, $F_n = F_{n-2}+F_{n-1}$. In part **a** we will define a Python function <code>fib_rec()</code> .
#
# Below is a ...
#
# ### Level 3 Header
#
# Next, we can make a bulleted list:
#
# * Item 1
#    - detail 1
#    - detail 2
# * Item 2
#
# Finally, we can make an enumerated list:
#
# <ol style="list-style-type: lower-alpha">
# <li>Item 1<br />
# </li>
# <li>Item 2<br />
# </li>
# <li>Item 3</li>
# </ol>
# ____
#
# ```
#

# ## Question 1 - Fibonaci Sequence
# **a.** Write a recursive function <code>fib_rec()</code> that takes a single input <code>n</code> and returns the value of $F_n$.

# +
def fib_rec(n):
    """
    The function returns the nth number in Fibonnaci sequence
    
    Parameters
    ----------
    n : the index in Fibonacci sequence
    
    Returns
    ----------
    The Fibonacci number indexed n
    """
    if n<=1:
        return n
    else:
        return(fib_rec(n-1)+fib_rec(n-2))

print(fib_rec(7))
print(fib_rec(11))
print(fib_rec(13))


# -

# **b.** Write a function <code>fib_for()</code> with the same signature that computes $F_n$ by summation using a <code>for</code> loop.

# +
def fib_for(n):
    """
    The function returns the nth number in Fibonnaci sequence
    
    Parameters
    ----------
    n : the index in Fibonacci sequence
    
    Returns
    ----------
    The Fibonacci number indexed n
    """
    if n<=1:
        return(n)
    else:
        a = 0
        b = 1
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return(c)
    
print(fib_for(7))
print(fib_for(11))
print(fib_for(13))


# -

# **c.** Write a function <code>fib_whl()</code> with the same signature that computes $F_n$ by summation using a <code>while</code> loop.

# +
def fib_whl(n):
    """
    The function returns the nth number in Fibonnaci sequence
    
    Parameters
    ----------
    n : the index in Fibonacci sequence
    
    Returns
    ----------
    The Fibonacci number indexed n
    """
    if n<=1:
        return(n)
    else:
        a = 0
        b = 1
        i = 1
        while i < n:
            c = a + b
            a = b
            b = c
            i = i+1
        return(c)

print(fib_whl(7))
print(fib_whl(11))
print(fib_whl(13))


# -

# **d.** Write a function <code>fib_rnd()</code> with the same signature that computes $F_n$ using the rounding method described on the Wikipedia page linked.

# +
def fib_rnd(n):
    """
    The function returns the nth number in Fibonnaci sequence
    
    Parameters
    ----------
    n : the index in Fibonacci sequence
    
    Returns
    ----------
    The Fibonacci number indexed n
    """
    if n<=1:
        return n
    else:
        phi = (1+(5 ** 0.5))/2
        return(round(phi** n/(5 ** 0.5)+1/2))

print(fib_rnd(7))
print(fib_rnd(11))
print(fib_rnd(13))


# -

# **e.** Write a function <code>fib_flr()</code> with the same signature that computes $Fn$ using the truncation method described on the Wikipedia page linked above.

# +
def fib_flr(n):
    """
    The function returns the nth number in Fibonnaci sequence
    
    Parameters
    ----------
    n : the index in Fibonacci sequence
    
    Returns
    ----------
    The Fibonacci number indexed n
    """
    if n<=1:
        return n
    else:
        phi = (1+(5 ** 0.5))/2
        return(int(phi** n/(5 ** 0.5)+1/2))

print(fib_flr(7))
print(fib_flr(11))
print(fib_flr(13))
# -

# **f.** For a sequence of increasingly large values of <code>n</code> compare the median computation time of each of the functions above. Present your results in a nicely formatted table. (Point estimates are sufficient).

# +
import pandas as pd
import numpy as np
import datetime
from IPython.core.display import display, HTML

n = range(1,41)
fib_rec_time = []
fib_for_time = []
fib_whl_time = []
fib_rnd_time = []
fib_flr_time = []

for i in range(len(n)):
    fib_rec_time_int = []
    fib_for_time_int = []
    fib_whl_time_int = []
    fib_rnd_time_int = []
    fib_flr_time_int = []
    for j in range(10):
        start = datetime.datetime.now()
        a = fib_rec(n[i])
        fib_rec_time_int.append(datetime.datetime.now()-start)
        start = datetime.datetime.now()
        a = fib_for(n[i])
        fib_for_time_int.append(datetime.datetime.now()-start)
        start = datetime.datetime.now()
        a = fib_whl(n[i])
        fib_whl_time_int.append(datetime.datetime.now()-start)
        start = datetime.datetime.now()
        a = fib_rnd(n[i])
        fib_rnd_time_int.append(datetime.datetime.now()-start)
        start = datetime.datetime.now()
        a = fib_flr(n[i])
        fib_flr_time_int.append(datetime.datetime.now()-start)
    fib_rec_time.append(str(np.median(fib_rec_time_int)))
    fib_for_time.append(str(np.median(fib_for_time_int)))
    fib_whl_time.append(str(np.median(fib_whl_time_int)))
    fib_rnd_time.append(str(np.median(fib_rnd_time_int)))
    fib_flr_time.append(str(np.median(fib_flr_time_int)))

    
tab = pd.DataFrame(
    {
     "n": n,
     "fib_rec() time": fib_rec_time,
     "fib_for() time": fib_for_time,
     "fib_whl() time": fib_whl_time,
     "fib_rnd() time": fib_rnd_time,
     "fib_flr() time": fib_flr_time
     }
    )


display(HTML(tab.to_html(index=False)))


# -

# ## Question 2 - Pascal's Triangle
# **a.** Write a function to compute a specified row of Pascal’s triangle. An arbitrary row of Pascal’s triangle can be computed efficiently by starting with $\binom{n}{0}=1$ and then applying the following recurrence relation among binomial coefficients, 
#
# $$
#    \binom{n}{k}=\binom{n}{k-1}\times\frac{n+1-k}{k}.
# $$

# +
def pascal_row(n):
    """
    The function returns the nth row of Pascal's triangle
    
    Parameters
    ----------
    n : the index of row in Pascal's triangle
    
    Returns
    ----------
    the nth row of Pascal's triangle
    """
    row = [1]
    if n==1:
        return row
    for i in range(n-1):
        row.append(int(row[i] * ((n-1)-i)/(i+1)))
    return row

print(pascal_row(6))


# -

# **b.** Write a function for printing the first $n$ rows of Pascal’s triangle using the conventional spacing with the numbers in each row staggered relative to adjacent rows. Use your function to display a minimum of 10 rows in your notebook.

# +
def pascal(n):
    """
    The function prints the first n rows of Pascal's triangle
    
    Parameters
    ----------
    n : the number of rows in Pascal's triangle to be shown
    
    Returns
    ----------
    no returns but print the first 
    n rows of Pascal's triangle
    """
    largest_row = pascal_row(n)
    largest_element = largest_row[len(largest_row) // 2]
    element_width = len(str(largest_element))
    def format_row(row):
        return " ".join([str(element).center(element_width) 
                        for element in row])
    triangle_width = len(format_row(largest_row))
    for i in range(1,n+1):
        print(format_row(pascal_row(i)).center(triangle_width))
        

pascal(12)
# -

# ## Question 3 - Statistics 101
# **a.** The standard point and interval estimate for the populaiton mean based on Normal theory takes the form $\bar{x}\pm z\times \text{se}(x)$ where $\bar{x}$ is the mean, se$(x)$ is the standard error, and $z$ is a Gaussian multiplier that depends on the desired confidence level. Write a function to return a point and interval estimate for the mean based on these statistics.

# +
import numpy as np
import scipy.stats


def CI_standard(data, level, fmat = 'string'):
    """
    The function returns a CI for given data
    
    Parameters
    ----------
    data : the data input as an array
    level : confidence level of the CI
    fmat : format of the output
    
    Returns
    ----------
    If fmat == "string", returns a string showing CI
    If fmat == "None", returns a dictionary with all information
    """
    try:
        data = np.array(data)
    except:
        print("Data should be a 1d Numpy array ")
    est = np.mean(data)
    se = np.std(data, ddof=1) / np.sqrt(np.size(data))
    z = scipy.stats.norm.ppf(1-(1-level/100)/2)
    lwr = est - z*se
    upr = est + z*se
    if fmat == None:
        return {"est":est, "lwr":lwr, "upr":upr, "level":level }
    if fmat == "string":
        return f"{est}[{level}%CI:({lwr},{upr})]"

print(CI_standard(np.random.normal(0,1,10000),95))
print(CI_standard(np.random.normal(0,1,10000),95,fmat = None))
# -

# **b.** There are a number of methods for computing a confidence interval for a population proportion arising from a Binomial experiment consisting of $n$ independent and identically distributed (iid) Bernoulli trials. Let $x$ be the number of successes in these trials. In this question you will write a function to return point and interval estimates based on several of these methods. Your function should have a parameter method that controls the <code>method</code> used. Include functionality for each of the following methods.
#
#    ( i ) The standard point and interval estimates for a population parameter based on the Normal approximation to the Binomial distribution takes the form $\hat{p}\pm z\times \sqrt{\frac{\hat{p}(1−\hat{p})}{n}}$ with $\hat{p}$  the sample proportion and $z$ as in part a. The approximation is conventionally considered adequate when $n\hat{p}\wedge n(1−\hat{p})>12$. When this method is selected, your function should raise an informative warning if this condition is not satisfied.

# +
import warnings
def CI1(data, level, fmat = 'string'):
    """
    The function returns a CI for given data
    
    Parameters
    ----------
    data : the data input as an array
    level : confidence level of the CI
    fmat : format of the output
    
    Returns
    ----------
    If fmat == "string", returns a string showing CI
    If fmat == "None", returns a dictionary with all information
    """
    try:
        data = np.array(data)
    except:
        print("Data should be a 1d Numpy array ")
    x = sum(data)
    n = np.size(data)
    phat = x/n
    se = np.sqrt(phat*(1-phat)/n)
    z = scipy.stats.norm.ppf(1-(1-level/100)/2)
    lwr = phat - z*se
    upr = phat + z*se
    if min(n*phat,n*(1-phat))<= 12:
        warnings.warn("The condition for adequacy is not satisfied.")
    if fmat == None:
        return {"est":phat, "lwr":lwr, "upr":upr, "level":level }
    if fmat == "string":
        return f"{phat}[{level}%CI:({lwr},{upr})]"

print(CI1(np.random.choice([0,1],10000,replace = True,
                                   p = [0.5,0.5]),95))
print(CI1(np.random.choice([0,1],10000,replace = True,
                                   p = [0.5,0.5]),95,fmat = None))
print(CI1(np.random.choice([0,1],2,replace = True,
                                   p = [0.5,0.5]),95))
# -

# ( ii ) The Clopper-Pearson interval for a population proportion can be expressed using quantiles from Beta distributions. Specifically, for a sample of size $n$ with $x$ successes and $\alpha$ 1 minus the confidence level the interval is,
# $$
#    (\hat{\theta}_L,\hat{\theta}_U) = \Bigl(B\bigl(\frac{\alpha}{2},x,n-x+1\bigr),B\bigl(1-\frac{\alpha}{2},x+1,n-x \bigr) \Bigr).
# $$

# +
from scipy.stats import beta
def CI2(data, level, fmat = 'string'):
    """
    The function returns a CI for given data
    
    Parameters
    ----------
    data : the data input as an array
    level : confidence level of the CI
    fmat : format of the output
    
    Returns
    ----------
    If fmat == "string", returns a string showing CI
    If fmat == "None", returns a dictionary with all information
    """
    try:
        data = np.array(data)
    except:
        print("Data should be a 1d Numpy array ")
    x = sum(data)
    n = np.size(data)
    phat = x/n
    alpha = 1-level/100
    lwr = beta.ppf(alpha/2, x, n-x+1)
    upr = beta.ppf(1-alpha/2, x+1, n-x)
    if fmat == None:
        return {"est":phat, "lwr":lwr, "upr":upr, "level":level }
    if fmat == "string":
        return f"{phat}[{level}%CI:({lwr},{upr})]"

print(CI2(np.random.choice([0,1],10000,replace = True,
                                   p = [0.5,0.5]),95))
print(CI2(np.random.choice([0,1],10000,replace = True,
                                   p = [0.5,0.5]),95,fmat = None))


# -

# ( iii ) The Jeffrey’s interval is a Bayesian credible interval with good frequentist properties. It is similar to the Clopper-Pearson interval in that it utilizes Beta quantiles, but is based on a so-called Jeffrey’s prior of $B(p,0.5,0.5)$. Specifically, the Jeffrey’s interval is $ (0\vee B(α/2,x+0.5,n−x+0.5),B(1−α/2,x+0.5,n−x+0.5)\wedge 1)$. (Use the sample proportion as the point estimate).

# +
def CI3(data, level, fmat = 'string'):
    """
    The function returns a CI for given data
    
    Parameters
    ----------
    data : the data input as an array
    level : confidence level of the CI
    fmat : format of the output
    
    Returns
    ----------
    If fmat == "string", returns a string showing CI
    If fmat == "None", returns a dictionary with all information
    """
    try:
        data = np.array(data)
    except:
        print("Data should be a 1d Numpy array ")
    x = sum(data)
    n = np.size(data)
    phat = x/n
    alpha = 1-level/100
    lwr = max(0,beta.ppf(alpha/2, x+0.5, n-x+0.5))
    upr = min(beta.ppf(1-alpha/2, x+0.5, n-x+0.5),1)
    if fmat == None:
        return {"est":phat, "lwr":lwr, "upr":upr, "level":level }
    if fmat == "string":
        return f"{phat}[{level}%CI:({lwr},{upr})]"

print(CI3(np.random.choice([0,1],10000,replace = True,
                                   p = [0.5,0.5]),95))
print(CI3(np.random.choice([0,1],10000,replace = True,
                                   p = [0.5,0.5]),95,fmat = None))


# -

# ( iv ) Finally, the Agresti-Coull interval arises from a notion “add 2 failures and 2 successes” as a means of regularization. More specifically, define $\tilde{n} =n+z^2$ and $\tilde{p} = (x+z^2/2)/\tilde{n}$. The Agresti-Coull interval is Normal approximation interval using $\tilde{p}$ in place of $\hat{p}$.

# +
def CI4(data, level, fmat = 'string'):
    """
    The function returns a CI for given data
    
    Parameters
    ----------
    data : the data input as an array
    level : confidence level of the CI
    fmat : format of the output
    
    Returns
    ----------
    If fmat == "string", returns a string showing CI
    If fmat == "None", returns a dictionary with all information
    """
    try:
        data = np.array(data)
    except:
        print("Data should be a 1d Numpy array ")
    x = sum(data)
    n = np.size(data)
    z = scipy.stats.norm.ppf(1-(1-level/100)/2)
    n_t = n + z**2
    p_t = (x + z**2/2 ) / n_t
    se = np.sqrt(p_t*(1-p_t)/n)
    lwr = p_t - z*se
    upr = p_t + z*se
    if min(n*p_t,n*(1-p_t))<= 12:
        warnings.warn("The condition for adequacy is not satisfied.")
    if fmat == None:
        return {"est":p_t, "lwr":lwr, "upr":upr, "level":level }
    if fmat == "string":
        return f"{p_t}[{level}%CI:({lwr},{upr})]"

print(CI4(np.random.choice([0,1],10000,replace = True,
                                   p = [0.5,0.5]),95))
print(CI4(np.random.choice([0,1],10000,replace = True,
                                   p = [0.5,0.5]),95,fmat = None))
# -

# **c.** Create a 1d Numpy array with 42 ones and 48 zeros. Construct a nicely formatted table comparing 90, 95, and 99% confidence intervals using each of the methods above (including part a) on this data. Choose the number of decimals to display carefully to emphasize differences. For each confidence level, which method produces the interval with the smallest width?

# +
import pandas as pd
from IPython.core.display import display, HTML
data = np.concatenate([[1]*42,[0]*48])
levels = [90,95,99]
levels_str = ["90%","95%","99%"]
CIa = []
CIb1 = []
CIb2 = []
CIb3 = []
CIb4 = []
for i in range(len(levels)):
    asol = CI_standard(data, levels[i],fmat = None)
    est = round(asol['est'],3)
    level = round(asol['level'],3)
    lwr = round(asol['lwr'],3)
    upr = round(asol['upr'],3)
    length = round(upr-lwr,3)
    CIa.append(f"{est}[{level}%CI:({lwr},{upr})] length: {length}")
    b1sol = CI1(data, levels[i],fmat = None)
    est = round(b1sol['est'],3)
    level = round(b1sol['level'],3)
    lwr = round(b1sol['lwr'],3)
    upr = round(b1sol['upr'],3)
    length = round(upr-lwr,3)
    CIb1.append(f"{est}[{level}%CI:({lwr},{upr})] length: {length}")
    b2sol = CI2(data, levels[i],fmat = None)
    est = round(b2sol['est'],3)
    level = round(b2sol['level'],3)
    lwr = round(b2sol['lwr'],3)
    upr = round(b2sol['upr'],3)
    length = round(upr-lwr,3)
    CIb2.append(f"{est}[{level}%CI:({lwr},{upr})] length: {length}")
    b3sol = CI3(data, levels[i],fmat = None)
    est = round(b3sol['est'],3)
    level = round(b3sol['level'],3)
    lwr = round(b3sol['lwr'],3)
    upr = round(b3sol['upr'],3)
    length = round(upr-lwr,3)
    CIb3.append(f"{est}[{level}%CI:({lwr},{upr})] length: {length}")
    b4sol = CI4(data, levels[i],fmat = None)
    est = round(b4sol['est'],3)
    level = round(b4sol['level'],3)
    lwr = round(b4sol['lwr'],3)
    upr = round(b4sol['upr'],3)
    length = round(upr-lwr,3)
    CIb4.append(f"{est}[{level}%CI:({lwr},{upr})] length: {length}")
    

tab2 = pd.DataFrame(
    {
     "Confidence levels": levels_str,
     "CI : a": CIa,
     "CI : b i.": CIb1,
     "CI : b ii.": CIb2,
     "CI : b iii.": CIb3,
     "CI : b iv.": CIb4
     }
    )


display(HTML(tab2.to_html(index=False)))
# -

# For $90\%$ level, the method in b iii. produces the interval with the smallest width. For $95\%$ level, the method in b iii. produces the interval with the smallest width. For $99\%$ level, the method in b iii. still produces the interval with the smallest width.

# Fitting a model to data

Try to answer the following questions as precisely as possible: 

* What is "data"?

* What is a "model"?

* What does "fit" mean?

  

What ingredients do we need to fit a model to data?

1. a model
2. some data
3. an **objective function**
4. an algorithm to find the minimum(/maximum) of a function (an **optimizer**)



In each step below, before you start writing any code, discuss and decide the following with your partner:

* What arguments will this function need?
* What will this function return?



## 1. Model

Write a function representing the model.  

```python
def model(...):  # fill in necessary arguments
  return y
```



## 2. Data

Write a function that generates some fake data according to the above model, as well as uncertainties.  You should be calling the function you wrote above somewhere in this function.

Generate some random x-values, and add a different normal-distributed random noise to each y-value.

```python
def generate_data(...):  # fill in necessary arguments
  return x, y, y_unc
```

Make a plot of this data with uncertainties.

## 3. Objective function

Fill in the code for the objective function.  What arguments will it need?  What will it return?

```python
def objective(...):  # fill in necessary arguments
  return ...
```

**Pause Point**: let's vizualize together what this looks like.

## 4. Optimize

Read about and learn how to use [scipy.optimize.minimize](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html).  Figure out what you need to pass it.  Minimize your objective function on the simulated data.  Does your answer make sense?



## 5. Put it all together

Do this all in one function!  Fill in the guts to the following code, save it in a `.py` file in your scratchwork repository, and import/use it from a notebook.

```python
def find_best_pars(x, y, y_unc, model_func, **kwargs):
  """Find parameters of model_func that best fit the (x, y, y_unc) data

	Parameters
	----------
	x, y, y_unc : `ndarray`
		1-d arrays of the same length, representing x-data (without uncertainty),
		y-data, and the uncertainties on y.
		
	model_func : callable
		A callable function that can be called as model_func(x, pars),
		where pars is a list of parameters, and returns "theoretically perfect"
		y-values.
	"""  
  return best_pars
  
```



If you are more experienced with python, and/or you finish the above, finish the following: 

```python
class Data(object):
  """Object representing observed data
  """

  
class Model(object):
  """Object representing theoretical model
  """
  

def find_best_pars(data, model, **kwargs):
	"""Computes best-fit parameters for theoretical model, given observed data
	
	Usage as follows:
	 
	>>> data = Data(...)
	>>> model = Model(...)
	>>> best_pars = find_best_pars(data, model)
	
	Parameters
	----------
	data : `Data` object
	model : `Model` object
	"""
  return best_pars
```
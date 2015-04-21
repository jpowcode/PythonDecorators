from functools import wraps
from datetime import datetime as dt
import logging
                    
logging.basicConfig(format='%(message)s',level=logging.NOTSET)

def timeit(interceptedFunction):
	"""A decorator that intercepts a function and it's arguments *args 
	and **kwargs times the duration of thefunction and then returns it 
	and logs it to the terminal """
	
	@wraps(interceptedFunction)
	def timer(*args, **kwargs):
		functionName = interceptedFunction.func_name
		start = dt.now()
		actualResult = interceptedFunction(*args, **kwargs)
		stop = dt.now()
		executionTime = stop - start
		logging.debug('Function: [{fnc}] => Took [{timed}]'
					.format(fnc=functionName, timed=executionTime))
		
		return actualResult
	
	return timer
  
def logit(interceptedFunction):
	"""A decorator that intercepts a function and it's arguments *args 
	and **kwargs and logs what the function returns to the terminal
	as well as the input to the function"""
	
	@wraps(interceptedFunction)
	def logger(*args, **kwargs):
		functionName = interceptedFunction.func_name
		functionArguments = []
		
		if kwargs is not None:
			for arg in args:
				functionArguments.append(arg)
            
		actualResult = interceptedFunction(*args, **kwargs)
		logging.debug('Function: [{fnc}] => Returns [{returned}] with input {inp}'
					.format(fnc=functionName, returned=actualResult, inp=functionArguments))
		return actualResult
	
	return logger
	
def countit(interceptedFunction):
	"""A decorator that intercepts a function and it's arguments *args 
	and **kwargs and logs the number of times the function has been 
	called to the terminal"""
	
	@wraps(interceptedFunction)
	def counter(*args, **kwargs):
		counter.called += 1
		functionName = interceptedFunction.func_name
		actualResult = interceptedFunction(*args, **kwargs)
		logging.debug('\n ######  Function: [{fnc}] =>  [{count}]  ######'
					.format(fnc=functionName, count=counter.called))
		return actualResult
	counter.called = 0
	return counter
	
	
def beforeit(inputFunc):
	"""A decorator that intercepts a function and it's arguments *args 
	and **kwargs and calls another function (inputFunc) first """
	functionName = inputFunc.func_name
	def beforeFunc(interceptedFunction):		
		@wraps(interceptedFunction)
		def before(*args, **kwargs):
			inputFunc()
			actualResult = interceptedFunction(*args, **kwargs)
			return actualResult					
		return before
	return beforeFunc
	
def afterit(inputFunc):
	"""A decorator that intercepts a function and it's arguments *args 
	and **kwargs and calls another function (inputFunc) after """
	functionName = inputFunc.func_name
	def afterFunc(interceptedFunction):				
		@wraps(interceptedFunction)
		def after(*args, **kwargs):			
			actualResult = interceptedFunction(*args, **kwargs)
			inputFunc()
			return actualResult			
		return after
	return afterFunc
		

		
    

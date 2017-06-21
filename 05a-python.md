# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are both ordered collection of elements, however while lists are mutable, tuples cannot be changed once made. This immutablity is also why tuples can be used as keys and lists cannot.

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets are similar in that the both are collections of elements. However while lists allow 



---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambdas are used to make small unnamed functions, usually as support for another, larger function.

In the `sorted` function, the `key` argument is the function applied to the list element by which it will be sorted. Using a lambda in the `key` argument allows one to designate a function without needing to write it separately and refer back to it.

ex. sorted([-1, 3, 5, 6, 7], key=lambda x: x ** 3)

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a compact method to generate lists in one statement as opposed to requiring a multiple lined function.
The same technique can generate sets and dictionaries as well.

`filter` is used as a function that returns a list of items for which an applied function returns `True`.  `map` is used as a method to apply a function to an iterable (like a list), or multiple iterables simultaneously.

ex.
lst = [x*5 for x in range(0, 10)]
dct = {x : x*5 for x in range(0, 10)}
set_ex = (x for x in [EnglishAlphabet] if x not in 'hello world')


list(filter(lambda x: x%2 == 0, [x**2 for x in range(0, 10)]))
list(map(lambda x: x%3 == 0, [x for x in range(0, 30)]))



---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)






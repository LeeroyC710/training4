import pytest
from factorial_function import factorial1

def test_factorial():
      assert factorial1.factorial(5)==120 

def test_big():
      assert factorial1.factorial(13) ==6227020800

def test_bigger():
      assert factorial1.factorial(20)==2432902008176640000

def test_superbig():
      assert factorial1.factorial(30)==265252859812191058636308480000000

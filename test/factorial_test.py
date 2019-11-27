import pytest
import factorial

def test_factorial():
      assert factorial.factorial(5)==120 

def test_big():
      assert factorial.factorial(13) ==6227020800

def test_bigger():
      assert factorial.factorial(20)==2432902008176640000

def test_superbig():
      assert factorial.factorial(30)==265252859812191058636308480000000

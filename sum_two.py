"""
Creating a test code to print sum of 2 integer inputs
"""
def sum(a, b):
  return (a + b)

def test_sum():
  result = sum(3,5)
  assert result == 8

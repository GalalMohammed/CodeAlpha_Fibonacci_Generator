def fibonacci_generator():
  """
  Generates an infinite sequence of Fibonacci numbers.

  Yields:
    int: The next Fibonacci number in the sequence.

  Example usage:
    fib_gen = fibonacci_generator()
    for i in range(10):
      print(next(fib_gen))
  """
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Example usage
fib_gen = fibonacci_generator()
for i in range(10):
  print(next(fib_gen))
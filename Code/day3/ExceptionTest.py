
try:
    raise ValueError("Howdy!")
except Exception as e:
    print(type(e))
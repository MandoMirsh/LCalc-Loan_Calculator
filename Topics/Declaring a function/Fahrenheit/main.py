def fahrenheit_to_celsius(fahrenheit):
    fahrenheit_celsius_range = 32
    celsius_fahrenheit_ratio = 1.8
    return round(((fahrenheit - fahrenheit_celsius_range) / celsius_fahrenheit_ratio), 3)

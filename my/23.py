
"""
Mr. Roy is living in Canada where temperature is mapped in Fahrenheit.
According to weather report current temperature in Canada is 130 °F. Roy’s
mother is living in different region of Canada where temperature is mapped in
Celsius. Convert current temperature of Canada into Celsius. C = (F - 32) * 5 /9
"""


def convert_temperature(fahrenheit):
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius
current_temperature_in_fahrenheit = 130
current_temperature_in_celsius = convert_temperature(current_temperature_in_fahrenheit)
print(current_temperature_in_celsius)

#output:
#54.44444444444444
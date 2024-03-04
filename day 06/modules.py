import converters
from converters import lbs_to_kg
# We can import all the methonds (line 1) or just the ones we need (line 2 - control + space to select the method)
print(converters.kg_to_lbs(70))

# If you use line 2 to import, you can call the method like any other function
print(lbs_to_kg(100))
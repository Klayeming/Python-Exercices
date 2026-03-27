"""
Module: Simple Class Demonstration

Demonstrates basic object-oriented programming concepts:
  - Class definition
  - Constructor (__init__)
  - Getter methods (get values)
  - Setter methods (set values)
"""

class SimpleClass:
    """A simple class with getter and setter methods."""
    
    def __init__(self, mon="default1", nom2="default2"):
        """Initialize class with two attributes."""
        self.mon = mon
        self.nom2 = nom2
    
    def getnom(self):
        """Get the value of mon attribute."""
        return self.mon
    
    def setnom(self, nom):
        """Set the value of mon attribute."""
        self.mon = nom

lui = "pop"
lo = "va chier"
monp = mer(lui, lo)

print(monp.getnom(), monp.nom2)
monp.setnom("connard")
print(monp.getnom())
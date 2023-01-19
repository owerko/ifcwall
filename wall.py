import ifcopenshell.util.element

m = ifcopenshell.open("Duplex_A.ifc")
walls = m.by_type("IfcWall")
print(len(walls))

print(f'Liczba ścian w modelu: {len(walls)}')

import ifcopenshell.util.element
import pprint as pp

m = ifcopenshell.open("Duplex_A.ifc")
walls = m.by_type("IfcWall")
print(len(walls))

print(f'Liczba ścian w modelu: {len(walls)}')

walls = m.by_type("IfcWall")
wall = walls[1]
pset_for_wall = ifcopenshell.util.element.get_psets(wall)
pp.pprint(pset_for_wall)

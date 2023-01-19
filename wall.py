import ifcopenshell.util.element
import pprint as pp

m = ifcopenshell.open("Duplex_A.ifc")
walls = m.by_type("IfcWall")
print(len(walls))

print(f'Liczba ścian w modelu: {len(walls)}')

walls = m.by_type("IfcWall")
ext_walls = []
for w in walls:
    psets = ifcopenshell.util.element.get_psets(w)
    if psets.get("Pset_WallCommon"):
        if bool(psets.get("Pset_WallCommon").get("IsExternal")):
            ext_walls.append(w)
            
print(f'Liczba ścian zewnętrznych: {len(ext_walls)}')

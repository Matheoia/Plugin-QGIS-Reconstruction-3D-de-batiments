import json
# Ouvrir le fichier JSON en lecture
with open('bat_simple_louhans.json', 'r') as f:
    # Charger les données JSON dans une variable Python
    data = json.load(f)

data['metadata']['referenceSystem'] = "EPSG::2154"
der_bound = data['CityObjects']["1"]["geometry"][0]["boundaries"][0][0][-1]

# Calculer les nouvelles valeurs et les stocker dans une liste
base_value = data['vertices'][der_bound+1][2]
new_verti = [v[2]-base_value if i > der_bound else v[2] for i, v in enumerate(data['vertices'])]

# Modifier les valeurs de la clé 'vertices' en utilisant les nouvelles valeurs
for i, vertex in enumerate(data['vertices']):
    vertex[2] = new_verti[i]
    

attributes = data['CityObjects']['1']['attributes']
attributes['ArrDissolve-LoD12.global_elevation_50p'] = attributes['ArrDissolve-LoD12.global_elevation_50p'] - attributes['LASInPolygons.ground_elevations']
attributes['ArrDissolve-LoD12.global_elevation_70p'] = attributes['ArrDissolve-LoD12.global_elevation_70p'] - attributes['LASInPolygons.ground_elevations']
attributes['ArrDissolve-LoD12.global_elevation_max'] = attributes['ArrDissolve-LoD12.global_elevation_max'] - attributes['LASInPolygons.ground_elevations']
attributes['ArrDissolve-LoD12.global_elevation_min'] = attributes['ArrDissolve-LoD12.global_elevation_min'] - attributes['LASInPolygons.ground_elevations']
attributes['LASInPolygons.ground_elevations'] = 0

# Écrire les données modifiées dans un nouveau fichier JSON
with open('nouveau_test.json', 'w') as f:
    json.dump(data, f)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json

# Spécifier le chemin d'accès pour le fichier d'entrée
input_path = r'C:\Users\maudb\OneDrive\Documents\Ordi_Maud\Maud\Master_1_ENSG\geodev\jeu_donnees_test\Louhans_71500\test_louhans\test_groupe_bat_louhans\output\groupe_bat_louhans.json'

# Ouvrir le fichier JSON en lecture
with open(input_path, 'r') as f:
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

# Spécifier le chemin d'accès pour le fichier de sortie
output_path = r'C:\Users\maudb\OneDrive\Documents\Ordi_Maud\Maud\Master_1_ENSG\geodev\jeu_donnees_test\Louhans_71500\test_louhans\test_groupe_bat_louhans\output\nouveau_test_groupe_bat_Louhans.json'

# Écrire les données modifiées dans un nouveau fichier JSON
with open(output_path, 'w') as f:
    json.dump(data, f)

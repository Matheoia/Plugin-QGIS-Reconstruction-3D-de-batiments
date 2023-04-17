import json
import numpy as np

# Ouvrir le fichier JSON en lecture
with open('C:/geoDev/output_runner/quartier/quartier.json', 'r') as f:
    # Charger les données JSON dans une variable Python
    data = json.load(f)

data['metadata']['referenceSystem'] = "EPSG::2154"

vertices = np.array(data['vertices'])
hauteurs = vertices[:, 2].astype(int)

base = np.unique(hauteurs)[1]

hauteurs = np.where(hauteurs != 0, hauteurs - int(base), 0)
vertices[:, 2] = hauteurs

data['vertices'] = vertices.tolist()

# Écrire les données modifiées dans un nouveau fichier JSON
with open('C:/geoDev/output_runner/quartier/quartier_corr.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False, default=lambda o: o.tolist() if isinstance(o, np.ndarray) else o)

#Importations
import os
import geopandas as gpd
import json

#Chemins des couches en entrée
footprint="C:\QGIS_test\wippolder\wippolder.gpkg "
pointcloud="C:\QGIS_test\wippolder\wippolder.las"

#Fonction qui appelle geoflow
def Construit_bat (index):
    """index est le batiment souhaité au sein du footprint"""
    footprint_select=str(index)
    output_json="C:\QGIS_test\output\wippolder_"+footprint_select+".json"
    output_ogr="C:\QGIS_test\output\wippolder_"+footprint_select+".gpkg"
    
    cmd="lod22-reconstruct --input_footprint="+footprint+" --input_pointcloud="+pointcloud
    cmd=cmd+" --output_cityjson="+output_json+" --output_ogr="+output_ogr
    cmd=cmd+" --input_footprint_select="+footprint_select
    
    os.system(cmd)
    
# Lecture du fichier geopackage
cadastre = gpd.read_file('C:\QGIS_test\wippolder\wippolder.gpkg')
Index=cadastre.iloc[:, 7] #7e colonne correspond à la colonne des indexes des batiments
print ("nombre de batiment=",len(Index))

# Construit_bat(2)

quartier = {} #pour créer la variable batiment_index (variable dont le nom change à chaque tour de boucle)

#Initialisation de city et vertices pour le JSON final
city = {}
vertices=[]
N=len(vertices)
for index in range(1,3): #Boucle pour 2 batiments (qui se nomment wippolder_1.json et [...]_2.json )
    with open('C:\QGIS_test\output\wippolder_'+str(index)+'.json') as mon_fichier:
        quartier[f'batiment_{index}'] = json.load(mon_fichier) #création d'un dictionnaire dans lequel on met les batiments
        
        vertices=vertices+quartier[f"batiment_{index}"]['vertices'] #On ajoute les points du batiment_index à la liste finale vertices
        for nom, cityobject in quartier[f"batiment_{index}"]['CityObjects'].items():
            city[str(index)+'.'+nom] = cityobject #On renomme le cityobject en fonction de la classe parent (index du batiment)
       
        
        for cityobject in quartier[f"batiment_{index}"]['CityObjects'].values():
            if cityobject['attributes']=={}:
                for geometry in cityobject["geometry"]:
                    for boundary in geometry["boundaries"]:
                        for L_point in boundary:
                            for point in L_point :
                                for coord in point:
                                    coord=coord+N
            else:
                for geometry in cityobject["geometry"]:
                    for boundary in geometry["boundaries"]:
                        for L_point in boundary:
                            for point in L_point :
                                point=point+N
    N=len(vertices) #nb actuel de pts dans le json final

#Initialisation des autres classes pour le JSON
metadata=quartier['batiment_1']['metadata'] #Pour l'instant données du 1e batiment
transform=quartier['batiment_1']['transform'] #Pour l'instant données du 1e batiment
version=quartier['batiment_1']['version'] #Pour l'instant données du 1e batiment
typ=quartier['batiment_1']['type'] #Pour l'instant données du 1e batiment

#Creation du json
json_obj = {"CityObjects": city, "metadata": metadata, "transform": transform, "type":typ, "version":version, "vertices":vertices}
with open('C:\QGIS_test\output\quartier.json', 'w') as f:
    json.dump(json_obj, f)
    


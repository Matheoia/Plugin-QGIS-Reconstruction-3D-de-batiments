# --- Read Me de geoflow --- #

Qu'est ce qu'il fait ?
- prend nuage de points et polygone 2D d'un batiment => modèle bâtiment 3D
- génère aussi la sémantique, et arrive en LoD 2.2 à distinguer les types
  de surfaces 
- sort format json ou équivalent pour cela il me semble


Qu'est ce que LoD : 
correspond au Level of Detail : 4 niveaux possibles 
en soit (cinquième : pour l'intérieur)

0.0 : premier plan 2D horizontal rectangulaire qui couvre le bat
0.1 : première distinction en cherchant un coin
0.x : ajoute de plus en plus de distinctions (de coins) dans le plan horizontal 

1.0 : première élévation qui suit le plan horizontal
      ressemble à un batiment rectangulaire simple
1.2 : batiment avec un plafond à hauteur similaire
1.3 : commence à ajouter les différentes élévations 
      selon la couche ajoutée par le .x

2.0 : ajoute la formation du toit
2.2 : quelques détails sur le toit avec un coin 
      à une différente hauteur
2.3 : relief et dépassement du toit amélioré

3.0 ajout des détails sur le toit uniquement en gardant
    le modèle 2.0 concernant les détails horizontaux

En somme et à retenir : 
dans le LoD x.y le x détermine le degré de détail 
concernant le plan vertical tandis que le y détermine 
celui du plan horizontal

https://3d.bk.tudelft.nl/lod/lodtud.png



Il existe des exigences sur les données en entrée : 

* Pour les nuages de points, acquis par balayage aérien
On préfère le LiDar (faudra gérer les valeurs aberrantes s'il y en a) 
Obtention de bon résultats avec 8 à 10 points le m².
Il faut alignement avec le polygne 2D 
quelques points au sol pour déterminer l'élévation du RdC
format : .LAS ou LAZ

* Pour le polygone 2D (bien un seul polygone) 
de préférence : l'empreinte du toit pour coincider avec nuage de points
acquis par voie aérienne
au format geoPackage ou ESRI shp ou connexion à bdd PostGis


Installation dans un autre fichier 

But pour l'instant 
https://github.com/geoflow3d/geoflow-bundle/blob/master/docs/img/model.png




 
 



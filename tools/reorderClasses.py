import owlready2 as owl
import pathlib
# import rdflib


tpoPath = pathlib.Path('../TissuePhenomics.owl')
importsPath = pathlib.Path('..\imports')
clPath = importsPath / 'cl_import.owl'
# TPO

tpoWorld = owl.World()
if tpoPath.exists():
    owl.onto_path.append(str(tpoPath.parent.resolve()))
    owl.onto_path.append(str(importsPath.resolve()))
    try:
        tpo = tpoWorld.get_ontology(str(tpoPath.resolve())).load(only_local=True)
    except:
        pass
else:
    raise FileNotFoundError

# CL Imports
clWorld = owl.World()
if clPath.exists():
    owl.onto_path.append(str(clPath.parent.resolve()))
    owl.onto_path.append(str(importsPath.resolve()))
    try:
        cl = clWorld.get_ontology(str(clPath.resolve())).load(only_local=True)
    except:
        pass
else:
    raise FileNotFoundError

#remove altogether
cell_components = clWorld.search_one(iri ='http://purl.obolibrary.org/obo/GO_0005575')
# cell = clWorld.search_one(iri = 'http://purl.obolibrary.org/obo/CL_0000000')
cellGo = clWorld.search_one(iri = 'http://purl.obolibrary.org/obo/GO_0005623')
subClassOf_iri='http://www.w3.org/2000/01/rdf-schema#subClassOf'

cellGo.is_a.remove(cell_components)

cl.save(str(clPath.resolve()))





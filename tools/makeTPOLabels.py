import owlready2 as owl
import rdflib
import pathlib

tpoPath = pathlib.Path('../TissuePhenomics.owl')
importsPath = pathlib.Path('..\imports')

if tpoPath.exists():
    owl.onto_path.append(str(tpoPath.parent.resolve()))
    owl.onto_path.append(str(importsPath.resolve()))
    try:
        tpo = owl.get_ontology(str(tpoPath.resolve())).load(only_local=True)
    except:
        pass
else:
    raise FileNotFoundError

world = owl.default_world
TPOLabel = world.search(label="*Tissue Phenomics Label")[0]


for cl in world.classes():
    if not TPOLabel[cl]:
        TPOLabel[cl] = []
        if cl.label:
            for l in cl.label:
                TPOLabel[cl].append(l.lower().replace('_', ' '))

for pr in world.properties():
    if pr.namespace.base_iri == "http://www.w3.org/2000/01/rdf-schema#":
        continue
    if not TPOLabel[pr]:
        TPOLabel[pr] = []
        if pr.label:
            for l in pr.label:
                TPOLabel[pr].append(l.lower().replace('_', ' '))

for pr in world.individuals():
    if not TPOLabel[pr]:
        TPOLabel[pr] = []
        if pr.label:
            for l in pr.label:
                TPOLabel[pr].append(l.lower().replace('_', ' '))

for pr in world.data_properties():
    if not TPOLabel[pr]:
        TPOLabel[pr] = []
        if pr.label:
            for l in pr.label:
                TPOLabel[pr].append(l.lower().replace('_', ' '))

graph = world.as_rdflib_graph()
TPOLabels = list(graph.query("""
SELECT ?s ?o
WHERE {
?s <http://www.definiens.com/ontologies/TissuePhenomicsOntology#TPO0000044> ?o .
}
"""))

newgraph = rdflib.graph.Graph(identifier='http://www.definiens.com/ontologies/TissuePhenomicsOntology/TPOLabels/')

for pair in TPOLabels:
    newgraph.add((pair[0],
                  rdflib.term.URIRef('http://www.definiens.com/ontologies/TissuePhenomicsOntology#TPO0000044'),
                  pair[1]))

savePath = pathlib.Path('..\imports\TissuePhenomicsOntologyLabels.rdfs')

serialized = newgraph.serialize(destination=str(savePath.resolve()), format="xml")


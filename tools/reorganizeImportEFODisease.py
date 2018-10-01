import owlready2 as owl
import pathlib

efoImportPath = pathlib.Path('../imports/efo_disease_import.owl')


if efoImportPath.exists():
    owl.onto_path.append(str(efoImportPath.parent.resolve()))
    efoImport = owl.get_ontology(str(efoImportPath.resolve())).load()
else:
    raise FileNotFoundError

#%%
neoplasm_import = efoImport.search(iri='*EFO_0000616')[0]

# wronglyPutTerms = ["EFO_0001422", "EFO_0002431", "EFO_0002892", "EFO_0002916", "EFO_0003769", 
# "EFO_0003817", "EFO_0003820", "EFO_0003824", "EFO_0003826", "EFO_0003828", "EFO_0003833", 
# "EFO_0003835", "EFO_0003841", "EFO_0003844", "EFO_0003846", "EFO_0003850", "EFO_0003851", 
# "EFO_0003853", "EFO_0003859", "EFO_0003860", "EFO_0003863", "EFO_0003865", "EFO_0003868", 
# "EFO_0003869", "EFO_0003871", "EFO_0003873", "EFO_0003880", "EFO_0003893", "EFO_0003897", 
# "EFO_0004198", "EFO_0005950", "EFO_1000921", "EFO_1001394", "EFO_1001513", "EFO_1001517",]

toFillTerms = ["EFO_0003850", 
               "EFO_0003835",
               "EFO_0003880",
               "EFO_0003820",
               "EFO_0003833", 
               "EFO_0003869", 
               "EFO_0001422", 
               "EFO_0003769", 
               "EFO_1000921", 
               "EFO_0002916", 
               "EFO_0003824",
               "EFO_0005950",
               "EFO_0003865",
               "EFO_0003817",
               "EFO_1001513",
               "EFO_0003851",
               "EFO_0003868",
               "EFO_0003893",
               "EFO_0003860",
               "EFO_0003873",
               "EFO_1001394",
               "EFO_1001517",
               "EFO_0003853",
               "EFO_0003826",
               "EFO_0004198",
               "EFO_0003828",
               "EFO_0003897",
               "EFO_0002892",
               "EFO_0003841",
               "EFO_0003871",
               "EFO_0002431",
               "EFO_0003844",
               "EFO_0003846",
               "EFO_0003863",
               "EFO_0003859"
               ]




for iri in toFillTerms:
    thisTerm = efoImport.search_one(iri="*"+iri)
    thisTerm.is_a.append(neoplasm_import)
    # if isinstance(thisTerm, list) and thisTerm:
    #     thisTerm[0].is_a.append(neoplasm_import)

efoImportPath2 = pathlib.Path('../imports/efo_disease_import.owl') #actually the same as efoImportPath here
efoImport.save(file=str(efoImportPath2.resolve()), format="rdfxml")

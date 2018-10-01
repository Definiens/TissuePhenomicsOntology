# Tissue Phenomics Ontology

## Tools
Most of the work was done using [protege (standalone version)](https://protege.stanford.edu/).

owlready2 (python package) was also used for some edition operations. See: https://pypi.org/project/Owlready2/

rdflib (python package) was used to directly generate some simple rdf files.

sparql queries, most of them executed against the inhouse JENA and Virtuoso instances. see the SPARQL folder for details.



## Development Principles

### imported ontologies
The main imported ontologies and their useage fields are:

| Ontology                    | Usage                                                                                                | namespace (shortcut) | Prefix                          | TP high level entry                                              |
| --------------------------- | :--------------------------------------------------------------------------------------------------- | :------------------- | :------------------------------ | :--------------------------------------------------------------- |
| Cell Ontology               | Specific cells (eg. macrophages, activated T cell)                                                   | obo                  | CL_                             | Biological entities/cell                                         |
| PRotein Ontology / GO       | For proteins/gene (as the entries match in this specific ontology)                                   | obo                  | [PR_ / GO_                      | Biological entities/Cell Marker                                  |
| UBERON                      | For tissue sorts (ex. 'cartilage tissue') and organs (indications)                                   | obo                  | UBERON_                         | Biological entities/[Excluded Region, organ part, organ, tissue] |
| OBI                         | For high level desription of data and their organisation. The following ontologies often refer to it | obo/IAO              | [OBI_/IAO_]                     | many                                                             |
| CHEBI                       | For chemical entities (DAB, eosin, etc.)                                                             | CHEBI                | CHEBI_                          | material entity, chemical entity                                 |
| EFO                         | extensive ontology covering most areas. Here: disease, p-values, etc.                                | EFO                  | EFO_  mostly                    | several                                                          |
| PATO / UO / GENEPIO / STATO | Phene descriptions and combinations                                                                  | ...                  | [PATO_ / UO_ / GENEPIO_ / ... ] | [data item/datum label]                                          |

The relevant terms of these ontologies were mireoted\* using [ontofox](http://ontofox.hegroup.org/). The configuration files and result files are under [imports](..\imports).

Note also the branch _refOntos_ in this very repository which contains most of the previously cited ontologies in a dedicated folder (not included in master as this corresponds to a significant amount of data).

In the case of EFO, two imports are generated:
* efo_import.owl the generic file including neoplasm
* efo_disease_import.owl which is 3.2mb large on its own and which contains several neoplasm sorts of tissues / diseases. efo_disease_import.owl is actually the output of tools/reorganizeImportEFODisease.py as most of the structure is lost during mireoting. An intermidiate owl (efo_disease_import_b.owl) file is used.  

#### Proteins entities - notes on PR

All proteins refer to the PRotein Ontology. This ontology has several domains. The entries used here should belong to the 'gene' category or 'external' in which case they should refer to the HGNC standardized term.
This way all entries can be mapped one to one to their coding gene and which is normally identified by ex. the hugo (hgng) term.
This makes the joined analysis of gene expression data and tissue phenomes easier as the same identifier can be used safely.

#### Units entities - notes on UO
UO defines most units as classes. Here only the main categories (area unit, volume unit, etc.) were imported and individuals are used.
Following the approach used in OBI, the individuals are given the same iri as the original class (see punning\*\*).

## properties annotations

The use of tpo:label allows to specify tissue phenomics specific terms.

## Todos

### short term list

## Remarks 

\* MIREOT: The minimum information to reference an external ontology term 
\*\* Punning: https://www.w3.org/TR/2012/REC-owl2-new-features-20121211/#F12:_Punning


# Cell markers and associated protein markers properties retrieval

The sparql queries 

* retrieveCellsPositiveMarkersRestrictions.sparql
* retrieveMarkersProperties.sparql
* retrieveProteinsHierarchy.sparql

were run agains a jena Fuseki server where the Cell Ontology (CL) and all its imports had been uploaded.
The cell ontology was placed in the graph http://purl.obolibrary.org/obo/cl.ow
The Tissue Phenomics Ontology was placed in the graph http://www.definiens.com/ontologies/TissuePhenomicsOntology

All results were concatenated in the ../imports/CL_supProperties.ttl file. 

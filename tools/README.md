# tools

Here is a small set of tools to help with the handling of the ontology or its development/maintenance

## Development tools
__makeTPOLabels__ allows to generate TissuePhenomicsOntologyLabels.rdfs

__changeAllURIs__ is a template script which allows to change all URIs. WARNING!!! this should not be done unless absolut necessity as this is a backward incompatible change which breaks the link to older datasets!

__determineOWL2Profile__: a very basic attempt to check for the complience of the ontology to some of the common OWL2 profiles (also OWL lite is checked). Effectively only the use of some keywords is checked.

__reorganizeImportEFODisease__ is used to reorganise the EFO imports after they were mireoted (as most of the hierarchy is lost and must be manualy reconstructed).

## ontoHelper
Mostly contains one helper class which allows the following operations:
* query the ontology for some specific label using either the rdfs:label tag or the Tissue Phenomics label
* create a JSON / python dictionary with all sub-classes of a specified entry (the entry is specified by label)
* create a Definiens Developer XD dkb class hierarchy file for one entry and all its sub-classes (recursively)


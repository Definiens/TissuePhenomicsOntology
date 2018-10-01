echo Start

curl -s -F file=@"imports/TPOntofoxImport EFO.conf" -o imports/efo_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport EFO Disease.conf" -o imports/efo_disease_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports\TPOntofoxImport OBI.conf" -o imports/obi_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport CL.conf" -o imports/cl_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport PATO.conf" -o imports/pato_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport STATO.conf" -o imports/stato_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport UBERON.conf" -o imports/uberon_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport UO.conf" -o imports/uo_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport PR.conf" -o imports/pr_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport CHEBI.conf" -o imports/chebi_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport RO.conf" -o imports/ro_import.owl http://ontofox.hegroup.org/service.php
curl -s -F file=@"imports/TPOntofoxImport OGG.conf" -o imports/ogg_import.owl http://ontofox.hegroup.org/service.php

cd tools
python reorganizeImportEFODisease.py
python reorderClasses.py


echo Done!
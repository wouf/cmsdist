### RPM cms data-Geometry-TrackerCommonData V01-09-03

%define patchsrc       grep -r -l -e "^#!.*perl.*" %{_builddir}/Geometry | xargs perl -p -i -e "s|^#!.*perl(.*)|#!/usr/bin/env perl\$1|"

## IMPORT cmssw-xmldata-build

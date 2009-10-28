### RPM cms cmssw CMSSW_3_4_0_pre3
## IMPORT configurations 
Provides: /bin/zsh
Provides: /bin/ksh
Provides: /bin/sed
Provides: /bin/bash
Provides: /usr/bin/awk
Provides: /usr/bin/python
Provides: perl(Date::Format)
Provides: perl(Term::ReadKey)
Provides: perl(full)
Provides: perl(LWP::UserAgent)
Provides: perl(Template)
Provides: perl(CMSDBA)
Provides: perl(Tk) >= 804
Provides: perl(Tk::ROText)
Provides: ld-linux.so.2(GLIBC_PRIVATE)
Provides: ld-linux-x86-64.so.2(GLIBC_PRIVATE)(64bit)
Requires: cmssw-tool-conf python glimpse

%define cvsprojuc       %(echo %n | sed -e "s|-debug||"| tr 'a-z' 'A-Z')
%define cvsprojlc       %(echo %cvsprojuc | tr 'A-Z' 'a-z')
%define cvsdir          %cvsprojuc
%define cvsserver       %cvsprojlc
%define prebuildtarget  gindices
%define buildtarget     release-build
%define useCmsTC        1
%define saveDeps        yes

## IMPORT cms-scram-build
## IMPORT scramv1-build

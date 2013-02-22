%define major 5
%define libname %mklibname ofx %{major}
%define develname %mklibname ofx -d

Summary:	LibOFX library provides support for OFX command responses
Name:		libofx
Version:	0.9.5
Release:	1
Group:		System/Libraries
License:	GPL
URL:		http://libofx.sourceforge.net
Source0:	http://download.sourceforge.net/libofx/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	opensp-devel

%description
This is the LibOFX library.  It is a API designed to allow applications to
very easily support OFX command responses, usually provided by financial
institutions.  See http://www.ofx.net/ofx/default.asp for details and
specification. LibOFX is based on the excellent OpenSP library written by
James Clark, and now part of the OpenJADE http://openjade.sourceforge.net/
project.  OpenSP by itself is not widely distributed.  OpenJADE 1.3.1 includes
a version on OpenSP that will link, however, it has some major problems with
LibOFX and isn't recommended.  Since LibOFX uses the generic interface to
OpenSP, it should be compatible with all recent versions of OpenSP (It has
been developed with OpenSP-1.5pre5).  LibOFX is written in C++, but provides a
C style interface usable transparently from both C and C++ using a single
include file.

%package -n %{libname}
Summary:	Libraries for libofx
Group:		System/Libraries

%description -n %{libname}
This package provides libraries to use libofx.

%package -n %{develname}
Group:		Development/C
Summary:	Libraries needed to develop for libofx
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{_lib}ofx2-devel < 0.8.2

%description -n %{develname}
Libraries needed to develop for libofx.

%prep
%setup -q

%build
# FIXME: better make it lib64 aware in configure script
# disable curl detection
%configure2_5x \
	--disable-static \
    --with-opensp-libs=%{_libdir} \
    --without-libcurl

%make

%install
rm -rf %{buildroot}

%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_docdir}/libofx

%files
%doc AUTHORS ChangeLog NEWS README totest.txt 
%{_bindir}/*
%{_datadir}/libofx
%_mandir/man1/ofxdump.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc doc/html doc/ofx_sample_files
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc


%changelog
* Sun May 15 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.4-1mdv2011.0
+ Revision: 674937
- new version
- add ofxdump man page

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-2
+ Revision: 662388
- mass rebuild

* Wed Feb 16 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.2-1
+ Revision: 638018
- new version
- drop patch

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-3mdv2011.0
+ Revision: 602589
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-2mdv2010.1
+ Revision: 520891
- rebuilt for 2010.1

* Tue Sep 29 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.1-1mdv2010.0
+ Revision: 451094
- update to new version 0.9.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.0-5mdv2010.0
+ Revision: 425647
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.9.0-4mdv2009.1
+ Revision: 351465
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-3mdv2009.0
+ Revision: 229893
- fix deps
- added a gcc43 patch (gentoo)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jan 01 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-1mdv2008.1
+ Revision: 140041
- new license policy
- new devel library policy
- spec file clean
- new version
- bump %%major

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 10 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.8.3-2mdv2008.0
+ Revision: 50807
- Rebuild to fix libosp dependency

* Tue May 29 2007 Frederic Crozat <fcrozat@mandriva.com> 0.8.3-1mdv2008.0
+ Revision: 32526
- Release 0.8.3
- Fix buildrequires and prevent libcurl detection, we don't need to build ofxconnect sample binary


* Fri Dec 29 2006 Frederic Crozat <fcrozat@mandriva.com> 0.8.2-1mdv2007.0
+ Revision: 102598
- Release 0.8.2
- bump major, add conflicts to ease upgrade
- remove patch0, no longer needed
- Import libofx

* Mon Dec 05 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.8.0-2mdk
- add BuildRequires: libcurl-devel

* Fri Dec 02 2005 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdk
- major 2
- New release 0.8.0

* Thu Aug 25 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.7.0-2mdk
- c++ fixes

* Mon Dec 13 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.0-1mdk
- major 1
- drop patch
- New release 0.7.0

* Thu Jun 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.6-2mdk
- Rebuild

* Thu Jan 15 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6.6-1mdk
- Release 0.6.6


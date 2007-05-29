%define lib_major 3
%define lib_name %mklibname ofx %{lib_major}

Summary: LibOFX library provides support for OFX command responses
Name: libofx
Version: 0.8.3
Release: %mkrel 1
Source: http://download.sourceforge.net/libofx/%{name}-%{version}.tar.bz2
Group:	System/Libraries
License: GPL
URL: http://libofx.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: OpenSP-devel

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



%package -n %{lib_name}
Summary:        Libraries for libofx
Group:          System/Libraries
Requires: %{name} >= %{version}-%{release}

%description -n %{lib_name}
This package provides libraries to use libofx.

%package -n %{lib_name}-devel
Group:	Development/C
Summary: Libraries needed to develop for libofx
Requires: %{lib_name} = %{version}
Provides: libofx-devel = %{version}-%{release}
Requires: OpenSP-devel
Conflicts: %{_lib}ofx2-devel < 0.8.2

%description -n %{lib_name}-devel
Libraries needed to develop for libofx.


%prep
%setup -q

%build
# FIXME: better make it lib64 aware in configure script
# disable curl detection
%configure2_5x --with-opensp-libs=%{_libdir} --without-libcurl

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

#remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_docdir}/libofx

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README totest.txt 
%{_bindir}/*
%{_datadir}/libofx

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc doc/html doc/ofx_sample_files
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc



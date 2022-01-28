%define major	7
%define libname	%mklibname ofx %{major}
%define devname	%mklibname ofx -d

Summary:	LibOFX library provides support for OFX command responses
Name:		libofx
Version:	0.10.3
Release:	1
Group:		System/Libraries
License:	GPLv2
Url:		http://libofx.sourceforge.net
Source0:	https://github.com/libofx/libofx/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
#Source0:	http://download.sourceforge.net/libofx/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	gengetopt
BuildRequires:	graphviz
BuildRequires:	help2man
BuildRequires:	opensp-devel
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libcurl)

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

%package -n %{devname}
Group:		Development/C
Summary:	Libraries needed to develop for libofx
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Libraries needed to develop for libofx.

%prep
%setup -q

%build
./autogen.sh
# FIXME: better make it lib64 aware in configure script
# disable curl detection
%configure \
	--disable-static \
	--with-opensp-libs=%{_libdir} \
	--without-libcurl

%make_build

%install
%make_install

#remove unpackaged files
rm -rf %{buildroot}%{_docdir}/libofx

%files
%doc AUTHORS ChangeLog NEWS README totest.txt 
%{_bindir}/*
%{_datadir}/libofx
%_mandir/man1/ofxdump.1*
%{_mandir}/man1/ofxconnect.1.*

%files -n %{libname}
%{_libdir}/libofx.so.%{major}*

%files -n %{devname}
%doc doc/html doc/ofx_sample_files
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc


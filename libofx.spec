%define major 4
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
BuildRequires:	OpenSP-devel

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

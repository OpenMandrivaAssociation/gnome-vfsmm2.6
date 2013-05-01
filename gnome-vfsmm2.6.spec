%define url_ver %(echo %{version}|cut -d. -f1,2)

%define pkgname gnome-vfsmm
%define api	2.6
%define major	1
%define libname	%mklibname %{pkgname} %{api} %{major}
%define devname %mklibname -d %{pkgname} %{api}

Name:		%{pkgname}%{api}
Summary:	A C++ interface for GNOME VFS library
Version:	2.26.0
Release:	8
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gtkmm.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-vfsmm/%{url_ver}/%{pkgname}-%{version}.tar.bz2

BuildRequires:	doxygen
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gnome-vfs-2.0)

%description
This package provides a C++ interface for gnome-vfs (the GNOME
Virtual File System), which provides an abstraction to common file
system operations like reading, writing and copying files, listing
directories and so on.  It is a subpackage of the gnomemm project,
which provides a C++ interface for GNOME libraries.

%package	-n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{pkgname} = %{version}-%{release}

%description	-n %{libname}
This package provides a C++ interface for gnome-vfs (the GNOME
Virtual File System), which provides an abstraction to common file
system operations like reading, writing and copying files, listing
directories and so on.  It is a subpackage of the gnomemm project,
which provides a C++ interface for GNOME libraries.

%package	-n %{devname}
Summary:	Headers and development files of GNOME VFS C++ wrapper
Group:		Development/GNOME and GTK+
Provides:	%{pkgname}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-doc < 2.26.0-8

%description -n %{devname}
This package contains the headers and various development files needed,
when compiling or developing programs which want C++ wrapper of GNOME
VFS library.

%prep
%setup -qn %{pkgname}-%{version}

%build
%configure2_5x --disable-static
%make 

### Build doc
pushd docs/reference
  sed -i -e 's/^(HAVE_DOT.*=) YES/$1 NO/' Doxyfile
  make all
popd

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgnomevfsmm-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%doc docs/reference/html


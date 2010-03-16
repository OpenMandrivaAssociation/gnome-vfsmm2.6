%define version 2.26.0
%define release %mkrel 2

%define major	1
%define api_version 2.6

%define glibmm_version 2.4.0
%define gnome_vfs_version 2.8.1

%define pkgname gnome-vfsmm
%define libname		%mklibname %pkgname %api_version %{major}
%define libname_orig	%mklibname %pkgname %api_version
%define develname %mklibname -d %pkgname %api_version

Name:	 	%{pkgname}%{api_version}
Summary: 	A C++ interface for GNOME VFS library
Version: 	%version
Release: 	%release
License: 	LGPLv2+
Group:   	System/Libraries
Source:  	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
URL:     	http://gtkmm.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gnome-vfs2-devel >= %{gnome_vfs_version}
BuildRequires:	glibmm2.4-devel >= %{glibmm_version}
BuildRequires:	doxygen

%description
This package provides a C++ interface for gnome-vfs (the GNOME
Virtual File System), which provides an abstraction to common file
system operations like reading, writing and copying files, listing
directories and so on.  It is a subpackage of the gnomemm project,
which provides a C++ interface for GNOME libraries.

%package	-n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name} = %{version}-%{release}
Provides:	%{libname_orig} = %{version}-%{release}

%description	-n %{libname}
This package provides a C++ interface for gnome-vfs (the GNOME
Virtual File System), which provides an abstraction to common file
system operations like reading, writing and copying files, listing
directories and so on.  It is a subpackage of the gnomemm project,
which provides a C++ interface for GNOME libraries.


%package	-n %develname
Summary:	Headers and development files of GNOME VFS C++ wrapper
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	gnome-vfs2-devel >= %{gnome_vfs_version}
Requires:	glibmm2.4-devel >= %{glibmm_version}
Obsoletes: %mklibname -d %pkgname 2.6 1

%description -n %develname
This package contains the headers and various development files needed,
when compiling or developing programs which want C++ wrapper of GNOME
VFS library.

%package	doc
Summary:	Documentation of %{pkgname} library
Group:		Books/Other

%description doc
This package provides API documentation of %{pkgname} library.


%prep
%setup -q -n %pkgname-%version

%build
%configure2_5x --enable-static
%make 

### Build doc
pushd docs/reference
  perl -pi -e 's/^(HAVE_DOT.*=) YES/$1 NO/' Doxyfile
  make all
popd

%install
rm -rf %{buildroot}
%makeinstall_std
find %buildroot -name \*.la|xargs chmod 644

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc COPYING
%{_libdir}/libgnomevfsmm-%{api_version}.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api_version}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so

%files doc
%defattr(-, root, root)
%doc docs/reference/html



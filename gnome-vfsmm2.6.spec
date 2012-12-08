%define major	1
%define api_version 2.6

%define pkgname gnome-vfsmm
%define libname		%mklibname %{pkgname} %{api_version} %{major}
%define libname_orig	%mklibname %{pkgname} %{api_version}
%define develname %mklibname -d %{pkgname} %{api_version}

Name:		%{pkgname}%{api_version}
Summary:	A C++ interface for GNOME VFS library
Version:	2.26.0
Release:	7
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(glibmm-2.4)
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

%package	-n %{develname}
Summary:	Headers and development files of GNOME VFS C++ wrapper
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	pkgconfig(gnome-vfs-2.0)
Requires:	pkgconfig(glibmm-2.4)

%description -n %{develname}
This package contains the headers and various development files needed,
when compiling or developing programs which want C++ wrapper of GNOME
VFS library.

%package	doc
Summary:	Documentation of %{pkgname} library
Group:		Books/Other

%description doc
This package provides API documentation of %{pkgname} library.


%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x --disable-static
%make 

### Build doc
pushd docs/reference
  perl -pi -e 's/^(HAVE_DOT.*=) YES/$1 NO/' Doxyfile
  make all
popd

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%doc COPYING
%{_libdir}/libgnomevfsmm-%{api_version}.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api_version}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%files doc
%doc docs/reference/html

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.26.0-4mdv2011.0
+ Revision: 664891
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.26.0-3mdv2011.0
+ Revision: 605476
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.26.0-2mdv2010.1
+ Revision: 521482
- rebuilt for 2010.1

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355975
- update to new version 2.26.0

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286536
- new version
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.22.0-2mdv2009.0
+ Revision: 221092
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 182999
- new version

* Tue Feb 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.0-2mdv2008.1
+ Revision: 166523
- fix deps

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 06 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.0-1mdv2008.1
+ Revision: 115985
- new version

* Fri Sep 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 85543
- new version
- new devel name
- bump deps


* Sat Mar 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 140351
- new version

* Wed Nov 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.1
+ Revision: 86159
- Import gnome-vfsmm2.6

* Wed Nov 22 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.1
- fix source URL
- new version

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Thu Aug 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.15.1-2mdv2007.0
- rebuild w/o selinux on x86_64

* Sat Jul 15 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.1-1mdk
- New release 2.15.1

* Tue Apr 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0
- use mkrel

* Sun Oct 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-1mdk
- New release 2.12.0

* Mon Mar 07 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.10.0-1mdk
- New release 2.10.0

* Wed Jan 05 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-2mdk 
- Rebuild with latest howl

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- New release 2.8.0
- requires new gnome-vfs
- fix source URL

* Mon Jun 21 2004 Abel Cheung <deaddog@deaddog.org> 2.6.1-2mdk
- Rebuild with new g++
- Reenable libtoolize

* Sat May 15 2004 Abel Cheung <deaddog@deaddog.org> 2.6.1-1mdk
- New version

* Thu Apr 29 2004 Abel Cheung <deaddog@deaddog.org> 2.6.0-1mdk
- First Mandrake package


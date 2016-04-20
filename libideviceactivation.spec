#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

Summary:	Library to handle activation of Apple iOS devices
Summary(pl.UTF-8):	Biblioteka do obsługi aktywacji urządzeń Apple iOS
Name:		libideviceactivation
# 1.2.x is stable
Version:	1.0.0
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	e8d133fd17bf688a457af88d84d97711
URL:		http://www.libimobiledevice.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.20
BuildRequires:	libimobiledevice-devel >= 1.1.4
BuildRequires:	libplist-devel >= 1.11
BuildRequires:	libxml2-devel >= 1:2.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libplist >= 1.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to manage the activation process of Apple iOS devices.

%description -l pl.UTF-8
Biblioteka do zarządzania procesem aktywacji urządzeń Apple iOS.

%package devel
Summary:	Header files for libideviceactivation library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libideviceactivation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel >= 7.20
Requires:	libimobiledevice-devel >= 1.1.4
Requires:	libplist-devel >= 1.11
Requires:	libxml2-devel >= 1:2.9

%description devel
Header files for libideviceactivation library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libideviceactivation.

%package static
Summary:	Static libideviceactivation library
Summary(pl.UTF-8):	Statyczna biblioteka libideviceactivation
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libideviceactivation library.

%description static -l pl.UTF-8
Statyczna biblioteka libideviceactivation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/ideviceactivation
%attr(755,root,root) %{_libdir}/libideviceactivation.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libideviceactivation.so.2
%{_mandir}/man1/ideviceactivation.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libideviceactivation.so
%{_includedir}/libideviceactivation.h
%{_pkgconfigdir}/libideviceactivation-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libideviceactivation.a
%endif

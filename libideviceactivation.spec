#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

Summary:	Library to handle activation of Apple iOS devices
Summary(pl.UTF-8):	Biblioteka do obsługi aktywacji urządzeń Apple iOS
Name:		libideviceactivation
Version:	1.1.1
Release:	2
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/libideviceactivation/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	1211fe0c589732cd7de7c45d6263ad2d
URL:		https://libimobiledevice.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.20
BuildRequires:	libimobiledevice-devel >= 1.3.0
BuildRequires:	libplist-devel >= 2.2.0
BuildRequires:	libxml2-devel >= 1:2.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libimobiledevice >= 1.3.0
Requires:	libplist >= 2.2.0
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
Requires:	libimobiledevice-devel >= 1.3.0
Requires:	libplist-devel >= 2.2.0
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
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/ideviceactivation
%attr(755,root,root) %{_libdir}/libideviceactivation-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libideviceactivation-1.0.so.2
%{_mandir}/man1/ideviceactivation.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libideviceactivation-1.0.so
%{_includedir}/libideviceactivation.h
%{_pkgconfigdir}/libideviceactivation-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libideviceactivation-1.0.a
%endif

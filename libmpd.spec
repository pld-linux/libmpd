#
Summary:	MPD client library
Name:		libmpd
Version:	0.12.0
Release:	1
License:	GPL
Group:		Applications
# http://sarine.nl/gmpc-downloads
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	bbfe28a5c3d7ef72b042030e3af52208
URL:		http://sarine.nl/gmpc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Music Player Daemon client development.

%package devel
Summary:	Header files for the MPD client library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for MPD client library.

%package static
Summary:	Static MPD client library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MPD client library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	CPPFLAGS="-I/usr/include/ncurses"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

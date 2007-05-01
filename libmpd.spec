Summary:	MPD client library
Summary(pl):	Biblioteka kliencka MPD
Name:		libmpd
Version:	0.13.0
Release:	1
License:	GPL
Group:		Libraries
# http://sarine.nl/gmpc-downloads
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	a1109d36da9c5c9c6e5fed59309b783b
URL:		http://sarine.nl/gmpc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Music Player Daemon client development.

%description -l pl
Biblioteka do tworzenia klientów demona MPD (Music Player Daemon).

%package devel
Summary:	Header files for the MPD client library
Summary(pl):	Pliki nag³ówkowe biblioteki klienckiej MPD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for MPD client library.

%description devel -l pl
Pliki nag³ówkowe biblioteki klienckiej MPD.

%package static
Summary:	Static MPD client library
Summary(pl):	Statyczna biblioteka kliencka MPD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MPD client library.

%description static -l pl.UTF-8
Statyczna biblioteka kliencka MPD.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

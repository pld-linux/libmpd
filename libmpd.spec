Summary:	MPD client library
Summary(pl.UTF-8):	Biblioteka kliencka MPD
Name:		libmpd
Version:	11.8.17
Release:	4
License:	GPL v2+
Group:		Libraries
Source0:	https://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5ae3d87467d52aef3345407adb0a2488
Patch0:		config.h.patch
Patch1:		%{name}-types.patch
URL:		https://gmpc.fandom.com/wiki/Libmpd
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Music Player Daemon client development.

%description -l pl.UTF-8
Biblioteka do tworzenia klientów demona MPD (Music Player Daemon).

%package devel
Summary:	Header files for the MPD client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej MPD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.16.0

%description devel
Header files for MPD client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej MPD.

%package static
Summary:	Static MPD client library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka MPD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MPD client library.

%description static -l pl.UTF-8
Statyczna biblioteka kliencka MPD.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmpd.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libmpd.so.*.*.*
%ghost %{_libdir}/libmpd.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmpd.so
%{_includedir}/libmpd-1.0
%{_pkgconfigdir}/libmpd.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpd.a

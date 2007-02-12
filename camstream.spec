Summary:	Digital camera utilities
Summary(pl.UTF-8):	Narzędzia do obsługi kamer cyfrowych
Name:		camstream
Version:	0.26.3
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.smcc.demon.nl/camstream/download/%{name}-%{version}.tar.gz
# Source0-md5:	1662fe8fd9af9e0065ba77254e836748
Patch1:		%{name}-destdir.patch
URL:		http://www.smcc.demon.nl/camstream/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CamStream is (going to be) a collection of tools for webcams and other
video-devices, enhancing your Linux system with multimedia video. All
written in C++ and with a nice GUI frontend. The interface is based on
Qt, an excellent GUI framework.

%description -l pl.UTF-8
CamStream jest (a właściwie ma być) zestawem narzędzi do kamer
internetowych i innych urządzeń video, rozszerzających możliwości
Linuksa o obraz multimedialny. Wszystkie narzędzia są napisane w C++ i
mają miły graficzny interfejs użytkownika. Interfejs jest oparty na
Qt.

%prep
%setup -q
%patch1 -p1

%build
cd lib/ccvt
%{__aclocal}
%{__autoconf}
cd ../../camstream
%{__aclocal}
%{__autoconf}
cd ..
%{__aclocal}
%{__autoconf}
QTDIR=%{_prefix} %configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/camstream

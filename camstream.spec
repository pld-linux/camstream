Summary:	Digital camera utilities
Summary(pl):	Narzêdzia do obs³ugi kamer cyfrowych
Name:		camstream
Version:	0.26.2
Release:	0.1
License:	GPL
Group:		Applications/Graphics
# Source0-md5:	5f2f245f6c7c1255ee60a007527e2fd2
Source0:	http://www.smcc.demon.nl/camstream/download/%{name}-%{version}.tar.gz
Patch1:		%{name}-destdir.patch
URL:		http://www.smcc.demon.nl/camstream
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empty

%description -l pl
Empty

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
cd ../
%{__aclocal}
%{__autoconf}
QTDIR=%{_prefix} %configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_datadir}/camstream/icons/*

Summary:	OMI - Open Media Interface
Summary(pl):	OMI - Interfejs Open Media
Name:		omi
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.linuxvideo.org/oms/data/%{name}-%{version}.tar.gz
# Source0-md5:	b9b540a57daad608b2a8158f8207963f
URL:		http://www.linuxvideo.org/oms/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel
BuildRequires:	oms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
OMI - Open Media Interface.

%description -l pl
OMI - Interfejs do Open Media System.

%prep
%setup  -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc README ChangeLog
%{_mandir}/man1/*
%{_datadir}/oms

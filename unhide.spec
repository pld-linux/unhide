Summary:	forensic tool to find hidden processes
Summary(pl.UTF-8):	narzędzie do znajdywania ukrytych procesów
Name:		unhide
Version:	20090810
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	http://www.security-projects.com/%{name}%{version}.tgz
# Source0-md5:	f9842175046e6eb10d22f5a988293171
URL:		http://www.security-projects.com/?Unhide
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unhide is a forensic tool to find hidden processes and TCP/UDP ports
by rootkits / LKMs or by another hidden technique.

%description -l pl.UTF-8
Unhide jest narzędziem służącym do znajdywania ukrytych procesów oraz
portów TCP/UDP używanych przez rootkity / LKM lub też inną technologie
ukrywania.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} unhide.c 		-o unhide-linux24
%{__cc} %{rpmcflags} %{rpmldflags} unhide-tcp.c 	-o unhide-tcp
%{__cc} %{rpmcflags} %{rpmldflags} unhide-linux26.c 	-o unhide

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8/}
install man/unhide* $RPM_BUILD_ROOT%{_mandir}/man8
install unhide-linux24 unhide-tcp unhide $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt LEEME.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/unhide*

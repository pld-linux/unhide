Summary:	forensic tool to find hidden processes
Summary(pl.UTF-8):	narzędzie do znajdywania ukrytych procesów
Name:		unhide
Version:	20240510
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://github.com/YJesus/Unhide/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	533a3701a631ada3b677a04bc9bd3a7f
URL:		https://www.unhide-forensics.info/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unhide is a forensic tool to find hidden processes and TCP/UDP ports
by rootkits / LKMs or by another hidden technique.

%description -l pl.UTF-8
Unhide jest narzędziem służącym do znajdywania ukrytych procesów oraz
portów TCP/UDP używanych przez rootkity / LKM lub też inną technologie
ukrywania.

%prep
%setup -q -n Unhide-%{version}

%build
%{__cc} %{rpmcflags} %{rpmcppflags} -pthread \
	unhide-linux*.c unhide-output.c %{rpmldflags} -o unhide-linux
%{__cc} %{rpmcflags} %{rpmcppflags} \
	unhide-posix.c %{rpmldflags} -o unhide-posix
%{__cc} %{rpmcflags} %{rpmcppflags} \
	unhide-tcp.c unhide-tcp-fast.c unhide-output.c %{rpmldflags} -o unhide-tcp
%{__cc} %{rpmcflags} %{rpmcppflags} \
	unhide_rb.c %{rpmldflags} -o unhide_rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8,%{_mandir}/es/man8,%{_mandir}/fr/man8}
install -p man/unhide.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p man/unhide-tcp.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p man/es/unhide.8 $RPM_BUILD_ROOT%{_mandir}/es/man8
install -p man/es/unhide-tcp.8 $RPM_BUILD_ROOT%{_mandir}/es/man8
install -p man/fr/unhide.8 $RPM_BUILD_ROOT%{_mandir}/fr/man8
install -p man/fr/unhide-tcp.8 $RPM_BUILD_ROOT%{_mandir}/fr/man8
install -p unhide-linux $RPM_BUILD_ROOT%{_bindir}
ln -sf unhide-linux $RPM_BUILD_ROOT%{_bindir}/unhide
install -p unhide-posix unhide-tcp unhide_rb $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt LEEME.txt LISEZ-MOI.TXT NEWS TODO changelog
%{_bindir}/unhide
%attr(755,root,root) %{_bindir}/unhide-linux
%attr(755,root,root) %{_bindir}/unhide-posix
%attr(755,root,root) %{_bindir}/unhide-tcp
%attr(755,root,root) %{_bindir}/unhide_rb
%{_mandir}/es/man8/unhide.8*
%{_mandir}/es/man8/unhide-tcp.8*
%{_mandir}/fr/man8/unhide.8*
%{_mandir}/fr/man8/unhide-tcp.8*
%{_mandir}/man8/unhide.8*
%{_mandir}/man8/unhide-tcp.8*

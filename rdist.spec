Summary:	Maintains identical copies of files on multiple machines
Name:		rdist
Version:	6.1.5
Release:	14
License:	BSD
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://www.MagniComp.com/download/rdist/%{name}-%{version}.tar.gz
Source1:	rdist-eu-license.txt
Patch0:		rdist-linux.patch
Patch1:		rdist-links.patch
Patch2:		rdist-oldpath.patch
Patch3:		rdist-hardlink.patch
Patch4:		rdist-glibc.patch
Patch5:		rdist-ostype.patch
URL:		http://www.MagniComp.com/rdist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rdist program maintains identical copies of files on multiple
hosts. If possible, rdist will preserve the owner, group, mode and
mtime of files and it can update programs that are executing.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__make} OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,8},%{_sbindir}}

install -s src/rdist $RPM_BUILD_ROOT%{_bindir}
install -s src/rdistd $RPM_BUILD_ROOT%{_sbindir}
ln -sf ../sbin/rdistd $RPM_BUILD_ROOT%{_bindir}/rdistd

install doc/rdist.man $RPM_BUILD_ROOT%{_mandir}/man1/rdist.1
install doc/rdistd.man $RPM_BUILD_ROOT%{_mandir}/man8/rdist.8

install %{SOURCE1} doc/

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* doc/rdist-eu-license.txt README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz doc/rdist-eu-license.txt.gz
%attr(755,root,root) %{_bindir}/rdist
%attr(755,root,root) %{_bindir}/rdistd
%attr(755,root,root) %{_sbindir}/rdistd
%{_mandir}/man[18]/*

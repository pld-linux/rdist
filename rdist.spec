Summary:	Maintains identical copies of files on multiple machines
Name:		rdist
Version:	6.1.5
Release:	7
License:	BSD
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://www.MagniComp.com/download/rdist/%{name}-%{version}.tar.gz
Patch0:		rdist-6.1.5-linux.patch
Patch1:		rdist-6.1.5-links.patch
Patch2:		rdist-6.1.5-oldpath.patch
URL:		http://www.MagniComp.comA/rdist
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

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{bin,man/man1,man/man8,sbin}

install -s src/rdist $RPM_BUILD_ROOT%{_bindir}
install -s src/rdistd $RPM_BUILD_ROOT%{_sbindir}
ln -sf ../sbin/rdistd $RPM_BUILD_ROOT%{_bindir}/rdistd

install doc/rdist.man $RPM_BUILD_ROOT%{_mandir}/man1/rdist.1
install doc/rdistd.man $RPM_BUILD_ROOT%{_mandir}/man8/rdist.8

gzip -9nf $RPM_BUILD_ROOT{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/rdist
%attr(755,root,root) %{_bindir}/rdistd
%attr(755,root,root) %{_sbindir}/rdistd
%{_mandir}/man[18]/*

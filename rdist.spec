Summary: Maintains identical copies of files on multiple machines.
Name: rdist
Version: 6.1.5
Release: 7
Copyright: BSD
Group: Applications/System
Source: http://www.MagniComp.com/download/rdist/rdist-%{version}.tar.gz
Patch0: rdist-6.1.5-linux.patch
Patch1: rdist-6.1.5-links.patch
Patch2: rdist-6.1.5-oldpath.patch
URL: http://www.MagniComp.comA/rdist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rdist program maintains identical copies of files on multiple
hosts.  If possible, rdist will preserve the owner, group, mode and
mtime of files and it can update programs that are executing.

%prep
%setup -q

%patch0 -p1 -b .linux
%patch1 -p1 -b .links
%patch2 -p1 -b .oldpath

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,man/man8,sbin}

install -s -m755 src/rdist $RPM_BUILD_ROOT/usr/bin
install -s -m755 src/rdistd $RPM_BUILD_ROOT/usr/sbin
ln -sf ../sbin/rdistd $RPM_BUILD_ROOT/usr/bin/rdistd

install -m644 doc/rdist.man $RPM_BUILD_ROOT/usr/man/man1/rdist.1
install -m644 doc/rdistd.man $RPM_BUILD_ROOT/usr/man/man8/rdist.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/bin/rdist
/usr/bin/rdistd
/usr/sbin/rdistd
/usr/man/man1/rdist.1
/usr/man/man8/rdist.8

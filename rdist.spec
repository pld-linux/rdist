Summary:	Maintains identical copies of files on multiple machines
Summary(de):	Dateienverteiler - Verwaltung von Dateien auf mehreren Computern
Summary(fr):	Distributeur de fichiers - maintien des fichiers sur différentes machines
Summary(tr):	Dosyalarý birden fazla makinada saklama sistemi
Name:		rdist
Version:	6.1.5
Release:	15
License:	BSD
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://www.MagniComp.com/download/rdist/%{name}-%{version}.tar.gz
Source1:	%{name}-eu-license.txt
Patch0:		%{name}-linux.patch
Patch1:		%{name}-links.patch
Patch2:		%{name}-oldpath.patch
Patch3:		%{name}-hardlink.patch
Patch4:		%{name}-glibc.patch
Patch5:		%{name}-ostype.patch
Patch6:		rdist-environ.patch
URL:		http://www.MagniComp.com/rdist/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	bison

%description
The rdist program maintains identical copies of files on multiple
hosts. If possible, rdist will preserve the owner, group, mode and
mtime of files and it can update programs that are executing.

%description -l de
Rdist ist ein Programm zur Aufrechterhaltung identischer Kopien von
Dateien über mehrere Hostrechner. Es behält den Besitzer, die Gruppe,
den Modus und mtime der Dateien wenn irgend möglich bei, und kann
Programme, die ausgeführt werden, aktualisieren.

%description -l fr
Rdist est un programme pour maintenir des copies d'un même fichier
identiques sur plusieurs machines. Il conserve le propriétaire, le
groupe, le mode, et la date des fichiers si possible et peut mettre à
jour les programmes qu'ils utilisent.

%description -l tr
rdist ile bir programýn birden fazla kopyasýnýn deðiþik makinalarda
ayný kullanýcý, grup ve kip bilgileri ile saklanmasý saðlanýr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0

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

Summary:	Maintains identical copies of files on multiple machines
Summary(de):	Dateienverteiler - Verwaltung von Dateien auf mehreren Computern
Summary(fr):	Distributeur de fichiers - maintien des fichiers sur diff�rentes machines
Summary(pl):	Narz�dzie do zarz�dzania identycznymi kopiami plik�w na wielu maszynach
Summary(tr):	Dosyalar� birden fazla makinada saklama sistemi
Name:		rdist
Version:	6.1.5
Release:	16
License:	BSD
Group:		Applications/System
Source0:	http://www.MagniComp.com/download/rdist/%{name}-%{version}.tar.gz
# Source0-md5:	546779700af70aa5f9103e08782cdcac
Source1:	%{name}-eu-license.txt
Patch0:		%{name}-linux.patch
Patch1:		%{name}-links.patch
Patch2:		%{name}-oldpath.patch
Patch3:		%{name}-hardlink.patch
Patch4:		%{name}-glibc.patch
Patch5:		%{name}-ostype.patch
Patch6:		%{name}-environ.patch
Patch7:		%{name}-bison.patch
Patch8:		%{name}-varargs.patch
URL:		http://www.MagniComp.com/rdist/
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rdist program maintains identical copies of files on multiple
hosts. If possible, rdist will preserve the owner, group, mode and
mtime of files and it can update programs that are executing.

%description -l de
Rdist ist ein Programm zur Aufrechterhaltung identischer Kopien von
Dateien �ber mehrere Hostrechner. Es beh�lt den Besitzer, die Gruppe,
den Modus und mtime der Dateien wenn irgend m�glich bei, und kann
Programme, die ausgef�hrt werden, aktualisieren.

%description -l fr
Rdist est un programme pour maintenir des copies d'un m�me fichier
identiques sur plusieurs machines. Il conserve le propri�taire, le
groupe, le mode, et la date des fichiers si possible et peut mettre �
jour les programmes qu'ils utilisent.

%description -l pl
Program rdist zarz�dza identycznymi kopiami plik�w na wielu maszynach.
Je�eli to mo�liwe, zachowuje w�a�ciciela, grup�, uprawnienia i czas
modyfikacji plik�w.

%description -l tr
rdist ile bir program�n birden fazla kopyas�n�n de�i�ik makinalarda
ayn� kullan�c�, grup ve kip bilgileri ile saklanmas� sa�lan�r.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p1
%patch8 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,8},%{_sbindir}}

install src/rdist $RPM_BUILD_ROOT%{_bindir}
install src/rdistd $RPM_BUILD_ROOT%{_sbindir}
ln -sf ../sbin/rdistd $RPM_BUILD_ROOT%{_bindir}/rdistd

install doc/rdist.man $RPM_BUILD_ROOT%{_mandir}/man1/rdist.1
install doc/rdistd.man $RPM_BUILD_ROOT%{_mandir}/man8/rdist.8

install %{SOURCE1} doc/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/rdist-eu-license.txt
%attr(755,root,root) %{_bindir}/rdist
%attr(755,root,root) %{_bindir}/rdistd
%attr(755,root,root) %{_sbindir}/rdistd
%{_mandir}/man[18]/*

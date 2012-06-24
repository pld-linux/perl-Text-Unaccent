#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Unaccent
Summary:	Text::Unaccent - remove accents from a string
Summary(pl):	Text::Unaccent - usuwanie akcent�w z napis�w
Name:		perl-Text-Unaccent
Version:	1.01
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Unaccent is a module that provides functions to remove accents
from a string.  For instance the string �t� will become ete.  The
charset of the input string is specified as an argument. The input is
converted to UTF-16 using iconv(3), accents are stripped and the
result is converted back to the original charset. The iconv --list
command on GNU/Linux will show all charset supported.

Text-Unaccent-1.01 has the same unac.[ch] files than unac-1.1.0.

%description -l pl
Text::Unaccent to modu� dostarczaj�cy funkcje do usuwania akcent�w z
napis�w. Na przyk�ad tekst �t� zostanie zamieniony na ete. Zestaw
znak�w �a�ucha wej�ciowego jest podawany jako argument. Wej�cie jest
konwertowane do UTF-16 przy u�yciu iconv(3), usuwane s� akcenty, a
wynik jest konwertowany z powrotem do oryginalnego zestawu znak�w.
Obs�ugiwane zestawy znak�w mo�na sprawdzi� poleceniem iconv --list.

Text-Unaccent-1.01 ma te same pliki unac.[ch] co unac-1.1.0.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	LIBS= \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/Text/*.pm
%dir %{perl_vendorarch}/auto/Text/Unaccent
%{perl_vendorarch}/auto/Text/Unaccent/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Unaccent/*.so
%{_mandir}/man3/*

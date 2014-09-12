#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Unaccent
Summary:	Text::Unaccent - remove accents from a string
Summary(pl.UTF-8):	Text::Unaccent - usuwanie akcentów z napisów
Name:		perl-Text-Unaccent
Version:	1.08
Release:	6
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ac9b28cbb66f4829a50d563ace79cb5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Unaccent is a module that provides functions to remove accents
from a string. For instance the string été will become ete. The
charset of the input string is specified as an argument. The input is
converted to UTF-16 using iconv(3), accents are stripped and the
result is converted back to the original charset. The iconv --list
command on GNU/Linux will show all charset supported.

Text-Unaccent-1.01 has the same unac.[ch] files than unac-1.1.0.

%description -l pl.UTF-8
Text::Unaccent to moduł dostarczający funkcje do usuwania akcentów z
napisów. Na przykład tekst été zostanie zamieniony na ete. Zestaw
znaków łańcucha wejściowego jest podawany jako argument. Wejście jest
konwertowane do UTF-16 przy użyciu iconv(3), usuwane są akcenty, a
wynik jest konwertowany z powrotem do oryginalnego zestawu znaków.
Obsługiwane zestawy znaków można sprawdzić poleceniem iconv --list.

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
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Unaccent/*.so
%{_mandir}/man3/*

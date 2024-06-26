#
# Conditional build:
%bcond_with	tests	# unit tests
#
%define	pdir	Net
%define	pnam	DNS-SEC
Summary:	Net::DNS::SEC - DNSSEC extensions to Net::DNS
Summary(pl.UTF-8):	Net::DNS::SEC - rozszerzenia DNSSEC do Net::DNS
Name:		perl-Net-DNS-SEC
Version:	1.24
Release:	2
License:	MIT
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	63879e0f104320f63633be7d4b02b851
URL:		https://metacpan.org/dist/Net-DNS-SEC
BuildRequires:	openssl-devel
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.48
BuildRequires:	perl-devel >= 1:5.8.9
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(DynaLoader) >= 1.04
BuildRequires:	perl(Exporter) >= 5.56
BuildRequires:	perl(File::Find) >= 1.13
BuildRequires:	perl(File::Spec) >= 3.29
BuildRequires:	perl(IO::File) >= 1.14
BuildRequires:	perl-Carp >= 1.10
BuildRequires:	perl-Digest-SHA >= 5.23
BuildRequires:	perl-MIME-Base64 >= 3.07
BuildRequires:	perl-Net-DNS >= 1.08
BuildRequires:	perl-Test-Simple >= 0.80
%endif
Requires:	perl-Digest-SHA >= 5.23
Requires:	perl-MIME-Base64 >= 3.07
Requires:	perl-Net-DNS >= 1.08
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::DNS::SEC suite provides the resource records that are needed
for DNSSEC (RFC 4033, 4034 and 4035). In addition the DLV RR, a clone
of the DS RR is supported (RFC 4431)

It also provides support for SIG0. That later is useful for dynamic
updates using key-pairs.

RSA and DSA crypto routines are supported.

Net::DNS contains all needed hooks to load the Net::DNS::SEC
extensions when they are available.

%description -l pl.UTF-8
Moduły Net::DNS::SEC udostępniają rekordy porzebne do obsługi DNSSEC
(RFC 4033, 4034 oraz 4035). Poza DLV RR obsługiwany jest też klon DS
RR (RFC 4431).

Pakiet udostępnia także obsługę SIG0. Jest to przydatne do
dynamicznych uaktualnień przy użyciu par kluczy.

Procedury kryptograficzne RSA i DSA są także obsługiwane.

Moduł Net::DNS zawiera wszystkie uchwyty konieczne do wczytywania
rozszerzeń Net::DNS::SEC w razie potrzeby.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%dir %{perl_vendorarch}/auto/Net/DNS
%dir %{perl_vendorarch}/auto/Net/DNS/SEC
%attr(755,root,root) %{perl_vendorarch}/auto/Net/DNS/SEC/SEC.so
%{perl_vendorarch}/Net/DNS/SEC.pm
%{perl_vendorarch}/Net/DNS/SEC
%{_mandir}/man3/Net::DNS::SEC*.3pm*

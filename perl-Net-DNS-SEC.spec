#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNS-SEC
Summary:	Net::DNS::SEC - DNSSEC extensions to Net::DNS
Summary(pl.UTF-8):	Net::DNS::SEC - rozszerzenia DNSSEC do Net::DNS
Name:		perl-Net-DNS-SEC
Version:	1.02
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3d11216697d0fe43e74484b59f94188d
URL:		http://search.cpan.org/dist/Net-DNS-SEC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-OpenSSL-Bignum >= 0.03
BuildRequires:	perl-Crypt-OpenSSL-DSA >= 0.1
BuildRequires:	perl-Crypt-OpenSSL-RSA >= 0.19
BuildRequires:	perl-Digest-BubbleBabble >= 0.01
BuildRequires:	perl-Digest-SHA >= 5.23
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-MIME-Base32
BuildRequires:	perl-Net-DNS >= 0.64
BuildRequires:	perl-Test-Simple >= 0.47
%endif
Requires:	perl-Crypt-OpenSSL-Bignum >= 0.03
Requires:	perl-Crypt-OpenSSL-DSA >= 0.1
Requires:	perl-Crypt-OpenSSL-RSA >= 0.19
Requires:	perl-Digest-SHA >= 5.23
Requires:	perl-Net-DNS >= 0.64
BuildArch:	noarch
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
%doc Changes README
%{perl_vendorlib}/Net/DNS/SEC.pm
%{perl_vendorlib}/Net/DNS/SEC
%{_mandir}/man3/Net::DNS::SEC*.3pm*

#
# Conditional build:
%bcond_with	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNS-SEC
Summary:	Net::DNS::SEC - DNSSEC extensions to Net::DNS
Summary(pl.UTF-8):	Net::DNS::SEC - rozszerzenie DNSSEC do Net::DNS
Name:		perl-Net-DNS-SEC
Version:	0.16
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70a8b59dda39a0effe22bfc12905d942
URL:		http://search.cpan.org/dist/Net-DNS-SEC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MIME::Base32)
BuildRequires:	perl-Crypt-OpenSSL-Bignum >= 0.03
BuildRequires:	perl-Crypt-OpenSSL-DSA >= 0.1
BuildRequires:	perl-Crypt-OpenSSL-RSA >= 0.19
BuildRequires:	perl-Digest-BubbleBabble >= 0.01
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Net-DNS >= 0.64
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::DSN::SEC suite provides the resource records that are needed
for DNSSEC (RFC 4033, 4034 and 4035). In addition the DLV RR, a clone
of the DS RR is supported (RFC 4431)

It also provides support for SIG0. That later is useful for dynamic
updates using key-pairs.

RSA and DSA crypto routines are supported.

For details see Net::DNS::RR::RRSIG, Net::DNS::RR::DNSKEY,
Net::DNS::RR::NSEC, Net::DNS::RR:DS, Net::DNS::RR::DLV, and see
Net::DNS::RR::SIG and Net::DNS::RR::KEY for the use with SIG0.

Net::DNS contains all needed hooks to load the Net::DNS::SEC
extensions when they are available.

# %description -l pl.UTF-8 # TODO

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
%doc Changes README TODO
%{perl_vendorlib}/Net/DNS/*.pm
%dir %{perl_vendorlib}/Net/DNS/RR
%{perl_vendorlib}/Net/DNS/RR/*.pm
%{perl_vendorlib}/Net/DNS/SEC
%{_mandir}/man3/*

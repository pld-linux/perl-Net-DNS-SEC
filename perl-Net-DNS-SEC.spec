#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNS-SEC
Summary:	Net::DNS::SEC - DNSSEC extensions to Net::DNS
Summary(pl.UTF-8):   Net::DNS::SEC - rozszerzenia DNSSEC dla Net::DNS
Name:		perl-Net-DNS-SEC
Version:	0.12
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	546a1776b23860d510b15303709456e9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-OpenSSL-Bignum >= 0.03
BuildRequires:	perl-Crypt-OpenSSL-DSA >= 0.1
BuildRequires:	perl-Crypt-OpenSSL-RSA >= 0.19
BuildRequires:	perl-Digest-BubbleBabble >= 0.01
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Net-DNS >= 0.44
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::DNS::SEC suit provides the resource records that are
needed for Secure DNS (RFC2535). DNSSEC is a protocol that is still
under development.

%description -l pl.UTF-8
Pakiet Net::DNS::SEC dostarcza rekordy zasobów potrzebne do obsługi
Secure DNS (RFC2535). DNSSEC jest protokołem będącym jeszcze w
stadium rozwoju.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
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
%doc Changes README TODO
%{perl_vendorlib}/Net/DNS/*.pm
%{perl_vendorlib}/Net/DNS/RR/*.pm
%{perl_vendorlib}/Net/DNS/RR/SIG/*.pm
%{perl_vendorlib}/Net/DNS/SEC
%{_mandir}/man3/*

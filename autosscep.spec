Summary:	Simple automatic certificate enroller
Name:		autosscep
Version:	0.9.28b
Release:	%mkrel 3
License:	BSD-like
Group:		Networking/Other
URL:		http://autosscep.spe.net/
Source0:	http://autosscep.spe.net/archives/autoSscep-%{version}.tar.bz2
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
AUTOSSCEP is an automatic x509 certificate enroller based on SCEP
(Simple Certificate Enrollment Protocol). It provides VPN users an
easy maintenance of their certificates. It was developed in S.P.E.
laboratories starting from Sscep client by Jarkko Turkulainen and
it's based on OpenSSL toolkit library

%prep

%setup -q -n autoSscep-%{version}

# fix strange perms
chmod 644 *

%build

make CFLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}/
install -m0755 autosscep %{buildroot}%{_sbindir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT EMPTYCONFIG ERRORS HOWTOCONFIGURE-Eng HOWTOCONFIGURE-Ita README
%{_sbindir}/autosscep

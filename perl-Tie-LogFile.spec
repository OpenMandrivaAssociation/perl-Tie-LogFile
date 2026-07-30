%define upstream_version 0.1
%define module	Tie-LogFile
Summary:	Interface for maintaining a log
Name:		perl-%{module}
Version:	0.1
Release:	2
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/%{module}
Source0:	https://cpan.metacpan.org/authors/id/C/CR/CREIN/Tie-LogFile-0.1.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Tie::LogFile gives a easy interface for maintaining a well formated log. Using
user tweakable sprintf like tags, Tie::LogFile is flexible, and probably a
little overkill for keeping a log.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Tie
%{_mandir}/man3/Tie*




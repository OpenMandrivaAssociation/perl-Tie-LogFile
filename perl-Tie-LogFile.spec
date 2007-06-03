
%define module	Tie-LogFile
%define name	perl-%{module}
%define version	0.1
%define rel	2

Summary:	Interface for maintaining a log
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%description
Tie::LogFile gives a easy interface for maintaining a well formated log. Using
user tweakable sprintf like tags, Tie::LogFile is flexible, and probably a
little overkill for keeping a log.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Tie
%{_mandir}/man3/Tie*


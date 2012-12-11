
%define module	Tie-LogFile
%define name	perl-%{module}
%define version	0.1
%define rel	3

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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1-3mdv2010.0
+ Revision: 430605
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1-2mdv2008.1
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jun 03 2007 Anssi Hannula <anssi@mandriva.org> 0.1-2mdv2008.0
+ Revision: 34883
- annual rebuild


* Sun May 28 2006 Anssi Hannula <anssi@mandriva.org> 0.1-1mdv2007.0
- initial Mandriva package


%define upstream_name    Pod-Xhtml
%define upstream_version 1.61

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Allow off-page links in POD to point to a URL
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		Pod-Xhtml-1.59-uri_escape.patch

BuildRequires:	perl-devel
BuildRequires:	perl(Pod::ParseUtils)
BuildRequires:	perl(Pod::Parser)
BuildRequires:	perl(Test::Assertions::TestScript)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI::Escape)

BuildArch:	noarch

%description
This is a module to translate POD to Xhtml. Lorem ipsum the Dolor/Dolor
manpage sit amet consectueur adipscing elit. Sed diam nomumny. This is a
module to translate POD to Xhtml. /Lorem ipsum dolor sit amet consectueur
adipscing elit. Sed diam nomumny. This is a module to translate _POD_ to
Xhtml. *Lorem* ipsum _dolor_ sit amet 'consectueur adipscing' elit. . This
is a module to translate POD to Xhtml. See the /Lorem manpage ipsum dolor
sit amet consectueur adipscing elit. Sed diam the nomumny manpage. the
http://foo.bar/baz/ manpage

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# https://rt.cpan.org/Public/Bug/Display.html?id=56324
%patch0 -p1 -b .uri

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/pod2xhtml

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.610.0-2mdv2011.0
+ Revision: 653883
- update file list
- rebuild for updated spec-helper

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.610.0-1mdv2011.0
+ Revision: 569952
- update to 1.61

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.590.0-1mdv2011.0
+ Revision: 552240
- fix rt#56324 - test failure with newer uri::escape

* Sat Jul 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.590.0-1mdv2010.0
+ Revision: 394682
- adding missing buildrequires:
- import perl-Pod-Xhtml


* Sat Jul 11 2009 cpan2dist 1.59-1mdv
- initial mdv release, generated with cpan2dist

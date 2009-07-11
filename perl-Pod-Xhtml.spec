%define upstream_name    Pod-Xhtml
%define upstream_version 1.59

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Allow off-page links in POD to point to a URL
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Pod::ParseUtils)
BuildRequires: perl(Pod::Parser)
BuildRequires: perl(Test::Assertions::TestScript)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Escape)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/pod2xhtml
/usr/share/man/man1/pod2xhtml.1.lzma


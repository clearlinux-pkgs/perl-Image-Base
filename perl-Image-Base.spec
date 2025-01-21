#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Image-Base
Version  : 1.17
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Image-Base-1.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Image-Base-1.17.tar.gz
Summary  : Base class for image manipulation
Group    : Development/Tools
License  : LGPL-2.0
Requires: perl-Image-Base-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
=head1 NAME
Image::Base - base class for loading, manipulating and saving images.

%package dev
Summary: dev components for the perl-Image-Base package.
Group: Development
Provides: perl-Image-Base-devel = %{version}-%{release}
Requires: perl-Image-Base = %{version}-%{release}

%description dev
dev components for the perl-Image-Base package.


%package perl
Summary: perl components for the perl-Image-Base package.
Group: Default
Requires: perl-Image-Base = %{version}-%{release}

%description perl
perl components for the perl-Image-Base package.


%prep
%setup -q -n Image-Base-1.17
cd %{_builddir}/Image-Base-1.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Image::Base.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

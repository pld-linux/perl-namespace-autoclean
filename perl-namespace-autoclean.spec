#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	namespace
%define	pnam	autoclean
Summary:	namespace::autoclean removes all imported symbols at the end of compile cycle
Summary(pl.UTF-8):	namespace::autoclean usuwa wszystkie zaimportowane symbole pod koniec cyklu kompilacji
Name:		perl-namespace-autoclean
Version:	0.29
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/namespace/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	39b38c776cd1f0ee03cc70781a2f2798
URL:		https://metacpan.org/release/namespace-autoclean
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-B-Hooks-EndOfScope >= 0.12
BuildRequires:	perl-Sub-Identify
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-namespace-clean >= 0.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When you import a function into a Perl package, it will naturally also
be available as a method.

The namespace::autoclean pragma will remove all imported symbols at
the end of the current package's compile cycle. Functions called in
the package itself will still be bound by their name, but they won't
show up as methods on your class or instances.

This module is very similar to namespace::clean, except it will clean
all imported functions, no matter if you imported them before or after
you used the pagma. It will also not touch anything that looks like a
method, according to Class::MOP::Class::get_method_list.

%description -l pl.UTF-8
namespace::autoclean usuwa wszystkie zaimportowane symbole pod koniec
cyklu kompilacji

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
%doc Changes README
%{perl_vendorlib}/namespace/*.pm
%{_mandir}/man3/*

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_IPC_SysV_enables_optional_test
%else
%bcond_with perl_IPC_SysV_enables_optional_test
%endif

Name:           perl-IPC-SysV
Version:        2.09
Release:        1%{?dist}
Summary:        Object interface to System V IPC
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IPC-SysV
Source0:        https://cpan.metacpan.org/authors/id/M/MH/MHX/IPC-SysV-%{version}.tar.gz
%if !%{with perl_IPC_SysV_enables_optional_test} || %{defined perl_bootstrap}
BuildRequires:  coreutils
%endif
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More) >= 0.45
BuildRequires:  perl(warnings)
%if %{with perl_IPC_SysV_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.10
BuildRequires:  perl(Test::Pod) >= 0.95
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Conflicts:      perl < 4:5.22.0-351

%description
This is an object interface for System V messages, semaphores, and
inter-process calls.

%prep
%setup -q -n IPC-SysV-%{version}
%if !%{with perl_IPC_SysV_enables_optional_test} || %{defined perl_bootstrap}
rm t/pod*
perl -i -ne 'print $_ unless m{^t/pod}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset PERL_CORE
make test

%files
%doc Changes README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/IPC*
%{_mandir}/man3/*

%changelog
* Mon Nov 16 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-1
- 2.09 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-2
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Petr Pisar <ppisar@redhat.com> - 2.08-1
- 2.08 bump

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-456
- Increase release to favour standalone package

* Wed Feb 05 2020 Petr Pisar <ppisar@redhat.com> - 2.07-442
- Modernize the spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-441
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-397
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-2
- Perl 5.24 rebuild

* Tue May 10 2016 Petr Pisar <ppisar@redhat.com> - 2.07-1
- 2.07 bump

* Mon Feb 29 2016 Petr Pisar <ppisar@redhat.com> - 2.06-1
- 2.06 bump

* Mon Feb 15 2016 Petr Pisar <ppisar@redhat.com> 2.05-1
- Specfile autogenerated by cpanspec 1.78.

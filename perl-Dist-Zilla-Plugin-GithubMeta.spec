%define upstream_name    Dist-Zilla-Plugin-GithubMeta
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Automatically include GitHub meta information in META.yml
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::Role::MetaProvider)
BuildRequires: perl(IPC::Cmd)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types::URI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Dist::Zilla::Plugin::GithubMeta is a the Dist::Zilla manpage plugin to
include GitHub the http://github.com manpage meta information in
'META.yml'.

It automatically detects if the distribution directory is under 'git'
version control and whether the 'origin' is a GitHub repository and will
set the 'repository' and 'homepage' meta in 'META.yml' to the appropriate
URLs for GitHub.

Based on the Module::Install::GithubMeta manpage which was based on the
Module::Install::Repository manpage by Tatsuhiko Miyagawa

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml LICENSE README META.json Changes
%{_mandir}/man3/*
%perl_vendorlib/*



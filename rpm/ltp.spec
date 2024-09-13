%define _name ltp
%define _prefix /opt/%{_name}

Name:       %{_name}
Summary:    Linux Test Project (LTP)
Version:    0.20250130.0
Release:    0
License:    GPLv2
URL:        https://github.com/mer-qa/ltp
Source0:    %{name}-%{version}.tar.gz
Patch1:     0001-Disable-broken-test-case.patch
Requires:   expect
Requires:   mailcap
Requires:   perl-Compress-Zlib
Requires:   perl-HTML-Parser
Requires:   perl-HTML-Tagset
Requires:   perl-libwww-perl
Requires:   perl-URI
Requires:   python3-base
Requires:   tcl
BuildRequires: automake
BuildRequires: sed

%description
The LTP testsuite contains a collection of tools for testing the Linux kernel and related features.

%prep
%autosetup -p1 -n %{name}-%{version}/ltp

%build
make autotools
%configure
%make_build

%install
%make_install
find %{buildroot}%{_prefix} -name "*.obj" | xargs rm -f --
rm -rf %{buildroot}%{_prefix}/testcases/bin/nmfile.c
rm -rf %{buildroot}%{_prefix}/testcases/bin/nmfile1.c
rm -rf %{buildroot}%{_prefix}/testcases/bin/nmfile2.c
rm -rf %{buildroot}%{_prefix}/testcases/bin/nmfile3.c
# remove executable bit from data files
find %{buildroot}%{_prefix}/testcases/data -type f | xargs chmod a-x

%files
%{_prefix}/*

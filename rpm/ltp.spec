%define _name ltp
%define _prefix /opt/%{_name}

Name:       %{_name}
Summary:    Linux Test Project (LTP)
Version:    0.20150420.1
Release:    1
Group:      Kernel/Linux Kernel
License:    GPLv2
URL:        http://ltp.sourceforge.net/
Source0:    %{name}-%{version}.tar.gz
Patch0:     0001-Remove-unsupported-csh-and-ksh.patch
Requires:   expect
Requires:   mailcap
Requires:   perl-Compress-Zlib
Requires:   perl-HTML-Parser
Requires:   perl-HTML-Tagset
Requires:   perl-libwww-perl
Requires:   perl-URI
Requires:   python3-base
Requires:   tcl
BuildRequires: sed

%description
The LTP testsuite contains a collection of tools for testing the Linux kernel and related features.

%prep
%setup -q -n %{name}-%{version}/ltp
%patch0 -p1

%build
make autotools
%configure
make %{?jobs:-j%jobs}

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
%defattr(-,root,root,-)
%{_prefix}/*


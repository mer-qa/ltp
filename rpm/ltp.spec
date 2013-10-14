%define _name ltp
%define _prefix /opt/%{_name}

Name:       %{_name}
Summary:    Linux Test Project (LTP)
Version:    0.20130904.1
Release:    1
Group:      Kernel/Linux Kernel
License:    GPLv2
URL:        http://ltp.sourceforge.net/
Source0:    %{name}-%{version}.tar.gz
Source1:    ltp_create_xml.sh
Requires:   expect
Requires:   mailcap
Requires:   perl-Compress-Zlib
Requires:   perl-HTML-Parser
Requires:   perl-HTML-Tagset
Requires:   perl-libwww-perl
Requires:   perl-URI
Requires:   tcl

%package tests
Summary:    Tests xml for LTP tests
Requires:   %{name} blts-tools

%description
The LTP testsuite contains a collection of tools for testing the Linux kernel and related features.

%description tests
This package contains tests.xml for The LTP testsuite.

%prep
%setup -q

%build
cd ltp
make autotools
%configure
make %{?jobs:-j%jobs}

%install
cd ltp
%make_install
find %{buildroot}%{_prefix} -name "*.obj" | xargs rm
rm -rf %{buildroot}%{_prefix}/testcases/bin/nmfile.c
rm -rf %{buildroot}%{_prefix}/testcases/bin/nmfile1.c
rm -rf %{buildroot}%{_prefix}/testcases/bin/nmfile2.c
rm -rf %{buildroot}%{_prefix}/testcases/bin/nmfile3.c
install -d -m 755 %{buildroot}/opt/tests/ltp-tests/
sh %{SOURCE1} %{_builddir}/%{name}-%{version}/ltp/runtest/ltplite > %{buildroot}/opt/tests/ltp-tests/tests.xml

%files
%defattr(-,root,root,-)
%{_prefix}/*

%files tests
%defattr(-,root,root,-)
/opt/tests/ltp-tests/tests.xml

%global debug_package %{nil}

Name:           dust
Version:        1.1.2
Release:        1%{?dist}
Summary:        du + rust = dust. Like du but more intuitive
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/bootandy/%{name}
BuildRequires:  cmake
BuildRequires:  cargo, rust
Source:         https://github.com/bootandy/%{name}/archive/v%{version}.tar.gz

%description
Dust is meant to give you an instant overview of which directories are
using disk space without requiring sort or head. Dust will print a
maximum of 1 'Did not have permissions message'.

Dust will list the 20 biggest sub directories or files and will smartly
recurse down the tree to find the larger ones. There is no need for a
'-d' flag or a '-h' flag. The largest sub directory will have its size
shown in red

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/dust %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE* *.md
/usr/bin/dust

%changelog
* Fri Feb 28 2025 Jamie Curnow <jc@jc21.com> - 1.1.2-1
- v1.1.2

* Tue Mar 26 2024 Jamie Curnow <jc@jc21.com> - 1.0.0-1
- v1.0.0

* Tue May 9 2023 Jamie Curnow <jc@jc21.com> - 0.8.6-1
- v0.8.6

* Fri Feb 3 2023 Jamie Curnow <jc@jc21.com> - 0.8.4-1
- v0.8.4

* Thu Sep 1 2022 Jamie Curnow <jc@jc21.com> - 0.8.3-1
- v0.8.3

* Tue Aug 23 2022 Jamie Curnow <jc@jc21.com> - 0.8.2-1
- v0.8.2

* Sat Feb 26 2022 Jamie Curnow <jc@jc21.com> - 0.8.0-1
- v0.8.0

* Mon Sep 20 2021 Jamie Curnow <jc@jc21.com> - 0.7.5-1
- v0.7.5

* Fri Aug 6 2021 Jamie Curnow <jc@jc21.com> - 0.6.2-1
- v0.6.2

* Tue Jul 20 2021 Jamie Curnow <jc@jc21.com> - 0.6.1-1
- v0.6.1

* Wed Jun 23 2021 Jamie Curnow <jc@jc21.com> - 0.6.0-1
- v0.6.0

* Mon Jan 18 2021 Jamie Curnow <jc@jc21.com> - 0.5.4-1
- v0.5.4

* Mon Sep 7 2020 Jamie Curnow <jc@jc21.com> - 0.5.3-1
- v0.5.3

* Mon Aug 3 2020 Jamie Curnow <jc@jc21.com> - 0.5.2-1
- v0.5.2

* Mon Mar 2 2020 Jamie Curnow <jc@jc21.com> - 0.5.1-1
- v0.5.1

* Thu Feb 20 2020 Jamie Curnow <jc@jc21.com> - 0.5.0-1
- v0.5.0

* Tue Feb 4 2020 Jamie Curnow <jc@jc21.com> - 0.4.41-1
- v0.4.41

* Mon Feb 3 2020 Jamie Curnow <jc@jc21.com> - 0.4.4-1
- v0.4.4

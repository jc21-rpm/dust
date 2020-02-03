%global debug_package %{nil}

Name:           dust
Version:        0.4.4
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
* Mon Feb 3 2019 Jamie Curnow <jc@jc21.com> - 0.4.4-1
- v0.4.4

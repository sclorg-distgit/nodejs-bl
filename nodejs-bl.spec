# spec file for package nodejs-nodejs-bl
%{?scl:%scl_package nodejs-nodejs-bl}
%{!?scl:%global pkg_name %{name}}

%global npm_name bl
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-bl
Version:	1.0.0
Release:	2%{?dist}
Summary:	Buffer List: collect buffers and access with a standard readable Buffer interface, streamable too!
Url:		https://github.com/rvagg/bl
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(brtapsauce)
BuildRequires:	npm(faucet)
BuildRequires:	npm(hash_file)
BuildRequires:	npm(tape)
%endif

%description
Buffer List: collect buffers and access with a standard readable Buffer interface, streamable too!

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json bl.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
node test/test.js | faucet
%endif

%files
%{nodejs_sitelib}/bl

%doc README.md LICENSE.md

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-2
- rebuilt

* Fri Aug 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-1
- Initial build

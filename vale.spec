Name:          vale
Version:       2.28.0
Release:       1%{?dist}
Summary:       A syntax-aware, command-line linter for prose
License:       MIT
URL:           https://github.com/errata-ai/vale
Source0:       https://github.com/errata-ai/%{name}/releases/download/v%{version}/%{name}_%{version}_Linux_64-bit.tar.gz

# Workaround for Golang missing build IDs
# https://github.com/tpokorra/lbs-mono-fedora/issues/3#issuecomment-219857688
%undefine _missing_build_ids_terminate_build

%description
Vale is a CLI linter for collaborative writing.
Vale enables you to parse a variety of
markup-formatted files, such as Markdown,
AsciiDoc, reStructuredText, HTML, or XML,
and impose proper spelling or style guide.

%prep
%setup -qc

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
install -m 0755 %{name} ${RPM_BUILD_ROOT}/%{_bindir}/%{name}
# Workaround for rpmlint issue script-without-shebang
# https://fedoraproject.org/wiki/Common_Rpmlint_issues#script-without-shebang
# Also fixing spurious-executable-perm on README.md
chmod -x LICENSE README.md

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Jul 15 2022 - mczernek@redhat.com - 2.20.0-1
- Modify RPM specfile to prepare for Fedora packages submission
* Fri May 13 2022 Initial build
- Create an initial RPM spec

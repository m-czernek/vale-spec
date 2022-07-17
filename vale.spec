Name:          vale
Version:       2.20.0
Release:       1%{?dist}
Summary:       A syntax-aware, command-line linter for prose
License:       MIT
URL:           https://github.com/errata-ai/vale
Source0:       https://github.com/errata-ai/vale/archive/refs/tags/v%{version}.tar.gz
BuildRequires: golang, git

# Workaround for Golang missing build IDs
# https://github.com/tpokorra/lbs-mono-fedora/issues/3#issuecomment-219857688
%undefine _missing_build_ids_terminate_build

# Workaround for error: Empty files file
# https://lists.opensuse.org/archives/list/buildservice@lists.opensuse.org/message/C3LSCEDT5INK3PCFM3MXWD3B7IUJ32L2/
%global debug_package %{nil}

%description
Vale is a CLI linter for collaborative writing.
Vale enables you to parse a variety of
markup-formatted files, such as Markdown,
AsciiDoc, reStructuredText, HTML, or XML,
and impose proper spelling or style guide.

%prep
%setup -q

%build
%make_build

%install
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
install -m 0755 bin/%{name} ${RPM_BUILD_ROOT}/%{_bindir}/%{name}
# Workaround for W: spurious-executable-perm and
# E: script-without-shebang linting errors
chmod -x README.md LICENSE

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Jul 15 2022 - mczernek@redhat.com - 2.20.0-1
- Modify RPM specfile to prepare for Fedora packages submission
* Fri May 13 2022 Initial build
- Create an initial RPM spec

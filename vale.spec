Name:           vale
Version:        2.17.0
Release:        1%{?dist}
Summary:        A syntax-aware, command-line linter for prose built with speed and extensibility in mind.

License:       MIT 
URL:           https://github.com/errata-ai/vale 
Source0:       https://github.com/errata-ai/%{name}/releases/download/v%{version}/%{name}_%{version}_Linux_64-bit.tar.gz 

#BuildRequires:  
#Requires:       

%description
Vale is a CLI linter for collaborative writing. Vale enables you to parse a variety of markup-formatted files, such as Markdown, AsciiDoc, reStructuredText, HTML, or XML, and impose proper spelling or style guide.

%prep
%setup -qc

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
install -m 0755 %{name} ${RPM_BUILD_ROOT}/%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}



%changelog
* Fri May 13 2022 Initial build
- 

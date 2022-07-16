# Vale

This repository is a community maintained SPEC file for the 
[vale](https://github.com/errata-ai/vale) command-line tool.

## Installing Vale

On Fedora and CentOS, you can enable the `mczernek/vale` COPR repository and install the `vale` package:

```
dnf copr enable mczernek/vale
dnf install vale
```

On other systems, download and install the RPM manually.
You can either build the RPM, or download the RPM from the [COPR repository](https://copr.fedorainfracloud.org/coprs/mczernek/vale/).

## Building the RPM

To build the RPM, use the `fedpkg` command:

```
fedpkg --release f36 mockbuild --enable-network
```

To check linting rules, use the `rpmlint` command, for example:

```
rpmlint vale.spec results_vale/2.20.0/1.fc36/vale-2.20.0*.{x86_64,src}.rpm
```

## Filing Bugs

For issues with packaging, feel free to create an [issue](https://github.com/m-czernek/vale-spec/issues).
For other issues, [vale](https://github.com/errata-ai/vale/issues) is the proper place.

If you are unsure, feel free to create an issue here and I will redirect your issue if necessary.

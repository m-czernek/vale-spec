# Automate Building Vale repository

To automate building Vale, you can use the Copr - Github integration.
Every time you push commit to the repository, Copr starts an RPM build.
Consequently, to automate building Vale RPM, you must automate:

1. Checking and committing the latest version to the `vale.spec` file.
2. Configure Copr - Github integration.

## Prerequisites

This text assumes that you have forked this repository.

## Configuring vale.spec Version Automation

The RPM build relies on the version in the [vale.spec](https://github.com/m-czernek/vale-spec/blob/main/vale.spec#L2) file.
This repository contains the [automation](https://github.com/m-czernek/vale-spec/tree/main/automation) directory, which automates synchronizing the version with the upstream release version.

To set up the automation script:

1. Create a Python virtual environment in a directory of your choice.
In this example, the virtual env is in the `automation` directory.

````
cd /path/to/vale-spec/automation
python3 -m venv .venv
````

2. Source the virtual environment and install the automation script dependencies.

````
. .venv/bin/activate
pip install -r requirements.txt
````

3. Ensure that the script is executed periodically.
You can achieve this, for example, by using crontab.
Execute `crontab -e` and add the following entry:

````
0 * * * * /path/to/repo/vale-spec/automation/.venv/bin/python3 /path/to/repo//vale-spec/automation/main.py
````

This means that crontab executes the `main.py` automation script every hour.

## Configuring Copr - Github Integration

Copr is the build environment that can download an RPM spec file and execute a build.

To configure a project:

1. Create an account at https://copr.fedorainfracloud.org
2. Create a project.
Select the build options that you want to support.
Vale is a single binary, so it should work on any `x86_64` Linux distribution.
See https://copr.fedorainfracloud.org/coprs/mczernek/vale/ for information about the most used build options.
*Important*: You must enable the `Enable internet access during builds` option.

4. In your project, click `packages` and define your `vale` package.
Use your fork repository URL in the `clone URL` field.
*Important*: You must enable the `Auto-rebuild the package? (i.e. every commit or new tag)` option.
Create that package.

5. Click `settings -> integrations` and copy the first Github URL, for example `https://copr.fedorainfracloud.org/webhooks/github/1234/abcdef...ghijk/`.
6. Open your vale-spec fork, for example `https://github.com/m-czernek/vale-spec`, and click `settings`.
7. Click `webhooks -> add webhook`.
8. Paste the URL from step 5. 
Configure the `content type` to `application/json` and click `add webhook`.


You should now have a working automation. When github.com/errata-ai/vale contains a new release, the next hour that your laptop is on, crontab executes the script, which updates the `vale.spec` file.
Then, Github sends a webhook request to Copr to rebuild the Vale package.

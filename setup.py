# Don't import __future__ packages here; they make setup fail

# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

with open("README.pypi.rst") as readmeFile:
    long_description = readmeFile.read()

install_requires = []
with open("requirements.txt") as requirementsFile:
    for line in requirementsFile:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        pinnedVersion = line.split()[0]
        install_requires.append(pinnedVersion)

dependency_links = []

try:
    with open("constraints.txt") as constraintsFile:
        for line in constraintsFile:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == '#':
                continue
            dependency_links.append(line)
except EnvironmentError:
    print('No constraints file found, proceeding without '
          'creating dependency links.')

setup(
    name="candig_client",
    description="A client for the CanDIG server",
    packages=["ga4gh", "ga4gh.client"],
    namespace_packages=["ga4gh"],
    url="https://github.com/CanDIG/candig-client",
    use_scm_version={"write_to": "ga4gh/client/_version.py"},
    entry_points={
        'console_scripts': [
            'ga4gh_client=ga4gh.client.cli:client_main',
            'candig_client=ga4gh.client.cli:client_main'
        ]
    },
    long_description=long_description,
    install_requires=install_requires,
    dependency_links=dependency_links,
    license='Apache License 2.0',
    include_package_data=True,
    zip_safe=True,
    author="CanDIG Team",
    author_email="info@distributedgenomics.ca",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    keywords=['genomics', 'CanDIG'],
    # Use setuptools_scm to set the version number automatically from Git
    setup_requires=['setuptools_scm'],
)

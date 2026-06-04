---
sourceFile: "Charts | Helm"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.275Z"
---

# Charts | Helm

51ca77d6-84d9-4867-aa62-925efef263d9

Charts | Helm

ed781c36-613e-4c7d-b77e-af0973ced1a3

https://helm.sh/docs/topics/charts/

Charts | Helm

Skip to main content

https://helm.sh/docs/topics/charts/#\_\_docusaurus\_skipToContent\_fallback

🎉 Helm v4.0.0 is out! See the

Helm 4 Overview

https://helm.sh/docs/overview

for details!

https://helm.sh/

https://helm.sh/docs

https://helm.sh/community

https://helm.sh/blog

https://artifacthub.io/

https://helm.sh/docs/topics/charts

https://helm.sh/docs/topics/charts

https://helm.sh/docs/v3/topics/charts

https://helm.sh/docs/v2/

https://helm.sh/docs/topics/charts/

https://helm.sh/docs/topics/charts

Deutsch (German)

https://helm.sh/de/docs/topics/charts

Ελληνικά (Greek)

https://helm.sh/el/docs/topics/charts

Español (Spanish)

https://helm.sh/es/docs/topics/charts

Français (French)

https://helm.sh/fr/docs/topics/charts

Italiano (Italian)

https://helm.sh/it/docs/topics/charts

日本語 (Japanese)

https://helm.sh/ja/docs/topics/charts

한국어 (Korean)

https://helm.sh/ko/docs/topics/charts

Português (Portuguese)

https://helm.sh/pt/docs/topics/charts

Русский (Russian)

https://helm.sh/ru/docs/topics/charts

Українська (Ukrainian)

https://helm.sh/uk/docs/topics/charts

中文 (Chinese)

https://helm.sh/zh/docs/topics/charts

https://helm.sh/

https://helm.sh/docs

https://helm.sh/community

https://helm.sh/blog

https://artifacthub.io/

https://helm.sh/docs/topics/charts/

https://helm.sh/docs/topics/charts

https://helm.sh/docs/v3/topics/charts

https://helm.sh/docs/v2/

https://helm.sh/docs/topics/charts/

← Back to main menu

https://helm.sh/docs/

Helm 4 Overview

https://helm.sh/docs/overview

Full Changelog

https://helm.sh/docs/changelog

Introduction

https://helm.sh/docs/intro/

https://helm.sh/docs/howto/

https://helm.sh/docs/topics/

https://helm.sh/docs/topics/charts

Chart Hooks

https://helm.sh/docs/topics/charts\_hooks

Chart Tests

https://helm.sh/docs/topics/chart\_tests

Library Charts

https://helm.sh/docs/topics/library\_charts

Helm Provenance and Integrity

https://helm.sh/docs/topics/provenance

The Chart Repository Guide

https://helm.sh/docs/topics/chart\_repository

Use OCI-based registries

https://helm.sh/docs/topics/registries

Helm Architecture

https://helm.sh/docs/topics/architecture

Advanced Helm Techniques

https://helm.sh/docs/topics/advanced

Kubernetes Distribution Guide

https://helm.sh/docs/topics/kubernetes\_distros

Role-based Access Control

https://helm.sh/docs/topics/rbac

The Helm Plugins Guide

https://helm.sh/docs/topics/plugins

Deprecated Kubernetes APIs

https://helm.sh/docs/topics/kubernetes\_apis

Permissions management for SQL storage backend

https://helm.sh/docs/topics/permissions\_sql\_storage\_backend

Helm Version Support Policy

https://helm.sh/docs/topics/version\_skew

Best Practices

https://helm.sh/docs/chart\_best\_practices/

Chart Template Guide

https://helm.sh/docs/chart\_template\_guide/

https://helm.sh/docs/plugins/

Helm Commands

https://helm.sh/docs/helm/

https://helm.sh/docs/sdk/

https://helm.sh/docs/glossary/

https://helm.sh/docs/

https://helm.sh/docs/topics/

Version: 4.1.1

On this page

This page has not yet been updated for Helm 4. Some of the content might be inaccurate or not applicable to Helm 4. For more information about the Helm 4 new features, improvements, and breaking changes, see

Helm 4 Overview

https://helm.sh/docs/overview

Helm uses a packaging format called

. A chart is a collection of files that describe a related set of Kubernetes resources. A single chart might be used to deploy something simple, like a memcached pod, or something complex, like a full web app stack with HTTP servers, databases, caches, and so on.

Charts are created as files laid out in a particular directory tree. They can be packaged into versioned archives to be deployed.

If you want to download and look at the files for a published chart, without installing it, you can do so with

helm pull chartrepo/chartname

This document explains the chart format, and provides basic guidance for building charts with Helm.

The Chart File Structure

https://helm.sh/docs/topics/charts/#the-chart-file-structure

A chart is organized as a collection of files inside of a directory. The directory name is the name of the chart (without versioning information). Thus, a chart describing WordPress would be stored in a

#### Inside of this directory, Helm will expect a structure that matches this:

wordpress/
  Chart.yaml          # A YAML file containing information about the chart
  LICENSE             # OPTIONAL: A plain text file containing the license for the chart
  README.md           # OPTIONAL: A human-readable README file
  values.yaml         # The default configuration values for this chart
  values.schema.json  # OPTIONAL: A JSON Schema for imposing a structure on the values.yaml file
  charts/             # A directory containing any charts upon which this chart depends.
  crds/               # Custom Resource Definitions
  templates/          # A directory of templates that, when combined with values,
                      # will generate valid Kubernetes manifest files.
  templates/NOTES.txt # OPTIONAL: A plain text file containing short usage notes

Helm reserves use of the

directories, and of the listed file names. Other files will be left as they are.

The Chart.yaml File

https://helm.sh/docs/topics/charts/#the-chartyaml-file

file is required for a chart. It contains the following fields:

apiVersion: The chart API version (required)
name: The name of the chart (required)
version: The version of the chart (required)
kubeVersion: A SemVer range of compatible Kubernetes versions (optional)
description: A single-sentence description of this project (optional)
type: The type of the chart (optional)
keywords:
  - A list of keywords about this project (optional)
home: The URL of this projects home page (optional)
sources:
  - A list of URLs to source code for this project (optional)
dependencies: # A list of the chart requirements (optional)
  - name: The name of the chart (nginx)
    version: The version of the chart ("1.2.3")
    repository: (optional) The repository URL ("https://example.com/charts") or alias ("@repo-name")
    condition: (optional) A yaml path that resolves to a boolean, used for enabling/disabling charts (e.g. subchart1.enabled )
    tags: # (optional)
      - Tags can be used to group charts for enabling/disabling together
    import-values: # (optional)
      - ImportValues holds the mapping of source values to parent key to be imported. Each item can be a string or pair of child/parent sublist items.
    alias: (optional) Alias to be used for the chart. Useful when you have to add the same chart multiple times
maintainers: # (optional)
  - name: The maintainers name (required for each maintainer)
    email: The maintainers email (optional for each maintainer)
    url: A URL for the maintainer (optional for each maintainer)
icon: A URL to an SVG or PNG image to be used as an icon (optional).
appVersion: The version of the app that this contains (optional). Needn't be SemVer. Quotes recommended.
deprecated: Whether this chart is deprecated (optional, boolean)
annotations:
  example: A list of annotations keyed by name (optional).

https://github.com/helm/helm/releases/tag/v3.3.2

, additional fields are not allowed. The recommended approach is to add custom metadata in

annotations

Charts and Versioning

https://helm.sh/docs/topics/charts/#charts-and-versioning

Every chart must have a version number. A version should follow the

https://semver.org/spec/v2.0.0.html

standard but it is not strictly enforced. Unlike Helm Classic, Helm v2 and later uses version numbers as release markers. Packages in repositories are identified by name plus version.

For example, an

chart whose version field is set to

version: 1.2.3

will be named:

nginx-1.2.3.tgz

More complex SemVer 2 names are also supported, such as

version: 1.2.3-alpha.1+ef365

. But non-SemVer names are explicitly disallowed by the system. Subject to exception are versions in format

. For example, if there is a leading v or a version listed without all 3 parts (e.g. v1.2) it will attempt to coerce it into a valid semantic version (e.g., v1.2.0).

Whereas Helm Classic and Deployment Manager were both very GitHub oriented when it came to charts, Helm v2 and later does not rely upon or require GitHub or even Git. Consequently, it does not use Git SHAs for versioning at all.

field inside of the

is used by many of the Helm tools, including the CLI. When generating a package, the

helm package

command will use the version that it finds in the

as a token in the package name. The system assumes that the version number in the chart package name matches the version number in the

. Failure to meet this assumption will cause an error.

https://helm.sh/docs/topics/charts/#the-apiversion-field

field should be

for Helm charts that require at least Helm 3. Charts supporting previous Helm versions have an

and are still installable by Helm 3.

Changes from

dependencies

field defining chart dependencies, which were located in a separate

requirements.yaml

charts (see

Chart Dependencies

https://helm.sh/docs/topics/charts/#chart-dependencies

field, discriminating application and library charts (see

Chart Types

https://helm.sh/docs/topics/charts/#chart-types

https://helm.sh/docs/topics/charts/#the-appversion-field

Note that the

field is not related to the

field. It is a way of specifying the version of the application. For example, the

chart may have an

appVersion: "8.2.1"

, indicating that the version of Drupal included in the chart (by default) is

. This field is informational, and has no impact on chart version calculations. Wrapping the version in quotes is highly recommended. It forces the YAML parser to treat the version number as a string. Leaving it unquoted can lead to parsing issues in some cases. For example, YAML interprets

as a floating point value, and a git commit SHA like

as scientific notation.

As of Helm v3.5.0,

helm create

wraps the default

field in quotes.

kubeVersion

https://helm.sh/docs/topics/charts/#the-kubeversion-field

The optional

kubeVersion

field can define semver constraints on supported Kubernetes versions. Helm will validate the version constraints when installing the chart and fail if the cluster runs an unsupported Kubernetes version.

Version constraints may comprise space separated AND comparisons such as

>= 1.13.0 < 1.15.0

which themselves can be combined with the OR

operator like in the following example

>= 1.13.0 < 1.14.0 || >= 1.14.1 < 1.15.0

In this example the version

is excluded, which can make sense if a bug in certain versions is known to prevent the chart from running properly.

Apart from version constrains employing operators

the following shorthand notations are supported

hyphen ranges for closed intervals, where

1.1 - 2.3.4

is equivalent to

>= 1.1 <= 2.3.4

is equivalent to

>= 1.2.0 < 1.3.0

tilde ranges (patch version changes allowed), where

is equivalent to

>= 1.2.3 < 1.3.0

caret ranges (minor version changes allowed), where

is equivalent to

>= 1.2.3 < 2.0.0

For a detailed explanation of supported semver constraints see

Masterminds/semver

https://github.com/Masterminds/semver

Deprecating Charts

https://helm.sh/docs/topics/charts/#deprecating-charts

When managing charts in a Chart Repository, it is sometimes necessary to deprecate a chart. The optional

can be used to mark a chart as deprecated. If the

version of a chart in the repository is marked as deprecated, then the chart as a whole is considered to be deprecated. The chart name can be later reused by publishing a newer version that is not marked as deprecated. The workflow for deprecating charts is:

Update chart's

to mark the chart as deprecated, bumping the version

Release the new chart version in the Chart Repository

Remove the chart from the source repository (e.g. git)

Chart Types

https://helm.sh/docs/topics/charts/#chart-types

field defines the type of chart. There are two types:

application

. Application is the default type and it is the standard chart which can be operated on fully. The

library chart

https://helm.sh/docs/topics/library\_charts

provides utilities or functions for the chart builder. A library chart differs from an application chart because it is not installable and usually doesn't contain any resource objects.

An application chart can be used as a library chart. This is enabled by setting the type to

. The chart will then be rendered as a library chart where all utilities and functions can be leveraged. All resource objects of the chart will not be rendered.

Chart LICENSE, README and NOTES

https://helm.sh/docs/topics/charts/#chart-license-readme-and-notes

Charts can also contain files that describe the installation, configuration, usage and license of a chart.

A LICENSE is a plain text file containing the

https://en.wikipedia.org/wiki/Software\_license

for the chart. The chart can contain a license as it may have programming logic in the templates and would therefore not be configuration only. There can also be separate license(s) for the application installed by the chart, if required.

A README for a chart should be formatted in Markdown (README.md), and should generally contain:

A description of the application or service the chart provides

Any prerequisites or requirements to run the chart

Descriptions of options in

values.yaml

and default values

Any other information that may be relevant to the installation or configuration of the chart

When hubs and other user interfaces display details about a chart that detail is pulled from the content in the

The chart can also contain a short plain text

templates/NOTES.txt

file that will be printed out after installation, and when viewing the status of a release. This file is evaluated as a

https://helm.sh/docs/topics/charts/#templates-and-values

, and can be used to display usage notes, next steps, or any other information relevant to a release of the chart. For example, instructions could be provided for connecting to a database, or accessing a web UI. Since this file is printed to STDOUT when running

helm install

helm status

, it is recommended to keep the content brief and point to the README for greater detail.

Chart Dependencies

https://helm.sh/docs/topics/charts/#chart-dependencies

In Helm, one chart may depend on any number of other charts. These dependencies can be dynamically linked using the

dependencies

or brought in to the

directory and managed manually.

Managing Dependencies with the

dependencies

https://helm.sh/docs/topics/charts/#managing-dependencies-with-the-dependencies-field

The charts required by the current chart are defined as a list in the

dependencies

dependencies:
  - name: apache
    version: 1.2.3
    repository: https://example.com/charts
  - name: mysql
    version: 3.2.1
    repository: https://another.example.com/charts

field is the name of the chart you want.

field is the version of the chart you want.

field is the full URL to the chart repository. Note that you must also use

helm repo add

to add that repo locally.

You might use the name of the repo instead of URL

$ helm repo add fantastic-charts https://charts.helm.sh/incubator

dependencies:
  - name: awesomeness
    version: 1.0.0
    repository: "@fantastic-charts"

Once you have defined dependencies, you can run

helm dependency update

and it will use your dependency file to download all the specified charts into your

directory for you.

$ helm dep up foochart
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "local" chart repository
...Successfully got an update from the "stable" chart repository
...Successfully got an update from the "example" chart repository
...Successfully got an update from the "another" chart repository
Update Complete. Happy Helming!
Saving 2 charts
Downloading apache from repo https://example.com/charts
Downloading mysql from repo https://another.example.com/charts

helm dependency update

retrieves charts, it will store them as chart archives in the

directory. So for the example above, one would expect to see the following files in the charts directory:

charts/
  apache-1.2.3.tgz
  mysql-3.2.1.tgz

Alias field in dependencies

https://helm.sh/docs/topics/charts/#alias-field-in-dependencies

In addition to the other fields above, each requirements entry may contain the optional field

Adding an alias for a dependency chart would put a chart in dependencies using alias as name of new dependency.

One can use

in cases where they need to access a chart with other name(s).

# parentchart/Chart.yaml
dependencies:
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
    alias: new-subchart-1
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
    alias: new-subchart-2
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0

In the above example we will get 3 dependencies in all for

parentchart

subchart
new-subchart-1
new-subchart-2

The manual way of achieving this is by copy/pasting the same chart in the

directory multiple times with different names.

Tags and Condition fields in dependencies

https://helm.sh/docs/topics/charts/#tags-and-condition-fields-in-dependencies

In addition to the other fields above, each requirements entry may contain the optional fields

All charts are loaded by default. If

fields are present, they will be evaluated and used to control loading for the chart(s) they are applied to.

Condition - The condition field holds one or more YAML paths (delimited by commas). If this path exists in the top parent's values and resolves to a boolean value, the chart will be enabled or disabled based on that boolean value. Only the first valid path found in the list is evaluated and if no paths exist then the condition has no effect.

Tags - The tags field is a YAML list of labels to associate with this chart. In the top parent's values, all charts with tags can be enabled or disabled by specifying the tag and a boolean value.

# parentchart/Chart.yaml
dependencies:
  - name: subchart1
    repository: http://localhost:10191
    version: 0.1.0
    condition: subchart1.enabled,global.subchart1.enabled
    tags:
      - front-end
      - subchart1
  - name: subchart2
    repository: http://localhost:10191
    version: 0.1.0
    condition: subchart2.enabled,global.subchart2.enabled
    tags:
      - back-end
      - subchart2

# parentchart/values.yaml
subchart1:
  enabled: true
tags:
  front-end: false
  back-end: true

In the above example all charts with the tag

would be disabled but since the

subchart1.enabled

path evaluates to 'true' in the parent's values, the condition will override the

will be enabled.

is tagged with

and that tag evaluates to

will be enabled. Also note that although

has a condition specified, there is no corresponding path and value in the parent's values so that condition has no effect.

Using the CLI with Tags and Conditions

https://helm.sh/docs/topics/charts/#using-the-cli-with-tags-and-conditions

parameter can be used as usual to alter tag and condition values.

helm install --set tags.front-end=true --set subchart2.enabled=false

Tags and Condition Resolution

https://helm.sh/docs/topics/charts/#tags-and-condition-resolution

Conditions (when set in values) always override tags.

The first condition path that exists wins and subsequent ones for that chart are ignored.

Tags are evaluated as 'if any of the chart's tags are true then enable the chart'.

Tags and conditions values must be set in the top parent's values.

key in values must be a top level key. Globals and nested

tables are not currently supported.

Importing Child Values via dependencies

https://helm.sh/docs/topics/charts/#importing-child-values-via-dependencies

In some cases it is desirable to allow a child chart's values to propagate to the parent chart and be shared as common defaults. An additional benefit of using the

format is that it will enable future tooling to introspect user-settable values.

The keys containing the values to be imported can be specified in the parent chart's

dependencies

in the field

import-values

using a YAML list. Each item in the list is a key which is imported from the child chart's

To import values not contained in the

key, use the

child-parent

https://helm.sh/docs/topics/charts/#using-the-child-parent-format

format. Examples of both formats are described below.

Using the exports format

https://helm.sh/docs/topics/charts/#using-the-exports-format

If a child chart's

values.yaml

file contains an

field at the root, its contents may be imported directly into the parent's values by specifying the keys to import as in the example below:

# parent's Chart.yaml file
dependencies:
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
    import-values:
      - data

# child's values.yaml file
exports:
  data:
    myint: 99

Since we are specifying the key

in our import list, Helm looks in the

field of the child chart for

key and imports its contents.

#### The final parent values would contain our exported field:

# parent's values
myint: 99

Please note the parent key

is not contained in the parent's final values. If you need to specify the parent key, use the 'child-parent' format.

Using the child-parent format

https://helm.sh/docs/topics/charts/#using-the-child-parent-format

To access values that are not contained in the

key of the child chart's values, you will need to specify the source key of the values to be imported (

) and the destination path in the parent chart's values (

import-values

in the example below instructs Helm to take any values found at

path and copy them to the parent's values at the path specified in

# parent's Chart.yaml file
dependencies:
  - name: subchart1
    repository: http://localhost:10191
    version: 0.1.0
    ...
    import-values:
      - child: default.data
        parent: myimports

In the above example, values found at

default.data

in the subchart1's values will be imported to the

key in the parent chart's values as detailed below:

# parent's values.yaml file
myimports:
  myint: 0
  mybool: false
  mystring: "helm rocks!"

# subchart1's values.yaml file
default:
  data:
    myint: 999
    mybool: true

#### The parent chart's resulting values would be:

# parent's final values
myimports:
  myint: 999
  mybool: true
  mystring: "helm rocks!"

The parent's final values now contains the

fields imported from subchart1.

Managing Dependencies manually via the

https://helm.sh/docs/topics/charts/#managing-dependencies-manually-via-the-charts-directory

If more control over dependencies is desired, these dependencies can be expressed explicitly by copying the dependency charts into the

A dependency should be an unpacked chart directory but its name cannot start with

. Such files are ignored by the chart loader.

For example, if the WordPress chart depends on the Apache chart, the Apache chart (of the correct version) is supplied in the WordPress chart's

wordpress:
  Chart.yaml
  # ...
  charts/
    apache/
      Chart.yaml
      # ...
    mysql/
      Chart.yaml
      # ...

The example above shows how the WordPress chart expresses its dependency on Apache and MySQL by including those charts inside of its

To drop a dependency into your charts/ directory, use the helm pull command

Operational aspects of using dependencies

https://helm.sh/docs/topics/charts/#operational-aspects-of-using-dependencies

The above sections explain how to specify chart dependencies, but how does this affect chart installation using

helm install

helm upgrade

Suppose that a chart named "A" creates the following Kubernetes objects

namespace "A-Namespace"

statefulset "A-StatefulSet"

service "A-Service"

Furthermore, A is dependent on chart B that creates objects

namespace "B-Namespace"

replicaset "B-ReplicaSet"

service "B-Service"

After installation/upgrade of chart A a single Helm release is created/modified. The release will create/update all of the above Kubernetes objects in the following order:

A-Namespace

B-Namespace

B-ReplicaSet

A-StatefulSet

This is because when Helm installs/upgrades charts, the Kubernetes objects from the charts and all its dependencies are

aggregated into a single set; then

sorted by type followed by name; and then

created/updated in that order.

Hence a single release is created with all the objects for the chart and its dependencies.

The install order of Kubernetes types is given by the enumeration InstallOrder in kind\_sorter.go (see

the Helm source file

https://github.com/helm/helm/blob/484d43913f97292648c867b56768775a55e4bba6/pkg/releaseutil/kind\_sorter.go

Templates and Values

https://helm.sh/docs/topics/charts/#templates-and-values

Helm Chart templates are written in the

Go template language

https://golang.org/pkg/text/template/

, with the addition of 50 or so add-on template functions

from the Sprig library

https://github.com/Masterminds/sprig

and a few other

specialized functions

https://helm.sh/docs/howto/charts\_tips\_and\_tricks

All template files are stored in a chart's

folder. When Helm renders the charts, it will pass every file in that directory through the template engine.

#### Values for the templates are supplied two ways:

Chart developers may supply a file called

values.yaml

inside of a chart. This file can contain default values.

Chart users may supply a YAML file that contains values. This can be provided on the command line with

helm install

When a user supplies custom values, these values will override the values in the chart's

values.yaml

Template Files

https://helm.sh/docs/topics/charts/#template-files

Template files follow the standard conventions for writing Go templates (see

the text/template Go package documentation

https://golang.org/pkg/text/template/

for details). An example template file might look something like this:

apiVersion: v1
kind: ReplicationController
metadata:
  name: deis-database
  namespace: deis
  labels:
    app.kubernetes.io/managed-by: deis
spec:
  replicas: 1
  selector:
    app.kubernetes.io/name: deis-database
  template:
    metadata:
      labels:
        app.kubernetes.io/name: deis-database
    spec:
      serviceAccount: deis-database
      containers:
        - name: deis-database
          image: {{ .Values.imageRegistry }}/postgres:{{ .Values.dockerTag }}
          imagePullPolicy: {{ .Values.pullPolicy }}
          ports:
            - containerPort: 5432
          env:
            - name: DATABASE\_STORAGE
              value: {{ default "minio" .Values.storage }}

The above example, based loosely on

https://github.com/deis/charts

https://github.com/deis/charts

, is a template for a Kubernetes replication controller. It can use the following four template values (usually defined in a

values.yaml

imageRegistry

: The source registry for the Docker image.

: The tag for the docker image.

: The Kubernetes pull policy.

: The storage backend, whose default is set to

All of these values are defined by the template author. Helm does not require or dictate parameters.

To see many working charts, check out the CNCF

Artifact Hub

https://artifacthub.io/packages/search?kind=0

Predefined Values

https://helm.sh/docs/topics/charts/#predefined-values

Values that are supplied via a

values.yaml

file (or via the

flag) are accessible from the

object in a template. But there are other pre-defined pieces of data you can access in your templates.

The following values are pre-defined, are available to every template, and cannot be overridden. As with all values, the names are

case sensitive

Release.Name

: The name of the release (not the chart)

Release.Namespace

: The namespace the chart was released to.

Release.Service

: The service that conducted the release.

Release.IsUpgrade

: This is set to true if the current operation is an upgrade or rollback.

Release.IsInstall

: This is set to true if the current operation is an install.

: The contents of the

. Thus, the chart version is obtainable as

Chart.Version

and the maintainers are in

Chart.Maintainers

: A map-like object containing all non-special files in the chart. This will not give you access to templates, but will give you access to additional files that are present (unless they are excluded using

.helmignore

). Files can be accessed using

{{ index .Files "file.name" }}

or using the

{{.Files.Get name }}

function. You can also access the contents of the file as

{{ .Files.GetBytes }}

Capabilities

: A map-like object that contains information about the versions of Kubernetes (

{{ .Capabilities.KubeVersion }}

) and the supported Kubernetes API versions (

{{ .Capabilities.APIVersions.Has "batch/v1" }}

Any unknown

fields will be dropped. They will not be accessible inside of the

object. Thus,

cannot be used to pass arbitrarily structured data into the template. The values file can be used for that, though.

Values files

https://helm.sh/docs/topics/charts/#values-files

Considering the template in the previous section, a

values.yaml

file that supplies the necessary values would look like this:

imageRegistry: "quay.io/deis"
dockerTag: "latest"
pullPolicy: "Always"
storage: "s3"

A values file is formatted in YAML. A chart may include a default

values.yaml

file. The Helm install command allows a user to override values by supplying additional YAML values:

$ helm install --generate-name --values=myvals.yaml wordpress

When values are passed in this way, they will be merged into the default values file. For example, consider a

myvals.yaml

file that looks like this:

storage: "gcs"

When this is merged with the

values.yaml

in the chart, the resulting generated content will be:

imageRegistry: "quay.io/deis"
dockerTag: "latest"
pullPolicy: "Always"
storage: "gcs"

Note that only the last field was overridden.

The default values file included inside of a chart

values.yaml

. But files specified on the command line can be named anything.

flag is used on

helm install

helm upgrade

, those values are simply converted to YAML on the client side.

If any required entries in the values file exist, they can be declared as required in the chart template by using the

'required' function

https://helm.sh/docs/howto/charts\_tips\_and\_tricks

Any of these values are then accessible inside of templates using the

apiVersion: v1
kind: ReplicationController
metadata:
  name: deis-database
  namespace: deis
  labels:
    app.kubernetes.io/managed-by: deis
spec:
  replicas: 1
  selector:
    app.kubernetes.io/name: deis-database
  template:
    metadata:
      labels:
        app.kubernetes.io/name: deis-database
    spec:
      serviceAccount: deis-database
      containers:
        - name: deis-database
          image: {{ .Values.imageRegistry }}/postgres:{{ .Values.dockerTag }}
          imagePullPolicy: {{ .Values.pullPolicy }}
          ports:
            - containerPort: 5432
          env:
            - name: DATABASE\_STORAGE
              value: {{ default "minio" .Values.storage }}

Scope, Dependencies, and Values

https://helm.sh/docs/topics/charts/#scope-dependencies-and-values

Values files can declare values for the top-level chart, as well as for any of the charts that are included in that chart's

directory. Or, to phrase it differently, a values file can supply values to the chart as well as to any of its dependencies. For example, the demonstration WordPress chart above has both

as dependencies. The values file could supply values to all of these components:

title: "My WordPress Site" # Sent to the WordPress template
mysql:
  max\_connections: 100 # Sent to MySQL
  password: "secret"
apache:
  port: 8080 # Passed to Apache

Charts at a higher level have access to all of the variables defined beneath. So the WordPress chart can access the MySQL password as

.Values.mysql.password

. But lower level charts cannot access things in parent charts, so MySQL will not be able to access the

property. Nor, for that matter, can it access

apache.port

Values are namespaced, but namespaces are pruned. So for the WordPress chart, it can access the MySQL password field as

.Values.mysql.password

. But for the MySQL chart, the scope of the values has been reduced and the namespace prefix removed, so it will see the password field simply as

.Values.password

Global Values

https://helm.sh/docs/topics/charts/#global-values

As of 2.0.0-Alpha.2, Helm supports special "global" value. Consider this modified version of the previous example:

title: "My WordPress Site" # Sent to the WordPress template
global:
  app: MyWordPress
mysql:
  max\_connections: 100 # Sent to MySQL
  password: "secret"
apache:
  port: 8080 # Passed to Apache

The above adds a

section with the value

app: MyWordPress

. This value is available to

.Values.global.app

For example, the

templates may access

{{ .Values.global.app}}

, and so can the

chart. Effectively, the values file above is regenerated like this:

title: "My WordPress Site" # Sent to the WordPress template
global:
  app: MyWordPress
mysql:
  global:
    app: MyWordPress
  max\_connections: 100 # Sent to MySQL
  password: "secret"
apache:
  global:
    app: MyWordPress
  port: 8080 # Passed to Apache

This provides a way of sharing one top-level variable with all subcharts, which is useful for things like setting

properties like labels.

If a subchart declares a global variable, that global will be passed

(to the subchart's subcharts), but not

to the parent chart. There is no way for a subchart to influence the values of the parent chart.

Also, global variables of parent charts take precedence over the global variables from subcharts.

Schema Files

https://helm.sh/docs/topics/charts/#schema-files

Sometimes, a chart maintainer might want to define a structure on their values. This can be done by defining a schema in the

values.schema.json

file. A schema is represented as a

JSON Schema

https://json-schema.org/

. It might look something like this:

{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "properties": {
    "image": {
      "description": "Container Image",
      "properties": {
        "repo": {
          "type": "string"
        },
        "tag": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "name": {
      "description": "Service name",
      "type": "string"
    },
    "port": {
      "description": "Port",
      "minimum": 0,
      "type": "integer"
    },
    "protocol": {
      "type": "string"
    }
  },
  "required": \[
    "protocol",
    "port"
  \],
  "title": "Values",
  "type": "object"
}

This schema will be applied to the values to validate it. Validation occurs when any of the following commands are invoked:

helm install

helm upgrade

helm template

An example of a

values.yaml

file that meets the requirements of this schema might look something like this:

name: frontend
protocol: https
port: 443

Note that the schema is applied to the final

object, and not just to the

values.yaml

file. This means that the following

file is valid, given that the chart is installed with the appropriate

option shown below.

name: frontend
protocol: https

helm install --set port=443

Furthermore, the final

object is checked against

subchart schemas. This means that restrictions on a subchart can't be circumvented by a parent chart. This also works backwards - if a subchart has a requirement that is not met in the subchart's

values.yaml

file, the parent chart

satisfy those restrictions in order to be valid.

Schema validation can be disabled by setting the option shown below. This is particularly useful in air-gapped environments when a chart's JSON Schema file contains remote references.

helm install --skip-schema-validation

https://helm.sh/docs/topics/charts/#references

When it comes to writing templates, values, and schema files, there are several standard references that will help you out.

Go templates

https://godoc.org/text/template

Extra template functions

https://godoc.org/github.com/Masterminds/sprig

The YAML format

https://yaml.org/spec/

JSON Schema

https://json-schema.org/

Custom Resource Definitions (CRDs)

https://helm.sh/docs/topics/charts/#custom-resource-definitions-crds

Kubernetes provides a mechanism for declaring new types of Kubernetes objects. Using CustomResourceDefinitions (CRDs), Kubernetes developers can declare custom resource types.

In Helm 3, CRDs are treated as a special kind of object. They are installed before the rest of the chart, and are subject to some limitations.

CRD YAML files should be placed in the

directory inside of a chart. Multiple CRDs (separated by YAML start and end markers) may be placed in the same file. Helm will attempt to load

of the files in the CRD directory into Kubernetes.

cannot be templated

. They must be plain YAML documents.

When Helm installs a new chart, it will upload the CRDs, pause until the CRDs are made available by the API server, and then start the template engine, render the rest of the chart, and upload it to Kubernetes. Because of this ordering, CRD information is available in the

.Capabilities

object in Helm templates, and Helm templates may create new instances of objects that were declared in CRDs.

For example, if your chart had a CRD for

directory, you may create instances of the

kind in the

crontabs/
  Chart.yaml
  crds/
    crontab.yaml
  templates/
    mycrontab.yaml

crontab.yaml

file must contain the CRD with no template directives:

kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab

Then the template

mycrontab.yaml

may create a new

(using templates as usual):

apiVersion: stable.example.com
kind: CronTab
metadata:
  name: {{ .Values.name }}
spec:
   # ...

Helm will make sure that the

kind has been installed and is available from the Kubernetes API server before it proceeds installing the things in

Limitations on CRDs

https://helm.sh/docs/topics/charts/#limitations-on-crds

Unlike most objects in Kubernetes, CRDs are installed globally. For that reason, Helm takes a very cautious approach in managing CRDs. CRDs are subject to the following limitations:

CRDs are never reinstalled. If Helm determines that the CRDs in the

directory are already present (regardless of version), Helm will not attempt to install or upgrade.

CRDs are never installed on upgrade or rollback. Helm will only create CRDs on installation operations.

CRDs are never deleted. Deleting a CRD automatically deletes all of the CRD's contents across all namespaces in the cluster. Consequently, Helm will not delete CRDs.

Operators who want to upgrade or delete CRDs are encouraged to do this manually and with great care.

Using Helm to Manage Charts

https://helm.sh/docs/topics/charts/#using-helm-to-manage-charts

tool has several commands for working with charts.

#### It can create a new chart for you:

$ helm create mychart
Created mychart/

Once you have edited a chart,

can package it into a chart archive for you:

$ helm package mychart
Archived mychart-0.1.-.tgz

You can also use

to help you find issues with your chart's formatting or information:

$ helm lint mychart
No issues found

Chart Repositories

https://helm.sh/docs/topics/charts/#chart-repositories

chart repository

is an HTTP server that houses one or more packaged charts. While

can be used to manage local chart directories, when it comes to sharing charts, the preferred mechanism is a chart repository.

Any HTTP server that can serve YAML files and tar files and can answer GET requests can be used as a repository server. The Helm team has tested some servers, including Google Cloud Storage with website mode enabled, and S3 with website mode enabled.

A repository is characterized primarily by the presence of a special file called

that has a list of all of the packages supplied by the repository, together with metadata that allows retrieving and verifying those packages.

On the client side, repositories are managed with the

commands. However, Helm does not provide tools for uploading charts to remote repository servers. This is because doing so would add substantial requirements to an implementing server, and thus raise the barrier for setting up a repository.

Chart Starter Packs

https://helm.sh/docs/topics/charts/#chart-starter-packs

helm create

command takes an optional

option that lets you specify a "starter chart". Also, the starter option has a short alias

#### Examples of usage:

helm create my-chart --starter starter-name
helm create my-chart -p starter-name
helm create my-chart -p /absolute/path/to/starter-name

Starters are just regular charts, but are located in

$XDG\_DATA\_HOME/helm/starters

. As a chart developer, you may author charts that are specifically designed to be used as starters. Such charts should be designed with the following considerations in mind:

will be overwritten by the generator.

Users will expect to modify such a chart's contents, so documentation should indicate how users can do so.

All occurrences of

<CHARTNAME>

will be replaced with the specified chart name so that starter charts can be used as templates, except for some variable files. For example, if you use custom files in the

directory or certain

<CHARTNAME>

will NOT override inside them. Additionally, the chart description is not inherited.

Currently the only way to add a chart to

$XDG\_DATA\_HOME/helm/starters

is to manually copy it there. In your chart's documentation, you may want to explain that process.

Edit this page

https://github.com/helm/helm-www/blob/main/docs/topics/charts.mdx

Previous Topics

https://helm.sh/docs/topics/

Next Chart Hooks

https://helm.sh/docs/topics/charts\_hooks

Helm Project

Source code

https://github.com/helm/helm

https://helm.sh/blog

https://www.cncf.io/community/kubecon-cloudnativecon-events/

Code of Conduct

https://github.com/cncf/foundation/blob/master/code-of-conduct.md

Introduction

https://helm.sh/docs/intro

Chart tips & tricks

https://helm.sh/docs/howto/charts\_tips\_and\_tricks

Developing Charts

https://helm.sh/docs/topics/charts

Search 800+ Charts

https://artifacthub.io/

Development

Slack (#helm-dev)

https://kubernetes.slack.com/messages/C51E88VDG

Contribution Guide

https://github.com/helm/helm/blob/main/CONTRIBUTING.md

Maintainers

https://github.com/helm/helm/blob/main/OWNERS

Weekly Meetings

https://github.com/helm/community/blob/main/communication.md#meetings

GitHub Community

https://github.com/helm/community

Slack (#helm-users)

https://kubernetes.slack.com/

Stack Overflow

https://stackoverflow.com/questions/tagged/kubernetes-helm

https://x.com/helmpack

Cloud Native Computing Foundation

https://www.cncf.io/

graduated project.

© Helm Authors 2026. Documentation distributed under

https://creativecommons.org/licenses/by/4.0

© 2026 The Linux Foundation. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our

Trademark Usage page

https://www.linuxfoundation.org/trademark-usage/


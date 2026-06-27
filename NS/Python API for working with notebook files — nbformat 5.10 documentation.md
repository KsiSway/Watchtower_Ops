---
sourceFile: "Python API for working with notebook files — nbformat 5.10 documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.530Z"
---

# Python API for working with notebook files — nbformat 5.10 documentation

28a64884-f690-4ad0-94e8-3619e37ead8d

Python API for working with notebook files — nbformat 5.10 documentation

2131798c-c9b6-46fa-98bf-79b71d0f8a57

https://nbformat.readthedocs.io/en/latest/api.html

Python API for working with notebook files — nbformat 5.10 documentation

Skip to main content

https://nbformat.readthedocs.io/en/latest/api.html#main-content

Back to top

nbformat 5.10 documentation

https://nbformat.readthedocs.io/en/latest/index.html

The Notebook file format

https://nbformat.readthedocs.io/en/latest/format\_description.html

Supported markup formats

https://nbformat.readthedocs.io/en/latest/markup.html

Python API for working with notebook files

https://nbformat.readthedocs.io/en/latest/api.html

https://nbformat.readthedocs.io/en/latest/changelog.html

The Notebook file format

https://nbformat.readthedocs.io/en/latest/format\_description.html

Supported markup formats

https://nbformat.readthedocs.io/en/latest/markup.html

Python API for working with notebook files

https://nbformat.readthedocs.io/en/latest/api.html

https://nbformat.readthedocs.io/en/latest/changelog.html

Section Navigation

This isn't a stack. It's a pile. Errors, perf, logs, hosts. One tool, one bill, built 4 devs who ship

https://server.ethicalads.io/proxy/click/10510/019f0193-150b-7c81-bf1a-5d7920879e7a/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Python API for working with notebook files

Python API for working with notebook files

https://nbformat.readthedocs.io/en/latest/api.html#module-nbformat

Reading and writing

https://nbformat.readthedocs.io/en/latest/api.html#reading-and-writing

nbformat. read(

capture\_validation\_error= None

, \*\* kwargs)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.read

Read a notebook from a file as a NotebookNode of the given version.

The string can contain a notebook of any version. The notebook will be returned as\_version , converting, if necessary.

Notebook format errors will be logged.

#### Parameters:

https://docs.python.org/3/library/stdtypes.html#str

) – A file-like object with a read method that returns unicode (use

in Python 2), or a path to a file.

https://docs.python.org/3/library/functions.html#int

) – The version of the notebook format to return. The notebook will be converted, if necessary. Pass nbformat.NO\_CONVERT to prevent conversion.

capture\_validation\_error

https://docs.python.org/3/library/stdtypes.html#dict

) – If provided, a key of “ValidationError” with a value of the ValidationError instance will be added to the dictionary.

– The notebook that was read.

#### Return type:

NotebookNode

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NotebookNode

nbformat. reads(

capture\_validation\_error= None

, \*\* kwargs)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.reads

Read a notebook from a string and return the NotebookNode object as the given version.

The string can contain a notebook of any version. The notebook will be returned as\_version , converting, if necessary.

Notebook format errors will be logged.

#### Parameters:

) – The raw unicode string to read the notebook from.

https://docs.python.org/3/library/functions.html#int

) – The version of the notebook format to return. The notebook will be converted, if necessary. Pass nbformat.NO\_CONVERT to prevent conversion.

capture\_validation\_error

https://docs.python.org/3/library/stdtypes.html#dict

) – If provided, a key of “ValidationError” with a value of the ValidationError instance will be added to the dictionary.

– The notebook that was read.

#### Return type:

NotebookNode

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NotebookNode

The reading functions require you to pass the

parameter. Your code should specify the notebook format that it knows how to work with: for instance, if your code handles version 4 notebooks:

nb = nbformat.read('path/to/notebook.ipynb', as\_version=4)

This will automatically upgrade or downgrade notebooks in other versions of the notebook format to the structure your code knows about.

nbformat. write(

version= nbformat.NO\_CONVERT

capture\_validation\_error= None

, \*\* kwargs)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.write

Write a notebook to a file in a given nbformat version.

The file-like object must accept unicode input.

#### Parameters:

NotebookNode

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NotebookNode

) – The notebook to write.

https://docs.python.org/3/library/stdtypes.html#str

) – Any file-like object with a write method that accepts unicode, or a path to write a file.

https://docs.python.org/3/library/functions.html#int

) – The nbformat version to write. If nb is not this version, it will be converted. If unspecified, or specified as nbformat.NO\_CONVERT, the notebook's own version will be used and no conversion performed.

capture\_validation\_error

https://docs.python.org/3/library/stdtypes.html#dict

) – If provided, a key of “ValidationError” with a value of the ValidationError instance will be added to the dictionary.

nbformat. writes(

version= nbformat.NO\_CONVERT

capture\_validation\_error= None

, \*\* kwargs)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.writes

Write a notebook to a string in a given format in the given nbformat version.

Any notebook format errors will be logged.

#### Parameters:

NotebookNode

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NotebookNode

) – The notebook to write.

https://docs.python.org/3/library/functions.html#int

) – The nbformat version to write. If unspecified, or specified as nbformat.NO\_CONVERT, the notebook's own version will be used and no conversion performed.

capture\_validation\_error

https://docs.python.org/3/library/stdtypes.html#dict

) – If provided, a key of “ValidationError” with a value of the ValidationError instance will be added to the dictionary.

– The notebook as a JSON string.

#### Return type:

nbformat. NO\_CONVERT

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NO\_CONVERT

This special value can be passed to the reading and writing functions, to indicate that the notebook should be loaded/saved in the format it's supplied.

nbformat. current\_nbformat

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.current\_nbformat

nbformat. current\_nbformat\_minor

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.current\_nbformat\_minor

These integers represent the current notebook format version that the nbformat module knows about.

NotebookNode objects

https://nbformat.readthedocs.io/en/latest/api.html#notebooknode-objects

The functions in this module work with

NotebookNode

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NotebookNode

objects, which are like dictionaries, but allow attribute access (

). The structure of these objects matches the notebook format described in

The Notebook file format

https://nbformat.readthedocs.io/en/latest/format\_description.html

nbformat. NotebookNode(\* args, \*\* kw)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NotebookNode

A dict-like node with attribute-access

nbformat. from\_dict(

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.from\_dict

Convert dict to dict-like NotebookNode

Recursively converts any dict in the container to a NotebookNode. This does not check that the contents of the dictionary make a valid notebook or part of a notebook.

Other functions

https://nbformat.readthedocs.io/en/latest/api.html#other-functions

nbformat. convert(

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.convert

Convert a notebook node object to a specific version. Assumes that all the versions starting from 1 to the latest major X are implemented. In other words, there should never be a case where v1 v2 v3 v5 exist without a v4. Also assumes that all conversions can be made in one step increments between major versions and ignores minor revisions.

#### Parameters:

NotebookNode

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NotebookNode

https://docs.python.org/3/library/functions.html#int

) – Major revision to convert the notebook to. Can either be an upgrade or a downgrade.

https://docs.python.org/3/library/exceptions.html#ValueError

– Notebook failed to convert.

https://docs.python.org/3/library/exceptions.html#ValueError

– The version specified is invalid or doesn't exist.

ValidationError

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.ValidationError

– Conversion failed due to missing expected attributes.

nbformat. validate(

nbdict: ~typing.Any = None

ref: str | None = None

version: int | None = None

version\_minor: int | None = None

relax\_add\_props: bool = False

nbjson: ~typing.Any = None

repair\_duplicate\_cell\_ids: bool =

strip\_invalid\_metadata: bool =

https://docs.python.org/3/library/constants.html#None

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.validate

Checks whether the given notebook dict-like object conforms to the relevant notebook format schema.

#### Parameters:

https://docs.python.org/3/library/stdtypes.html#dict

) – notebook document

https://docs.python.org/3/library/stdtypes.html#str

) – reference to the subset of the schema we want to validate against. for example

"markdown\_cell"

, “code\_cell” ….

https://docs.python.org/3/library/functions.html#int

version\_minor

https://docs.python.org/3/library/functions.html#int

relax\_add\_props

https://docs.python.org/3/library/functions.html#bool

) – Whether to allow extra properties in the JSON schema validating the notebook. When True, all known fields are validated, but unknown fields are ignored.

repair\_duplicate\_cell\_ids

https://docs.python.org/3/library/functions.html#bool

) – Deprecated since 5.5.0 - will be removed in the future.

strip\_invalid\_metadata

https://docs.python.org/3/library/functions.html#bool

) – Deprecated since 5.5.0 - will be removed in the future.

#### Return type:

ValidationError if not valid.

Prior to Nbformat 5.5.0 the validate and isvalid method would silently try to fix invalid notebook and mutate arguments. This behavior is deprecated and will be removed in a near future.

Please explicitly call normalize if you need to normalize notebooks.

nbformat. ValidationError(

message: str

validator: str =

path: Iterable\[str | int\] = ()

cause: Exception | None = None

validator\_value: Any =

instance: Any =

schema: Mapping\[str

Any\] | bool =

schema\_path: Iterable\[str | int\] = ()

parent: \_Error | None = None

type\_checker: \_types.TypeChecker =

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.ValidationError

An instance was invalid under a provided schema.

Constructing notebooks programmatically

https://nbformat.readthedocs.io/en/latest/api.html#module-nbformat.v4

These functions return

NotebookNode

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NotebookNode

objects with the necessary fields.

nbformat.v4. new\_notebook(\*\* kwargs)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_notebook

Create a new notebook

nbformat.v4. new\_code\_cell(

, \*\* kwargs)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_code\_cell

Create a new code cell

nbformat.v4. new\_markdown\_cell(

, \*\* kwargs)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_markdown\_cell

Create a new markdown cell

nbformat.v4. new\_raw\_cell(

, \*\* kwargs)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_raw\_cell

Create a new raw cell

nbformat.v4. new\_output(

output\_type

, \*\* kwargs)

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_output

Create a new output, to go in the

cell.outputs

list of a code cell.

nbformat.v4. output\_from\_msg(

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.output\_from\_msg

Create a NotebookNode for an output from a kernel's IOPub message.

NotebookNode

#### Return type:

the output as a notebook node.

https://docs.python.org/3/library/exceptions.html#ValueError

– if the message is not an output message.:

Notebook signatures

https://nbformat.readthedocs.io/en/latest/api.html#module-nbformat.sign

This machinery is used by the notebook web application to record which notebooks are

, and may show dynamic output as soon as they're loaded. See

Security in the Jupyter Server

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#server-security

for more information.

nbformat.sign. NotebookNotary(\*\* kwargs:

https://docs.python.org/3/library/typing.html#typing.Any

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary

A class for computing and verifying notebook signatures.

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.sign

Sign a notebook, indicating that its output is trusted on this machine

Stores hash algorithm and hmac digest in a local database of trusted notebooks.

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.unsign

Ensure that a notebook is untrusted

by removing its signature from the trusted database, if present.

check\_signature(

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.check\_signature

Check a notebook's stored signature

If a signature is stored in the notebook's metadata, a new signature is computed and compared with the stored value.

Returns True if the signature is found and matches, False otherwise.

The following conditions must all be met for a notebook to be trusted: - a signature is stored in the form 'scheme:hexdigest' - the stored scheme matches the requested scheme - the requested scheme is available from hashlib - the computed hash from notebook\_signature matches the stored hash

mark\_cells(

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.mark\_cells

Mark cells as trusted if the notebook's signature can be verified

cell.metadata.trusted = True | False

on all code cells, depending on the

parameter. This will typically be the return value from

self.check\_signature(nb)

This function is the inverse of check\_cells

check\_cells(

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.check\_cells

Return whether all code cells are trusted.

A cell is trusted if the 'trusted' field in its metadata is truthy, or if it has no potentially unsafe outputs. If there are no code cells, return True.

This function is the inverse of mark\_cells.

Signature storage

https://nbformat.readthedocs.io/en/latest/api.html#signature-storage

Signatures are stored using a pluggable

SignatureStore

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore

subclass. To implement your own, override the methods below and configure

NotebookNotary.store\_factory

nbformat.sign. SignatureStore

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore

Base class for a signature store.

store\_signature(

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore.store\_signature

Implement in subclass to store a signature.

Should not raise if the signature is already stored.

remove\_signature(

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore.remove\_signature

Implement in subclass to delete a signature.

Should not raise if the signature is not stored.

check\_signature(

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore.check\_signature

Implement in subclass to check if a signature is known.

Return True for a known signature, False for unknown.

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore.close

Close any open connections this store may use.

If the store maintains any open connections (e.g. to a database), they should be closed.

By default,

NotebookNotary

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary

will use an SQLite based store if SQLite bindings are available, and an in-memory store otherwise.

nbformat.sign. SQLiteSignatureStore(\*\* kwargs:

https://docs.python.org/3/library/typing.html#typing.Any

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SQLiteSignatureStore

Store signatures in an SQLite database.

nbformat.sign. MemorySignatureStore

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.MemorySignatureStore

Non-persistent storage of signatures in memory.

previous Supported markup formats

https://nbformat.readthedocs.io/en/latest/markup.html

next Changelog

https://nbformat.readthedocs.io/en/latest/changelog.html

On this page

Reading and writing

https://nbformat.readthedocs.io/en/latest/api.html#reading-and-writing

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.read

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.reads

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.write

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.writes

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NO\_CONVERT

current\_nbformat

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.current\_nbformat

current\_nbformat\_minor

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.current\_nbformat\_minor

NotebookNode objects

https://nbformat.readthedocs.io/en/latest/api.html#notebooknode-objects

NotebookNode

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.NotebookNode

from\_dict()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.from\_dict

Other functions

https://nbformat.readthedocs.io/en/latest/api.html#other-functions

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.convert

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.validate

ValidationError

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.ValidationError

Constructing notebooks programmatically

https://nbformat.readthedocs.io/en/latest/api.html#module-nbformat.v4

new\_notebook()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_notebook

new\_code\_cell()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_code\_cell

new\_markdown\_cell()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_markdown\_cell

new\_raw\_cell()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_raw\_cell

new\_output()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.new\_output

output\_from\_msg()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.v4.output\_from\_msg

Notebook signatures

https://nbformat.readthedocs.io/en/latest/api.html#module-nbformat.sign

NotebookNotary

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary

NotebookNotary.sign()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.sign

NotebookNotary.unsign()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.unsign

NotebookNotary.check\_signature()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.check\_signature

NotebookNotary.mark\_cells()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.mark\_cells

NotebookNotary.check\_cells()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.NotebookNotary.check\_cells

Signature storage

https://nbformat.readthedocs.io/en/latest/api.html#signature-storage

SignatureStore

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore

SignatureStore.store\_signature()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore.store\_signature

SignatureStore.remove\_signature()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore.remove\_signature

SignatureStore.check\_signature()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore.check\_signature

SignatureStore.close()

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SignatureStore.close

SQLiteSignatureStore

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.SQLiteSignatureStore

MemorySignatureStore

https://nbformat.readthedocs.io/en/latest/api.html#nbformat.sign.MemorySignatureStore

Show Source

https://nbformat.readthedocs.io/en/latest/\_sources/api.rst.txt

© Copyright 2015, Jupyter Development Team.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://nbformat.readthedocs.io/en/stable/api.html

https://nbformat.readthedocs.io/en/v5.10.4/api.html

https://nbformat.readthedocs.io/en/v5.10.3/api.html

https://nbformat.readthedocs.io/en/v5.10.2/api.html

https://nbformat.readthedocs.io/en/v5.10.1/api.html

https://nbformat.readthedocs.io/en/v5.10.0/api.html

https://nbformat.readthedocs.io/en/v5.9.2/api.html

https://nbformat.readthedocs.io/en/v5.9.1/api.html

https://nbformat.readthedocs.io/en/v5.9.0/api.html

https://nbformat.readthedocs.io/en/v5.8.0/api.html

https://nbformat.readthedocs.io/en/v5.7.3/api.html

https://nbformat.readthedocs.io/en/v5.7.2/api.html

https://nbformat.readthedocs.io/en/v5.7.1/api.html

https://nbformat.readthedocs.io/en/5.7.0/api.html

https://nbformat.readthedocs.io/en/5.6.1/api.html

https://nbformat.readthedocs.io/en/5.6.0/api.html

https://nbformat.readthedocs.io/en/5.5.0/api.html

https://nbformat.readthedocs.io/en/5.4.0/api.html

https://nbformat.readthedocs.io/en/5.3.0/api.html

https://nbformat.readthedocs.io/en/5.2.0/api.html

https://nbformat.readthedocs.io/en/5.1.3/api.html

https://nbformat.readthedocs.io/en/5.1.2/api.html

https://nbformat.readthedocs.io/en/5.1.1/api.html

https://nbformat.readthedocs.io/en/5.1.0/api.html

https://nbformat.readthedocs.io/en/5.0.8/api.html

https://nbformat.readthedocs.io/en/5.0.7/api.html

https://nbformat.readthedocs.io/en/5.0.6/api.html

https://nbformat.readthedocs.io/en/5.0.5/api.html

https://nbformat.readthedocs.io/en/5.0.4/api.html

https://nbformat.readthedocs.io/en/5.0.3/api.html

https://nbformat.readthedocs.io/en/5.0.2/api.html

https://nbformat.readthedocs.io/en/5.0.1/api.html

https://nbformat.readthedocs.io/en/5.0.0/api.html

https://nbformat.readthedocs.io/en/4.4.0/api.html

https://nbformat.readthedocs.io/en/4.3.0/api.html

https://nbformat.readthedocs.io/en/4.2.0/api.html

https://nbformat.readthedocs.io/en/4.1.0/api.html

https://nbformat.readthedocs.io/en/4.0.1/api.html

https://nbformat.readthedocs.io/en/4.0.0/api.html

https://nbformat.readthedocs.io/en/main/api.html

On Read the Docs

Project Home

https://app.readthedocs.org/projects/nbformat/?utm\_source=nbformat&utm\_content=flyout

https://app.readthedocs.org/projects/nbformat/builds/?utm\_source=nbformat&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=nbformat&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=nbformat&utm\_content=flyout

No recent searches

to navigate

Search powered by


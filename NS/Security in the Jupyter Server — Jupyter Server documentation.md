---
sourceFile: "Security in the Jupyter Server — Jupyter Server documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.612Z"
---

# Security in the Jupyter Server — Jupyter Server documentation

0955e2ce-d6ae-461f-a36f-1909affdace0

Security in the Jupyter Server — Jupyter Server documentation

77ea98b1-bfca-4a10-845a-53d0f8cd93b1

https://jupyter-server.readthedocs.io/en/stable/operators/security.html

Security in the Jupyter Server — Jupyter Server documentation

Skip to main content

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#main-content

Back to top

Jupyter Server documentation - HomeJupyter Server documentation - Home

https://jupyter-server.readthedocs.io/en/stable/index.html

https://jupyter-server.readthedocs.io/en/stable/users/index.html

https://jupyter-server.readthedocs.io/en/stable/operators/index.html

https://jupyter-server.readthedocs.io/en/stable/developers/index.html

Contributors

https://jupyter-server.readthedocs.io/en/stable/contributors/index.html

https://jupyter-server.readthedocs.io/en/stable/other/index.html

System Settings

https://github.com/jupyter-server/jupyter\_server

https://jupyter-server.readthedocs.io/en/stable/users/index.html

https://jupyter-server.readthedocs.io/en/stable/operators/index.html

https://jupyter-server.readthedocs.io/en/stable/developers/index.html

Contributors

https://jupyter-server.readthedocs.io/en/stable/contributors/index.html

https://jupyter-server.readthedocs.io/en/stable/other/index.html

System Settings

https://github.com/jupyter-server/jupyter\_server

Collapse Sidebar Expand Sidebar

Section Navigation

Managing multiple extensions

https://jupyter-server.readthedocs.io/en/stable/operators/multiple-extensions.html

Configuring Extensions

https://jupyter-server.readthedocs.io/en/stable/operators/configuring-extensions.html

Migrating from Notebook Server

https://jupyter-server.readthedocs.io/en/stable/operators/migrate-from-nbserver.html

Running a public Jupyter Server

https://jupyter-server.readthedocs.io/en/stable/operators/public-server.html

Security in the Jupyter Server

https://jupyter-server.readthedocs.io/en/stable/operators/security.html

Configuring Logging

https://jupyter-server.readthedocs.io/en/stable/operators/configuring-logging.html

$ lightcone run "what can I do for you?" — agents that actually act. Try the API →

https://server.ethicalads.io/proxy/click/10604/019f0192-a135-71d3-b7a2-9c4242c9dea1/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Documentation for Operators

https://jupyter-server.readthedocs.io/en/stable/operators/index.html

Security in the Jupyter Server

Security in the Jupyter Server

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#security-in-the-jupyter-server

Since access to the Jupyter Server means access to running arbitrary code, it is important to restrict access to the server. For this reason, Jupyter Server uses a token-based authentication that is

on by default

If you enable a password for your server, token authentication is not enabled by default.

When token authentication is enabled, the server uses a token to authenticate requests. This token can be provided to login to the server in three ways:

Authorization

header, e.g.:

Authorization: token abcdef...

#### In a URL parameter, e.g.:

https://my-server/tree/?token=abcdef...

In the password field of the login form that will be shown to you if you are not logged in.

When you start a Jupyter server with token authentication enabled (default), a token is generated to use for authentication. This token is logged to the terminal, so that you can copy/paste the URL into your browser:

\[I 11:59:16.597 ServerApp\] The Jupyter Server is running at:
\[I 11:59:16.597 ServerApp\]
http://localhost:8888/?token=c8de56fa4deed24899803e93c227592aef6538f93025fe01

\[I 11:59:16.597 ServerApp\]
http://127.0.0.1:8888/?token=c8de56fa4deed24899803e93c227592aef6538f93025fe01

\[I 11:59:16.597 ServerApp\]
    To access the server, open this file in a browser:
    file:///Users/username/Library/Jupyter/runtime/jpserver-46320-open.html
Or copy and paste one of these URLs:
    http://localhost:8888/?token=c8de56fa4deed24899803e93c227592aef6538f93025fe01
    http://127.0.0.1:8888/?token=c8de56fa4deed24899803e93c227592aef6538f93025fe01

Copy either of the HTTP URLs and paste it into your browser to see the server running with a message - “A Jupyter Server is running.” If you are using the file link, opening it in your browser should automatically redirect you to the Jupyter server launch page, including the authentication token. In case it doesn't redirect automatically, you'll find an HTTP link on the page; clicking this link will take you to the Jupyter server landing page.

At any later time, you can see the tokens and URLs for all of your running servers with

jupyter server list

$ jupyter server list
Currently running servers:
http://localhost:8888/?token=abc... :: /home/you/notebooks
https://0.0.0.0:9999/?token=123... :: /tmp/public
http://localhost:8889/ :: /tmp/has-password

For servers with token-authentication enabled, the URL in the above listing will include the token, so you can copy and paste that URL into your browser to login. If a server has no token (e.g. it has a password or has authentication disabled), the URL will not include the token argument. Once you have visited this URL, a cookie will be set in your browser and you won't need to use the token again, unless you switch browsers, clear your cookies, or start a Jupyter server on a new port.

Alternatives to token authentication

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#alternatives-to-token-authentication

If a generated token doesn't work well for you, you can set a password for your server.

jupyter server password

will prompt you for a password, and store the hashed password in your

jupyter\_server\_config.json

It is possible to disable authentication altogether by setting the token and password to empty strings, but this is

NOT RECOMMENDED

, unless authentication or access restrictions are handled at a different layer in your web application:

c.ServerApp.token = ""
c.ServerApp.password = ""

Authentication and Authorization

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#authentication-and-authorization

Added in version 2.0.

There are two steps to deciding whether to allow a given request to be happen.

The first step is “Authentication” (identifying who is making the request). This is handled by the

jupyter\_server.auth.IdentityProvider

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider

Whether a given user is allowed to take a specific action is called “Authorization”, and is handled separately, by an

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.Authorizer

These two classes may work together, as the information returned by the IdentityProvider is given to the Authorizer when it makes its decisions.

Authentication always takes precedence because if no user is authenticated, no authorization checks need to be made, as all requests requiring

authorization

must first complete

authentication

Identity Providers

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#identity-providers

jupyter\_server.auth.IdentityProvider

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider

class is responsible for the “authentication” step, identifying the user making the request, and constructing information about them.

It principally implements two methods.

jupyter\_server.auth. IdentityProvider(\*\* kwargs)

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider

Interface for providing identity management and authentication.

#### Two principle methods:

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider.get\_user

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.User

object for successful authentication, or None for no-identity-found.

identity\_model()

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider.identity\_model

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.User

into a JSONable dict. The default is to use

dataclasses.asdict()

, and usually shouldn't need override.

Additional methods can customize authentication.

Added in version 2.0.

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider.get\_user

Get the authenticated user for a request

Must return a

jupyter\_server.auth.User

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.User

, though it may be a subclass.

Return None if the request is not authenticated.

be a coroutine

#### Return type:

https://jupyter-server.readthedocs.io/en/stable/api/jupyter\_server.auth.html#jupyter\_server.auth.identity.User

https://docs.python.org/3/library/constants.html#None

https://docs.python.org/3/library/typing.html#typing.Awaitable

https://jupyter-server.readthedocs.io/en/stable/api/jupyter\_server.auth.html#jupyter\_server.auth.identity.User

https://docs.python.org/3/library/constants.html#None

identity\_model(

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider.identity\_model

Return a User as an Identity model

#### Return type:

https://docs.python.org/3/library/stdtypes.html#dict

https://docs.python.org/3/library/stdtypes.html#str

https://docs.python.org/3/library/typing.html#typing.Any

The first is

jupyter\_server.auth.IdentityProvider.get\_user()

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider.get\_user

. This method is given a RequestHandler, and is responsible for deciding whether there is an authenticated user making the request. If the request is authenticated, it should return a

jupyter\_server.auth.User

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.User

object representing the authenticated user. It should return None if the request is not authenticated.

The default implementation accepts token or password authentication.

This User object will be available as

self.current\_user

in any request handler. Request methods decorated with tornado's

@web.authenticated

decorator will only be allowed if this method returns something.

The User object will be a Python

dataclasses.dataclass

jupyter\_server.auth.User

jupyter\_server.auth. User(

display\_name=''

initials= None

avatar\_url= None

color= None

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.User

Object representing a User

This or a subclass should be returned from IdentityProvider.get\_user

A custom IdentityProvider

return a custom subclass.

The next method an identity provider has is

identity\_model()

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider.identity\_model

identity\_model(user)

is responsible for transforming the user object returned from

.get\_user()

into a standard identity model dictionary, for use in the

If your user object is a simple username string or a dict with a

field, you may not need to implement this method, as the default implementation will suffice.

Any required fields missing from the dict returned by this method will be filled-out with defaults. Only

is strictly required, if that is all the information the identity provider has available.

#### Missing will be derived according to:

is missing, use

display\_name

is missing, use

Other required fields will be filled with

Identity Model

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#identity-model

The identity model is the model accessed at

, and describes the currently authenticated user.

#### It has the following fields:

(string) Unique string identifying the user. Must be non-empty.

(string) For-humans name of the user. May be the same as

in systems where only usernames are available.

display\_name

(string) Alternate rendering of name for display, such as a nickname. Often the same as

(string or null) Short string of initials. Initials should not be derived automatically due to localization issues. May be

if unavailable.

(string or null) URL of an avatar image to be used for the user. May be

if unavailable.

(string or null) A CSS color string to use as a preferred color, such as for collaboration cursors. May be

if unavailable.

The default implementation of the identity provider is stateless, meaning it doesn't store user information on the server side. Instead, it utilizes session cookies to generate and store random user information on the client side.

When a user logs in or authenticates, the server generates a session cookie that is stored on the client side. This session cookie is used to keep track of the identity model between requests. If the client does not support session cookies or fails to send the cookie in subsequent requests, the server will treat each request as coming from a new anonymous user and generate a new set of random user information for each request.

To ensure proper functionality of the identity model and to maintain user context between requests, it's important for clients to support session cookies and send it in subsequent requests. Failure to do so may result in the server generating a new anonymous user for each request, leading to loss of user context.

Authorization

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#authorization

Authorization is the second step in allowing an action, after a user has been

authenticated

by the IdentityProvider.

Authorization in Jupyter Server serves to provide finer grained control of access to its API resources. With authentication, requests are accepted if the current user is known by the server. Thus it can restrain access to specific users, but there is no way to give allowed users more or less permissions. Jupyter Server provides a thin and extensible authorization layer which checks if the current user is authorized to make a specific request.

jupyter\_server.auth. Authorizer(\*\* kwargs)

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.Authorizer

Base class for authorizing access to resources in the Jupyter Server.

All authorizers used in Jupyter Server should inherit from this base class and, at the very minimum, implement an

is\_authorized

method with the same signature as in this base class.

is\_authorized

method is called by the

@authorized

decorator in JupyterHandler. If it returns True, the incoming request to the server is accepted; if it returns False, the server returns a 403 (Forbidden) error code.

The authorization check will only be applied to requests that have already been authenticated.

Added in version 2.0.

is\_authorized(

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.Authorizer.is\_authorized

A method to determine if

is authorized to perform

(read, write, or execute) on the

#### Parameters:

jupyter\_server.auth.User

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.User

) – An object representing the authenticated user, as returned by

jupyter\_server.auth.IdentityProvider.get\_user()

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider.get\_user

https://docs.python.org/3/library/stdtypes.html#str

) – the category of action for the current request: read, write, or execute.

https://docs.python.org/3/library/stdtypes.html#str

) – the type of resource (i.e. contents, kernels, files, etc.) the user is requesting.

True if user authorized to make request; False, otherwise

#### Return type:

https://docs.python.org/3/library/functions.html#bool

This is done by calling a

is\_authorized(handler, user, action, resource)

method before each request handler. Each request is labeled as either a “read”, “write”, or “execute”

“read” wraps all

requests. In general, read permissions grants access to read but not modify anything about the given resource.

“write” wraps all

requests. In general, write permissions grants access to modify the given resource.

“execute” wraps all requests to ZMQ/Websocket channels (terminals and kernels). Execute is a special permission that usually corresponds to arbitrary execution, such as via a kernel or terminal. These permissions should generally be considered sufficient to perform actions equivalent to ~all other permissions via other means.

being accessed refers to the resource name in the Jupyter Server's API endpoints. In most cases, this is the field after

. For instance, values for

in the endpoints provided by the base Jupyter Server package, and the corresponding permissions:

resource name

what can you do with read permissions?

what can you do with write permissions?

what can you do with execute permissions, if anything?

what endpoints are governed by this resource?

read server status (last activity, number of kernels, etc.), OpenAPI specification

/api/status

/api/spec.yaml

report content-security-policy violations

/api/security/csp-report

read frontend configuration, such as for notebook extensions

modify frontend configuration

/api/config

modify files (create, modify, delete)

/api/contents

list kernels, get status of kernels

start, stop, and restart kernels

Connect to kernel websockets, send/recv kernel messages.

This generally means arbitrary code execution, and should usually be considered equivalent to having all other permissions.

/api/kernels

kernelspecs

read, list information about available kernels

/api/kernelspecs

render notebooks to other formats via nbconvert.

Note: depending on server-side configuration, this could involve execution.

/api/nbconvert

Shutdown the server

/api/shutdown

list current sessions (association of documents to kernels)

create, modify, and delete existing sessions, which includes starting, stopping, and deleting kernels.

/api/sessions

list running terminals and their last activity

start new terminals, stop running terminals

Connect to terminal websockets, execute code in a shell.

This generally means arbitrary code execution, and should usually be considered equivalent to having all other permissions.

/api/terminals

Extensions may define their own resources. Extension resources should start with

extension\_name:

to avoid namespace conflicts.

is\_authorized(...)

, the request is made; otherwise, a

HTTPError(403)

(403 means “Forbidden”) error is raised, and the request is blocked.

By default, authorization is turned off—i.e.

is\_authorized()

always returns

and all authenticated users are allowed to make all types of requests. To turn-on authorization, pass a class that inherits from

ServerApp.authorizer\_class

parameter, implementing a

is\_authorized()

method with your desired authorization logic, as follows:

from jupyter\_server.auth import Authorizer

class MyAuthorizationManager(Authorizer):
    """Class for authorizing access to resources in the Jupyter Server.

    All authorizers used in Jupyter Server should inherit from
    AuthorizationManager and, at the very minimum, override and implement
    an \`is\_authorized\` method with the following signature.

    The \`is\_authorized\` method is called by the \`@authorized\` decorator in
    JupyterHandler. If it returns True, the incoming request to the server
    is accepted; if it returns False, the server returns a 403 (Forbidden) error code.
    """

    def is\_authorized(
        self, handler: JupyterHandler, user: Any, action: str, resource: str
    ) -> bool:
        """A method to determine if \`user\` is authorized to perform \`action\`
        (read, write, or execute) on the \`resource\` type.

        Parameters
        ------------
        user : usually a dict or string
            A truthy model representing the authenticated user.
            A username string by default,
            but usually a dict when integrating with an auth provider.

        action : str
            the category of action for the current request: read, write, or execute.

        resource : str
            the type of resource (i.e. contents, kernels, files, etc.) the user is requesting.

        Returns True if user authorized to make request; otherwise, returns False.
        """
        return True  # implement your authorization logic here

is\_authorized()

method will automatically be called whenever a handler is decorated with

@authorized

jupyter\_server.auth

), similarly to the

@authenticated

decorator for authentication (from

tornado.web

Kernel transport encryption

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#kernel-transport-encryption

Added in version 2.20.

By default, ZMQ sockets used to communicate with kernels (shell, IOPub, stdin, control, heartbeat) are bound to TCP ports with no transport-level encryption. Any process on the same host that can reach those ports can connect and read messages, including all IOPub output.

https://rfc.zeromq.org/spec/26/

adds elliptic-curve encryption and authentication directly at the ZMQ transport layer. When enabled, the

KernelManager

generates a keypair, writes the keys into the kernel's connection file, and configures all sockets as a CurveZMQ server. Clients must present the correct server public key to connect; unauthenticated connections are silently dropped before any data is delivered.

CurveZMQ is only available when pyzmq was compiled against a libzmq that includes libsodium. You can verify this with:

python -c "import zmq; print(zmq.has('curve'))"

If this prints

transport\_encryption

setting has no effect and attempts to set it to

will raise a configuration error.

transport\_encryption

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#the-transport-encryption-setting

Transport encryption is controlled by the

KernelManager.transport\_encryption

traitlet, which accepts three values:

No CurveZMQ keys are generated. All kernel sockets are unencrypted.

Keys are generated

only when the kernelspec declares support

metadata.supported\_encryption: \['curve'\]

. Kernelspecs that do not declare this field are started without encryption, so the setting is safe to enable globally without breaking existing kernels.

Keys are always generated. Startup fails with a

RuntimeError

if the kernelspec does not declare

metadata.supported\_encryption: \['curve'\]

, so kernels that have not been updated to handle the connection-file keys are never started unencrypted.

transport\_encryption

applies to both the

transports. IPC sockets also rely on filesystem permissions for access control, but CurveZMQ can be layered on top for defense in depth.

To enable encryption globally for all kernels that support it, add the following to your

jupyter\_server\_config.py

c.KernelManager.transport\_encryption = "auto"

#### To enforce encryption and prevent unencrypted kernels from starting:

c.KernelManager.transport\_encryption = "required"

Kernelspec requirements

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#kernelspec-requirements

A kernel must declare CurveZMQ support in its

kernel.json

KernelManager

will provision keys for it:

{
    "argv": \["python", "-m", "ipykernel\_launcher", "-f", "{connection\_file}"\],
    "display\_name": "Python 3",
    "language": "python",
    "metadata": {
        "supported\_encryption": \["curve"\]
    }
}

transport\_encryption

, kernelspecs without this field are started normally without encryption. When it is

, their startup is refused.

The kernel itself must read

curve\_publickey

curve\_secretkey

from the connection file and apply them to its ZMQ sockets. Kernels based on ipykernel 7.3 do this automatically when the fields are present.

When updating a previously installed kernel to a version that supports encryption you may need to re-install the kernelspec or manually add the

supported\_encryption

metadata field. If you subsequently decide to downgrade, you will need to remove this field as otherwise the kernel will silently fail to connect.

Security in notebook documents

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#security-in-notebook-documents

As Jupyter Server become more popular for sharing and collaboration, the potential for malicious people to attempt to exploit the notebook for their nefarious purposes increases. IPython 2.0 introduced a security model to prevent execution of untrusted code without explicit user input.

The problem

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#the-problem

The whole point of Jupyter is arbitrary code execution. We have no desire to limit what can be done with a notebook, which would negatively impact its utility.

Unlike other programs, a Jupyter notebook document includes output. Unlike other documents, that output exists in a context that can execute code (via Javascript).

The security problem we need to solve is that no code should execute just because a user has

a notebook that

they did not write

. Like any other program, once a user decides to execute code in a notebook, it is considered trusted, and should be allowed to do anything.

Our security model

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#our-security-model

Untrusted HTML is always sanitized

Untrusted Javascript is never executed

HTML and Javascript in Markdown cells are never trusted

generated by the user are trusted

Any other HTML or Javascript (in Markdown cells, output generated by others) is never trusted

The central question of trust is “Did the current user do this?”

The details of trust

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#the-details-of-trust

When a notebook is executed and saved, a signature is computed from a digest of the notebook's contents plus a secret key. This is stored in a database, writable only by the current user. By default, this is located at:

~/.local/share/jupyter/nbsignatures.db  # Linux
~/Library/Jupyter/nbsignatures.db       # OS X
%APPDATA%/jupyter/nbsignatures.db       # Windows

Each signature represents a series of outputs which were produced by code the current user executed, and are therefore trusted.

When you open a notebook, the server computes its signature, and checks if it's in the database. If a match is found, HTML and Javascript output in the notebook will be trusted at load, otherwise it will be untrusted.

Any output generated during an interactive session is trusted.

Updating trust

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#updating-trust

A notebook's trust is updated when the notebook is saved. If there are any untrusted outputs still in the notebook, the notebook will not be trusted, and no signature will be stored. If all untrusted outputs have been removed (either via

Clear Output

or re-execution), then the notebook will become trusted.

While trust is updated per output, this is only for the duration of a single session. A newly loaded notebook file is either trusted or not in its entirety.

Explicit trust

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#explicit-trust

Sometimes re-executing a notebook to generate trusted output is not an option, either because dependencies are unavailable, or it would take a long time. Users can explicitly trust a notebook in two ways:

#### At the command-line, with:

jupyter trust /path/to/notebook.ipynb

After loading the untrusted notebook, with

File / Trust Notebook

These two methods simply load the notebook, compute a new signature, and add that signature to the user's database.

Content-Security-Policy for nbconvert

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#content-security-policy-for-nbconvert

When notebooks are rendered via nbconvert (

/nbconvert/

endpoints), the server adds a

sandbox allow-scripts

directive to the

Content-Security-Policy

header by default. This confines any JavaScript in the rendered output to a unique origin, preventing it from interacting with the Jupyter server.

This behavior is controlled by

nbconvert\_csp\_sandbox

https://jupyter-server.readthedocs.io/en/stable/api/jupyter\_server.html#jupyter\_server.serverapp.ServerApp.nbconvert\_csp\_sandbox

# jupyter\_server\_config.py
c.ServerApp.nbconvert\_csp\_sandbox = True  # default

Reporting security issues

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#reporting-security-issues

If you find a security vulnerability in Jupyter, either a failure of the code to properly implement the model described here, or a failure of the model itself, please report it to

security@ ipython. org

mailto:security%40ipython.org

Affected use cases

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#affected-use-cases

Some use cases that work in Jupyter 1.0 became less convenient in 2.0 as a result of the security changes. We do our best to minimize these annoyances, but security is always at odds with convenience.

Javascript and CSS in Markdown cells

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#javascript-and-css-in-markdown-cells

While never officially supported, it had become common practice to put hidden Javascript or CSS styling in Markdown cells, so that they would not be visible on the page. Since Markdown cells are now sanitized (by

Google Caja

https://developers.google.com/caja

), all Javascript (including click event handlers, etc.) and CSS will be stripped.

We plan to provide a mechanism for notebook themes, but in the meantime styling the notebook can only be done via either

or CSS in HTML output. The latter only have an effect if the notebook is trusted, because otherwise the output will be sanitized just like Markdown.

Collaboration

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#collaboration

When collaborating on a notebook, people probably want to see the outputs produced by their colleagues' most recent executions. Since each collaborator's key will differ, this will result in each share starting in an untrusted state. There are three basic approaches to this:

re-run notebooks when you get them (not always viable)

explicitly trust notebooks via

jupyter trust

or the notebook menu (annoying, but easy)

share a notebook signatures database, and use configuration dedicated to the collaboration while working on the project.

#### To share a signatures database among users, you can configure:

c.NotebookNotary.data\_dir = "/path/to/signature\_dir"

to specify a non-default path to the SQLite database (of notebook hashes, essentially).

previous Running a public Jupyter Server

https://jupyter-server.readthedocs.io/en/stable/operators/public-server.html

next Configuring Logging

https://jupyter-server.readthedocs.io/en/stable/operators/configuring-logging.html

On this page

Security in the Jupyter Server

https://jupyter-server.readthedocs.io/en/stable/operators/security.html

Alternatives to token authentication

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#alternatives-to-token-authentication

Authentication and Authorization

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#authentication-and-authorization

Identity Providers

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#identity-providers

IdentityProvider

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider

IdentityProvider.get\_user()

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider.get\_user

IdentityProvider.identity\_model()

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.IdentityProvider.identity\_model

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.User

Identity Model

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#identity-model

Authorization

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#authorization

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.Authorizer

Authorizer.is\_authorized()

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#jupyter\_server.auth.Authorizer.is\_authorized

Kernel transport encryption

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#kernel-transport-encryption

The transport\_encryption setting

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#the-transport-encryption-setting

Kernelspec requirements

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#kernelspec-requirements

Security in notebook documents

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#security-in-notebook-documents

The problem

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#the-problem

Our security model

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#our-security-model

The details of trust

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#the-details-of-trust

Updating trust

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#updating-trust

Explicit trust

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#explicit-trust

Content-Security-Policy for nbconvert

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#content-security-policy-for-nbconvert

Reporting security issues

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#reporting-security-issues

Affected use cases

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#affected-use-cases

Javascript and CSS in Markdown cells

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#javascript-and-css-in-markdown-cells

Collaboration

https://jupyter-server.readthedocs.io/en/stable/operators/security.html#collaboration

Edit on GitHub

https://github.com/jupyter-server/jupyter\_server/edit/main/docs/source/operators/security.rst

Show Source

https://jupyter-server.readthedocs.io/en/stable/\_sources/operators/security.rst.txt

© Copyright 2020, Jupyter Team, https://jupyter.org.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://jupyter-server.readthedocs.io/en/latest/operators/security.html

https://jupyter-server.readthedocs.io/\_/downloads/en/stable/htmlzip/

https://jupyter-server.readthedocs.io/\_/downloads/en/stable/epub/

On Read the Docs

Project Home

https://app.readthedocs.org/projects/jupyter-server/?utm\_source=jupyter-server&utm\_content=flyout

https://app.readthedocs.org/projects/jupyter-server/builds/?utm\_source=jupyter-server&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=jupyter-server&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=jupyter-server&utm\_content=flyout

No recent searches

to navigate

Search powered by


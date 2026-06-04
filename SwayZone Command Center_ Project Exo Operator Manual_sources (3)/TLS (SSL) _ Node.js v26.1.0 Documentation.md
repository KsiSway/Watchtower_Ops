---
sourceFile: "TLS (SSL) | Node.js v26.1.0 Documentation"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.724Z"
---

# TLS (SSL) | Node.js v26.1.0 Documentation

6fdfcf48-0695-4c64-a1cb-9ef7cd0d918d

TLS (SSL) | Node.js v26.1.0 Documentation

50fb03ba-f6aa-496f-95e7-e7543eda16de

https://nodejs.org/api/tls.html#tlsgetcacertificates-type

TLS (SSL) | Node.js v26.1.0 Documentation

Skip to content

https://nodejs.org/api/tls.html#apicontent

https://nodejs.org/

About this documentation

https://nodejs.org/api/documentation.html

Usage and example

https://nodejs.org/api/synopsis.html

Assertion testing

https://nodejs.org/api/assert.html

Asynchronous context tracking

https://nodejs.org/api/async\_context.html

Async hooks

https://nodejs.org/api/async\_hooks.html

https://nodejs.org/api/buffer.html

https://nodejs.org/api/addons.html

C/C++ addons with Node-API

https://nodejs.org/api/n-api.html

C++ embedder API

https://nodejs.org/api/embedding.html

Child processes

https://nodejs.org/api/child\_process.html

https://nodejs.org/api/cluster.html

Command-line options

https://nodejs.org/api/cli.html

https://nodejs.org/api/console.html

https://nodejs.org/api/crypto.html

https://nodejs.org/api/debugger.html

Deprecated APIs

https://nodejs.org/api/deprecations.html

Diagnostics Channel

https://nodejs.org/api/diagnostics\_channel.html

https://nodejs.org/api/dns.html

https://nodejs.org/api/domain.html

Environment Variables

https://nodejs.org/api/environment\_variables.html

https://nodejs.org/api/errors.html

https://nodejs.org/api/events.html

File system

https://nodejs.org/api/fs.html

https://nodejs.org/api/ffi.html

https://nodejs.org/api/globals.html

https://nodejs.org/api/http.html

https://nodejs.org/api/http2.html

https://nodejs.org/api/https.html

https://nodejs.org/api/inspector.html

Internationalization

https://nodejs.org/api/intl.html

Iterable Streams API

https://nodejs.org/api/stream\_iter.html

Modules: CommonJS modules

https://nodejs.org/api/modules.html

Modules: ECMAScript modules

https://nodejs.org/api/esm.html

Modules: node:module API

https://nodejs.org/api/module.html

Modules: Packages

https://nodejs.org/api/packages.html

Modules: TypeScript

https://nodejs.org/api/typescript.html

https://nodejs.org/api/net.html

https://nodejs.org/api/os.html

https://nodejs.org/api/path.html

Performance hooks

https://nodejs.org/api/perf\_hooks.html

Permissions

https://nodejs.org/api/permissions.html

https://nodejs.org/api/process.html

https://nodejs.org/api/punycode.html

Query strings

https://nodejs.org/api/querystring.html

https://nodejs.org/api/readline.html

https://nodejs.org/api/repl.html

https://nodejs.org/api/report.html

Single executable applications

https://nodejs.org/api/single-executable-applications.html

https://nodejs.org/api/sqlite.html

https://nodejs.org/api/stream.html

String decoder

https://nodejs.org/api/string\_decoder.html

Test runner

https://nodejs.org/api/test.html

https://nodejs.org/api/timers.html

https://nodejs.org/api/tls.html

Trace events

https://nodejs.org/api/tracing.html

https://nodejs.org/api/tty.html

UDP/datagram

https://nodejs.org/api/dgram.html

https://nodejs.org/api/url.html

https://nodejs.org/api/util.html

https://nodejs.org/api/v8.html

https://nodejs.org/api/vm.html

https://nodejs.org/api/wasi.html

Web Crypto API

https://nodejs.org/api/webcrypto.html

Web Streams API

https://nodejs.org/api/webstreams.html

Worker threads

https://nodejs.org/api/worker\_threads.html

https://nodejs.org/api/zlib.html

Code repository and issue tracker

https://github.com/nodejs/node

Node.js v26.1.0 documentation

Node.js v26.1.0

Table of contents

https://nodejs.org/api/tls.html#toc-picker

https://nodejs.org/api/tls.html#tls-ssl

Determining if crypto support is unavailable

https://nodejs.org/api/tls.html#determining-if-crypto-support-is-unavailable

TLS/SSL concepts

https://nodejs.org/api/tls.html#tlsssl-concepts

Perfect forward secrecy

https://nodejs.org/api/tls.html#perfect-forward-secrecy

ALPN and SNI

https://nodejs.org/api/tls.html#alpn-and-sni

Pre-shared keys

https://nodejs.org/api/tls.html#pre-shared-keys

Client-initiated renegotiation attack mitigation

https://nodejs.org/api/tls.html#client-initiated-renegotiation-attack-mitigation

Session resumption

https://nodejs.org/api/tls.html#session-resumption

Session identifiers

https://nodejs.org/api/tls.html#session-identifiers

Session tickets

https://nodejs.org/api/tls.html#session-tickets

Modifying the default TLS cipher suite

https://nodejs.org/api/tls.html#modifying-the-default-tls-cipher-suite

OpenSSL security level

https://nodejs.org/api/tls.html#openssl-security-level

Setting security levels

https://nodejs.org/api/tls.html#setting-security-levels

Using --tls-cipher-list

https://nodejs.org/api/tls.html#-tls-cipher-list

X509 certificate error codes

https://nodejs.org/api/tls.html#x509-certificate-error-codes

Class: tls.Server

https://nodejs.org/api/tls.html#class-tlsserver

Event: 'connection'

https://nodejs.org/api/tls.html#event-connection

Event: 'keylog'

https://nodejs.org/api/tls.html#event-keylog

Event: 'newSession'

https://nodejs.org/api/tls.html#event-newsession

Event: 'OCSPRequest'

https://nodejs.org/api/tls.html#event-ocsprequest

Event: 'resumeSession'

https://nodejs.org/api/tls.html#event-resumesession

Event: 'secureConnection'

https://nodejs.org/api/tls.html#event-secureconnection

Event: 'tlsClientError'

https://nodejs.org/api/tls.html#event-tlsclienterror

server.addContext(hostname, context)

https://nodejs.org/api/tls.html#serveraddcontexthostname-context

server.address()

https://nodejs.org/api/tls.html#serveraddress

server.close(\[callback\])

https://nodejs.org/api/tls.html#serverclosecallback

server.getTicketKeys()

https://nodejs.org/api/tls.html#servergetticketkeys

server.listen()

https://nodejs.org/api/tls.html#serverlisten

server.setSecureContext(options)

https://nodejs.org/api/tls.html#serversetsecurecontextoptions

server.setTicketKeys(keys)

https://nodejs.org/api/tls.html#serversetticketkeyskeys

Class: tls.TLSSocket

https://nodejs.org/api/tls.html#class-tlstlssocket

new tls.TLSSocket(socket\[, options\])

https://nodejs.org/api/tls.html#new-tlstlssocketsocket-options

Event: 'keylog'

https://nodejs.org/api/tls.html#event-keylog-1

Event: 'OCSPResponse'

https://nodejs.org/api/tls.html#event-ocspresponse

Event: 'secure'

https://nodejs.org/api/tls.html#event-secure

Event: 'secureConnect'

https://nodejs.org/api/tls.html#event-secureconnect

Event: 'session'

https://nodejs.org/api/tls.html#event-session

tlsSocket.address()

https://nodejs.org/api/tls.html#tlssocketaddress

tlsSocket.authorizationError

https://nodejs.org/api/tls.html#tlssocketauthorizationerror

tlsSocket.authorized

https://nodejs.org/api/tls.html#tlssocketauthorized

tlsSocket.disableRenegotiation()

https://nodejs.org/api/tls.html#tlssocketdisablerenegotiation

tlsSocket.enableTrace()

https://nodejs.org/api/tls.html#tlssocketenabletrace

tlsSocket.encrypted

https://nodejs.org/api/tls.html#tlssocketencrypted

tlsSocket.exportKeyingMaterial(length, label\[, context\])

https://nodejs.org/api/tls.html#tlssocketexportkeyingmateriallength-label-context

tlsSocket.getCertificate()

https://nodejs.org/api/tls.html#tlssocketgetcertificate

tlsSocket.getCipher()

https://nodejs.org/api/tls.html#tlssocketgetcipher

tlsSocket.getEphemeralKeyInfo()

https://nodejs.org/api/tls.html#tlssocketgetephemeralkeyinfo

tlsSocket.getFinished()

https://nodejs.org/api/tls.html#tlssocketgetfinished

tlsSocket.getPeerCertificate(\[detailed\])

https://nodejs.org/api/tls.html#tlssocketgetpeercertificatedetailed

Certificate object

https://nodejs.org/api/tls.html#certificate-object

tlsSocket.getPeerFinished()

https://nodejs.org/api/tls.html#tlssocketgetpeerfinished

tlsSocket.getPeerX509Certificate()

https://nodejs.org/api/tls.html#tlssocketgetpeerx509certificate

tlsSocket.getProtocol()

https://nodejs.org/api/tls.html#tlssocketgetprotocol

tlsSocket.getSession()

https://nodejs.org/api/tls.html#tlssocketgetsession

tlsSocket.getSharedSigalgs()

https://nodejs.org/api/tls.html#tlssocketgetsharedsigalgs

tlsSocket.getTLSTicket()

https://nodejs.org/api/tls.html#tlssocketgettlsticket

tlsSocket.getX509Certificate()

https://nodejs.org/api/tls.html#tlssocketgetx509certificate

tlsSocket.isSessionReused()

https://nodejs.org/api/tls.html#tlssocketissessionreused

tlsSocket.localAddress

https://nodejs.org/api/tls.html#tlssocketlocaladdress

tlsSocket.localPort

https://nodejs.org/api/tls.html#tlssocketlocalport

tlsSocket.remoteAddress

https://nodejs.org/api/tls.html#tlssocketremoteaddress

tlsSocket.remoteFamily

https://nodejs.org/api/tls.html#tlssocketremotefamily

tlsSocket.remotePort

https://nodejs.org/api/tls.html#tlssocketremoteport

tlsSocket.renegotiate(options, callback)

https://nodejs.org/api/tls.html#tlssocketrenegotiateoptions-callback

tlsSocket.setKeyCert(context)

https://nodejs.org/api/tls.html#tlssocketsetkeycertcontext

tlsSocket.setMaxSendFragment(size)

https://nodejs.org/api/tls.html#tlssocketsetmaxsendfragmentsize

tls.checkServerIdentity(hostname, cert)

https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert

tls.connect(options\[, callback\])

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

tls.connect(path\[, options\]\[, callback\])

https://nodejs.org/api/tls.html#tlsconnectpath-options-callback

tls.connect(port\[, host\]\[, options\]\[, callback\])

https://nodejs.org/api/tls.html#tlsconnectport-host-options-callback

tls.createSecureContext(\[options\])

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

tls.createServer(\[options\]\[, secureConnectionListener\])

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

tls.setDefaultCACertificates(certs)

https://nodejs.org/api/tls.html#tlssetdefaultcacertificatescerts

tls.getCACertificates(\[type\])

https://nodejs.org/api/tls.html#tlsgetcacertificatestype

tls.getCiphers()

https://nodejs.org/api/tls.html#tlsgetciphers

tls.rootCertificates

https://nodejs.org/api/tls.html#tlsrootcertificates

tls.DEFAULT\_ECDH\_CURVE

https://nodejs.org/api/tls.html#tlsdefault\_ecdh\_curve

tls.DEFAULT\_MAX\_VERSION

https://nodejs.org/api/tls.html#tlsdefault\_max\_version

tls.DEFAULT\_MIN\_VERSION

https://nodejs.org/api/tls.html#tlsdefault\_min\_version

tls.DEFAULT\_CIPHERS

https://nodejs.org/api/tls.html#tlsdefault\_ciphers

https://nodejs.org/api/tls.html#gtoc-picker

https://nodejs.org/api/index.html

About this documentation

https://nodejs.org/api/documentation.html

Usage and example

https://nodejs.org/api/synopsis.html

Assertion testing

https://nodejs.org/api/assert.html

Asynchronous context tracking

https://nodejs.org/api/async\_context.html

Async hooks

https://nodejs.org/api/async\_hooks.html

https://nodejs.org/api/buffer.html

https://nodejs.org/api/addons.html

C/C++ addons with Node-API

https://nodejs.org/api/n-api.html

C++ embedder API

https://nodejs.org/api/embedding.html

Child processes

https://nodejs.org/api/child\_process.html

https://nodejs.org/api/cluster.html

Command-line options

https://nodejs.org/api/cli.html

https://nodejs.org/api/console.html

https://nodejs.org/api/crypto.html

https://nodejs.org/api/debugger.html

Deprecated APIs

https://nodejs.org/api/deprecations.html

Diagnostics Channel

https://nodejs.org/api/diagnostics\_channel.html

https://nodejs.org/api/dns.html

https://nodejs.org/api/domain.html

Environment Variables

https://nodejs.org/api/environment\_variables.html

https://nodejs.org/api/errors.html

https://nodejs.org/api/events.html

File system

https://nodejs.org/api/fs.html

https://nodejs.org/api/ffi.html

https://nodejs.org/api/globals.html

https://nodejs.org/api/http.html

https://nodejs.org/api/http2.html

https://nodejs.org/api/https.html

https://nodejs.org/api/inspector.html

Internationalization

https://nodejs.org/api/intl.html

Iterable Streams API

https://nodejs.org/api/stream\_iter.html

Modules: CommonJS modules

https://nodejs.org/api/modules.html

Modules: ECMAScript modules

https://nodejs.org/api/esm.html

Modules: node:module API

https://nodejs.org/api/module.html

Modules: Packages

https://nodejs.org/api/packages.html

Modules: TypeScript

https://nodejs.org/api/typescript.html

https://nodejs.org/api/net.html

https://nodejs.org/api/os.html

https://nodejs.org/api/path.html

Performance hooks

https://nodejs.org/api/perf\_hooks.html

Permissions

https://nodejs.org/api/permissions.html

https://nodejs.org/api/process.html

https://nodejs.org/api/punycode.html

Query strings

https://nodejs.org/api/querystring.html

https://nodejs.org/api/readline.html

https://nodejs.org/api/repl.html

https://nodejs.org/api/report.html

Single executable applications

https://nodejs.org/api/single-executable-applications.html

https://nodejs.org/api/sqlite.html

https://nodejs.org/api/stream.html

String decoder

https://nodejs.org/api/string\_decoder.html

Test runner

https://nodejs.org/api/test.html

https://nodejs.org/api/timers.html

https://nodejs.org/api/tls.html

Trace events

https://nodejs.org/api/tracing.html

https://nodejs.org/api/tty.html

UDP/datagram

https://nodejs.org/api/dgram.html

https://nodejs.org/api/url.html

https://nodejs.org/api/util.html

https://nodejs.org/api/v8.html

https://nodejs.org/api/vm.html

https://nodejs.org/api/wasi.html

Web Crypto API

https://nodejs.org/api/webcrypto.html

Web Streams API

https://nodejs.org/api/webstreams.html

Worker threads

https://nodejs.org/api/worker\_threads.html

https://nodejs.org/api/zlib.html

Other versions

https://nodejs.org/api/tls.html#alt-docs

https://nodejs.org/docs/latest-v26.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v25.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v24.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v23.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v22.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v21.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v20.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v19.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v18.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v17.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v16.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v15.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v14.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v13.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v12.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v11.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v10.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v9.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v8.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v7.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v6.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v5.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v4.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v0.12.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/docs/latest-v0.10.x/api/tls.html#tlsgetcacertificates-type

https://nodejs.org/api/tls.html#options-picker

View on single page

https://nodejs.org/api/all.html

View as JSON

https://nodejs.org/api/tls.json

Edit on GitHub

https://github.com/nodejs/node/edit/main/doc/api/tls.md

Table of contents

https://nodejs.org/api/tls.html#tls-ssl

Determining if crypto support is unavailable

https://nodejs.org/api/tls.html#determining-if-crypto-support-is-unavailable

TLS/SSL concepts

https://nodejs.org/api/tls.html#tlsssl-concepts

Perfect forward secrecy

https://nodejs.org/api/tls.html#perfect-forward-secrecy

ALPN and SNI

https://nodejs.org/api/tls.html#alpn-and-sni

Pre-shared keys

https://nodejs.org/api/tls.html#pre-shared-keys

Client-initiated renegotiation attack mitigation

https://nodejs.org/api/tls.html#client-initiated-renegotiation-attack-mitigation

Session resumption

https://nodejs.org/api/tls.html#session-resumption

Session identifiers

https://nodejs.org/api/tls.html#session-identifiers

Session tickets

https://nodejs.org/api/tls.html#session-tickets

Modifying the default TLS cipher suite

https://nodejs.org/api/tls.html#modifying-the-default-tls-cipher-suite

OpenSSL security level

https://nodejs.org/api/tls.html#openssl-security-level

Setting security levels

https://nodejs.org/api/tls.html#setting-security-levels

Using --tls-cipher-list

https://nodejs.org/api/tls.html#-tls-cipher-list

X509 certificate error codes

https://nodejs.org/api/tls.html#x509-certificate-error-codes

Class: tls.Server

https://nodejs.org/api/tls.html#class-tlsserver

Event: 'connection'

https://nodejs.org/api/tls.html#event-connection

Event: 'keylog'

https://nodejs.org/api/tls.html#event-keylog

Event: 'newSession'

https://nodejs.org/api/tls.html#event-newsession

Event: 'OCSPRequest'

https://nodejs.org/api/tls.html#event-ocsprequest

Event: 'resumeSession'

https://nodejs.org/api/tls.html#event-resumesession

Event: 'secureConnection'

https://nodejs.org/api/tls.html#event-secureconnection

Event: 'tlsClientError'

https://nodejs.org/api/tls.html#event-tlsclienterror

server.addContext(hostname, context)

https://nodejs.org/api/tls.html#serveraddcontexthostname-context

server.address()

https://nodejs.org/api/tls.html#serveraddress

server.close(\[callback\])

https://nodejs.org/api/tls.html#serverclosecallback

server.getTicketKeys()

https://nodejs.org/api/tls.html#servergetticketkeys

server.listen()

https://nodejs.org/api/tls.html#serverlisten

server.setSecureContext(options)

https://nodejs.org/api/tls.html#serversetsecurecontextoptions

server.setTicketKeys(keys)

https://nodejs.org/api/tls.html#serversetticketkeyskeys

Class: tls.TLSSocket

https://nodejs.org/api/tls.html#class-tlstlssocket

new tls.TLSSocket(socket\[, options\])

https://nodejs.org/api/tls.html#new-tlstlssocketsocket-options

Event: 'keylog'

https://nodejs.org/api/tls.html#event-keylog-1

Event: 'OCSPResponse'

https://nodejs.org/api/tls.html#event-ocspresponse

Event: 'secure'

https://nodejs.org/api/tls.html#event-secure

Event: 'secureConnect'

https://nodejs.org/api/tls.html#event-secureconnect

Event: 'session'

https://nodejs.org/api/tls.html#event-session

tlsSocket.address()

https://nodejs.org/api/tls.html#tlssocketaddress

tlsSocket.authorizationError

https://nodejs.org/api/tls.html#tlssocketauthorizationerror

tlsSocket.authorized

https://nodejs.org/api/tls.html#tlssocketauthorized

tlsSocket.disableRenegotiation()

https://nodejs.org/api/tls.html#tlssocketdisablerenegotiation

tlsSocket.enableTrace()

https://nodejs.org/api/tls.html#tlssocketenabletrace

tlsSocket.encrypted

https://nodejs.org/api/tls.html#tlssocketencrypted

tlsSocket.exportKeyingMaterial(length, label\[, context\])

https://nodejs.org/api/tls.html#tlssocketexportkeyingmateriallength-label-context

tlsSocket.getCertificate()

https://nodejs.org/api/tls.html#tlssocketgetcertificate

tlsSocket.getCipher()

https://nodejs.org/api/tls.html#tlssocketgetcipher

tlsSocket.getEphemeralKeyInfo()

https://nodejs.org/api/tls.html#tlssocketgetephemeralkeyinfo

tlsSocket.getFinished()

https://nodejs.org/api/tls.html#tlssocketgetfinished

tlsSocket.getPeerCertificate(\[detailed\])

https://nodejs.org/api/tls.html#tlssocketgetpeercertificatedetailed

Certificate object

https://nodejs.org/api/tls.html#certificate-object

tlsSocket.getPeerFinished()

https://nodejs.org/api/tls.html#tlssocketgetpeerfinished

tlsSocket.getPeerX509Certificate()

https://nodejs.org/api/tls.html#tlssocketgetpeerx509certificate

tlsSocket.getProtocol()

https://nodejs.org/api/tls.html#tlssocketgetprotocol

tlsSocket.getSession()

https://nodejs.org/api/tls.html#tlssocketgetsession

tlsSocket.getSharedSigalgs()

https://nodejs.org/api/tls.html#tlssocketgetsharedsigalgs

tlsSocket.getTLSTicket()

https://nodejs.org/api/tls.html#tlssocketgettlsticket

tlsSocket.getX509Certificate()

https://nodejs.org/api/tls.html#tlssocketgetx509certificate

tlsSocket.isSessionReused()

https://nodejs.org/api/tls.html#tlssocketissessionreused

tlsSocket.localAddress

https://nodejs.org/api/tls.html#tlssocketlocaladdress

tlsSocket.localPort

https://nodejs.org/api/tls.html#tlssocketlocalport

tlsSocket.remoteAddress

https://nodejs.org/api/tls.html#tlssocketremoteaddress

tlsSocket.remoteFamily

https://nodejs.org/api/tls.html#tlssocketremotefamily

tlsSocket.remotePort

https://nodejs.org/api/tls.html#tlssocketremoteport

tlsSocket.renegotiate(options, callback)

https://nodejs.org/api/tls.html#tlssocketrenegotiateoptions-callback

tlsSocket.setKeyCert(context)

https://nodejs.org/api/tls.html#tlssocketsetkeycertcontext

tlsSocket.setMaxSendFragment(size)

https://nodejs.org/api/tls.html#tlssocketsetmaxsendfragmentsize

tls.checkServerIdentity(hostname, cert)

https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert

tls.connect(options\[, callback\])

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

tls.connect(path\[, options\]\[, callback\])

https://nodejs.org/api/tls.html#tlsconnectpath-options-callback

tls.connect(port\[, host\]\[, options\]\[, callback\])

https://nodejs.org/api/tls.html#tlsconnectport-host-options-callback

tls.createSecureContext(\[options\])

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

tls.createServer(\[options\]\[, secureConnectionListener\])

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

tls.setDefaultCACertificates(certs)

https://nodejs.org/api/tls.html#tlssetdefaultcacertificatescerts

tls.getCACertificates(\[type\])

https://nodejs.org/api/tls.html#tlsgetcacertificatestype

tls.getCiphers()

https://nodejs.org/api/tls.html#tlsgetciphers

tls.rootCertificates

https://nodejs.org/api/tls.html#tlsrootcertificates

tls.DEFAULT\_ECDH\_CURVE

https://nodejs.org/api/tls.html#tlsdefault\_ecdh\_curve

tls.DEFAULT\_MAX\_VERSION

https://nodejs.org/api/tls.html#tlsdefault\_max\_version

tls.DEFAULT\_MIN\_VERSION

https://nodejs.org/api/tls.html#tlsdefault\_min\_version

tls.DEFAULT\_CIPHERS

https://nodejs.org/api/tls.html#tlsdefault\_ciphers

https://nodejs.org/api/tls.html#tls-ssl

#### Source Code:

https://github.com/nodejs/node/blob/main/lib/tls.js

Stability: 2

https://nodejs.org/api/documentation.html#stability-index

module provides an implementation of the Transport Layer Security (TLS) and Secure Socket Layer (SSL) protocols that is built on top of OpenSSL. The module can be accessed using:

import tls from 'node:tls';
const tls = require('node:tls');
javascriptcopy

Determining if crypto support is unavailable

https://nodejs.org/api/tls.html#determining-if-crypto-support-is-unavailable

It is possible for Node.js to be built without including support for the

node:crypto

module. In such cases, attempting to

require('node:tls')

will result in an error being thrown.

#### When using CommonJS, the error thrown can be caught using try/catch:

let tls;
try {
  tls = require('node:tls');
} catch (err) {
  console.error('tls support is disabled!');
}
cjscopy

When using the lexical ESM

keyword, the error can only be caught if a handler for

process.on('uncaughtException')

is registered

any attempt to load the module is made (using, for instance, a preload module).

When using ESM, if there is a chance that the code may be run on a build of Node.js where crypto support is not enabled, consider using the

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import

function instead of the lexical

let tls;
try {
  tls = await import('node:tls');
} catch (err) {
  console.error('tls support is disabled!');
}
mjscopy

TLS/SSL concepts

https://nodejs.org/api/tls.html#tlsssl-concepts

TLS/SSL is a set of protocols that rely on a public key infrastructure (PKI) to enable secure communication between a client and a server. For most common cases, each server must have a private key.

Private keys can be generated in multiple ways. The example below illustrates use of the OpenSSL command-line interface to generate a 2048-bit RSA private key:

openssl genrsa -out ryans-key.pem 2048
bashcopy

With TLS/SSL, all servers (and some clients) must have a

certificate

. Certificates are

public keys

that correspond to a private key, and that are digitally signed either by a Certificate Authority or by the owner of the private key (such certificates are referred to as "self-signed"). The first step to obtaining a certificate is to create a

Certificate Signing Request

(CSR) file.

The OpenSSL command-line interface can be used to generate a CSR for a private key:

openssl req -new -sha256 -key ryans-key.pem -out ryans-csr.pem
bashcopy

Once the CSR file is generated, it can either be sent to a Certificate Authority for signing or used to generate a self-signed certificate.

Creating a self-signed certificate using the OpenSSL command-line interface is illustrated in the example below:

openssl x509 -req -in ryans-csr.pem -signkey ryans-key.pem -out ryans-cert.pem
bashcopy

Once the certificate is generated, it can be used to generate a

openssl pkcs12 -export -in ryans-cert.pem -inkey ryans-key.pem \
      -certfile ca-cert.pem -out ryans.pfx
bashcopy

: is the signed certificate

: is the associated private key

: is a concatenation of all Certificate Authority (CA) certs into a single file, e.g.

cat ca1-cert.pem ca2-cert.pem > ca-cert.pem

Perfect forward secrecy

https://nodejs.org/api/tls.html#perfect-forward-secrecy

forward secrecy

perfect forward secrecy

describes a feature of key-agreement (i.e., key-exchange) methods. That is, the server and client keys are used to negotiate new temporary keys that are used specifically and only for the current communication session. Practically, this means that even if the server's private key is compromised, communication can only be decrypted by eavesdroppers if the attacker manages to obtain the key-pair specifically generated for the session.

Perfect forward secrecy is achieved by randomly generating a key pair for key-agreement on every TLS/SSL handshake (in contrast to using the same key for all sessions). Methods implementing this technique are called "ephemeral".

Currently two methods are commonly used to achieve perfect forward secrecy (note the character "E" appended to the traditional abbreviations):

https://en.wikipedia.org/wiki/Elliptic\_curve\_Diffie%E2%80%93Hellman

: An ephemeral version of the Elliptic Curve Diffie-Hellman key-agreement protocol.

https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman\_key\_exchange

: An ephemeral version of the Diffie-Hellman key-agreement protocol.

Perfect forward secrecy using ECDHE is enabled by default. The

option can be used when creating a TLS server to customize the list of supported ECDH curves to use. See

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

for more info.

DHE is disabled by default but can be enabled alongside ECDHE by setting the

. Custom DHE parameters are also supported but discouraged in favor of automatically selected, well-known parameters.

Perfect forward secrecy was optional up to TLSv1.2. As of TLSv1.3, (EC)DHE is always used (with the exception of PSK-only connections).

ALPN and SNI

https://nodejs.org/api/tls.html#alpn-and-sni

ALPN (Application-Layer Protocol Negotiation Extension) and SNI (Server Name Indication) are TLS handshake extensions:

ALPN: Allows the use of one TLS server for multiple protocols (HTTP, HTTP/2)

SNI: Allows the use of one TLS server for multiple hostnames with different certificates.

Pre-shared keys

https://nodejs.org/api/tls.html#pre-shared-keys

TLS-PSK support is available as an alternative to normal certificate-based authentication. It uses a pre-shared key instead of certificates to authenticate a TLS connection, providing mutual authentication. TLS-PSK and public key infrastructure are not mutually exclusive. Clients and servers can accommodate both, choosing either of them during the normal cipher negotiation step.

TLS-PSK is only a good choice where means exist to securely share a key with every connecting machine, so it does not replace the public key infrastructure (PKI) for the majority of TLS uses. The TLS-PSK implementation in OpenSSL has seen many security flaws in recent years, mostly because it is used only by a minority of applications. Please consider all alternative solutions before switching to PSK ciphers. Upon generating PSK it is of critical importance to use sufficient entropy as discussed in

https://tools.ietf.org/html/rfc4086

. Deriving a shared secret from a password or other low-entropy sources is not secure.

PSK ciphers are disabled by default, and using TLS-PSK thus requires explicitly specifying a cipher suite with the

option. The list of available ciphers can be retrieved via

openssl ciphers -v 'PSK'

. All TLS 1.3 ciphers are eligible for PSK and can be retrieved via

openssl ciphers -v -s -tls1\_3 -psk

. On the client connection, a custom

checkServerIdentity

should be passed because the default one will fail in the absence of a certificate.

According to the

https://tools.ietf.org/html/rfc4279

, PSK identities up to 128 bytes in length and PSKs up to 64 bytes in length must be supported. As of OpenSSL 1.1.0 maximum identity size is 128 bytes, and maximum PSK length is 256 bytes.

The current implementation doesn't support asynchronous PSK callbacks due to the limitations of the underlying OpenSSL API.

To use TLS-PSK, client and server must specify the

pskCallback

option, a function that returns the PSK to use (which must be compatible with the selected cipher's digest).

#### It will be called first on the client:

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

optional message sent from the server to help the client decide which identity to use during negotiation. Always

if TLS 1.3 is used.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

in the form

{ psk: <Buffer|TypedArray|DataView>, identity: <string> }

#### Then on the server:

<tls.TLSSocket>

https://nodejs.org/api/tls.html#tlstlssocket

the server socket instance, equivalent to

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

identity parameter sent from the client.

https://nodejs.org/api/buffer.html#class-buffer

<TypedArray>

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/TypedArray

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/DataView

the PSK (or

A return value of

stops the negotiation process and sends an

unknown\_psk\_identity

alert message to the other party. If the server wishes to hide the fact that the PSK identity was not known, the callback must provide some random data as

to make the connection fail with

decrypt\_error

before negotiation is finished.

Client-initiated renegotiation attack mitigation

https://nodejs.org/api/tls.html#client-initiated-renegotiation-attack-mitigation

The TLS protocol allows clients to renegotiate certain aspects of the TLS session. Unfortunately, session renegotiation requires a disproportionate amount of server-side resources, making it a potential vector for denial-of-service attacks.

To mitigate the risk, renegotiation is limited to three times every ten minutes. An

event is emitted on the

tls.TLSSocket

https://nodejs.org/api/tls.html#class-tlstlssocket

instance when this threshold is exceeded. The limits are configurable:

tls.CLIENT\_RENEG\_LIMIT

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Specifies the number of renegotiation requests.

tls.CLIENT\_RENEG\_WINDOW

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Specifies the time renegotiation window in seconds.

(10 minutes).

The default renegotiation limits should not be modified without a full understanding of the implications and risks.

TLSv1.3 does not support renegotiation.

Session resumption

https://nodejs.org/api/tls.html#session-resumption

Establishing a TLS session can be relatively slow. The process can be sped up by saving and later reusing the session state. There are several mechanisms to do so, discussed here from oldest to newest (and preferred).

Session identifiers

https://nodejs.org/api/tls.html#session-identifiers

Servers generate a unique ID for new connections and send it to the client. Clients and servers save the session state. When reconnecting, clients send the ID of their saved session state and if the server also has the state for that ID, it can agree to use it. Otherwise, the server will create a new session. See

https://www.ietf.org/rfc/rfc2246.txt

for more information, page 23 and 30.

Resumption using session identifiers is supported by most web browsers when making HTTPS requests.

For Node.js, clients wait for the

https://nodejs.org/api/tls.html#event-session

event to get the session data, and provide the data to the

option of a subsequent

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

to reuse the session. Servers must implement handlers for the

'newSession'

https://nodejs.org/api/tls.html#event-newsession

'resumeSession'

https://nodejs.org/api/tls.html#event-resumesession

events to save and restore the session data using the session ID as the lookup key to reuse sessions. To reuse sessions across load balancers or cluster workers, servers must use a shared session cache (such as Redis) in their session handlers.

Session tickets

https://nodejs.org/api/tls.html#session-tickets

The servers encrypt the entire session state and send it to the client as a "ticket". When reconnecting, the state is sent to the server in the initial connection. This mechanism avoids the need for a server-side session cache. If the server doesn't use the ticket, for any reason (failure to decrypt it, it's too old, etc.), it will create a new session and send a new ticket. See

https://tools.ietf.org/html/rfc5077

for more information.

Resumption using session tickets is becoming commonly supported by many web browsers when making HTTPS requests.

For Node.js, clients use the same APIs for resumption with session identifiers as for resumption with session tickets. For debugging, if

tls.TLSSocket.getTLSTicket()

https://nodejs.org/api/tls.html#tlssocketgettlsticket

returns a value, the session data contains a ticket, otherwise it contains client-side session state.

With TLSv1.3, be aware that multiple tickets may be sent by the server, resulting in multiple

events, see

https://nodejs.org/api/tls.html#event-session

for more information.

Single process servers need no specific implementation to use session tickets. To use session tickets across server restarts or load balancers, servers must all have the same ticket keys. There are three 16-byte keys internally, but the tls API exposes them as a single 48-byte buffer for convenience.

It's possible to get the ticket keys by calling

server.getTicketKeys()

https://nodejs.org/api/tls.html#servergetticketkeys

on one server instance and then distribute them, but it is more reasonable to securely generate 48 bytes of secure random data and set them with the

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

. The keys should be regularly regenerated and server's keys can be reset with

server.setTicketKeys()

https://nodejs.org/api/tls.html#serversetticketkeyskeys

Session ticket keys are cryptographic keys, and they

must be stored securely

. With TLS 1.2 and below, if they are compromised all sessions that used tickets encrypted with them can be decrypted. They should not be stored on disk, and they should be regenerated regularly.

If clients advertise support for tickets, the server will send them. The server can disable tickets by supplying

require('node:constants').SSL\_OP\_NO\_TICKET

secureOptions

Both session identifiers and session tickets timeout, causing the server to create new sessions. The timeout can be configured with the

sessionTimeout

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

For all the mechanisms, when resumption fails, servers will create new sessions. Since failing to resume the session does not cause TLS/HTTPS connection failures, it is easy to not notice unnecessarily poor TLS performance. The OpenSSL CLI can be used to verify that servers are resuming sessions. Use the

openssl s\_client

, for example:

openssl s\_client -connect localhost:443 -reconnect
bashcopy

Read through the debug output. The first connection should say "New", for example:

New, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
textcopy

#### Subsequent connections should say "Reused", for example:

Reused, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
textcopy

Modifying the default TLS cipher suite

https://nodejs.org/api/tls.html#modifying-the-default-tls-cipher-suite

Node.js is built with a default suite of enabled and disabled TLS ciphers. This default cipher list can be configured when building Node.js to allow distributions to provide their own default list.

#### The following command can be used to show the default cipher suite:

node -p crypto.constants.defaultCoreCipherList | tr ':' '\n'
TLS\_AES\_256\_GCM\_SHA384
TLS\_CHACHA20\_POLY1305\_SHA256
TLS\_AES\_128\_GCM\_SHA256
ECDHE-RSA-AES128-GCM-SHA256
ECDHE-ECDSA-AES128-GCM-SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-ECDSA-AES256-GCM-SHA384
DHE-RSA-AES128-GCM-SHA256
ECDHE-RSA-AES128-SHA256
DHE-RSA-AES128-SHA256
ECDHE-RSA-AES256-SHA384
DHE-RSA-AES256-SHA384
ECDHE-RSA-AES256-SHA256
DHE-RSA-AES256-SHA256
HIGH
!aNULL
!eNULL
!EXPORT
!DES
!RC4
!MD5
!PSK
!SRP
!CAMELLIA
consolecopy

#### This default can be replaced entirely using the

--tls-cipher-list

https://nodejs.org/api/cli.html#--tls-cipher-listlist

command-line switch (directly, or via the

NODE\_OPTIONS

https://nodejs.org/api/cli.html#node\_optionsoptions

environment variable). For instance, the following makes

ECDHE-RSA-AES128-GCM-SHA256:!RC4

the default TLS cipher suite:

node --tls-cipher-list='ECDHE-RSA-AES128-GCM-SHA256:!RC4' server.js

export NODE\_OPTIONS=--tls-cipher-list='ECDHE-RSA-AES128-GCM-SHA256:!RC4'
node server.js
bashcopy

To verify, use the following command to show the set cipher list, note the difference between

defaultCoreCipherList

defaultCipherList

node --tls-cipher-list='ECDHE-RSA-AES128-GCM-SHA256:!RC4' -p crypto.constants.defaultCipherList | tr ':' '\n'
ECDHE-RSA-AES128-GCM-SHA256
!RC4
bashcopy

defaultCoreCipherList

list is set at compilation time and the

defaultCipherList

is set at runtime.

To modify the default cipher suites from within the runtime, modify the

tls.DEFAULT\_CIPHERS

variable, this must be performed before listening on any sockets, it will not affect sockets already opened. For example:

// Remove Obsolete CBC Ciphers and RSA Key Exchange based Ciphers as they don't provide Forward Secrecy
tls.DEFAULT\_CIPHERS +=
  ':!ECDHE-RSA-AES128-SHA:!ECDHE-RSA-AES128-SHA256:!ECDHE-RSA-AES256-SHA:!ECDHE-RSA-AES256-SHA384' +
  ':!ECDHE-ECDSA-AES128-SHA:!ECDHE-ECDSA-AES128-SHA256:!ECDHE-ECDSA-AES256-SHA:!ECDHE-ECDSA-AES256-SHA384' +
  ':!kRSA';
jscopy

The default can also be replaced on a per client or server basis using the

option from

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

, which is also available in

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

, and when creating new

tls.TLSSocket

https://nodejs.org/api/tls.html#class-tlstlssocket

The ciphers list can contain a mixture of TLSv1.3 cipher suite names, the ones that start with

, and specifications for TLSv1.2 and below cipher suites. The TLSv1.2 ciphers support a legacy specification format, consult the OpenSSL

cipher list format

https://www.openssl.org/docs/man1.1.1/man1/ciphers.html#CIPHER-LIST-FORMAT

documentation for details, but those specifications do

apply to TLSv1.3 ciphers. The TLSv1.3 suites can only be enabled by including their full name in the cipher list. They cannot, for example, be enabled or disabled by using the legacy TLSv1.2

specification.

Despite the relative order of TLSv1.3 and TLSv1.2 cipher suites, the TLSv1.3 protocol is significantly more secure than TLSv1.2, and will always be chosen over TLSv1.2 if the handshake indicates it is supported, and if any TLSv1.3 cipher suites are enabled.

The default cipher suite included within Node.js has been carefully selected to reflect current security best practices and risk mitigation. Changing the default cipher suite can have a significant impact on the security of an application. The

--tls-cipher-list

option should by used only if absolutely necessary.

The default cipher suite prefers GCM ciphers for

Chrome's 'modern cryptography' setting

https://www.chromium.org/Home/chromium-security/education/tls#TOC-Cipher-Suites

and also prefers ECDHE and DHE ciphers for perfect forward secrecy, while offering

backward compatibility.

Old clients that rely on insecure and deprecated RC4 or DES-based ciphers (like Internet Explorer 6) cannot complete the handshaking process with the default configuration. If these clients

be supported, the

TLS recommendations

https://wiki.mozilla.org/Security/Server\_Side\_TLS

may offer a compatible cipher suite. For more details on the format, see the OpenSSL

cipher list format

https://www.openssl.org/docs/man1.1.1/man1/ciphers.html#CIPHER-LIST-FORMAT

documentation.

#### There are only five TLSv1.3 cipher suites:

'TLS\_AES\_256\_GCM\_SHA384'

'TLS\_CHACHA20\_POLY1305\_SHA256'

'TLS\_AES\_128\_GCM\_SHA256'

'TLS\_AES\_128\_CCM\_SHA256'

'TLS\_AES\_128\_CCM\_8\_SHA256'

The first three are enabled by default. The two

-based suites are supported by TLSv1.3 because they may be more performant on constrained systems, but they are not enabled by default since they offer less security.

OpenSSL security level

https://nodejs.org/api/tls.html#openssl-security-level

The OpenSSL library enforces security levels to control the minimum acceptable level of security for cryptographic operations. OpenSSL's security levels range from 0 to 5, with each level imposing stricter security requirements. The default security level is 2, which is generally suitable for most modern applications. However, some legacy features and protocols, such as TLSv1, require a lower security level (

) to function properly. For more detailed information, please refer to the

OpenSSL documentation on security levels

https://www.openssl.org/docs/manmaster/man3/SSL\_CTX\_set\_security\_level.html#DEFAULT-CALLBACK-BEHAVIOUR

Setting security levels

https://nodejs.org/api/tls.html#setting-security-levels

To adjust the security level in your Node.js application, you can include

@SECLEVEL=X

within a cipher string, where

is the desired security level. For example, to set the security level to 0 while using the default OpenSSL cipher list, you could use:

import { createServer, connect } from 'node:tls';
const port = 443;

createServer({ ciphers: 'DEFAULT@SECLEVEL=0', minVersion: 'TLSv1' }, function(socket) {
  console.log('Client connected with protocol:', socket.getProtocol());
  socket.end();
  this.close();
})
.listen(port, () => {
  connect(port, { ciphers: 'DEFAULT@SECLEVEL=0', maxVersion: 'TLSv1' });
});
const { createServer, connect } = require('node:tls');
const port = 443;

createServer({ ciphers: 'DEFAULT@SECLEVEL=0', minVersion: 'TLSv1' }, function(socket) {
  console.log('Client connected with protocol:', socket.getProtocol());
  socket.end();
  this.close();
})
.listen(port, () => {
  connect(port, { ciphers: 'DEFAULT@SECLEVEL=0', maxVersion: 'TLSv1' });
});
javascriptcopy

This approach sets the security level to 0, allowing the use of legacy features while still leveraging the default OpenSSL ciphers.

--tls-cipher-list

https://nodejs.org/api/cli.html#--tls-cipher-listlist

https://nodejs.org/api/tls.html#-tls-cipher-list

#### You can also set the security level and ciphers from the command line using the

--tls-cipher-list=DEFAULT@SECLEVEL=X

as described in

Modifying the default TLS cipher suite

https://nodejs.org/api/tls.html#modifying-the-default-tls-cipher-suite

. However, it is generally discouraged to use the command line option for setting ciphers and it is preferable to configure the ciphers for individual contexts within your application code, as this approach provides finer control and reduces the risk of globally downgrading the security level.

X509 certificate error codes

https://nodejs.org/api/tls.html#x509-certificate-error-codes

Multiple functions can fail due to certificate errors that are reported by OpenSSL. In such a case, the function provides an

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Error

via its callback that has the property

which can take one of the following values:

'UNABLE\_TO\_GET\_ISSUER\_CERT'

: Unable to get issuer certificate.

'UNABLE\_TO\_GET\_CRL'

: Unable to get certificate CRL.

'UNABLE\_TO\_DECRYPT\_CERT\_SIGNATURE'

: Unable to decrypt certificate's signature.

'UNABLE\_TO\_DECRYPT\_CRL\_SIGNATURE'

: Unable to decrypt CRL's signature.

'UNABLE\_TO\_DECODE\_ISSUER\_PUBLIC\_KEY'

: Unable to decode issuer public key.

'CERT\_SIGNATURE\_FAILURE'

: Certificate signature failure.

'CRL\_SIGNATURE\_FAILURE'

: CRL signature failure.

'CERT\_NOT\_YET\_VALID'

: Certificate is not yet valid.

'CERT\_HAS\_EXPIRED'

: Certificate has expired.

'CRL\_NOT\_YET\_VALID'

: CRL is not yet valid.

'CRL\_HAS\_EXPIRED'

: CRL has expired.

'ERROR\_IN\_CERT\_NOT\_BEFORE\_FIELD'

: Format error in certificate's notBefore field.

'ERROR\_IN\_CERT\_NOT\_AFTER\_FIELD'

: Format error in certificate's notAfter field.

'ERROR\_IN\_CRL\_LAST\_UPDATE\_FIELD'

: Format error in CRL's lastUpdate field.

'ERROR\_IN\_CRL\_NEXT\_UPDATE\_FIELD'

: Format error in CRL's nextUpdate field.

'OUT\_OF\_MEM'

: Out of memory.

'DEPTH\_ZERO\_SELF\_SIGNED\_CERT'

: Self signed certificate.

'SELF\_SIGNED\_CERT\_IN\_CHAIN'

: Self signed certificate in certificate chain.

'UNABLE\_TO\_GET\_ISSUER\_CERT\_LOCALLY'

: Unable to get local issuer certificate.

'UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE'

: Unable to verify the first certificate.

'CERT\_CHAIN\_TOO\_LONG'

: Certificate chain too long.

'CERT\_REVOKED'

: Certificate revoked.

'INVALID\_CA'

: Invalid CA certificate.

'PATH\_LENGTH\_EXCEEDED'

: Path length constraint exceeded.

'INVALID\_PURPOSE'

: Unsupported certificate purpose.

'CERT\_UNTRUSTED'

: Certificate not trusted.

'CERT\_REJECTED'

: Certificate rejected.

'HOSTNAME\_MISMATCH'

: Hostname mismatch.

When certificate errors like

UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE

DEPTH\_ZERO\_SELF\_SIGNED\_CERT

UNABLE\_TO\_GET\_ISSUER\_CERT

occur, Node.js appends a hint suggesting that if the root CA is installed locally, try running with the

--use-system-ca

flag to direct developers towards a secure solution, to prevent unsafe workarounds.

https://nodejs.org/api/tls.html#class-tlsserver

Added in: v0.3.2

<net.Server>

https://nodejs.org/api/net.html#class-netserver

Accepts encrypted connections using TLS or SSL.

'connection'

https://nodejs.org/api/tls.html#event-connection

Added in: v0.3.2

<stream.Duplex>

https://nodejs.org/api/stream.html#class-streamduplex

This event is emitted when a new TCP stream is established, before the TLS handshake begins.

is typically an object of type

https://nodejs.org/api/net.html#class-netsocket

but will not receive events unlike the socket created from the

https://nodejs.org/api/net.html#class-netserver

'connection'

event. Usually users will not want to access this event.

This event can also be explicitly emitted by users to inject connections into the TLS server. In that case, any

https://nodejs.org/api/stream.html#class-streamduplex

stream can be passed.

https://nodejs.org/api/tls.html#event-keylog

Added in: v12.3.0, v10.20.0

https://nodejs.org/api/buffer.html#class-buffer

Line of ASCII text, in NSS

SSLKEYLOGFILE

<tls.TLSSocket>

https://nodejs.org/api/tls.html#tlstlssocket

tls.TLSSocket

instance on which it was generated.

event is emitted when key material is generated or received by a connection to this server (typically before handshake has completed, but not necessarily). This keying material can be stored for debugging, as it allows captured TLS traffic to be decrypted. It may be emitted multiple times for each socket.

A typical use case is to append received lines to a common text file, which is later used by software (such as Wireshark) to decrypt the traffic:

const logFile = fs.createWriteStream('/tmp/ssl-keys.log', { flags: 'a' });
// ...
server.on('keylog', (line, tlsSocket) => {
  if (tlsSocket.remoteAddress !== '...')
    return; // Only log keys for a particular IP
  logFile.write(line);
});
jscopy

'newSession'

https://nodejs.org/api/tls.html#event-newsession

Added in: v0.9.2 History

argument is now supported.

'newSession'

event is emitted upon creation of a new TLS session. This may be used to store sessions in external storage. The data should be provided to the

'resumeSession'

https://nodejs.org/api/tls.html#event-resumesession

#### The listener callback is passed three arguments when called:

https://nodejs.org/api/buffer.html#class-buffer

The TLS session identifier

sessionData

https://nodejs.org/api/buffer.html#class-buffer

The TLS session data

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

A callback function taking no arguments that must be invoked in order for data to be sent or received over the secure connection.

Listening for this event will have an effect only on connections established after the addition of the event listener.

'OCSPRequest'

https://nodejs.org/api/tls.html#event-ocsprequest

Added in: v0.11.13

'OCSPRequest'

event is emitted when the client sends a certificate status request. The listener callback is passed three arguments when called:

certificate

https://nodejs.org/api/buffer.html#class-buffer

The server certificate

https://nodejs.org/api/buffer.html#class-buffer

The issuer's certificate

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

A callback function that must be invoked to provide the results of the OCSP request.

The server's current certificate can be parsed to obtain the OCSP URL and certificate ID; after obtaining an OCSP response,

callback(null, resp)

is then invoked, where

instance containing the OCSP response. Both

certificate

DER-representations of the primary and issuer's certificates. These can be used to obtain the OCSP certificate ID and OCSP endpoint URL.

Alternatively,

callback(null, null)

may be called, indicating that there was no OCSP response.

callback(err)

will result in a

socket.destroy(err)

#### The typical flow of an OCSP request is as follows:

Client connects to the server and sends an

'OCSPRequest'

(via the status info extension in ClientHello).

Server receives the request and emits the

'OCSPRequest'

event, calling the listener if registered.

Server extracts the OCSP URL from either the

certificate

and performs an

OCSP request

https://en.wikipedia.org/wiki/OCSP\_stapling

Server receives

'OCSPResponse'

from the CA and sends it back to the client via the

Client validates the response and either destroys the socket or performs a handshake.

if the certificate is either self-signed or the issuer is not in the root certificates list. (An issuer may be provided via the

option when establishing the TLS connection.)

Listening for this event will have an effect only on connections established after the addition of the event listener.

An npm module like

https://www.npmjs.com/package/asn1.js

may be used to parse the certificates.

'resumeSession'

https://nodejs.org/api/tls.html#event-resumesession

Added in: v0.9.2

'resumeSession'

event is emitted when the client requests to resume a previous TLS session. The listener callback is passed two arguments when called:

https://nodejs.org/api/buffer.html#class-buffer

The TLS session identifier

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

#### A callback function to be called when the prior session has been recovered:

callback(\[err\[, sessionData\]\])

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Error

sessionData

https://nodejs.org/api/buffer.html#class-buffer

The event listener should perform a lookup in external storage for the

sessionData

saved by the

'newSession'

https://nodejs.org/api/tls.html#event-newsession

event handler using the given

. If found, call

callback(null, sessionData)

to resume the session. If not found, the session cannot be resumed.

must be called without

sessionData

so that the handshake can continue and a new session can be created. It is possible to call

callback(err)

to terminate the incoming connection and destroy the socket.

Listening for this event will have an effect only on connections established after the addition of the event listener.

#### The following illustrates resuming a TLS session:

const tlsSessionStore = {};
server.on('newSession', (id, data, cb) => {
  tlsSessionStore\[id.toString('hex')\] = data;
  cb();
});
server.on('resumeSession', (id, cb) => {
  cb(null, tlsSessionStore\[id.toString('hex')\] || null);
});
jscopy

'secureConnection'

https://nodejs.org/api/tls.html#event-secureconnection

Added in: v0.3.2

'secureConnection'

event is emitted after the handshaking process for a new connection has successfully completed. The listener callback is passed a single argument when called:

<tls.TLSSocket>

https://nodejs.org/api/tls.html#tlstlssocket

The established TLS socket.

tlsSocket.authorized

property is a

indicating whether the client has been verified by one of the supplied Certificate Authorities for the server. If

tlsSocket.authorized

socket.authorizationError

is set to describe how authorization failed. Depending on the settings of the TLS server, unauthorized connections may still be accepted.

tlsSocket.alpnProtocol

property is a string that contains the selected ALPN protocol. When ALPN has no selected protocol because the client or the server did not send an ALPN extension,

tlsSocket.alpnProtocol

tlsSocket.servername

property is a string containing the server name requested via SNI.

'tlsClientError'

https://nodejs.org/api/tls.html#event-tlsclienterror

Added in: v6.0.0

'tlsClientError'

event is emitted when an error occurs before a secure connection is established. The listener callback is passed two arguments when called:

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Error

object describing the error

<tls.TLSSocket>

https://nodejs.org/api/tls.html#tlstlssocket

tls.TLSSocket

instance from which the error originated.

server.addContext(hostname, context)

https://nodejs.org/api/tls.html#serveraddcontexthostname-context

Added in: v0.5.3

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

A SNI host name or wildcard (e.g.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

<tls.SecureContext>

https://nodejs.org/api/tls.html#class-tlssecurecontext

An object containing any of the possible properties from the

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

arguments (e.g.

, etc), or a TLS context object created with

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

server.addContext()

method adds a secure context that will be used if the client request's SNI name matches the supplied

(or wildcard).

When there are multiple matching contexts, the most recently added one is used.

server.address()

https://nodejs.org/api/tls.html#serveraddress

Added in: v0.6.0

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

Returns the bound address, the address family name, and port of the server as reported by the operating system. See

net.Server.address()

https://nodejs.org/api/net.html#serveraddress

for more information.

server.close(\[callback\])

https://nodejs.org/api/tls.html#serverclosecallback

Added in: v0.3.2

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

A listener callback that will be registered to listen for the server instance's

<tls.Server>

https://nodejs.org/api/tls.html#class-tlsserver

server.close()

method stops the server from accepting new connections.

This function operates asynchronously. The

event will be emitted when the server has no more open connections.

server.getTicketKeys()

https://nodejs.org/api/tls.html#servergetticketkeys

Added in: v3.0.0

https://nodejs.org/api/buffer.html#class-buffer

A 48-byte buffer containing the session ticket keys.

Returns the session ticket keys.

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

server.listen()

https://nodejs.org/api/tls.html#serverlisten

Starts the server listening for encrypted connections. This method is identical to

server.listen()

https://nodejs.org/api/net.html#serverlisten

https://nodejs.org/api/net.html#class-netserver

server.setSecureContext(options)

https://nodejs.org/api/tls.html#serversetsecurecontextoptions

Added in: v11.0.0

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

An object containing any of the possible properties from the

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

arguments (e.g.

server.setSecureContext()

method replaces the secure context of an existing server. Existing connections to the server are not interrupted.

server.setTicketKeys(keys)

https://nodejs.org/api/tls.html#serversetticketkeyskeys

Added in: v3.0.0

https://nodejs.org/api/buffer.html#class-buffer

<TypedArray>

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/TypedArray

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/DataView

A 48-byte buffer containing the session ticket keys.

Sets the session ticket keys.

Changes to the ticket keys are effective only for future server connections. Existing or currently pending server connections will use the previous keys.

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

tls.TLSSocket

https://nodejs.org/api/tls.html#class-tlstlssocket

Added in: v0.11.4

<net.Socket>

https://nodejs.org/api/net.html#class-netsocket

Performs transparent encryption of written data and all required TLS negotiation.

Instances of

tls.TLSSocket

implement the duplex

https://nodejs.org/api/stream.html#stream

Methods that return TLS connection metadata (e.g.

tls.TLSSocket.getPeerCertificate()

https://nodejs.org/api/tls.html#tlssocketgetpeercertificatedetailed

) will only return data while the connection is open.

new tls.TLSSocket(socket\[, options\])

https://nodejs.org/api/tls.html#new-tlstlssocketsocket-options

Added in: v0.11.4 History

enableTrace

option is now supported.

ALPN options are supported now.

<net.Socket>

https://nodejs.org/api/net.html#class-netsocket

<stream.Duplex>

https://nodejs.org/api/stream.html#class-streamduplex

On the server side, any

stream. On the client side, any instance of

https://nodejs.org/api/net.html#class-netsocket

(for generic

stream support on the client side,

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

must be used).

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

enableTrace

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

: The SSL/TLS protocol is asymmetrical, TLSSockets must know if they are to behave as a server or a client. If

the TLS socket will be instantiated as a server.

<net.Server>

https://nodejs.org/api/net.html#class-netserver

https://nodejs.org/api/net.html#class-netserver

requestCert

: Whether to authenticate the remote peer by requesting a certificate. Clients always request a server certificate. Servers (

is true) may set

requestCert

to true to request a client certificate.

rejectUnauthorized

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

ALPNProtocols

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

SNICallback

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

ALPNCallback

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

https://nodejs.org/api/buffer.html#class-buffer

instance containing a TLS session.

requestOCSP

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

, specifies that the OCSP status request extension will be added to the client hello and an

'OCSPResponse'

event will be emitted on the socket before establishing a secure communication

secureContext

: TLS context object created with

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

secureContext

provided, one will be created by passing the entire

tls.createSecureContext()

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

options that are used if the

secureContext

option is missing. Otherwise, they are ignored.

Construct a new

tls.TLSSocket

object from an existing TCP socket.

https://nodejs.org/api/tls.html#event-keylog-1

Added in: v12.3.0, v10.20.0

https://nodejs.org/api/buffer.html#class-buffer

Line of ASCII text, in NSS

SSLKEYLOGFILE

event is emitted on a

tls.TLSSocket

when key material is generated or received by the socket. This keying material can be stored for debugging, as it allows captured TLS traffic to be decrypted. It may be emitted multiple times, before or after the handshake completes.

A typical use case is to append received lines to a common text file, which is later used by software (such as Wireshark) to decrypt the traffic:

const logFile = fs.createWriteStream('/tmp/ssl-keys.log', { flags: 'a' });
// ...
tlsSocket.on('keylog', (line) => logFile.write(line));
jscopy

'OCSPResponse'

https://nodejs.org/api/tls.html#event-ocspresponse

Added in: v0.11.13

'OCSPResponse'

event is emitted if the

requestOCSP

option was set when the

tls.TLSSocket

was created and an OCSP response has been received. The listener callback is passed a single argument when called:

https://nodejs.org/api/buffer.html#class-buffer

The server's OCSP response

Typically, the

is a digitally signed object from the server's CA that contains information about server's certificate revocation status.

https://nodejs.org/api/tls.html#event-secure

Added in: v0.11.4

event is emitted after the TLS handshake has successfully completed and a secure connection has been established.

This event is emitted on both client and server

<tls.TLSSocket>

https://nodejs.org/api/tls.html#tlstlssocket

instances, including sockets created using the

new tls.TLSSocket()

constructor.

'secureConnect'

https://nodejs.org/api/tls.html#event-secureconnect

Added in: v0.11.4

'secureConnect'

event is emitted after the handshaking process for a new connection has successfully completed. The listener callback will be called regardless of whether or not the server's certificate has been authorized. It is the client's responsibility to check the

tlsSocket.authorized

property to determine if the server certificate was signed by one of the specified CAs. If

tlsSocket.authorized === false

, then the error can be found by examining the

tlsSocket.authorizationError

property. If ALPN was used, the

tlsSocket.alpnProtocol

property can be checked to determine the negotiated protocol.

'secureConnect'

event is not emitted when a

<tls.TLSSocket>

https://nodejs.org/api/tls.html#tlstlssocket

is created using the

new tls.TLSSocket()

constructor.

https://nodejs.org/api/tls.html#event-session

Added in: v11.10.0

https://nodejs.org/api/buffer.html#class-buffer

event is emitted on a client

tls.TLSSocket

when a new session or TLS ticket is available. This may or may not be before the handshake is complete, depending on the TLS protocol version that was negotiated. The event is not emitted on the server, or if a new session was not created, for example, when the connection was resumed. For some TLS protocol versions the event may be emitted multiple times, in which case all the sessions can be used for resumption.

On the client, the

can be provided to the

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

to resume the connection.

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

For TLSv1.2 and below,

tls.TLSSocket.getSession()

https://nodejs.org/api/tls.html#tlssocketgetsession

can be called once the handshake is complete. For TLSv1.3, only ticket-based resumption is allowed by the protocol, multiple tickets are sent, and the tickets aren't sent until after the handshake completes. So it is necessary to wait for the

event to get a resumable session. Applications should use the

event instead of

getSession()

to ensure they will work for all TLS versions. Applications that only expect to get or use one session should listen for this event only once:

tlsSocket.once('session', (session) => {
  // The session can be used immediately or later.
  tls.connect({
    session: session,
    // Other connect options...
  });
});
jscopy

tlsSocket.address()

https://nodejs.org/api/tls.html#tlssocketaddress

Added in: v0.11.4 History

property now returns a string instead of a number.

property now returns a number instead of a string.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

Returns the bound

, the address

of the underlying socket as reported by the operating system:

{ port: 12346, family: 'IPv4', address: '127.0.0.1' }

tlsSocket.authorizationError

https://nodejs.org/api/tls.html#tlssocketauthorizationerror

Added in: v0.11.4

Returns the reason why the peer's certificate was not been verified. This property is set only when

tlsSocket.authorized === false

tlsSocket.authorized

https://nodejs.org/api/tls.html#tlssocketauthorized

Added in: v0.11.4

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

This property is

if the peer certificate was signed by one of the CAs specified when creating the

tls.TLSSocket

instance, otherwise

tlsSocket.disableRenegotiation()

https://nodejs.org/api/tls.html#tlssocketdisablerenegotiation

Added in: v8.4.0

Disables TLS renegotiation for this

instance. Once called, attempts to renegotiate will trigger an

event on the

tlsSocket.enableTrace()

https://nodejs.org/api/tls.html#tlssocketenabletrace

Added in: v12.2.0

When enabled, TLS packet trace information is written to

. This can be used to debug TLS connection problems.

The format of the output is identical to the output of

openssl s\_client -trace

openssl s\_server -trace

. While it is produced by OpenSSL's

SSL\_trace()

function, the format is undocumented, can change without notice, and should not be relied on.

tlsSocket.encrypted

https://nodejs.org/api/tls.html#tlssocketencrypted

Added in: v0.11.4

Always returns

. This may be used to distinguish TLS sockets from regular

tlsSocket.exportKeyingMaterial(length, label\[, context\])

https://nodejs.org/api/tls.html#tlssocketexportkeyingmateriallength-label-context

Added in: v13.10.0, v12.17.0

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

number of bytes to retrieve from keying material

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

an application specific label, typically this will be a value from the

IANA Exporter Label Registry

https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#exporter-labels

https://nodejs.org/api/buffer.html#class-buffer

Optionally provide a context.

https://nodejs.org/api/buffer.html#class-buffer

requested bytes of the keying material

Keying material is used for validations to prevent different kind of attacks in network protocols, for example in the specifications of IEEE 802.1X.

const keyingMaterial = tlsSocket.exportKeyingMaterial(
  128,
  'client finished');

/\*
 Example return value of keyingMaterial:
 <Buffer 76 26 af 99 c5 56 8e 42 09 91 ef 9f 93 cb ad 6c 7b 65 f8 53 f1 d8 d9
    12 5a 33 b8 b5 25 df 7b 37 9f e0 e2 4f b8 67 83 a3 2f cd 5d 41 42 4c 91
    74 ef 2c ... 78 more bytes>
\*/
jscopy

See the OpenSSL

SSL\_export\_keying\_material

https://www.openssl.org/docs/man1.1.1/man3/SSL\_export\_keying\_material.html

documentation for more information.

tlsSocket.getCertificate()

https://nodejs.org/api/tls.html#tlssocketgetcertificate

Added in: v11.2.0

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

Returns an object representing the local certificate. The returned object has some properties corresponding to the fields of the certificate.

tls.TLSSocket.getPeerCertificate()

https://nodejs.org/api/tls.html#tlssocketgetpeercertificatedetailed

for an example of the certificate structure.

If there is no local certificate, an empty object will be returned. If the socket has been destroyed,

will be returned.

tlsSocket.getCipher()

https://nodejs.org/api/tls.html#tlssocketgetcipher

Added in: v0.11.4 History

v13.4.0, v12.16.0

Return the IETF cipher name as

standardName

Return the minimum cipher version, instead of a fixed string (

'TLSv1/SSLv3'

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

OpenSSL name for the cipher suite.

standardName

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

IETF name for the cipher suite.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The minimum TLS protocol version supported by this cipher suite. For the actual negotiated protocol, see

tls.TLSSocket.getProtocol()

https://nodejs.org/api/tls.html#tlssocketgetprotocol

Returns an object containing information on the negotiated cipher suite.

#### For example, a TLSv1.2 protocol with AES256-SHA cipher:

{
    "name": "AES256-SHA",
    "standardName": "TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA",
    "version": "SSLv3"
}
jsoncopy

SSL\_CIPHER\_get\_name

https://www.openssl.org/docs/man1.1.1/man3/SSL\_CIPHER\_get\_name.html

for more information.

tlsSocket.getEphemeralKeyInfo()

https://nodejs.org/api/tls.html#tlssocketgetephemeralkeyinfo

Added in: v5.0.0

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

Returns an object representing the type, name, and size of parameter of an ephemeral key exchange in

perfect forward secrecy

https://nodejs.org/api/tls.html#perfect-forward-secrecy

on a client connection. It returns an empty object when the key exchange is not ephemeral. As this is only supported on a client socket;

is returned if called on a server socket. The supported types are

property is available only when type is

#### For example:

{ type: 'ECDH', name: 'prime256v1', size: 256 }

tlsSocket.getFinished()

https://nodejs.org/api/tls.html#tlssocketgetfinished

Added in: v9.9.0

https://nodejs.org/api/buffer.html#class-buffer

<undefined>

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#undefined\_type

message that has been sent to the socket as part of a SSL/TLS handshake, or

message has been sent yet.

messages are message digests of the complete handshake (with a total of 192 bits for TLS 1.0 and more for SSL 3.0), they can be used for external authentication procedures when the authentication provided by SSL/TLS is not desired or is not enough.

Corresponds to the

SSL\_get\_finished

routine in OpenSSL and may be used to implement the

channel binding from

https://tools.ietf.org/html/rfc5929

tlsSocket.getPeerCertificate(\[detailed\])

https://nodejs.org/api/tls.html#tlssocketgetpeercertificatedetailed

Added in: v0.11.4

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

Include the full certificate chain if

, otherwise include just the peer's certificate.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

A certificate object.

Returns an object representing the peer's certificate. If the peer does not provide a certificate, an empty object will be returned. If the socket has been destroyed,

will be returned.

If the full certificate chain was requested, each certificate will include an

issuerCertificate

property containing an object representing its issuer's certificate.

Certificate object

https://nodejs.org/api/tls.html#certificate-object

v19.1.0, v18.13.0

Add "ca" property.

v17.2.0, v16.14.0

Add fingerprint512.

Support Elliptic Curve public key info.

A certificate object has properties corresponding to the fields of the certificate.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

if a Certificate Authority (CA),

https://nodejs.org/api/buffer.html#class-buffer

The DER encoded X.509 certificate data.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

The certificate subject, described in terms of Country (

), StateOrProvince (

), Locality (

), Organization (

), OrganizationalUnit (

), and CommonName (

). The CommonName is typically a DNS name with TLS certificates. Example:

{C: 'UK', ST: 'BC', L: 'Metro', O: 'Node Fans', OU: 'Docs', CN: 'example.com'}

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

The certificate issuer, described in the same terms as the

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The date-time the certificate is valid from.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The date-time the certificate is valid to.

serialNumber

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

#### The certificate serial number, as a hex string. Example:

'B9B0D332A1AA5635'

fingerprint

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The SHA-1 digest of the DER encoded certificate. It is returned as a

separated hexadecimal string. Example:

'2A:7A:C2:DD:...'

fingerprint256

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The SHA-256 digest of the DER encoded certificate. It is returned as a

separated hexadecimal string. Example:

'2A:7A:C2:DD:...'

fingerprint512

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The SHA-512 digest of the DER encoded certificate. It is returned as a

separated hexadecimal string. Example:

'2A:7A:C2:DD:...'

ext\_key\_usage

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Array

(Optional) The extended key usage, a set of OIDs.

subjectaltname

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

(Optional) A string containing concatenated names for the subject, an alternative to the

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Array

(Optional) An array describing the AuthorityInfoAccess, used with OCSP.

issuerCertificate

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

(Optional) The issuer certificate object. For self-signed certificates, this may be a circular reference.

The certificate may contain information about the public key, depending on the key type.

#### For RSA keys, the following properties may be defined:

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

#### The RSA bit size. Example:

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

#### The RSA exponent, as a string in hexadecimal number notation. Example:

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

#### The RSA modulus, as a hexadecimal string. Example:

'B56CE45CB7...'

https://nodejs.org/api/buffer.html#class-buffer

The public key.

#### For EC keys, the following properties may be defined:

https://nodejs.org/api/buffer.html#class-buffer

The public key.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

#### The key size in bits. Example:

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

(Optional) The ASN.1 name of the OID of the elliptic curve. Well-known curves are identified by an OID. While it is unusual, it is possible that the curve is identified by its mathematical properties, in which case it will not have an OID. Example:

'prime256v1'

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

(Optional) The NIST name for the elliptic curve, if it has one (not all well-known curves have been assigned names by NIST). Example:

#### Example certificate:

{ subject:
   { OU: \[ 'Domain Control Validated', 'PositiveSSL Wildcard' \],
     CN: '\*.nodejs.org' },
  issuer:
   { C: 'GB',
     ST: 'Greater Manchester',
     L: 'Salford',
     O: 'COMODO CA Limited',
     CN: 'COMODO RSA Domain Validation Secure Server CA' },
  subjectaltname: 'DNS:\*.nodejs.org, DNS:nodejs.org',
  infoAccess:
   { 'CA Issuers - URI':
      \[ 'http://crt.comodoca.com/COMODORSADomainValidationSecureServerCA.crt' \],
     'OCSP - URI': \[ 'http://ocsp.comodoca.com' \] },
  modulus: 'B56CE45CB740B09A13F64AC543B712FF9EE8E4C284B542A1708A27E82A8D151CA178153E12E6DDA15BF70FFD96CB8A88618641BDFCCA03527E665B70D779C8A349A6F88FD4EF6557180BD4C98192872BCFE3AF56E863C09DDD8BC1EC58DF9D94F914F0369102B2870BECFA1348A0838C9C49BD1C20124B442477572347047506B1FCD658A80D0C44BCC16BC5C5496CFE6E4A8428EF654CD3D8972BF6E5BFAD59C93006830B5EB1056BBB38B53D1464FA6E02BFDF2FF66CD949486F0775EC43034EC2602AEFBF1703AD221DAA2A88353C3B6A688EFE8387811F645CEED7B3FE46E1F8B9F59FAD028F349B9BC14211D5830994D055EEA3D547911E07A0ADDEB8A82B9188E58720D95CD478EEC9AF1F17BE8141BE80906F1A339445A7EB5B285F68039B0F294598A7D1C0005FC22B5271B0752F58CCDEF8C8FD856FB7AE21C80B8A2CE983AE94046E53EDE4CB89F42502D31B5360771C01C80155918637490550E3F555E2EE75CC8C636DDE3633CFEDD62E91BF0F7688273694EEEBA20C2FC9F14A2A435517BC1D7373922463409AB603295CEB0BB53787A334C9CA3CA8B30005C5A62FC0715083462E00719A8FA3ED0A9828C3871360A73F8B04A4FC1E71302844E9BB9940B77E745C9D91F226D71AFCAD4B113AAF68D92B24DDB4A2136B55A1CD1ADF39605B63CB639038ED0F4C987689866743A68769CC55847E4A06D6E2E3F1',
  exponent: '0x10001',
  pubkey: <Buffer ... >,
  valid\_from: 'Aug 14 00:00:00 2017 GMT',
  valid\_to: 'Nov 20 23:59:59 2019 GMT',
  fingerprint: '01:02:59:D9:C3:D2:0D:08:F7:82:4E:44:A4:B4:53:C5:E2:3A:87:4D',
  fingerprint256: '69:AE:1A:6A:D4:3D:C6:C1:1B:EA:C6:23:DE:BA:2A:14:62:62:93:5C:7A:EA:06:41:9B:0B:BC:87:CE:48:4E:02',
  fingerprint512: '19:2B:3E:C3:B3:5B:32:E8:AE:BB:78:97:27:E4:BA:6C:39:C9:92:79:4F:31:46:39:E2:70:E5:5F:89:42:17:C9:E8:64:CA:FF:BB:72:56:73:6E:28:8A:92:7E:A3:2A:15:8B:C2:E0:45:CA:C3:BC:EA:40:52:EC:CA:A2:68:CB:32',
  ext\_key\_usage: \[ '1.3.6.1.5.5.7.3.1', '1.3.6.1.5.5.7.3.2' \],
  serialNumber: '66593D57F20CBC573E433381B5FEC280',
  raw: <Buffer ... > }
jscopy

tlsSocket.getPeerFinished()

https://nodejs.org/api/tls.html#tlssocketgetpeerfinished

Added in: v9.9.0

https://nodejs.org/api/buffer.html#class-buffer

<undefined>

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#undefined\_type

message that is expected or has actually been received from the socket as part of a SSL/TLS handshake, or

if there is no

message so far.

messages are message digests of the complete handshake (with a total of 192 bits for TLS 1.0 and more for SSL 3.0), they can be used for external authentication procedures when the authentication provided by SSL/TLS is not desired or is not enough.

Corresponds to the

SSL\_get\_peer\_finished

routine in OpenSSL and may be used to implement the

channel binding from

https://tools.ietf.org/html/rfc5929

tlsSocket.getPeerX509Certificate()

https://nodejs.org/api/tls.html#tlssocketgetpeerx509certificate

Added in: v15.9.0

<X509Certificate>

https://nodejs.org/api/crypto.html#class-x509certificate

Returns the peer certificate as an

<X509Certificate>

https://nodejs.org/api/crypto.html#class-x509certificate

If there is no peer certificate, or the socket has been destroyed,

will be returned.

tlsSocket.getProtocol()

https://nodejs.org/api/tls.html#tlssocketgetprotocol

Added in: v5.7.0

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#null\_type

Returns a string containing the negotiated SSL/TLS protocol version of the current connection. The value

will be returned for connected sockets that have not completed the handshaking process. The value

will be returned for server sockets or disconnected client sockets.

#### Protocol versions are:

See the OpenSSL

SSL\_get\_version

https://www.openssl.org/docs/man1.1.1/man3/SSL\_get\_version.html

documentation for more information.

tlsSocket.getSession()

https://nodejs.org/api/tls.html#tlssocketgetsession

Added in: v0.11.4

https://nodejs.org/api/buffer.html#class-buffer

Returns the TLS session data or

if no session was negotiated. On the client, the data can be provided to the

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

to resume the connection. On the server, it may be useful for debugging.

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

getSession()

works only for TLSv1.2 and below. For TLSv1.3, applications must use the

https://nodejs.org/api/tls.html#event-session

event (it also works for TLSv1.2 and below).

tlsSocket.getSharedSigalgs()

https://nodejs.org/api/tls.html#tlssocketgetsharedsigalgs

Added in: v12.11.0

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Array

List of signature algorithms shared between the server and the client in the order of decreasing preference.

SSL\_get\_shared\_sigalgs

https://www.openssl.org/docs/man1.1.1/man3/SSL\_get\_shared\_sigalgs.html

for more information.

tlsSocket.getTLSTicket()

https://nodejs.org/api/tls.html#tlssocketgettlsticket

Added in: v0.11.4

https://nodejs.org/api/buffer.html#class-buffer

For a client, returns the TLS session ticket if one is available, or

. For a server, always returns

It may be useful for debugging.

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

tlsSocket.getX509Certificate()

https://nodejs.org/api/tls.html#tlssocketgetx509certificate

Added in: v15.9.0

<X509Certificate>

https://nodejs.org/api/crypto.html#class-x509certificate

Returns the local certificate as an

<X509Certificate>

https://nodejs.org/api/crypto.html#class-x509certificate

If there is no local certificate, or the socket has been destroyed,

will be returned.

tlsSocket.isSessionReused()

https://nodejs.org/api/tls.html#tlssocketissessionreused

Added in: v0.5.6

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

if the session was reused,

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

tlsSocket.localAddress

https://nodejs.org/api/tls.html#tlssocketlocaladdress

Added in: v0.11.4

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Returns the string representation of the local IP address.

tlsSocket.localPort

https://nodejs.org/api/tls.html#tlssocketlocalport

Added in: v0.11.4

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Returns the numeric representation of the local port.

tlsSocket.remoteAddress

https://nodejs.org/api/tls.html#tlssocketremoteaddress

Added in: v0.11.4

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Returns the string representation of the remote IP address. For example,

'74.125.127.100'

'2001:4860:a005::68'

tlsSocket.remoteFamily

https://nodejs.org/api/tls.html#tlssocketremotefamily

Added in: v0.11.4

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Returns the string representation of the remote IP family.

tlsSocket.remotePort

https://nodejs.org/api/tls.html#tlssocketremoteport

Added in: v0.11.4

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Returns the numeric representation of the remote port. For example,

tlsSocket.renegotiate(options, callback)

https://nodejs.org/api/tls.html#tlssocketrenegotiateoptions-callback

Added in: v0.11.8 History

Passing an invalid callback to the

argument now throws

ERR\_INVALID\_ARG\_TYPE

ERR\_INVALID\_CALLBACK

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

rejectUnauthorized

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

, the server certificate is verified against the list of supplied CAs. An

event is emitted if verification fails;

contains the OpenSSL error code.

requestCert

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

renegotiate()

, callback is attached once to the

https://nodejs.org/api/tls.html#event-secure

renegotiate()

will be called in the next tick with an error, unless the

has been destroyed, in which case

will not be called at all.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

if renegotiation was initiated,

tlsSocket.renegotiate()

method initiates a TLS renegotiation process. Upon completion, the

function will be passed a single argument that is either an

(if the request failed) or

This method can be used to request a peer's certificate after the secure connection has been established.

When running as the server, the socket will be destroyed with an error after

handshakeTimeout

For TLSv1.3, renegotiation cannot be initiated, it is not supported by the protocol.

tlsSocket.setKeyCert(context)

https://nodejs.org/api/tls.html#tlssocketsetkeycertcontext

Added in: v22.5.0, v20.17.0

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

<tls.SecureContext>

https://nodejs.org/api/tls.html#class-tlssecurecontext

An object containing at least

properties from the

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

, or a TLS context object created with

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

tlsSocket.setKeyCert()

method sets the private key and certificate to use for the socket. This is mainly useful if you wish to select a server certificate from a TLS server's

ALPNCallback

tlsSocket.setMaxSendFragment(size)

https://nodejs.org/api/tls.html#tlssocketsetmaxsendfragmentsize

Added in: v0.11.11

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

The maximum TLS fragment size. The maximum value is

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

tlsSocket.setMaxSendFragment()

method sets the maximum TLS fragment size. Returns

if setting the limit succeeded;

Smaller fragment sizes decrease the buffering latency on the client: larger fragments are buffered by the TLS layer until the entire fragment is received and its integrity is verified; large fragments can span multiple roundtrips and their processing can be delayed due to packet loss or reordering. However, smaller fragments add extra TLS framing bytes and CPU overhead, which may decrease overall server throughput.

tls.checkServerIdentity(hostname, cert)

https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert

Added in: v0.8.4 History

v17.3.1, v16.13.2, v14.18.3, v12.22.9

Support for

uniformResourceIdentifier

subject alternative names has been disabled in response to CVE-2021-44531.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The host name or IP address to verify the certificate against.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

certificate object

https://nodejs.org/api/tls.html#certificate-object

representing the peer's certificate.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Error

<undefined>

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#undefined\_type

Verifies the certificate

is issued to

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Error

object, populating it with

on failure. On success, returns

<undefined>

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#undefined\_type

This function is intended to be used in combination with the

checkServerIdentity

option that can be passed to

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

and as such operates on a

certificate object

https://nodejs.org/api/tls.html#certificate-object

. For other purposes, consider using

x509.checkHost()

https://nodejs.org/api/crypto.html#x509checkhostname-options

This function can be overwritten by providing an alternative function as the

options.checkServerIdentity

option that is passed to

tls.connect()

. The overwriting function can call

tls.checkServerIdentity()

of course, to augment the checks done with additional verification.

This function is only called if the certificate passed all other checks, such as being issued by trusted CA (

Earlier versions of Node.js incorrectly accepted certificates for a given

if a matching

uniformResourceIdentifier

subject alternative name was present (see

CVE-2021-44531

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44531

). Applications that wish to accept

uniformResourceIdentifier

subject alternative names can use a custom

options.checkServerIdentity

function that implements the desired behavior.

tls.connect(options\[, callback\])

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

Added in: v0.11.3 History

v15.1.0, v14.18.0

v14.1.0, v13.14.0

highWaterMark

option is accepted now.

v13.6.0, v12.16.0

pskCallback

option is now supported.

Support the

allowHalfOpen

option is now supported.

enableTrace

option is now supported.

v11.8.0, v10.16.0

option is supported now.

option is supported now.

ALPNProtocols

option can be a

v5.3.0, v4.7.0

secureContext

option is supported now.

ALPN options are supported now.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

enableTrace

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Host the client should connect to.

'localhost'

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Port the client should connect to.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Creates Unix socket connection to path. If this option is specified,

are ignored.

<stream.Duplex>

https://nodejs.org/api/stream.html#class-streamduplex

Establish secure connection on a given socket rather than creating a new socket. Typically, this is an instance of

https://nodejs.org/api/net.html#class-netsocket

stream is allowed. If this option is specified,

are ignored, except for certificate validation. Usually, a socket is already connected when passed to

tls.connect()

, but it can be connected later. Connection/disconnection/destruction of

is the user's responsibility; calling

tls.connect()

will not cause

net.connect()

to be called.

allowHalfOpen

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

, then the socket will automatically end the writable side when the readable side ends. If the

option is set, this option has no effect. See the

allowHalfOpen

https://nodejs.org/api/net.html#class-netsocket

for details.

rejectUnauthorized

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

, the server certificate is verified against the list of supplied CAs. An

event is emitted if verification fails;

contains the OpenSSL error code.

pskCallback

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

For TLS-PSK negotiation, see

Pre-shared keys

https://nodejs.org/api/tls.html#pre-shared-keys

ALPNProtocols

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://nodejs.org/api/buffer.html#class-buffer

<TypedArray>

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/TypedArray

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/DataView

An array of strings, or a single

containing the supported ALPN protocols. Buffers should have the format

\[len\]\[name\]\[len\]\[name\]...

'\x08http/1.1\x08http/1.0'

, where the

byte is the length of the next protocol name. Passing an array is usually much simpler, e.g.

\['http/1.1', 'http/1.0'\]

. Protocols earlier in the list have higher preference than those later.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Server name for the SNI (Server Name Indication) TLS extension. It is the name of the host being connected to, and must be a host name, and not an IP address. It can be used by a multi-homed server to choose the correct certificate to present to the client, see the

SNICallback

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

checkServerIdentity(servername, cert)

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

A callback function to be used (instead of the builtin

tls.checkServerIdentity()

function) when checking the server's host name (or the provided

when explicitly set) against the certificate. This should return an

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Error

if verification fails. The method should return

are verified.

https://nodejs.org/api/buffer.html#class-buffer

instance, containing TLS session.

requestOCSP

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

, specifies that the OCSP status request extension will be added to the client hello and an

'OCSPResponse'

event will be emitted on the socket before establishing a secure communication.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Minimum size of the DH parameter in bits to accept a TLS connection. When a server offers a DH parameter with a size less than

, the TLS connection is destroyed and an error is thrown.

highWaterMark

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Consistent with the readable stream

highWaterMark

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

If set and if a socket is created internally, will call

socket.setTimeout(timeout)

https://nodejs.org/api/net.html#socketsettimeouttimeout-callback

after the socket is created, but before it starts the connection.

secureContext

: TLS context object created with

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

secureContext

provided, one will be created by passing the entire

tls.createSecureContext()

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

option is missing, incoming data is stored in a single

and passed to the supplied

when data arrives on the socket, otherwise the option is ignored. See the

https://nodejs.org/api/net.html#class-netsocket

for details.

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

options that are used if the

secureContext

option is missing, otherwise they are ignored.

socket.connect()

https://nodejs.org/api/net.html#socketconnectoptions-connectlistener

option not already listed.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

<tls.TLSSocket>

https://nodejs.org/api/tls.html#tlstlssocket

function, if specified, will be added as a listener for the

'secureConnect'

https://nodejs.org/api/tls.html#event-secureconnect

tls.connect()

tls.TLSSocket

https://nodejs.org/api/tls.html#class-tlstlssocket

tls.connect()

does not enable the SNI (Server Name Indication) extension by default, which may cause some servers to return an incorrect certificate or reject the connection altogether. To enable SNI, set the

option in addition to

The following illustrates a client for the echo server example from

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

// Assumes an echo server that is listening on port 8000.
import { connect } from 'node:tls';
import { readFileSync } from 'node:fs';
import { stdin } from 'node:process';

const options = {
  // Necessary only if the server requires client certificate authentication.
  key: readFileSync('client-key.pem'),
  cert: readFileSync('client-cert.pem'),

  // Necessary only if the server uses a self-signed certificate.
  ca: \[ readFileSync('server-cert.pem') \],

  // Necessary only if the server's cert isn't for "localhost".
  checkServerIdentity: () => { return null; },
};

const socket = connect(8000, options, () => {
  console.log('client connected',
              socket.authorized ? 'authorized' : 'unauthorized');
  stdin.pipe(socket);
  stdin.resume();
});
socket.setEncoding('utf8');
socket.on('data', (data) => {
  console.log(data);
});
socket.on('end', () => {
  console.log('server ends connection');
});
// Assumes an echo server that is listening on port 8000.
const { connect } = require('node:tls');
const { readFileSync } = require('node:fs');

const options = {
  // Necessary only if the server requires client certificate authentication.
  key: readFileSync('client-key.pem'),
  cert: readFileSync('client-cert.pem'),

  // Necessary only if the server uses a self-signed certificate.
  ca: \[ readFileSync('server-cert.pem') \],

  // Necessary only if the server's cert isn't for "localhost".
  checkServerIdentity: () => { return null; },
};

const socket = connect(8000, options, () => {
  console.log('client connected',
              socket.authorized ? 'authorized' : 'unauthorized');
  process.stdin.pipe(socket);
  process.stdin.resume();
});
socket.setEncoding('utf8');
socket.on('data', (data) => {
  console.log(data);
});
socket.on('end', () => {
  console.log('server ends connection');
});
javascriptcopy

#### To generate the certificate and key for this example, run:

openssl req -x509 -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' \
  -keyout client-key.pem -out client-cert.pem
bashcopy

Then, to generate the

server-cert.pem

certificate for this example, run:

openssl pkcs12 -certpbe AES-256-CBC -export -out server-cert.pem \
  -inkey client-key.pem -in client-cert.pem
bashcopy

tls.connect(path\[, options\]\[, callback\])

https://nodejs.org/api/tls.html#tlsconnectpath-options-callback

Added in: v0.11.3

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Default value for

options.path

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

<tls.TLSSocket>

https://nodejs.org/api/tls.html#tlstlssocket

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

except that

can be provided as an argument instead of an option.

A path option, if specified, will take precedence over the path argument.

tls.connect(port\[, host\]\[, options\]\[, callback\])

https://nodejs.org/api/tls.html#tlsconnectport-host-options-callback

Added in: v0.11.3

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Default value for

options.port

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Default value for

options.host

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

<tls.TLSSocket>

https://nodejs.org/api/tls.html#tlstlssocket

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

except that

can be provided as arguments instead of options.

A port or host option, if specified, will take precedence over any port or host argument.

tls.createSecureContext(\[options\])

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

Added in: v0.11.13 History

v22.9.0, v20.18.0

allowPartialTrustChain

option has been added.

v22.4.0, v20.16.0

clientCertEngine

privateKeyEngine

privateKeyIdentifier

options depend on custom engine support in OpenSSL which is deprecated in OpenSSL 3.

v19.8.0, v18.16.0

option can now be set to

to enable DHE with appropriate well-known parameters.

privateKeyIdentifier

privateKeyEngine

options to get private key from an OpenSSL engine.

option to override supported signature algorithms.

TLSv1.3 support added.

option now supports

BEGIN TRUSTED CERTIFICATE

v11.4.0, v10.16.0

can be used to restrict the allowed TLS protocol versions.

cannot be set to

anymore due to a change in OpenSSL.

parameter can now include

clientCertEngine

option can now be multiple

separated curve names or

option is an array, individual entries do not need a

property anymore.

entries can also just be

option can now be a single string containing multiple CA certificates.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

allowPartialTrustChain

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

Treat intermediate (non-self-signed) certificates in the trust CA certificate list as trusted.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://nodejs.org/api/buffer.html#class-buffer

https://nodejs.org/api/buffer.html#class-buffer

Optionally override the trusted CA certificates. If not specified, the CA certificates trusted by default are the same as the ones returned by

tls.getCACertificates()

https://nodejs.org/api/tls.html#tlsgetcacertificatestype

type. If specified, the default list would be completely replaced (instead of being concatenated) by the certificates in the

option. Users need to concatenate manually if they wish to add additional certificates instead of completely overriding the default. The value can be a string or

of strings and/or

s. Any string or

can contain multiple PEM CAs concatenated together. The peer's certificate must be chainable to a CA trusted by the server for the connection to be authenticated. When using certificates that are not chainable to a well-known CA, the certificate's CA must be explicitly specified as a trusted or the connection will fail to authenticate. If the peer uses a certificate that doesn't match or chain to one of the default CAs, use the

option to provide a CA certificate that the peer's certificate can match or chain to. For self-signed certificates, the certificate is its own CA, and must be provided. For PEM encoded certificates, supported types are "TRUSTED CERTIFICATE", "X509 CERTIFICATE", and "CERTIFICATE".

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://nodejs.org/api/buffer.html#class-buffer

https://nodejs.org/api/buffer.html#class-buffer

Cert chains in PEM format. One cert chain should be provided per private key. Each cert chain should consist of the PEM formatted certificate for a provided private

, followed by the PEM formatted intermediate certificates (if any), in order, and not including the root CA (the root CA must be pre-known to the peer, see

). When providing multiple cert chains, they do not have to be in the same order as their private keys in

. If the intermediate certificates are not provided, the peer will not be able to validate the certificate, and the handshake will fail.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Colon-separated list of supported signature algorithms. The list can contain digest algorithms (

etc.), public key algorithms (

etc.), combination of both (e.g 'RSA+SHA384') or TLS v1.3 scheme names (e.g.

rsa\_pss\_pss\_sha512

OpenSSL man pages

https://www.openssl.org/docs/man1.1.1/man3/SSL\_CTX\_set1\_sigalgs\_list.html

for more info.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Cipher suite specification, replacing the default. For more information, see

Modifying the default TLS cipher suite

https://nodejs.org/api/tls.html#modifying-the-default-tls-cipher-suite

. Permitted ciphers can be obtained via

tls.getCiphers()

https://nodejs.org/api/tls.html#tlsgetciphers

. Cipher names must be uppercased in order for OpenSSL to accept them.

clientCertEngine

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Name of an OpenSSL engine which can provide the client certificate.

Deprecated.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://nodejs.org/api/buffer.html#class-buffer

https://nodejs.org/api/buffer.html#class-buffer

PEM formatted CRLs (Certificate Revocation Lists).

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://nodejs.org/api/buffer.html#class-buffer

or custom Diffie-Hellman parameters, required for non-ECDHE

perfect forward secrecy

https://nodejs.org/api/tls.html#perfect-forward-secrecy

. If omitted or invalid, the parameters are silently discarded and DHE ciphers will not be available.

https://en.wikipedia.org/wiki/Elliptic\_curve\_Diffie%E2%80%93Hellman

perfect forward secrecy

https://nodejs.org/api/tls.html#perfect-forward-secrecy

will still be available.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

A string describing a named curve or a colon separated list of curve NIDs or names, for example

P-521:P-384:P-256

, to use for ECDH key agreement. Set to

to select the curve automatically. Use

crypto.getCurves()

https://nodejs.org/api/crypto.html#cryptogetcurves

to obtain a list of available curve names. On recent releases,

openssl ecparam -list\_curves

will also display the name and description of each available elliptic curve.

tls.DEFAULT\_ECDH\_CURVE

https://nodejs.org/api/tls.html#tlsdefault\_ecdh\_curve

honorCipherOrder

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

Attempt to use the server's cipher suite preferences instead of the client's. When

SSL\_OP\_CIPHER\_SERVER\_PREFERENCE

to be set in

secureOptions

OpenSSL Options

https://nodejs.org/api/crypto.html#openssl-options

for more information.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://nodejs.org/api/buffer.html#class-buffer

https://nodejs.org/api/buffer.html#class-buffer

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

Private keys in PEM format. PEM allows the option of private keys being encrypted. Encrypted keys will be decrypted with

options.passphrase

. Multiple keys using different algorithms can be provided either as an array of unencrypted key strings or buffers, or an array of objects in the form

{pem: <string|buffer>\[, passphrase: <string>\]}

. The object form can only occur in an array.

object.passphrase

is optional. Encrypted keys will be decrypted with

object.passphrase

if provided, or

options.passphrase

if it is not.

privateKeyEngine

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Name of an OpenSSL engine to get private key from. Should be used together with

privateKeyIdentifier

Deprecated.

privateKeyIdentifier

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Identifier of a private key managed by an OpenSSL engine. Should be used together with

privateKeyEngine

. Should not be set together with

, because both options define a private key in different ways.

Deprecated.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Optionally set the maximum TLS version to allow. One of

. Cannot be specified along with the

secureProtocol

option; use one or the other.

tls.DEFAULT\_MAX\_VERSION

https://nodejs.org/api/tls.html#tlsdefault\_max\_version

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Optionally set the minimum TLS version to allow. One of

. Cannot be specified along with the

secureProtocol

option; use one or the other. Avoid setting to less than TLSv1.2, but it may be required for interoperability. Versions before TLSv1.2 may require downgrading the

OpenSSL Security Level

https://nodejs.org/api/tls.html#openssl-security-level

tls.DEFAULT\_MIN\_VERSION

https://nodejs.org/api/tls.html#tlsdefault\_min\_version

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Shared passphrase used for a single private key and/or a PFX.

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://nodejs.org/api/buffer.html#class-buffer

https://nodejs.org/api/buffer.html#class-buffer

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

PFX or PKCS12 encoded private key and certificate chain.

is an alternative to providing

individually. PFX is usually encrypted, if it is,

will be used to decrypt it. Multiple PFX can be provided either as an array of unencrypted PFX buffers, or an array of objects in the form

{buf: <string|buffer>\[, passphrase: <string>\]}

. The object form can only occur in an array.

object.passphrase

is optional. Encrypted PFX will be decrypted with

object.passphrase

if provided, or

options.passphrase

if it is not.

secureOptions

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Optionally affect the OpenSSL protocol behavior, which is not usually necessary. This should be used carefully if at all! Value is a numeric bitmask of the

options from

OpenSSL Options

https://nodejs.org/api/crypto.html#openssl-options

secureProtocol

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Legacy mechanism to select the TLS protocol version to use, it does not support independent control of the minimum and maximum version, and does not support limiting the protocol to TLSv1.3. Use

instead. The possible values are listed as

SSL\_METHODS

https://www.openssl.org/docs/man1.1.1/man7/ssl.html#Dealing-with-Protocol-Methods

, use the function names as strings. For example, use

'TLSv1\_1\_method'

to force TLS version 1.1, or

'TLS\_method'

to allow any TLS protocol version up to TLSv1.3. It is not recommended to use TLS versions less than 1.2, but it may be required for interoperability.

sessionIdContext

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Opaque identifier used by servers to ensure session state is not shared between applications. Unused by clients.

https://nodejs.org/api/buffer.html#class-buffer

48-bytes of cryptographically strong pseudorandom data. See

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

sessionTimeout

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

The number of seconds after which a TLS session created by the server will no longer be resumable. See

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

sets the default value of the

honorCipherOrder

, other APIs that create secure contexts leave it unset.

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

uses a 128 bit truncated SHA1 hash value generated from

process.argv

as the default value of the

sessionIdContext

option, other APIs that create secure contexts have no default value.

tls.createSecureContext()

method creates a

SecureContext

object. It is usable as an argument to several

APIs, such as

server.addContext()

https://nodejs.org/api/tls.html#serveraddcontexthostname-context

, but has no public methods. The

https://nodejs.org/api/tls.html#class-tlsserver

constructor and the

tls.createServer()

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

method do not support the

secureContext

for ciphers that use certificates. Either

can be used to provide it.

option is not given, then Node.js will default to using

Mozilla's publicly trusted list of CAs

https://hg.mozilla.org/mozilla-central/raw-file/tip/security/nss/lib/ckfw/builtins/certdata.txt

Custom DHE parameters are discouraged in favor of the new

dhparam: 'auto'

option. When set to

, well-known DHE parameters of sufficient strength will be selected automatically. Otherwise, if necessary,

openssl dhparam

can be used to create custom parameters. The key length must be greater than or equal to 1024 bits or else an error will be thrown. Although 1024 bits is permissible, use 2048 bits or larger for stronger security.

tls.createServer(\[options\]\[, secureConnectionListener\])

https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener

Added in: v0.3.2 History

v22.4.0, v20.16.0

clientCertEngine

option depends on custom engine support in OpenSSL which is deprecated in OpenSSL 3.

v20.4.0, v18.19.0

parameter can now include

ALPNCallback

ALPNProtocols

is set, incoming connections that send an ALPN extension with no supported protocols are terminated with a fatal

no\_application\_protocol

parameter now supports

net.createServer()

parameter can now include

clientCertEngine

ALPNProtocols

option can be a

ALPN options are supported now.

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Object

ALPNProtocols

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

https://nodejs.org/api/buffer.html#class-buffer

<TypedArray>

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/TypedArray

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/DataView

An array of strings, or a single

containing the supported ALPN protocols. Buffers should have the format

\[len\]\[name\]\[len\]\[name\]...

0x05hello0x05world

, where the first byte is the length of the next protocol name. Passing an array is usually much simpler, e.g.

\['hello', 'world'\]

. (Protocols should be ordered by their priority.)

ALPNCallback

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

If set, this will be called when a client opens a connection using the ALPN extension. One argument will be passed to the callback: an object containing

fields, respectively containing the server name from the SNI extension (if any) and an array of ALPN protocol name strings. The callback must return either one of the strings listed in

, which will be returned to the client as the selected ALPN protocol, or

, to reject the connection with a fatal alert. If a string is returned that does not match one of the client's ALPN protocols, an error will be thrown. This option cannot be used with the

ALPNProtocols

option, and setting both options will throw an error.

clientCertEngine

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Name of an OpenSSL engine which can provide the client certificate.

Deprecated.

enableTrace

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

tls.TLSSocket.enableTrace()

https://nodejs.org/api/tls.html#tlssocketenabletrace

will be called on new connections. Tracing can be enabled after the secure connection is established, but this option must be used to trace the secure connection setup.

handshakeTimeout

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

Abort the connection if the SSL/TLS handshake does not finish in the specified number of milliseconds. A

'tlsClientError'

is emitted on the

object whenever a handshake times out.

(120 seconds).

rejectUnauthorized

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

the server will reject any connection which is not authorized with the list of supplied CAs. This option only has an effect if

requestCert

requestCert

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#boolean\_type

the server will request a certificate from clients that connect and attempt to verify that certificate.

sessionTimeout

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#number\_type

The number of seconds after which a TLS session created by the server will no longer be resumable. See

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

SNICallback(servername, callback)

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

A function that will be called if the client supports SNI TLS extension. Two arguments will be passed when called:

is an error-first callback that takes two optional arguments:

, if provided, is a

SecureContext

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

can be used to get a proper

SecureContext

is called with a falsy

argument, the default secure context of the server will be used. If

SNICallback

wasn't provided the default callback with high-level API will be used (see below).

https://nodejs.org/api/buffer.html#class-buffer

48-bytes of cryptographically strong pseudorandom data. See

Session Resumption

https://nodejs.org/api/tls.html#session-resumption

for more information.

pskCallback

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

For TLS-PSK negotiation, see

Pre-shared keys

https://nodejs.org/api/tls.html#pre-shared-keys

pskIdentityHint

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

optional hint to send to a client to help with selecting the identity during TLS-PSK negotiation. Will be ignored in TLS 1.3. Upon failing to set pskIdentityHint

'tlsClientError'

will be emitted with

'ERR\_TLS\_PSK\_SET\_IDENTITY\_HINT\_FAILED'

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

option can be provided. For servers, the identity options (

pskCallback

) are usually required.

net.createServer()

https://nodejs.org/api/net.html#netcreateserveroptions-connectionlistener

option can be provided.

secureConnectionListener

https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global\_Objects/Function

<tls.Server>

https://nodejs.org/api/tls.html#class-tlsserver

Creates a new

https://nodejs.org/api/tls.html#class-tlsserver

secureConnectionListener

, if provided, is automatically set as a listener for the

'secureConnection'

https://nodejs.org/api/tls.html#event-secureconnection

options is automatically shared between

node:cluster

module workers.

#### The following illustrates a simple echo server:

import { createServer } from 'node:tls';
import { readFileSync } from 'node:fs';

const options = {
  key: readFileSync('server-key.pem'),
  cert: readFileSync('server-cert.pem'),

  // This is necessary only if using client certificate authentication.
  requestCert: true,

  // This is necessary only if the client uses a self-signed certificate.
  ca: \[ readFileSync('client-cert.pem') \],
};

const server = createServer(options, (socket) => {
  console.log('server connected',
              socket.authorized ? 'authorized' : 'unauthorized');
  socket.write('welcome!\n');
  socket.setEncoding('utf8');
  socket.pipe(socket);
});
server.listen(8000, () => {
  console.log('server bound');
});
const { createServer } = require('node:tls');
const { readFileSync } = require('node:fs');

const options = {
  key: readFileSync('server-key.pem'),
  cert: readFileSync('server-cert.pem'),

  // This is necessary only if using client certificate authentication.
  requestCert: true,

  // This is necessary only if the client uses a self-signed certificate.
  ca: \[ readFileSync('client-cert.pem') \],
};

const server = createServer(options, (socket) => {
  console.log('server connected',
              socket.authorized ? 'authorized' : 'unauthorized');
  socket.write('welcome!\n');
  socket.setEncoding('utf8');
  socket.pipe(socket);
});
server.listen(8000, () => {
  console.log('server bound');
});
javascriptcopy

#### To generate the certificate and key for this example, run:

openssl req -x509 -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' \
  -keyout server-key.pem -out server-cert.pem
bashcopy

Then, to generate the

client-cert.pem

certificate for this example, run:

openssl pkcs12 -certpbe AES-256-CBC -export -out client-cert.pem \
  -inkey server-key.pem -in server-cert.pem
bashcopy

The server can be tested by connecting to it using the example client from

tls.connect()

https://nodejs.org/api/tls.html#tlsconnectoptions-callback

tls.setDefaultCACertificates(certs)

https://nodejs.org/api/tls.html#tlssetdefaultcacertificatescerts

Added in: v24.5.0, v22.19.0

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

An array of CA certificates in PEM format.

Sets the default CA certificates used by Node.js TLS clients. If the provided certificates are parsed successfully, they will become the default CA certificate list returned by

tls.getCACertificates()

https://nodejs.org/api/tls.html#tlsgetcacertificatestype

and used by subsequent TLS connections that don't specify their own CA certificates. The certificates will be deduplicated before being set as the default.

This function only affects the current Node.js thread. Previous sessions cached by the HTTPS agent won't be affected by this change, so this method should be called before any unwanted cachable TLS connections are made.

#### To use system CA certificates as the default:

const tls = require('node:tls');
tls.setDefaultCACertificates(tls.getCACertificates('system'));
import tls from 'node:tls';
tls.setDefaultCACertificates(tls.getCACertificates('system'));
javascriptcopy

This function completely replaces the default CA certificate list. To add additional certificates to the existing defaults, get the current certificates and append to them:

const tls = require('node:tls');
const currentCerts = tls.getCACertificates('default');
const additionalCerts = \['-----BEGIN CERTIFICATE-----\n...'\];
tls.setDefaultCACertificates(\[...currentCerts, ...additionalCerts\]);
import tls from 'node:tls';
const currentCerts = tls.getCACertificates('default');
const additionalCerts = \['-----BEGIN CERTIFICATE-----\n...'\];
tls.setDefaultCACertificates(\[...currentCerts, ...additionalCerts\]);
javascriptcopy

tls.getCACertificates(\[type\])

https://nodejs.org/api/tls.html#tlsgetcacertificatestype

Added in: v23.10.0, v22.15.0

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

<undefined>

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#undefined\_type

The type of CA certificates that will be returned. Valid values are

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

An array of PEM-encoded certificates. The array may contain duplicates if the same certificate is repeatedly stored in multiple sources.

Returns an array containing the CA certificates from various sources, depending on

: return the CA certificates that will be used by the Node.js TLS clients by default.

--use-bundled-ca

https://nodejs.org/api/cli.html#--use-bundled-ca---use-openssl-ca

is enabled (default), or

--use-openssl-ca

https://nodejs.org/api/cli.html#--use-bundled-ca---use-openssl-ca

is not enabled, this would include CA certificates from the bundled Mozilla CA store.

--use-system-ca

https://nodejs.org/api/cli.html#--use-system-ca

is enabled, this would also include certificates from the system's trusted store.

NODE\_EXTRA\_CA\_CERTS

https://nodejs.org/api/cli.html#node\_extra\_ca\_certsfile

is used, this would also include certificates loaded from the specified file.

: return the CA certificates that are loaded from the system's trusted store, according to rules set by

--use-system-ca

https://nodejs.org/api/cli.html#--use-system-ca

. This can be used to get the certificates from the system when

--use-system-ca

https://nodejs.org/api/cli.html#--use-system-ca

is not enabled.

: return the CA certificates from the bundled Mozilla CA store. This would be the same as

tls.rootCertificates

https://nodejs.org/api/tls.html#tlsrootcertificates

: return the CA certificates loaded from

NODE\_EXTRA\_CA\_CERTS

https://nodejs.org/api/cli.html#node\_extra\_ca\_certsfile

. It's an empty array if

NODE\_EXTRA\_CA\_CERTS

https://nodejs.org/api/cli.html#node\_extra\_ca\_certsfile

is not set.

tls.getCiphers()

https://nodejs.org/api/tls.html#tlsgetciphers

Added in: v0.10.2

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

Returns an array with the names of the supported TLS ciphers. The names are lower-case for historical reasons, but must be uppercased to be used in the

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

Not all supported ciphers are enabled by default. See

Modifying the default TLS cipher suite

https://nodejs.org/api/tls.html#modifying-the-default-tls-cipher-suite

Cipher names that start with

are for TLSv1.3, all the others are for TLSv1.2 and below.

console.log(tls.getCiphers()); // \['aes128-gcm-sha256', 'aes128-sha', ...\]
jscopy

tls.rootCertificates

https://nodejs.org/api/tls.html#tlsrootcertificates

Added in: v12.3.0

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

An immutable array of strings representing the root certificates (in PEM format) from the bundled Mozilla CA store as supplied by the current Node.js version.

The bundled CA store, as supplied by Node.js, is a snapshot of Mozilla CA store that is fixed at release time. It is identical on all supported platforms.

To get the actual CA certificates used by the current Node.js instance, which may include certificates loaded from the system store (if

--use-system-ca

is used) or loaded from a file indicated by

NODE\_EXTRA\_CA\_CERTS

tls.getCACertificates()

https://nodejs.org/api/tls.html#tlsgetcacertificatestype

tls.DEFAULT\_ECDH\_CURVE

https://nodejs.org/api/tls.html#tlsdefault\_ecdh\_curve

Added in: v0.11.13 History

Default value changed to

The default curve name to use for ECDH key agreement in a tls server. The default value is

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

for further information.

tls.DEFAULT\_MAX\_VERSION

https://nodejs.org/api/tls.html#tlsdefault\_max\_version

Added in: v11.4.0

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The default value of the

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

. It can be assigned any of the supported TLS protocol versions,

, unless changed using CLI options. Using

--tls-max-v1.2

sets the default to

--tls-max-v1.3

sets the default to

. If multiple of the options are provided, the highest maximum is used.

tls.DEFAULT\_MIN\_VERSION

https://nodejs.org/api/tls.html#tlsdefault\_min\_version

Added in: v11.4.0

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The default value of the

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

. It can be assigned any of the supported TLS protocol versions,

. Versions before TLSv1.2 may require downgrading the

OpenSSL Security Level

https://nodejs.org/api/tls.html#openssl-security-level

, unless changed using CLI options. Using

--tls-min-v1.0

sets the default to

--tls-min-v1.1

sets the default to

--tls-min-v1.3

sets the default to

. If multiple of the options are provided, the lowest minimum is used.

tls.DEFAULT\_CIPHERS

https://nodejs.org/api/tls.html#tlsdefault\_ciphers

Added in: v0.11.3

https://developer.mozilla.org/docs/Web/JavaScript/Data\_structures#string\_type

The default value of the

tls.createSecureContext()

https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions

. It can be assigned any of the supported OpenSSL ciphers. Defaults to the content of

crypto.constants.defaultCoreCipherList

, unless changed using CLI options using

--tls-default-ciphers


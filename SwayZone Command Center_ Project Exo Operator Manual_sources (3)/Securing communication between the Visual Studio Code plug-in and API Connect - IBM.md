---
sourceFile: "Securing communication between the Visual Studio Code plug-in and API Connect - IBM"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.694Z"
---

# Securing communication between the Visual Studio Code plug-in and API Connect - IBM

54ea0448-2e29-4521-acf1-69361b3b4391

Securing communication between the Visual Studio Code plug-in and API Connect - IBM

bdf408e9-5cde-44f2-af44-14dfed8eab41

https://www.ibm.com/docs/en/api-connect/software/12.1.0?topic=configuring-securing-communication-between-visual-studio-code-plug-in-api-connect

Securing communication between the Visual Studio Code plug-in and API Connect

Securing communication between the Visual Studio Code plug-in and API Connect

Edit online

https://oxygen.dcs-openshift-cnv.dal.app.cirrus.ibm.com/oxygenxml-web-author/app/oxygen.html?url=gitgh%3A%2F%2Fhttps%253A%252F%252Fgithub.ibm.com%252Fvelox%252Fdocs-v10CD%2Fmaster%2Fsrc%2Fcom.ibm.apic.assistant.doc%2Flicense\_apiagent.dita

Configure trusted certificates so the Visual Studio Code plug-in can establish a secure connection with API Agent. Use this procedure only when your deployment uses self-signed or nonpublicly trusted CA certificates.

About this task

The Visual Studio Code plug-in relies on trusted certificates to authenticate and encrypt its connection with the product. Manually add the root CA certificate to your system's truststore when your environment uses self-signed certificates or a private certificate authority issues the certificates. The steps that you follow depend on the operating system where the Visual Studio Code plug-in is installed.

From the Visual Studio Code editor, open the settings and set

http.systemCertificates: true

. The default value is true. Ensure that it is set to true.

Add the root CA certificate to the trusted list on the system that has the Visual Studio Code plug-in. The steps vary depending on the operating system.

#### For macOS, complete the following steps:

Copy the root CA certificate to the system.

To open the Keychain Access application, press

Command + Space

From the left side menu bar, select System.

Drag the certificate to add the saved certificate to the system certificates. In the list of certificates, the root certificate that was added is displayed with a red error.

Double-click the name of the certificate, which opens a new window. Expand the Trust section.

In the When using this certificate field, select Always Trust.

To add the certificate to the list of trusted certificates, close the window.

#### For Linux®, complete the following steps:

Copy the root CA certificate in PEM or DER format to the system.

#### Run the following commands:

sudo cp apic-dev-internal-root-ca.crt /etc/pki/ca-trust/source/anchors/

sudo update-ca-trust

#### For Ubuntu, complete the following steps:

Copy the root CA certificate in the PEM or DER format to the system.

#### Run the following command to create a directory:

sudo mkdir -p /usr/local/share/ca-certificates

3. Run the following command to copy the certificate file to the directory:

sudo cp cert\_file.crt /usr/local/share/ca-certificates

4. Run the following command to update the system's truststore:

sudo update-ca-certificates

5. Verify that the certificate is in the /etc/ssl/certs/ca-certificates.crt file.

For Windows, see the Windows documentation to use Microsoft Management Console (MMC) to add the certificate.

#### Parent topic:

Configuring

https://www.ibm.com/docs/en/api-connect/software/configure\_apiagent\_apimgmt.html


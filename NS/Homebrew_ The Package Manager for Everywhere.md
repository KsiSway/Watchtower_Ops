---
sourceFile: "Homebrew: The Package Manager for Everywhere"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.364Z"
---

# Homebrew: The Package Manager for Everywhere

10d74326-87fc-4900-970f-c387120f3287

Homebrew: The Package Manager for Everywhere

c785e04a-eac2-4440-bdee-a0171e36caf3

https://brew.sh/

Homebrew: The Package Manager for Everywhere

https://brew.sh/

The Package Manager for Everywhere

https://docs.brew.sh/Support-Tiers

macOS (Sonoma 14 and newer), Linux and Windows Subsystem for Linux (WSL).

Azərbaycanca

Lëtzebuergesch

Norsk bokmål

Norsk nynorsk

Português Brasileiro

🚀 Install Homebrew

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

⧉ Paste that in the macOS Terminal, a Linux shell or WSL. The script explains what it will do and then pauses before it does it. Read about other

installation options

https://docs.brew.sh/Installation

. If you're on macOS, try our

installer for interactive or unattended MDM installs. Download it from

Homebrew's latest GitHub release

https://github.com/Homebrew/brew/releases/latest

🔧 What Does Homebrew Do?

Homebrew installs

the command-line tools and applications you need

https://formulae.brew.sh/formula/

across macOS, Linux and WSL.

Homebrew won't install files outside its

https://docs.brew.sh/Formula-Cookbook#homebrew-terminology

. It installs each package into its own

https://docs.brew.sh/Formula-Cookbook#homebrew-terminology

https://docs.brew.sh/Formula-Cookbook#homebrew-terminology

, then symlinks its files into the prefix, the path where Homebrew is installed:

/opt/homebrew

on Apple Silicon,

/home/linuxbrew/.linuxbrew

on Linux/WSL and

on macOS Intel.

$ brew install ffmpeg firefox
$ find $(brew --cellar)/ffmpeg
/opt/homebrew/Cellar/ffmpeg/8.1.1/bin/ffmpeg
/opt/homebrew/Cellar/ffmpeg/8.1.1/share/man/man1/ffmpeg.1
$ ls -l $(brew --prefix)/bin
/opt/homebrew/bin/ffmpeg -> ../Cellar/ffmpeg/8.1.1/bin/ffmpeg
$ find $(brew --caskroom)/firefox
/opt/homebrew/Caskroom/firefox/151.0.3/Firefox.app
$ ls /Applications
Firefox.app

📦 Homebrew Packages

Homebrew packages are

formulae and casks

https://docs.brew.sh/Formula-Cookbook#homebrew-terminology

https://docs.brew.sh/Formula-Cookbook#homebrew-terminology

are package definitions that build command-line tools, libraries and services from upstream source code. Formulae in

homebrew/core

https://github.com/Homebrew/homebrew-core

require human review before they are accepted, changed or updated and must be open source software with a

Debian Free Software Guidelines

https://wiki.debian.org/DFSGLicenses

-compatible licence (see the requirements in

Acceptable Formulae

https://docs.brew.sh/Acceptable-Formulae

). They are maintained by Homebrew's maintainers and contributors. Create formulae with help from the

Formula Cookbook

https://docs.brew.sh/Formula-Cookbook

. Other package repositories are called

https://docs.brew.sh/Taps

; they let anyone maintain their own formulae and casks outside the officially supported repositories. Read how

https://docs.brew.sh/Tap-Trust

works before using non-official taps, then learn how to

create and maintain a tap

https://docs.brew.sh/How-to-Create-and-Maintain-a-Tap

$ brew create https://ffmpeg.org/releases/ffmpeg-8.1.1.tar.xz
Created .../homebrew-core/Formula/ffmpeg.rb

class Ffmpeg < Formula
  desc "Play, record, convert, and stream select audio and video codecs"
  homepage "https://ffmpeg.org/"
  url "https://ffmpeg.org/releases/ffmpeg-8.1.1.tar.xz"
  sha256 "b6863adde98898f42602017462871b5f6333e65aec803fdd7a6308639c52edf3"
  license "GPL-3.0-or-later"

  def install
    system "./configure", "--prefix=#{prefix}", "--enable-shared"
    system "make", "install"
  end
end

https://docs.brew.sh/Formula-Cookbook#homebrew-terminology

are package definitions that install upstream pre-built binaries such as applications, fonts and plugins. Some casks

auto-update

https://docs.brew.sh/Cask-Cookbook#stanza-auto\_updates

outside Homebrew, so use

brew upgrade --greedy

if you want Homebrew to update them too. Casks in

homebrew/cask

https://github.com/Homebrew/homebrew-cask

require human review before they are accepted, changed or updated and must meet the requirements in

Acceptable Casks

https://docs.brew.sh/Acceptable-Casks

. They are maintained by Homebrew's maintainers and contributors. Create casks with help from the

Cask Cookbook

https://docs.brew.sh/Cask-Cookbook

$ brew create --cask https://download-installer.cdn.mozilla.net/pub/firefox/releases/151.0.3/mac/en-US/Firefox%20151.0.3.dmg
Created .../homebrew-cask/Casks/firefox.rb

cask "firefox" do
  version "151.0.3"
  sha256 "60d5cb29412b161c76ecc58f3f8a960cd0048081cf84c6fe91579f1957564277"

  url "https://download-installer.cdn.mozilla.net/pub/firefox/releases/#{version}/mac/en-US/Firefox%20#{version}.dmg"
  name "Mozilla Firefox"
  desc "Web browser"
  homepage "https://www.mozilla.org/firefox/"
end

📋 Homebrew Bundle

Homebrew Bundle

https://docs.brew.sh/Brew-Bundle-and-Brewfile

is declarative: it uses a

to describe the state you want. Run

brew bundle

to install missing dependencies, update outdated ones and keep project or machine setup repeatable. Homebrew Bundle supports formulae, casks, taps, Mac App Store apps, WinGet packages on WSL, VSCode extensions, Go packages, Cargo packages, uv tools, Flatpak packages, krew kubectl plugins and starting background services with

brew services

$ cat Brewfile
brew "ffmpeg"
cask "firefox"

$ brew bundle
Installing ffmpeg
Installing firefox
\`brew bundle\` complete! 2 Brewfile dependencies now installed.

💸 Donate to Homebrew

Homebrew is a non-profit project run entirely by volunteers, not employees. We need your funds to pay for software, hardware and hosting around continuous integration and future improvements to the project. Every donation will be spent on making Homebrew better for our users. Please consider a regular donation through

GitHub Sponsors

https://github.com/sponsors/Homebrew

Open Collective

https://opencollective.com/homebrew

https://www.patreon.com/homebrew

. Homebrew is fiscally hosted by the

Open Source Collective

https://opencollective.com/opensource

📚 Homebrew Resources

Documentation

Read the Homebrew manual with

https://docs.brew.sh/Manpage

installation

https://docs.brew.sh/Installation

troubleshooting

https://docs.brew.sh/Troubleshooting

contribution

https://github.com/Homebrew/brew/blob/HEAD/docs/How-To-Open-a-Homebrew-Pull-Request.md

development

https://docs.brew.sh/Formula-Cookbook

guides, including the

FAQ (Frequently Asked Questions)

https://docs.brew.sh/FAQ

docs.brew.sh

https://docs.brew.sh/

Homebrew Blog

Homebrew Blog

https://brew.sh/blog/

for release notes, project updates and announcements. Latest post

Homebrew 6.0.0

https://brew.sh/2026/06/11/homebrew-6.0.0/

Have a question or need help choosing where to report a problem? Start with Homebrew's

discussions

https://github.com/orgs/Homebrew/discussions

new issue form

https://github.com/Homebrew/brew/issues/new/choose

Homebrew Packages

https://formulae.brew.sh/formula/

https://formulae.brew.sh/cask/

, dependencies, versions and package metadata on

formulae.brew.sh

https://formulae.brew.sh/

Analytics Data

View anonymised install, build and operating system usage data at

formulae.brew.sh/analytics

https://formulae.brew.sh/analytics/

. Read how Homebrew uses

Anonymous Analytics

https://docs.brew.sh/Analytics

Follow Homebrew on

https://fosstodon.org/@homebrew

https://bsky.app/profile/brew.sh

𝕏 (Twitter)

https://x.com/MacHomebrew

or subscribe to the

https://buttondown.email/homebrew

Homebrew is run by the volunteer Homebrew maintainers and contributors. Website by

Mike McQuaid

https://mikemcquaid.com/

Rémi Prévost

https://exomel.com/

Danielle Lalonde

https://cargocollective.com/danilalo

. Homebrew was originally created by

https://mxcl.dev/


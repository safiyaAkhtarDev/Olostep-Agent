<!-- source: https://docs.olostep.com/cli/install -->
# https://docs.olostep.com/cli/install

Install and update the Olostep CLI - Olostep Docs  

> Documentation Index
> -------------------
> 
> Fetch the complete documentation index at: [/llms.txt](/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

[Olostep Docs home page![light logo](https://mintcdn.com/olostep-58/294AdrknPYBl2RjK/logo/light.svg?fit=max&auto=format&n=294AdrknPYBl2RjK&q=85&s=fad5e5ee72a916722d9ad8279ee7186d)![dark logo](https://mintcdn.com/olostep-58/294AdrknPYBl2RjK/logo/dark.svg?fit=max&auto=format&n=294AdrknPYBl2RjK&q=85&s=dc0971e24a94b91a46d7dd802d74b94f)](https://www.olostep.com/)

English

Search...

⌘K

Search...

Navigation

Olostep CLI

Install and update the Olostep CLI

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Olostep CLI

Install and update the Olostep CLI
==================================

Copy pageCopy page

Install the olostep command, keep it up to date, and remove it.

Copy pageCopy page

[​

](#requirements)

Requirements
------------------------------------

*   macOS or Linux, with a POSIX shell.
*   [Node.js](https://nodejs.org) 20.19 or newer, and `npm` (it comes with Node.js).
*   `curl` or `wget`.

Check your Node.js version:

    node -v
    

[​

](#install)

Install
--------------------------

    curl -fsSL https://cli.olostep.com | sh
    

The script:

1.  Checks for Node.js 20.19+ and `npm`.
2.  Downloads the CLI package and checks its SHA-256 checksum. If the checksum differs, nothing is installed.
3.  Installs the package into `~/.olostep`. No `sudo` is needed.
4.  Links `olostep` into a writable directory that is already on your `PATH`. If there is none, it links into `~/.local/bin` and adds that directory to your shell’s startup file (`~/.zshrc`, `~/.bashrc` or `~/.bash_profile`, fish’s `conf.d`, or `~/.profile`).

When it finishes, it prints `Installed olostep <version> in ~/.olostep/bin`. If it had to change your `PATH`, open a new terminal first. Then run:

    olostep
    

### 

[​

](#install-somewhere-else)

Install somewhere else

Set `OLOSTEP_HOME` to an absolute path to install there instead of `~/.olostep`:

    curl -fsSL https://cli.olostep.com | OLOSTEP_HOME="$HOME/tools/olostep" sh
    

The script stops if another `olostep` command is already on your `PATH` and was not installed by this script. Remove the other one first, then run the script again. The older npm package `olostep-cli` is a separate, older tool and is not covered by these docs.

[​

](#update)

Update
------------------------

Run:

    olostep update
    

`olostep update` runs the install script again: `curl -fsSL https://cli.olostep.com | sh`. Running the script yourself does the same thing. When a newer version is out, the CLI tells you after a command finishes:

    A new version of olostep is out: <version> (you have <version>). Run olostep update to get it.
    

The notice only appears for a person at a terminal. It is not shown to coding agents, when `CI` is set, or with `--json`.

[​

](#uninstall)

Uninstall
------------------------------

1

Sign out

    olostep logout
    

Olostep revokes this computer’s connection and the CLI forgets its sign-in. Skip this if you were never signed in.

2

Remove the linked command

    rm "$(command -v olostep)"
    

This removes the `olostep` link the installer put on your `PATH`.

3

Remove the installation

    rm -rf ~/.olostep
    

Use your `OLOSTEP_HOME` path instead if you set one.

4

Remove the CLI's settings

    rm -rf "${XDG_CONFIG_HOME:-$HOME/.config}/olostep"
    

This folder holds the saved sign-in and the `olostep chat` conversation reference.

If the installer added a `PATH` line to your shell’s startup file, it sits under the comment `# olostep CLI`. Delete both lines.

Was this page helpful?

YesNo
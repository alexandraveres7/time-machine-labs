# Working with git

## What is Git?

Git is a distributed version-control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files. Its goals include speed, data integrity, and support for distributed, non-linear workflows.

Git was created by Linus Torvalds in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development.

## Configure

### Installing Git

https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Windows Installer Settings

- Use git and optional Unix tools from the Windows Command Prompt
- Checkout Windows-style, commit unix-style line endings

### Setting up

```bash
$ git config user.name
$ git config user.email

$ git config user.name <user_name>
$ git config user.email <email>
```

Show global git settings file

```bash
$ git config --global --edit
```

### Creating or cloning a repository

Git projects are called repositories.
You can create one by using `git init` or `git clone <url>`

We'll create one from scratch.

```bash
$ cd <My projects folder>
$ mkdir working-with-git
$ cd working-with-git
$ git init
```

Now you can type `git status` command to check if you have a git repository.

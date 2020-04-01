# Working with git

<!-- TOC -->

- [Working with git](#working-with-git)
    - [What is Git?](#what-is-git)
    - [Configure](#configure)
        - [Installing Git](#installing-git)
        - [Setting up](#setting-up)
        - [Creating or cloning a repository](#creating-or-cloning-a-repository)
    - [Files and commit](#files-and-commit)
        - [Making a new commit](#making-a-new-commit)

<!-- /TOC -->
## What is Git?

Git is a distributed version-control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files. Its goals include speed, data integrity, and support for distributed, non-linear workflows.

Git was created by Linus Torvalds in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development.

## Configure

### Installing Git

[Getting started installing git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

**Windows Installer Settings**

- Use git from the command prompt **or** Use git and optional Unix tools from the Windows Command Prompt
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

Git projects are called *repositories*.
You can create one by using `git init` or `git clone <url>`.

We'll create one from scratch. Open your favourite terminal. ( windows is cmd )

```bash
$ cd <My projects folder>
$ mkdir working-with-git
$ cd working-with-git
$ git init
```

Now you can type `git status` command to check if you have a git repository.

## Files and commit

### Making a new commit

In our local *repository*, we need to create some files.

```bash
$ touch hello.txt world.txt
```

Check local changes registered by git.

```bash
$ git status
```

All all changes and review *staged changes* before commit.

```bash
$ git add -A # git add --all
$ git status
```

Now we see all the changes that will be commited to git history if we move forward. Let's make the commit'

```bash
$ git commit -m "first commit message" # git commit --message <msg>
```

Good work! You now have your first commit on this *git local repository*.

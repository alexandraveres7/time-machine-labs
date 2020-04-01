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
        - [Viewing history](#viewing-history)
        - [Deleting files and commit changes](#deleting-files-and-commit-changes)
        - [Using .gitignore](#using-gitignore)
    - [Remote repositories](#remote-repositories)
        - [Adding a new `origin`](#adding-a-new-origin)
        - [Pushing code to remote server](#pushing-code-to-remote-server)
        - [Pulling code from remote server](#pulling-code-from-remote-server)
    - [Branches](#branches)
        - [List local and remote branches](#list-local-and-remote-branches)
        - [Creating a new local branch](#creating-a-new-local-branch)
        - [Pull changes from local `experimental-feature` branch to local `master` branch](#pull-changes-from-local-experimental-feature-branch-to-local-master-branch)
        - [Push changes from local `experimental-feature` branch to remote `experimental-feature` branch](#push-changes-from-local-experimental-feature-branch-to-remote-experimental-feature-branch)
        - [Branching is hard](#branching-is-hard)
    - [Git diff command](#git-diff-command)
        - [Show recent changes across project repository](#show-recent-changes-across-project-repository)
        - [Show diff between files on same branch](#show-diff-between-files-on-same-branch)
        - [Show diff between local `master` branch and local `experimental-feature` branch](#show-diff-between-local-master-branch-and-local-experimental-feature-branch)
    - [Patch files](#patch-files)

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

In our local **repository**, we need to create some files.

```bash
$ touch hello.txt world.txt
```

Check local changes registered by git.

```bash
$ git status
```

All all changes and review **staged changes** before commit.

```bash
$ git add -A # git add --all
$ git status
```

Now we see all the changes that will be commited to git history if we move forward. Let's make the commit'

```bash
$ git commit -m "first commit message" # git commit --message <msg>
```

Good work! You now have your first commit on this **git local repository**.

Now that you know how to make commits, add a couple more before moving to the next section. Change `hello.txt` and `world.txt` contents and commit changes.

### Viewing history

Viewing changes made so far in this **repository**.

```bash
$ git log
```

A lot of information is displayed and can be a bit hard to understand what is happening. We'll fix that by creating an alias for showing history.

```bash
$ git config --global --edit
```

Add this snippet.

```ini
[alias]
    history = log --pretty=format:'%ad %h | %s%d %an' --graph --date=short

    # or python pretty formatted

    history = log --pretty=format:'%C(blue)%ad%C(reset) %C(yellow)%h%C(reset) | %C(white)%s%C(reset)%C(cyan)%d%C(reset) %C(bold)%an%C(reset)' --graph --date=short
```

Now check the history using the newly created alias for `git log`.

```bash
$ git history
```

This is a lot better structured history!


### Deleting files and commit changes

Let's delete the `world.txt` from this repository.

```bash
$ git rm world.txt # rm world.txt or right-click -> delete file
$ git status # review changes
$ git add -A # add changes, git add world.txt works too!
$ git status # review staged changes before making a commit
$ git commit -m "deleted world.txt"
$ git history
```

You've learned all these commands! Awesome!

### Using .gitignore

Sometimes we need to ignore files in our project. We usually want to ignore hidden files ( starting with dot ) or generated files that we do not want to commit. These are settings or can be generated by running our project.

Let's create a `.gitignore` file

```bash
$ touch .gitignore
$ vi .gitignore # use your text editor if this does not work. "notepad .gitignore"
$ # press insert
```

Copy and paste the following lines:

```txt
always_ignored.txt

# ignore all hiden files
.*

# preserve .gitignore and .gitkeep files
!.gitignore
!.gitkeep
```

Save file, add changes and commit.
```bash
$ git add -A
$ git status
$ git commit -m "added .gitignore file"
```

Let's test if we ignore files!

```bash
$ touch always_ignore.txt # this was added to .gitignored
$ git add -A
$ git status
```

No changes should have been staged and ready for a commit. File should be ignored when staging changes. If this is the case, well done! It works.


## Remote repositories

### Adding a new `origin`

Since git is a **distributed version control system**, let's distribute our code.

Go to your github.com account. Create a new empty repository.
Copy the link **after** `git remote add origin`.

Let's go back to our **local git repository**.
We want to find out where do we send repository code.

```bash
$ git remote show
```

This shows all the remote endpoints where we can **push** code.
Since we don't have an endpoint set, let's add it.

```bash
$ git remote add origin <paste copied url>
$ git remote show
$ git remote show origin # requires authentication with github credentials
```

Now we have our **local repository** linked to **our github repository** and we can **push** code there.

### Pushing code to remote server

```bash
$ git push -u origin master # git push --set-upstream origin master
```

This command pushes our code to origin which is github.com on branch master. Don't worry about what branches are at the moment. We'll get there soon enough.

Go to your github.com repository and see your code there.
Edit one file using the github.com interface and save it.

### Pulling code from remote server

Since now our remote server aka github repository has changes, we should **pull** them and see what's changed.

In your local repository:

```bash
$ git pull origin master # or just "git pull"
```

All changes are now downloaded from the github server and saved locally.
See `git history` of what has changed.

## Branches

We have been working with branches all this time and not know it.
Branches are **modified or exact copies** of your code, stored in git.

Let's say we want to add an experimental feature to our project but also continue working on current project without releasing the experimental feature.

What do we do? Without git we would probably end up `copying` and `pasting` entire project `folder` and add changes. That is similar to creating another `branch` without using git.

### List local and remote branches

We can see our local branches using:

```bash
$ git branch
```

`master` will probably be displayed and it's default branch in 99% of the projects. Remote origin ( in our case github.com ) master branch can be seen using:

```bash
$ git branch --all
```

Cool.

### Creating a new local branch

Since we want to add changes to our local repository, we'll create a new branch.

```bash
$ git branch -c "experimental-feature"
$ git branch
```

We've created a new branch but haven't switched to it to see the files.

```bash
$ git checkout experimental-feature
$ git branch
$ ls # list files
```

We've switched branches and can see all project files.
Make some commits here, but do not push to remote.
How does the history look like?

```bash
$ git history
```

Let's get back to our initial project branch ( master ).

```bash
$ git checkout master
$ git history
$ ls
```

All commited changes are not here. All changes are on the `experimental-feature` branch and `master` branch has been untouched by commits. You've learned branching!

### Pull changes from local `experimental-feature` branch to local `master` branch

Experimental feature is done and we need to `merge` the changes with our `master` branch.

```bash
# dot signifies local repository, you can also pull from remote server using "git pull origin master"
$ git pull . master
$ git history
$ ls
```

All changes from experimental branch should be here.

### Push changes from local `experimental-feature` branch to remote `experimental-feature` branch

All commits and changes on our `experimental-feature` are stored locally. We can push the changes to remote server on `experimental-feature-remote` branch.

```bash
$ git checkout experimental-feature
$ git push -u origin experimental-feature-remote
$ git history
```

All changes have been uploaded to github.com on branch `experimental-feature-remote`. You can check it out from the github.com web interface.

### Branching is hard

Branching is hard and it will get easier if you keep using git.
Here are some links on the topic.

- [a successful git branching-model](https://nvie.com/posts/a-successful-git-branching-model/) ( old model, not used anymore )
- [gitflow branching model](https://guides.github.com/introduction/flow/) ( recommended approach )

## Git diff command

`git diff` is one of the most helpful commands. It will display all changed lines in your project repository.

### Show recent changes across project repository

```bash
$ git checkout master
$ echo "git\n is\n awesome\n" > "good.txt"
$ git diff
```

Added lines are usually displayed with `green` and removed lines with `red`.

You can see all the changes we've made.

### Show diff between files on same branch

```bash
$ git checkout master
$ echo "git\n is\n awesome\n" > "good.txt"
$ echo "git\n kinda\n sucks\n" > "bad.txt"
$ git diff "good.txt" "bad.txt"
```

Commit these files to `master` branch.

### Show diff between local `master` branch and local `experimental-feature` branch

```bash
$ git diff master experimental-feature
```

## Patch files

You can send `git commits` by email if you need to. To do that you need to create a `patch` file with all the changes.

Creating a patch is really easy.

1. Use `git diff` command to get the changes
2. Save changes to a local file

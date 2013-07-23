## How to install zshrc ##

Rename <code>zshrc</code> to <code>.zshrc</code> and put it in your home
directory

Make zsh show the git prompt (thanks to (<https://github.com/olivierverdier/zsh-git-prompt>))

<code>mkdir ~/.zsh</code>

<code>mkdir ~/.zsh/git-prompt</code>

Copy <code>gitstatus.py</code> into <code>~/.zsh/git-prompt/</code>

Also copy <code>zshrc.sh</code> into <code>~/.zsh/</code>

Open <code>screenshot.png</code> to see how it looks :)

### Trouble-shooting ###
If you want to turn off the git prompt, open <code>~/.zshrc</code> and go to the bottom. Then choose style 1 for <code>PROMPT</code> instead of 3.

Also, you can toggle the cache for git prompt by opening <code>~/.zsh/zshrc.sh</code> and changing the variable <code>ZSH...NOCACHE</code> at the bottom.

## Commands ##
### Shell Commands ###

<code>.. = "cd .."</code>

<code>lsa = "ls -a" </code>

Recursive grep, ignoring binary files and cases. Also colors the matched term.

<code>mgrep [phrase]</code> (e.g., <code>mgrep "stanford university"</code>)

Recursive find. Ignores case and lists filenames. 

<code>mfind [filename]</code> (e.g., <code>mfind "*.pdf"</code>)

### Git commands ###

new [branch-name]: create a branch

sw [branch-name]: switch to the branch

rename [oldname] [newname]: rename branch

del [branch-name]: delete the branch

Del [branch-name]: force delete the branch

up [branch-name]: rebase onto that branch

add [path]: git add

br: show existing branches

com: git commit

acom: git commit --amend

st: git status

hist: show 10 most recent commits in a pretty way

pull: git pull origin

push: git push origin HEAD

git checkout -- . : remove all unstaged changes
## How to install zshrc ##

Rename <code>zshrc</code> to <code>.zshrc</code> and put it in your home
directory

Note: Currently, zsh doesn't show git prompt because of some alias issue. If you want to try, do the below

Thanks to (<https://github.com/olivierverdier/zsh-git-prompt>).

<code>mkdir ~/.zsh</code>

<code>mkdir ~/.zsh/git-prompt</code>

Copy <code>gitstatus.py</code> into <code>~/.zsh/git-prompt/</code>

Go to the last several lines of <code>~/.zshrc</code>. Choose style 3 instead of 1.

The last line of <code>~/.zsh/zshrc.sh</code> can be either true or false. Setting it to false will turn off the cache.

Open <code>screenshot.png</code> to see how it looks :)

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
# 0705 실습 코드

```bash
user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL (master)
$ git status
On branch master
nothing to commit, working tree clean
$ git config --global user.name 'Vidse'

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL
$ git config --global user.email 'dse04145@gmail.com'

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL
$ git init
Initialized empty Git repository in C:/Users/user/Desktop/TIL/.git/

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        "\353\247\210\355\201\254\353\213\244\354\232\264.assets/"
        "\353\247\210\355\201\254\353\213\244\354\232\264.md"

nothing added to commit but untracked files present 
(use "git add" to track)

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL (master) 
$ git add .

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL (master) 
$ git commit -m '마크다운'
[master (root-commit) 6f4083b] 마크다운
 3 files changed, 155 insertions(+)
 create mode 100644 "\353\247\210\355\201\254\353\213\244\354\232\264.assets/IMG_8327-16569839009911.jpeg"
 create mode 100644 "\353\247\210\355\201\254\353\213\244\354\232\264.assets/IMG_8327.jpeg"
 create mode 100644 "\353\247\210\355\201\254\353\213\244\354\232\264.md"

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL (master)
$ git log
commit 6f4083bc7738fb150cae36b737288e1b03e3aa2e (HEAD -> master)
Author: Vidse <dse04145@gmail.com>
Date:   Tue Jul 5 16:29:59 2022 +0900

    마크다운

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL (master)
$ git log -1
commit 6f4083bc7738fb150cae36b737288e1b03e3aa2e (HEAD -> master)
Author: Vidse <dse04145@gmail.com>
Date:   Tue Jul 5 16:29:59 2022 +0900

    마크다운

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL (master)
$ git log --oneline
6f4083b (HEAD -> master) 마크다운

user@DESKTOP-VDFDA2J MINGW64 ~/Desktop/TIL (master)
$ git status
On branch master
nothing to commit, working tree clean
```


# CLI

> Command Line Interface

명령(커맨드를 줄단위로)

명령어 인터페이스. 터미널을 통해서 사용자와 컴퓨터가 상호 작용하는 방식

mac os에는 터미널, windows는 cmd powershell



- 디렉토리 : 현재 폴더/파일
- pwd(print working directory) : 현재 디렉토리 출력
- cd(change directory) : 디렉토리 이동
- ls(list) : 목록
- mkdir(make directory) : 디렉토리 생성
- touch : 파일 생성
- rm 파일명 : 파일 삭제하기
- rm -r 폴더명 : 폴더 삭제하기
- 단축키 ctrl + l : 화면 깔끔하게 정리
- rm -rf .git : master 없애기



# GUI

> Graphic user Interface

그래픽





## 1. (Master)가 있는 곳에서는 git init을 하지 않는다.

## 2. git 명령어를 입력할때는 항.상. 경로를 잘 보자

## 3. 명령어의 결과 영어를 잘 읽자





# Git Status

## a.txt 파일을 만든 직후

> 빨간 글씨 => 1통

```bash
$ git status
On branch master

# 트래킹이 되고 있지 않은 파일?
# => 1통 (working directory)
# => 한번도 git으로 관리되고 있지 않은 파일!
Untracked files:
# git add 사용해봐...
# 포함시키기 위해서 / 커밋이 될 것 => 2통에 넣으려면
  (use "git add <file>..." to include in what will be committed)
        a.txt

# 커밋할 것은 없어 => 2통이 비어있어
# 하지만(but) 트래킹되지 않은 파일은 존재한다. 
# (git add 사용해서 트래킹해)
nothing added to commit but untracked files present (use "git add" to track)
```

## b.txt 파일을 만들고 add한 이후

> 초록 글씨 => 2통

```bash
$ git status
On branch master
# (커밋될) 변경사항들 => 2통
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
  		# 새로운 파일: b.txt
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

```

## a.txt 파일과 b.txt 파일을 모두 add한 이후 커밋까지

```bash
$ git status
On branch master
# 2통, 1통 모두 클린~!
nothing to commit, working tree clean
```



- 저장소 처음 만들때 : git init
- 버전을 기록할 때
  - git add
  - git commit -m '커밋메세지'
- 상태 확인할 때
  - git status : 1통, 2통
  - git log : 커밋 확인

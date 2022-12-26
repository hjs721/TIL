\1) 원격 저장소(https://github.com/rhello/hello.git)를 로컬에 클론(clone)

```git clone https://github.com/rhello/hello.git```

\2) 1)을 실행한 후 새로운 브랜치(issue-10)를 checkout 명령으로 생성

```git checkdout -b issue-10```

\3) 브랜치(issue-10)에 파일(hello.txt)을 수정

```파일 수정 후 git add hello.txt```

\4) 커밋 메시지에 깃허브 이슈(10번) 해소 메시지(closed)를 추가

```git commit --amend -m 해결: close #10```

\5) 브랜치(issue-10)를 브랜치(master)에 병한 후 원격 저장소에 저장

```git merge master```

```git push origin master```

\6) 5) 실행 후 브랜치(issue-10)를 삭제

```git branch -d issue-10```


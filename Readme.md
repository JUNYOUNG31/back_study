### spring boot 



> day1

```
project 설치 및 환경설정
run project
```



> day2

```
라이브러리
```



> day3

```
View 환경설정
컨트롤러에서 리턴 값으로 문자를 반환하면 viewResolver 가 화면을 찾아서 처리

helloController
return hello
model(data:hello!!)

viewResolver (resources/templates/hello.html)
${data} => hello!!
```

```
빌드하고 실행
git에서 실행(이클립스는 stop => 8080이 중복됨) 
project
./gradlew.bat build

project/build/libs
java -jar 빌드실행파일


8080 사용중 일 경우
cmd를 열고 아래 명령어 순차적으로 실행
현재 포트를 사용중인 프로세스 찾기
netstat -ano | findstr :포트번호
프로세스 강제 종료하기
taskkill /f /pid 프로세스번호
```

```
정적파일
static 폴더에 저장
수정불가능하지만 보기는 가능
```

```
MVC 템플릿 엔진
@RequestParam("name")
http://localhost:8080/hello-mvc?name=spring

param => ?name=spring 을 념겨줘야 에러가 발생하지않음
```


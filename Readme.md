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



> day4

```
API

alt + insert  => getter and setter 

@ResponseBody 를 사용
HTTP의 BODY에 문자 내용을 직접 반환
viewResolver 대신에 HttpMessageConverter 가 동작
기본 문자처리: String HttpMessageConverter
기본 객체처리: MappingJackson2HttpMessageConverter(JSON으로 바꿔주는 라이브러리)
```



> day5

```
회원 도메인과 리포지토리 만들기

리포지토리: 데이터베이스에 접근, 도메인 객체를 DB에 저장하고 관리
도메인: 비즈니스 도메인 객체, 예) 회원, 주문, 쿠폰 등등 주로 데이터베이스에 저장하고 관리됨



회원 리포지토리 테스트 케이스 작성
자바는 JUnit이라는 프레임워크로 테스트를 실행

테스트는 각각 독립적으로 실행. 테스트 순서에 의존관계가 있는 것은 좋은 테스트가 아니다.
```



> day6

```
회원 서비스 개발

optional 단축키 ctrl alt v
```


- [Interpretor](#Interpretor)
- [GIL](#GIL)
## 레파지토리 설명
코딩테스트에 대비하기 위해 백준, 프로그래머스의 문제를 풀고 풀이를 올리는 레파지토리입니다.

### 지금까지 푼 문제
- BFS/DFS
- DP
- 정렬
- 스택/큐
- 구현
- 그리디
- 브루트포스
- 문자열

### 앞으로 해야 할 것
- [ ] 한 번 푼 문제들 효율성에 유의하여 다시 풀기

### 다시 푼 문제
- [1541](https://github.com/gaeunpark924/CT-practice/blob/main/3%EC%9B%942%EC%A3%BC%EC%B0%A8_%EA%B7%B8%EB%A6%AC%EB%94%94/%EC%9E%83%EC%96%B4%EB%B2%84%EB%A6%B0%20%EA%B4%84%ED%98%B8_%EC%95%8C%EB%B0%94%EC%83%9D%20%EA%B0%95%ED%98%B8.py)

### 규칙(1/1~)
- 1일 1문제(1월 3주차 부터 2월 3주차까지 사이드 프로젝트에 참여하게 되어서 지키지 못했음)
- 하루에 두 가지 유형의 문제 1개씩 풀기(3월 3주차 부터 폴더에 유형 표시X) 

## 📌Interpretor
- 소스코드를 기계어로 변역하는 과정 없이 코드를 실행 시점에(코드 한 줄씩) 해석해 컴퓨터가 처리할 수 있도록 함. 간단히 작성 가능하고 메모리를 적게 필요로 하지만 실행속도가 느리다.
<p align="center">
  <img src="https://user-images.githubusercontent.com/51811995/156788504-d668d845-2141-4a6f-bb8d-c42818697a2f.png" width=400>
</p>

- 위 방식외에도 컴파일러로 중간 코드인 바이트코드로 만들고 이것을 다시 인터프리터 방식으로 해석해 수행하는 방법도 파이썬에서 종종 사용된다.
<p align="center">
  <img src="https://user-images.githubusercontent.com/51811995/156791134-73cd62df-785d-4c44-8f85-b153211ab778.png" width=600>
</p>

## 📌GIL
- Global Interpreter Lock, 전역 인터프리터 락
- 초창기 파이썬은 동시성과 메모리 관리를 쉽게하기 위해 thread-safe하게 설계되었다.
- 파이썬 객체로의 접근을 제한해 race condition을 막는 mutex를 GIL이라고 한다.
- 파이썬이 다른 코테 언어보다 느린 이유 중 하나가 GIL 으로 인해 멀티 코어임에도 하나의 스레드가 자원을 독점하는 형태로 실행되기 때문이라고 한다.

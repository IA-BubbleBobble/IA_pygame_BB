# Python - Pygame
HUFS ICE 인터넷응용 <br>
Team Project 4조<br>
이유진(팀장), 이채영, 신동현<br>
게임 설명, 시연영상 : https://youtu.be/FULAe9zhJ1A
## 1. 게임기획, 구조
### 모듈
  * Start.py : 게임의 전반적인 실행 구조(main loop, game class, 화면 구현 함수들)
  * setting.py : 설정값에 대한 정의(image, sound, ...)
  * sprites.py : 객체에 대한 정의

## 2. Game 설명
### Key 조작법
  * SPACE : PLAYER SHOOT BUBBLE
  * LEFT : PALYER MOVE LEFT
  * RIGHT : PLAYER MOVE RIGHT
  * UP : PLAYER JUMP
### Rule
>player가 monster에게 bubble을 쏜 후 bubble에 갇힌 몬스터를 죽이고, item을 얻어 score를 올리는 게임
## 3. 화면 구성
### 시작화면
> A 선택 --> start stage1 <br>
> B 선택 ---> start tutorial <br>
### Tutorial
> 시작시 간단한 Key 조작법을 화면에 띄워줌.<br>
> 몬스터 3마리를 죽이면 스테이지로 이동.<br>
### Stage1, Stage2, Stage3
> 랜덤으로 몬스터 생성, 버블에 갇힌 몬스터를 죽이면 item이 생성됨.<br>
> player가 item 을 touch함 ---> item별 점수 획득(item : random생성)<br>
> 모든 몬스터를 죽이면 다음 stage로 이동.<br>
### Ending page
#### 1) Happy Ending : 모든 Stage에서 몬스터를 죽였을 때
> score를 화면에 띄움.<br>
> A 선택 ---> restart ---> 처음화면으로 이동(현재 score은 High Score에 update됨.) <br>
> B 선택 ---> game 종료<br>
#### 2) Game Over : stage도중 목숨을 모두 잃어 player가 죽었을 때
> 현재 실행중인 화면을 멈춤.<br>
> 화면에 현재 Game Over 문구와 score를 띄워줌.<br>
> 7초뒤 시작화면으로 이동.<br>

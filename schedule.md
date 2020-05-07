# Bubble Bobble
## 최종
 * 이유진 : platform, player, bubbleMonster, 초반 merge작업, 코드관리, 영상편집
 * 이채영 : Monster, Item, start page, ending page, 코드관리
 * 신동현 : git, stage3 map, 영상 녹화, 코드관리
## 2020/04/29
### <역할분담>
  * 이유진 : 튜토리얼 맵 만들기 ---ok<br>
  * 이채영 : 시작화면 + 폰트다운받기 ---ok<br>  
  * 신동현 : 캐릭터 & 과일 이미지 캡쳐 ---ok<br><br>

### <일정>
#### ~5/1(금)
  * 코드이해
  * 각자 역할분담 맡은것(시작화면~튜토리얼화면, 튜토리얼실행, )
#### ~5/4(월)
  * 게임실행
  
영상)https://www.youtube.com/watch?v=wA89xLQknKA <br>

## 2020/05/01
### <역할분담>
  * 이유진 : 캐릭터 움직임 구현, 코드 합치기 ---ok<br>
  * 이채영 : 시작화면, 마지막 화면 ---ok<br>  
  * 신동현 : stage 2, 3 맵 만들기 ---ok<br><br>
  
### <일정>
#### ~5/2 (토)
 * 각자 역할분담 맡은거 완료
#### 5/4 (월)
 * 다음 진행할 것 회의
 
## 2020/05/04
 * 이유진 : 캐릭터 움직임 구현, bubble, bubbled monster구현 ---ok
 * 이채영 : 몬스터 생성, item생성, score, ending page ---ok
 * 신동현 : stage3맵 만들기, tutorial맵 수정 ---ok
 
## 2020/05/05
 * 이유진 : 코드 수정 ---ok
 * 이채영 : 코드 수정 ---ok
 * 신동현 : 발표 대본 작성, 영상녹화, 게임시연
<hr>

##### 20200501 update(youjin)
### ~~Start page~~
  * Logo ---ok
  * Tutorial button (how to를 tutorial로 변경!!)->튜토리얼 화면으로 넘어가기 ---ok
  * Game start button->stage1 화면으로 넘어가기 ---ok
### ~~Tutorial~~
  * key 조작법(글자로) ---ok
  * 몬스터 4마리만 출현 ---ok
  * 과일도 몇 개 추가 ---ok
  * 몬스터 4마리 다 죽이면 stage 1으로 이동 -> 게임시작 ---ok
### ~~Stage~~
  * Stage 시작시 -> Stage stage_num READY!! 뜨도록 ---ok
  * 목숨(3개, 몬스터와 부딪히면 목숨 줄어든다) ---ok
  * 과일을 먹으면 score가 올라간다 ---ok
  * 몬스터를 모두 죽이면 다음 stage로(stage별 몬스터 수 제한) ---ok
  * stage를 깼을 때 -> stage complete + score -> 일정시간 후 다음 stage화면으로 ---ok
  * stage 중간에 실패 했을 때 -> Ending page참고 ---ok
### ~~Ending page~~
#### ~~stage를 모두 성공 했을 때~~
  * happy end 이미지(100000pts는 score로 대체) ---ok
  * button) restart(start 화면으로), exit button(게임종료) ---ok
#### ~~stage 중간에 실패했을 때~~
  * stage화면 위에 Game over(빨간색 글씨) & score 띄우기 -> 일정시간 후 start page로 ---ok
  

### 필요한 image
  * Bubble(green) - 캐릭터가 버블쏘면
  * Bubble(red) - 캐릭터가 버블 쏜 후 터지기 직전(몬스터가 들어있지 않을 때)
  * Bubble(pop) - bubble 터질때(몬스터가 들어있는거&빨간풍선)
  * Monster(single) - blue, (red - bubble 갇혔다가 나오면)
  * Monster(group)
  * Monster(bubbled) - 캐릭터가 몬스터 향해서 버블쏘면 갇힘
  * Fruit

### letter (글씨체 적용 필요)
  * Score - fruit먹으면 fruit별 점수 상승(죽인 몬스터 갯수별 과일 다르게 나옴)
  * How to shot bubble - push space bar => tutorial에 적어주기
  * How to move (방향키) - left, right, up(jump)
  * Fruit(score) - 캐릭터가 먹으면 점수로 바뀜 (+score 올리기)
  * Stage number => Only appear on the stage page

### ~~구현해야할 것~~
  * Map(map:1050\*700, image:70\*70) ---ok
  * Bubble - shoot bubble ---ok (bubble 점점커지게)
  * Jump - character(막대기 위에서만 or 맨 밑으로 떨어짐) ---ok
  * Move - character(방향에 맞게 이미지 바꾸기)---ok, monster(막대기 위에서만), bubble(항상위로) ---ok
  * Bubbled 몬스터 움직임 ---ok
  * 버블에 갇힌 몬스터는 5초후 탈출 ---ok
  * 목숨 3개(몬스터와 부딪히면 줄어든다) ---ok


  

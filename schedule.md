# Bubble Bobble
## 2020/04/29
### <역할분담>
  * 이유진 : 튜토리얼 맵 만들기<br>
  * 이채영 : 시작화면 + 폰트다운받기<br>  
  * 신동현 : 캐릭터 & 과일 이미지 캡쳐<br><br>

### <일정>
#### ~5/1(금)
  * 코드이해
  * 각자 역할분담 맡은것(시작화면~튜토리얼화면, 튜토리얼실행, )
#### ~5/4(월)
  * 
  * 맵 만들기(stage3까지?) & 게임실행
  
영상)https://www.youtube.com/watch?v=wA89xLQknKA

<hr>

### 시작화면
  * Logo
  * Tutorial button
  * Game start button
  
### 마지막화면
  * Score
  * Restart button
  * Exit button
  
### 필요한 image
  * Bubble(green) - 캐릭터가 버블쏘면
  * Bubble(red) - 캐릭터가 버블 쏜 후 터지기 직전(몬스터가 들어있지 않을 때)
  * Bubble(pop) - bubble 터질때(몬스터가 들어있는거&빨간풍선)
  * Monster(single) - blue, red(bubble 갇혔다가 나오면)
  * Monster(group)
  * Monster(bubbled) - 캐릭터가 몬스터 향해서 버블쏘면 갇힘
  * Fruit

### letter (글씨체 적용 필요)
  * Score - fruit먹으면 fruit별 점수 상승, (몬스터 터뜨려도?)
  * How to shot bubble - ex)push space bar => tutorial only
  * How to move (방향키) - left, right, up, down
  * Fruit(score) - 캐릭터가 먹으면 점수로 바뀜 (+score 올리기)
  * Stage number => Only appear on the stage page

### 구현해야할 것
  * Map(map:1050\*700, image:70\*70)
  * Jump - character(막대기 위에서만 or 맨 밑으로 떨어짐)
  * Move - character(무작위로, ), monster(막대기 위에서만), bubble(항상위로)
  * Bubbled 몬스터 움직임

### 더 생각해야 할 것
  * Stage별 몇초
  * Stage통과기준
  * Bubble 쏘는 거리
  * 몬스터 bubble 탈출시간
  * 목숨 갯수
  *  

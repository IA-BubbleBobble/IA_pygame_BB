# Bubble Bobble
## 2020/04/29
### <역할분담>
  * 이유진 : 튜토리얼 맵 만들기<br>
  * 이채영 : 시작화면 + 폰트다운받기<br>  
  * 신동현 : 캐릭터 & 과일 이미지 캡쳐<br><br>

### <일정>
#### ~5/1(금)
  * 코드이해
  * 각자 역할분담 맡은것(시작화면~튜토리얼화면, 튜토리얼실행)
#### ~5/4(월)
  * 맵 만들기(stage3까지?) & 게임실행
  
영상)https://www.youtube.com/watch?v=wA89xLQknKA

<hr>

### 시작화면
  * high score
  * logo
  * tutorial button
  * game start button

### 필요한 image
  * bubble(green) - 캐릭터가 버블쏘면
  * bubble(red) - 캐릭터가 버블 쏜 후 터지기 직전(몬스터가 들어있지 않을 때)
  * bubble(pop) - bubble 터질때(몬스터가 들어있는거&빨간풍선)
  * monster(single)
  * monster(group)
  * monster(bubbled) - 캐릭터가 몬스터 향해서 버블쏘면 갇힘
  * fruite

### letter (글씨체 적용 필요)
  * score - fruit먹으면 fruit별 점수 상승, (몬스터 터뜨려도?)
  * how to shot bubble - ex)push space bar => tutorial only
  * how to move(w,a,s,d) - ex)w : up, a : left, s : down, d : right => tutorial only
  * fruite(score) - 캐릭터가 먹으면 점수로 바뀜 (+score 올리기)
  * stage number => stage only

### 구현해야할 것
  * map(map:1050\*700, image:70\*70)
  * jump - character(막대기 위에서만 or 맨 밑으로 떨어짐)
  * move - character(무작위로, ), monster(막대기 위에서만), bubble(항상위로)
  * bubbled 몬스터 움직임

### 더 생각해야 할 것
  * stage별 몇초
  * stage통과기준
  * bubble 쏘는 거리
  * 몬스터 bubble 탈출시간

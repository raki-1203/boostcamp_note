# [Week5] 이미지 분류 - 김태진 강사

### [Week5 피어세션 정리](https://github.com/raki-1203/Boostcamp_2st_Hot6/tree/main/Meetup-log/week5)

---
### 학습회고

> [Day20]

facenet 을 사용해 얼굴을 탐색하고 crop 을 진행하면서 png 파일이 저장될 때 

alpha 채널까지 가져서 4채널로 저장되는 이슈를 확인했다.

그래서 새로 저장할 때 확장자명을 jpg 로 모두 변경했다.

오늘 나온 special mission 에서 cutmix 관련 kaggle notebook 주소를 공유해주셨다. [참고](https://www.kaggle.com/debanga/cutmix-in-python)

여기 코드를 통해 mask 데이터에 cutmix 를 적용해보고 있다.

이미지의 크기가 모두 동일하면 좋을 것 같아서 facenet 이용해 crop 할 때 사이즈를 (224, 224) 로 바꿔서 다시 저장했다.

train 데이터에 대해서는 accuracy, f1_score, loss 모두 기존보다 반정도밖에 성능이 안나왔다.

그런데 validation 데이터에 대해서는 accuracy, f1_score, loss 모두 0.1정도 오른 느낌이다.

제출해봐야 겠다.

augmentation 방법들의 성능을 좀 비교해봐야겠다.

너무 막연하게 이거해보고 저거해본거 같다.

다시 처음부터 해봐야겠다.

Optimizer 중 Adam, AdamW, MadGrad 를 이용해 3 epochs 씩 돌려서 비교해 본 결과 MadGrad 가 같은 3 epochs 에서 

가장 빠르게 성능이 올라감을 발견!





피어세션을 통해서 역할 분담

1. 스케줄러 : 상준, 은우
    StepLR, CyclicLR, 그외 등등 스케쥴러 조절해보고 그 안에 파라미터 조절해보기 다양하게
2. 모델 : 재현, 희락
    ResNet18, 50, 101, EFFI, Darknet 등 다양하게 조절해보기
3. Loss : 상민, 별이
    F1_LOSS, CrossEntropy, WeightCrossEntropy, FocalLoss, LabelSmoothingLoss 사용하기
4. Mixcut : 재현, 상민
5. Stratified K-Fold : 희락, 은우
    구현해보고, K수 조절해보기
6. Mutually Exclusive : 상준, 별이


# [Week5] 이미지 분류 - 김태진 강사

### [[Day21] 8/25일자 Special Mission](https://github.com/raki-1203/boostcamp_note/tree/main/Week_5/Day_21)

- Darknet-53 모델 PyTorch 로 구현하기

### [[Day22] train data set 에서 잘 못 labeling 된 데이터 수정한 csv 파일 만들기](https://github.com/raki-1203/boostcamp_note/tree/main/Week_5/Day_22)

- LabelCorrection_raki.ipynb

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

이번주 부터는 팀별로 하나의 프로젝트로 관리하고 각자 역할 분담해서 테스트 하기로 함

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

> [Day_21]

상민캠퍼님의 점수가 가장 높아서 그 코드를 기준으로 테스트 하기로 함

[Hot6 깃허브](https://github.com/boostcampaitech2/image-classification-level1-06) 를 사용하여 코드 공유 후

상민님이 적용한 방법을 정리해 보았다.

1. facenet MTCNN 을 사용해 얼굴 인식 후 Crop
2. Train 시 Cutmix 적용
3. scheduler CyclicLR 사용
4. Data 를 age 와 gender 기준으로 먼저 Train set 과 Valid set 으로 Split 하고 Mask 착용까지 사용해서 18개의 Class로 분류
5. Resize [280, 210], ColorJitter(brightness=(0.2, 3)), ColorJitter(contrast=(0.2, 3)), 
ColorJitter(saturation=(0.2, 3)), ColorJitter(hue=(-0.3, 0.3)), RandomHorizontalFlip()
ToTensor(), Normalize() 적용
6. 모델 EfficientNet_B4 사용

이걸 기준으로 각자 맡은 역할 테스트 진행

나는 모델을 테스트 하는 역할을 맡았다.

ResNet18, ResNet50, ResNet101, Rexnet,
EfficientNet_B4, EfficientNet_B3_prune, EfficientNet_B2_prune, EfficientNet_B1_prune 등을 테스트 해봤고

이 중 EffientNet_B2_prune 의 F1_Score 기준 성능이 가장 좋게 나타났다.

> [Day_22]

parser.argument 의 인자를 nargs 를 받을 수 있는데 정규표현식을 사용해서 몇개를 받을 수 있을지 정할 수 있는 것 같다.

nargs='+' 하면 --resize param1 param2 param3 몇개의 인자든 받을 수 있게 된다.

오늘은 팀원들과 어제 각자 했던 테스트를 마치고 가장 성능이 좋았다고 여겨지는 criterion, model, scheduler 등을 모았다.

이 때 사용된 적용 기준은 cutmix 0.8, CyclicLR base_lr 1e-5, args_lr 1e-3, model efficientnet_b4, optimizer MADGRAD,
criterion focalloss 였다.

이렇게 모인 하이퍼파라미터에 Stratified K-Fold 를 사용해 5번의 학습을 진행해서 평균적인 valid_f1_score 를 구했다.

이렇게 구해진 5개의 모델의 test set 에 대한 예측값을 soft voting 해서 결과를 제출해보니 리더보드에서 상당히 높은 위치까지 도달했다.

각자 좋았던 부분을 git 을 통해 합치고 다시 각자 나눠서 테스트를 진행하니 확실히 혼자할 때보다 더 좋은 영향력을 얻는 듯 하다.


> [Day_23]
 
오늘은 대회 마지막 날이다.

성능은 최선을 다해 끌어 올린 것 같다.

오늘은 이렇게 저렇게 모델을 생성하고 결과가 잘 나온 애들 가지고 soft voting 을 적용하고 마지막 제출을 할 예정이다.

마지막에 age, gender, mask 를 따로 예측하는 모델을 팀원분이 같이 작업해주셨다.

이렇게 작업한 결과가 어떻게 나올지 궁금하다.

그리고 한가지 아쉬운 점은 너무 늦게 구현이 되서 age, gender, mask 에 전부 똑같은 input 이 들어갔다는 점이다.

우리조의 경우 facenet 을 사용해서 얼굴을 crop 하고 이미지를 수정해서 input 으로 사용했는데

age, gender 의 경우 옷 부분이 필요할 수도 있겠다는 생각이 들었다.

시간이 더 있었더라면 데이터를 나눠서 학습을 시켜봤으면 결과가 어떻게 나왔을지 실험을 해보고 싶다.

그리고 하나더 아쉬운점이 있다면 autoML 을 사용해보지 못했다는 것이다.

다음 P-Stage 에서나 다른 기회가 생겼을 때 무조건 autoML 을 사용해봐야겠다.

age, gender, mask 를 분리해서 예측한다고 하면 외부이미지도 추가해서 사용했을수도 있을 것 같은데 아쉽다.

Tensorboard event 파일을 dataframe 으로 바꿔주는 코드를 알아냈다.

[jupyter 파일](https://github.com/raki-1203/boostcamp_note/blob/main/Week_5/Day_23/Tensorboard_Visualization.ipynb) 로 정리를 해놨다. 

wrap-up report 또는 나중에 결과를 시각화할 때 사용하면 좋을 것 같다.
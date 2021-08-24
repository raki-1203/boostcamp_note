# [Week4] 이미지 분류 - 김태진 강사 & [Special] Data Viz - 안수빈 강사

### [[Day15] 이미지 분류 1 ~ 2강 & 시각화 4-1 ~ 4-2강](https://github.com/raki-1203/boostcamp_note/tree/main/Week_4/Day_15)

- Competition with AI Stages!
- Image Classification & EDA
- Seaborn 소개
- Seaborn 기초
- 마스크 착용 상태 분류 대회 - EDA & Train

### [[Day16] 이미지 분류 3 ~ 4강 & 시각화 4-3강](https://github.com/raki-1203/boostcamp_note/tree/main/Week_4/Day_16)

- Dataset
- Data Generation
- Seaborn 심화
- 마스크 착용 상태 분류 대회 - EDA & Dataset & DataLoader & Train

### [Week4 피어세션 정리](https://github.com/raki-1203/Boostcamp_2st_Hot6/tree/main/Meetup-log/week4)

---
### 학습회고

> [Day15]

기본적인 EDA를 진행해보고자 하는데 Train Data Image & Test Data Image 시각화 해보고

train_info 데이터를 이용해서 라벨링을 진행했고

Pretrained ResNet Model 을 사용해 학습을 진행하고 있다.

학습진행이 잘 됐으면 좋겠다.

> [Day16]

EDA 샘플 코드가 주어졌다.

t-SNE, PCA 분석 등 여러가지를 하던데 저렇게 해서 뭘 얻는지 잘 모르겠다.

생각지도 못했던 이미지에서 라벨링이 잘 못된 데이터가 있는걸 확인했고

일일히 모든 데이터를 확인해봤다.

실제로 남자인데 여자로 라벨링 된 데이터 또는 실제 여자인데 남자로 라벨링 된 데이터

사람의 눈으로 봐도 확인이 어려운 것도 있었다. 임의로 바꿨는데 어떤 역할을 할지 모르겠다.

ResNet 보다 EfficientNet 의 성능이 더 좋다는 얘기를 들었다.

구글링을 통해 EfficientNet-B4 모델을 사용해서 테스트를 진행해 볼 예정이다.

정답 class 간의 불균형을 해결할 방법도 찾아야 할텐데

SMOTE 를 사용할지 생각 해봐야 겠다.

오늘은 데이터 확인하는데 굉장히 많은 시간이 흐른 것 같다.

데이터는 꽤 수정했다고 생각하고 이제 Dataset, DataLoader, Model 관련해서 더 집중해봐야 겠다.
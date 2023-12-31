# 운전자 상태인식

# 1.  **개 요**

## **[ 과제 선정의 배경 ]**

1. 사회적 관심의 증대

: 최근 사고 통계를 보면, 졸음 운전에 의한 교통사고가 늘어나는 추세를 보이고 있습니다. 이로 인한 사회적 손실과 인명 피해가 크게 발생하고 있어, 졸음 운전 예방은 긴급한 사회적 문제로 부상하고 있습니다.

2. 운전자의 상태 인식의 중요성

: 운전자의 상태 인식은 그 자체로 운전의 안전성을 크게 향상시킬 수 있는 핵심 요소입니다. 특히 긴 거리 운전이나 야간 운전 중 졸음 또는 다른 건강 이슈가 발생할 경우, 즉각적으로 파악하고 조치를 취할 수 있도록 하는 것은 교통사고 예방의 중요한 관점입니다.

3. 기술의 발전과 적용

: 최근에는 다양한 센서 기술 및 인공지능이 발전함에 따라 운전자의 상태를 실시간으로 모니터링하고 분석할 수 있는 기술이 출현하였습니다. 이러한 기술의 적용을 통해 졸음운전 예방 솔루션을 효과적으로 구현할 수 있다고 판단하였습니다.

## **[ 과제 수행 목적 ]**

안전하게 운전을 유도하면서 교통 흐름을 원활하게 하려면 운전자의 상태 파악이 중요하며, 이를 통해 다른 차량과의 안전한 거리 유지, 적절한 속도 조절 등이 가능해집니다. 졸음 운전 예방은 개인의 안전을 지키는 것 뿐만 아니라, 원활한 도로교통 환경 조성에도 큰 역할을 합니다.

운전자의 안전뿐만 아니라 사회 전체의 안전 문화 조성과 교통 환경 개선에 기여할 수 있으며, 최신 기술의 발전을 반영하여 효과적인 솔루션을 제안하고자 합니다.

# 2. **내 용**

## [ 졸음운전 예방 솔루션 프로세스 ]

1. 딥러닝 이미지 처리를 통한 운전자 상태 인식
- 데이터 수집: 운전자의 상태가 나타난 측면 이미지 데이터를 활용하여 학습합니다.
- 데이터 전처리: 모델 성능을 최적화하기 위해 이미지의 명암, 대비, 밝기 등을 조정하고, 불필요한 배경은 제거합니다.
- 딥러닝 모델 적용: 전이 학습된 CNN 기반의 ResNet-50 딥러닝 모델을 이용하여 운전자의 상태를 인식하고 분류합니다.
2. 딥러닝 모델 학습과 최적화
- 손실 함수: 교차 엔트로피 손실(Cross-Entropy Loss)를 사용하여 실제 클래스 레이블과 모델의 예측 확률 분포 간의 차이를 측정합니다.
- 최적화 알고리즘: SGD(Stochastic Gradient Descent)를 사용합니다. 모델 학습은 총 5개 에포크 동안 진행됩니다.
- 학습률 스케줄링: ReduceLROnPlateau 스케줄러를 적용하여, 정확도의 변화를 기준으로 학습률을 조절합니다. 5번째 에포크에서 개선률이 떨어지면 학습을 종료합니다.
3. 비정상 운전 상태 판별 및 졸음 운전 여부 확인
- 상태 분류: 딥러닝 모델의 출력값을 바탕으로 운전자의 상태를 정상, 비정상(전화 통화, 졸음, 음식 섭취) 등의 상태로 분류합니다.
- 졸음 인지 알고리즘: 운전자의 눈의 움직임, 눈 감김 시간 등의 데이터를 분석하여 졸음 여부를 확인합니다. 연속적으로 눈을 감고 있는 시간이 특정 임계값을 초과할 경우 졸음 상태로 판별합니다.

## [ 대책 솔루션 마련 ]

 - 졸음 운전 예방 솔루션 제공 및 교통 사고 예방

- 경고 알림: 졸음 상태로 판별될 경우, 진동으로 운전자에게 즉시 알립니다.
- 자동 차량 제어: 상황에 따라 자동차의 속도를 줄이거나, 비상등을 켜서 다른 차량에 위험을 알릴 수 있습니다.
- 정지 권유 시스템: 지속적으로 졸음 상태가 감지되면, 운전자에게 가장 가까운 휴게소나 주차장 위치 정보를 제공하여 안전하게 차량을 정지하도록 권유합니다.

## 3.  **기대 효과 및 실적 현황**

**졸음 운전 탐지 및 경고**: Facemesh 기술을 활용하여 운전자의 눈 깜빡임 빈도, 눈 깜빡임 각도 등을 모니터링하여 졸음 운전의 초기 징후를 탐지할 수 있습니다. 시스템은 운전자가 피로하거나 졸음 상태에 접어들었을 때 경고음이나 진동 등의 방법으로 운전자에게 주의를 줄 수 있습니다.

**운전자 상태 분석**: 본 졸음운전 예방 솔루션에 사용되는 Facemesh 기술은 랜드마크 포인트 데이터를 활용하여 운전자의 얼굴 표정과 표정 변화를 분석할 수 있습니다. 이를 통해 운전자의 기분, 피로도, 분노 등의 감정 상태를 파악하고, 운전 환경을 조절하거나 필요한 조치를 취할 수 있습니다. 또한 운전자의 운전 습관을 모니터링하고 분석할 수 있기 때문에 과도한 고개 돌리기, 자주 눈 깜빡임 없이 오랜 시간 눈을 뜨고 있음 등의 나쁜 습관을 탐지하여 개선할 수 있는 기회를 제공하고 모니터링을 바탕으로 축적된 데이터는 운전자의 운전 습관 및 상태에 대한 귀중한 정보를 제공합니다. 이 데이터를 분석하여 운전자들의 행동 패턴을 파악하고 교통 안전을 개선하는데 활용할 수 있습니다.

**보안 강화**: 운전자의 얼굴을 인식하는 기술을 활용하여 운전자 식별을 강화할 수 있습니다. 이를 통해 다른 사람이 운전 중에 대신 운전을 하려는 시도나, 운전자를 모방하여 사기성 운전 등을 방지할 수 있습니다.

**산업 발전**: 운전자 행동 다중 클래스 분류 네트워크의 개발과 활용은 차량 안전 기술 분야에서의 혁신을 가능하게 합니다. 이는 자동차 제조사 및 관련 산업의 기술적 경쟁력을 높이며, 이를 바탕으로 새로운 비즈니스 모델이나 서비스를 창출하는 기회를 제공합니다. 예를 들어, 이 기술을 활용하여 차량 내부에서의 운전자 상태를 실시간으로 체크하는 안전 서비스를 제공하는 스타트업이 생길 수 있습니다. 또한, 기존의 자동차 제조사들은 이 기술을 활용하여 차량의 안전 기능을 강화함으로써 소비자들에게 더 큰 가치를 제공할 수 있게 됩니다.

**논문 및 연구 활성화**: 해당 논문이 학계에서 인지되고 인용됨으로써, 다른 연구자들에게 이 주제에 대한 추가 연구를 진행하게 만드는 계기가 됩니다. 특히, 운전자의 상태를 판단하는 기술에 대한 연구가 활성화되어 더욱 정확하고 다양한 행동 분류 기술의 개발이 가능해질 것입니다. 이는 궁극적으로 안전한 운전 환경 구축에 기여하며, 이에 대한 관심과 연구가 계속 확산되는 효과를 가져올 것입니다.

**기술의 확장 및 다양한 활용**: 초기 목적인 졸음운전 예방 뿐만 아니라, 다른 비정상적인 운전 행동을 감지하고 운전자에게 이를 알려주는 서비스로 확장될 수 있습니다. 이를 통해 운전자는 자신의 상태를 실시간으로 파악하고 이에 따른 조치를 취할 수 있게 됩니다. 예를 들어, 운전자의 스트레스 수준이나 의식 상태 등을 파악하여 운전 중 필요한 휴식 시간을 알려주거나, 적절한 음악을 선택하여 스트레스를 해소하는 등 다양한 운전자 편의 서비스를 제공할 수 있습니다. 이러한 기술의 확장은 운전 경험의 질을 향상시키며, 교통사고를 줄이는 데에도 크게 기여할 것입니다.
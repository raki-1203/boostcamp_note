# Ubuntu 18.04 konlpy & mecab install

> AI stage server 를 기준으로 작성합니다.

- Ubuntu 18.04

## 1. JDK 설치

apt를 사용하여 jdk와 python-dev, python3-dev를 설치합니다.

jdk는 무난하게 1.8 버전을 설치하겠습니다.

`> apt-get install openjdk-8-jdk python-dev python3-dev`

설치가 끝났으면 java 버전을 확인하여 jdk가 정상적으로 설치되었는지 테스트해봅니다.

```
> java -version
openjdk version "1.8.0_292"
OpenJDK Runtime Environment (build 1.8.0_292-8u292-b10-0ubuntu1~18.04-b10)
OpenJDK 64-Bit Server VM (build 25.292-b10, mixed mode)
```

## 2. KoNLPy 설치

`> pip install konlpy jpype1-py3`

설치가 완료되었다면 파이썬에서 konlpy 패키지를 사용할 수 있는지 확인해봅시다.

```
> python
Python 3.8.5 (default, Sep  4 2020, 07:30:14)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.

> from konlpy.tag import Okt
> okt = Okt()
> okt.pos("안녕 라키야")
[('안녕', 'Noun'), ('라', 'Josa'), ('키', 'Noun'), ('야', 'Josa')]
```

pos 함수에 문장을 넣었을 때 잘 동작하는 모습을 볼 수 있습니다.

## 3. Mecab 설치

konlpy를 설치했다고 해서 mecab을 바로 사용할 수 없습니다.

```
> python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

> from konlpy.tag import Mecab
> m = Mecab()
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/konlpy/tag/_mecab.py", line 107, in __init__
    self.tagger = Tagger('-d %s' % dicpath)
NameError: name 'Tagger' is not defined
```

일단 konlpy 공식문서에는 mecab을 사용하고 싶으면 아래 명령을 실행하라고 나와있습니다.

`> bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)`

여전히 NameError: name 'Tagger' is not defined 를 뱉습니다.

## 4. libmecab.so.2 링크 생성

이제부터 mecab을 손수 설치해봅니다.

위 명령을 실행했다면 /tmp 경로에 mecab과 관련된 파일들이 위치하게 됩니다.

만약 /tmp 경로에 mecab-0.996-ko-0.9.2와 mecab-ko-dic-2.1.1-20180720이 없다면 
/tmp 경로에서 아래 명령을 따라 다운받아줍니다.

```
> curl -LO https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
> tar zxfv mecab-0.996-ko-0.9.2.tar.gz

> curl -LO https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
> tar -zxvf mecab-ko-dic-2.1.1-20180720.tar.gz
```

curl command not found 시 아래 명령어 실행해줍니다.

`> apt install curl` 

다음은 mecab-ko-dic-2.1.1-20180720 경로로 이동하여 아래 명령을 실행합니다.

```
> cd /tmp/mecab-ko-dic-2.1.1-20180720
> ldconfig
> ldconfig -p | grep /usr/local/lib
libmecab.so.2 (libc6,x86-64) => /usr/local/lib/libmecab.so.2
libmecab.so (libc6,x86-64) => /usr/local/lib/libmecab.so
```
저는 마지막 명령어 쳤을 때 아무것도 나오지 않아서 뒤에서 에러가 났는데요

계속 진행하시다 보면 저부분도 해결하는 방법이 나옵니다.

## 5. mecab-ko 설치

우선 mecab-0.996-ko-0.9.2 경로로 이동하여 아래 명령을 수행합니다.

```
> cd /tmp/mecab-0.996-ko-0.9.2
> ./configure
> make
> make check
> sudo make install
```

이 때, make 명령어 실행이 안되는 경우 아래 명령어 실행하면 돌아

`apt-get install build-essential`

## 6. mecab-ko-dic 설치

mecab-ko-dic-2.1.1-20180720 경로로 이동하여 아래 명령을 수행합니다.

```
> cd /tmp/mecab-ko-dic-2.1.1-20180720
> ./autogen.sh
> ./configure
> make
> sudo make install
```

만약 이 명령을 수행하는 도중 작업이 진행되지 않고 에러가 나온다면!!

libmecab.so.2가 있는지 확인하기

```
> ls /usr/local/lib/libmecab.so.2
/usr/local/lib/libmecab.so.2
```

ld.so.conf두 /usr/local/lib이상의 추가

`> vi /etc/ld.so.conf`

수정 된 파일

```
include ld.so.conf.d/*.conf
/usr/local/lib
```

ld.so.conf 설정을 반영

`ldconfig`

마지막으로 mecab-python 을 설치해주자

`> pip install mecab-python3`

```
> python
Python 3.8.5 (default, Sep  4 2020, 07:30:14)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.

> from konlpy.tag import Mecab
> m = Mecab()
> m.pos('일등이 아니어도 괜찮아')
[('일등', 'NNG'), ('이', 'JKC'), ('아니', 'VCN'), ('어도', 'EC'), ('괜찮', 'VA'), ('아', 'EC')]
```

이러면 끝!

잘쓰세요!

reference https://yuddomack.tistory.com/entry/%EC%B2%98%EC%9D%8C%EB%B6%80%ED%84%B0-%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-EC2-konlpy-mecab-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0ubuntu

여기를 참고해서 작성했습니다.

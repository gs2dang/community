# 게시판 만들기

배운 내용을 복습하기 위해서 게시판을 만들었습니다. 학원에

<br>

## 설치

```
pip install -r requirements/base.tx
```

<br>

## secrets

Root(bulletin_board 폴더) 밑에 `.secrets` 폴더를 만들고 각각의 파일을 설정합니다.

`base.json`

```json
{
   "SECRET_KEY" : "<SECRET_KEY>"
}
```

`dev.json`

```
{
	"ALLOWED_HOSTS": []
}
```

`production.json`

```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "<DB_ENGINE>",
      "HOST": "<HOST>",
      "NAME": "<DB_NAME>",
      "USER": "<DB_USER>",
      "PASSWORD": "<DB_PASSWORD>",
      "PORT": PORT
    }
  },
  "AWS_ACCESS_KEY_ID":"<ACCESS_KEY>",
  "AWS_SECRET_ACCESS_KEY":"<ACCESS_SECRET>",
  "AWS_STORAGE_BUCKET_NAME":"<BUCKETNAME>",
  "ALLOWED_HOSTS": []
}
```

<br>

## Model

![](/home/feynman/Pictures/bulletin_board_db.png)

<br>

## 기능

- 유저
  - 회원가입
  - 로그인: 소셜 로그인은 로컬에서 되도록 구현
- 포스트
  - 작성
  - 수정
  - 삭제
  - 좋아요
- 댓글
  - 작성
  - 수성
  - 삭제
- 그 외
  - 조건에 따른 글 검색
  - 페이지네이션
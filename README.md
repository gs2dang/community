# 게시판 만들기

인스타그램으로 Django를 배웠지만 MTV 개념이나 각 Model, View, Form 구현하는 것이 너무 어려웠습니다. 



## Secrets

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
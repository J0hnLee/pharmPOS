# pharmPOS

...
pip install python-dotenv (for using the .flaskenv )

###react-flask-app 
是前端專案

### api 
為flask 框架下的後端
測試版
1. api.py 可以回傳時間

```localhost:5000/time```

2. restfulAPI.py 可做資料庫的CRUD (用postman測)
```localhost:5000/pts```

### init_mysql(未完成)
第一步
```python setupData.py```

自動部署ｍySQL 資料庫 and add dummy data to mySQL

## setup the environment

pip install -r requirements.txt 

## Deployment backend
```cd api```

```python restfulAPI.py```
```flask run```

## Deployment frontend
```cd react-complete-guide```

```npm start```



範例:
同時啟動frontend and backend
每重新整理一次前端
會重新去抓一次後端的資料(時間)

參考:

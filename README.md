# pharmPOS

...
pip install python-dotenv (for using the .flaskenv )

###frentend
是前端專案

### backend
為flask 框架下的後端
測試版
1. api.py 可以回傳時間

```localhost:5000/time```

2. restfulAPI.py 可做資料庫的CRUD (用postman測)
```localhost:5000/pts```

### init_mysql(未完成)
第一步 in backend
```python  manger.py db init```
這指令會依據Model的結構產生初始化設定並放置於migrations資料夾內。

```python  manger.py db --migrate```
透過這指令可以產生資料庫內容，而不用去寫SQL語法建立Table以及設定DB Schema。

```python  manger.py db upgrade```
當Model的結構有異動時要自動更新資料庫的話首先先執行此指令，接下來再執行flask db migrate，如此即可更新資料庫以符合Model資料結構。



## setup the environment

pip install -r requirements.txt 

## start backend

```python manager.py run```

## Deployment frontend
```cd react-complete-guide```

```npm start```



範例:
同時啟動frontend and backend
每重新整理一次前端
會重新去抓一次後端的資料(時間)

參考:

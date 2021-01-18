# 社團管理系統

[簡報影片](https://youtu.be/-KhV7QNqIF4)

## Usage

> 前端 templates 已有打包，如需自行打包請見 [此連結](frontend/README.md)

安裝 pipenv
```
pip install pipenv
```

進入 `backend` 目錄
```
cd backend
```

使用 pipenv 建立虛擬環境
```
pipenv --python 3.7
```

Install Dependence
```
pipenv install
```

進入 pipenv 環境
```
pipenv shell
```

設定 `FLASK_APP` 環境變數
```
FLASK_APP=run
```

執行
```
flask run
```

### DB

修改 `backend/config.py` 中的 `SQLALCHEMY_DATABASE_URI`

進入 `backend` 目錄
```
cd backend
```

使用 flask-migrate + flask cli 遷移資料庫
```
flask db upgrade
```

建立初始化資料
```
flask data init
```

如需建立測試資料
```
flask data test
```
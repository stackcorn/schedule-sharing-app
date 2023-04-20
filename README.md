# schedule-sharing-app
 
Djangoで作った、予定共有アプリです。
 
部屋名とパスワードを共有した人同士でスケジュールを共有できます。
 
# DEMO
 
![schedule_list](https://user-images.githubusercontent.com/86920995/233412009-1e2255f9-e77c-47d9-9c12-73edf52e6c9f.jpeg)
 
# Features
 
* スケジュールの日程が昇順に並ぶようになってます。
* スケジュール作成時に日付をカレンダーから入力できるようにしました。
 
# Requirement
 
* dj-database-url==1.3.0
* Django==4.2
* django-widget-tweaks==1.4.12
* gunicorn==20.1.0
* python-dotenv==1.0.0
* whitenoise==6.4.0
 
# Installation
 
```bash
pip install --upgrade pip
 
pip install -r requirements.txt
```
 
# Usage
 
1. 部屋名とパスワードを決める
2. サインアップ画面で部屋名とパスワードを入力しSubmit
3. サインイン画面で部屋名とパスワードを入力しSubmit
4. スケジュールを書き込む！
5. スケジュールをシェアしたい人と、部屋名とパスワードを共有！
 
# Note
 
render.com(https://render.com/) を使用し、デプロイしました。
 
アプリ: https://schedule-sharing-app.onrender.com
 
# Author
 
Bigmcqueen(https://github.com/BigMcQueen/)
 
# License
 
© Bigmcqueen(https://github.com/BigMcQueen/)
 

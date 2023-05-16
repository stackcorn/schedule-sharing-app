# schedule-sharing-app
 
Djangoで作った、予定共有アプリです。
 
部屋名とパスワードを共有した人同士でスケジュールを共有できます。
 
# DEMO
 
![schedule_list](https://user-images.githubusercontent.com/86920995/233412009-1e2255f9-e77c-47d9-9c12-73edf52e6c9f.jpeg)
 
# Features
 
* スケジュールの日程が昇順に並ぶようになってます。
* スケジュール作成時に日付をカレンダーから入力できるようにしました。
* Docker, docker-composeで環境構築をしました。

# DEV
* Macbook Air(M1, 2020)
* Docker, docker-compose
* Visual Studio Code
 
# Requirement
 
Python=3.9.16
 
* asgiref==3.6.0
* dj-database-url==1.3.0
* Django==4.2
* django-widgets-improved==1.5.0
* gunicorn==20.1.0
* psycopg2==2.9.6
* python-dotenv==1.0.0
* sqlparse==0.4.3
* typing_extensions==4.5.0
* whitenoise==6.4.0
　 
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
 

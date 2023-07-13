# Schedule-Sharing-App

## Introduction

このアプリケーションはDjangoで作成された予定共有アプリケーションです。部屋名とパスワードを共有することで、特定の人々と予定を共有することが可能になります。

## Features

- スケジュールの日程が昇順に表示
- スケジュール作成時にカレンダーから日付の入力可能
- Dockerとdocker-composeを使用した環境構築

## Demo

![schedule_list](https://user-images.githubusercontent.com/86920995/233412009-1e2255f9-e77c-47d9-9c12-73edf52e6c9f.jpeg)

## Technologies Used

- Python 3.9.16
- Django 4.2.3
- Docker / Docker Compose

## Installation

```shell:terminal
# プロジェクトをクローンします。
$ git clone https://github.com/BigMcQueen/schedule-sharing-app.git

# プロジェクトのディレクトリに移動します。
$ cd schudule-sharing-app

# docker compose でビルドします。
$ docker compose up -d --build
```

localhost:8000にアクセスすると、トップ画面が表示されます。

## Usage

1. 部屋名とパスワードを決定します。
2. サインアップ画面で部屋名とパスワードを入力し、Submitをクリックします。
3. サインイン画面で部屋名とパスワードを入力し、Submitをクリックします。
4. スケジュールを作成します。
5. スケジュールを共有したい人と部屋名とパスワードを共有します。

## License

© Bigmcqueen

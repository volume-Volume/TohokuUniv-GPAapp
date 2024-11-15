# EIGOイスト
自分の好きなモノをもとに楽しく英語スピーキングを学習できるアプリ、 **EIGOイスト** 
<img width="830" alt="Screenshot 2024-10-28 at 5 46 54" src="https://github.com/user-attachments/assets/3ece4beb-f113-4fb5-9f93-c6283c3a0e2b">

## デモ動画
[こちら](https://youtu.be/5FQa3x18Aqk)からデモ動画をご覧いただけます。

## 製品概要
### 背景(製品開発のきっかけ、課題等）
英語の学習習慣、特にスピーキングの学習習慣がまったく身につかない学生生活が義務教育時代から続いています。また、「英語勉強は楽しくないモノ」という認識をしている人が世の中にも多いのではと考えています。
これによって義務教育によって強制的に学習させられるリーディングばかり伸びていくのに対し、スピーキングは強制されないし楽しくもないから勉強しなくなるのでできるようにならないという問題が生まれます。将来的に英語を「自分を表現するツール」として使うためにはスピーキングが最も重要なのにも関わらず、です。
この問題を解決するために、まずは楽しく継続して学習できるスピーキングアプリを開発しようと考えました。

私達は「自分の好きなことで勉強するのは楽しい」という考えをもとにスピーキングアプリの開発を行ってきました。実際、私達が熱を持ってここまで開発を行ってこれたのも、自分たちがプログラミングやアプリ開発が好きだからです。そのため、私達は従来の英語アプリのようなビジネス・日常会話・道案内などの型にはまった退屈なテーマでスピーキングを学ぶのではなく、むしろ自分のエゴに従い、自分の趣味の延長にある好きなコンテンツでスピーキング練習できるアプリ「EIGOイスト」を開発しました。

#### 課題
以上の背景を踏まえて、下記の3つの課題を分析し、アプリの「特長」を開発していきました。
1. 既存アプリはテーマに親近感、面白みを感じないので楽しくない
2. スピーキングの学習にそもそもモチベーションがない
3. 既存アプリの題材は自分の生活や趣味に関わらないので、自分の体験をスピーチに入れにくい。このせいでユーザーのスピーチの表現力が向上しない

### 対象ユーザー
* 日本人
* 全年齢の英語学習者
* 特に、英語学習を継続していきたい多趣味な人
* Youtube、ニュースを見るのが趣味だけど勉強しないことに罪悪感を感じてしまっている英語学習者
　

より多くの英語学習者がこのアプリの対象ユーザーになってもらうために、後の説明の通りたくさんの機能を作りました。機能ごとの対象ユーザーは製品説明に書いてあります。


### 特長

#### 1.自分に大きく関わる大好きなテーマや動画、気になるニュースでスピーキング練習ができます
このアプリには、自分の好きなキーワードをもとにテーマを生成する「好きなテーマ」機能、自分の好きなYoutubeの動画を見て学習できる「Youtube」機能、自分の好きなニュースを検索して学習できる「news」機能、自分の好きな画像を入力してそれをもとにテーマを生成する「画像テーマ」機能があります。
自分の生活や趣味志向を素材として生成されたテーマを話す楽しさ、スピーチのテーマ、シチュエーションを自分でカスタマイズする楽しさを提供します。

#### 2. スピーチの内容面での評価にもこだわっています
「マラソンモード」という機能の中で過去のスコア(=自分の努力)の可視化、過去の平均スコアと直近のこの機能による学習の継続率によって金、銀、銅、青のランクが決まるシステムの導入、ランクやスコアが向上した喜びを友達と分かち合うSNS共有の実装を行っています。これにより競技性やランクが上がること、日々の頑張りを共有することによるモチベーションや楽しさを提供します。

#### 3. スピーチに個人の体験や経験を入れる力が身につきます
自分の生活や趣味をスピーチの題材とすることで、ユーザーはスピーチにより詳細な具体例や経験を含みやすくなります。また、スピーチの内容評価部分で構成や表現の多様性やスピーチの独自性を重視することでユーザーが具体例や経験の入ったスピーチをすることをプラスに評価します。これにより、ユーザーはより具体性の高いスピーチを構成を意識して行う力が身につき、表現力が向上します。

### 製品説明（具体的な製品の説明）
取り組みやすいたくさんの機能を実装したので、自分にあった形で、楽しく効果的にスピーキングを勉強できます。 このアプリでは「好きなテーマ」モード、「Youtube」モード、「News」モード、「画像テーマ」モードの4つのスピーチテーマ生成コンテンツを提供しています。
それぞれのモードでは、「興味のあるモノ」(好きなテーマ、Youtube動画の内容、ニュース記事の内容、好きな画像)がテーマ生成のもととなっていて、テーマ生成ボタンを押すと、ChatGPTが 「興味のあるモノ」 に基づいた複数の多彩なスピーチテーマを提案します。 その後、気になるスピーチテーマを選び、マイクボタンを押してそのテーマについて話してみます。 最後に、その音声を提出すると、ChatGPTが内容や流暢さを分析し、改善点が丁寧にフィードバックされます！

また、これら4つの機能に競技性を持たせたモードとして「マラソンモード」を開発しました。

各モードごとの具体的な動作の流れは、以下で説明します。

### 1.好きなテーマ
#### 1.1. 好きなワードを入力します。
#### 1.2. 好きなワードに対してテーマ生成をして、複数のスピーチテーマから最も話したいテーマを選びます。テーマ横の電球ボタンを押すことでヒントを生成してくれます。

<img src="https://github.com/user-attachments/assets/b3f776f9-d5d7-408c-b0fc-e848931c4275" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/3bb2b184-389e-487e-b3c2-82257929f828" alt="画像説明" width="230"/>

#### 1.3. マイクボタンを押して選択した「最も話したいテーマ」に関するスピーチを行い、音声を提出すると、評価が得られる。評価では、WordPerMinute、発音と流暢さ、話した内容の独自性、発音のチェック、模範解答等を分析＆採点しています。

<img src="https://github.com/user-attachments/assets/8d75c466-6bec-49cd-84cc-e29e78d89047" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/5b03ef37-aebe-41ab-b312-d3e7de2280b8" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/0479eefa-f35b-4a74-9c00-ab80f0cac788" alt="画像説明" width="230"/>

#### ＜対象ユーザー＞
* **自分の好きなことならたくさん話せる人**
* **動画、ニュース等を介さないシンプルなスピーキング練習をしたい人**




### 2.Youtube
#### 2.1. 見たい動画の検索ワードを入力し検索し、複数の動画が提案されるので最も見たい動画を選択する。(ダブルタップすることで動画をアプリ内で簡単に見られる。)

<img src="https://github.com/user-attachments/assets/81c9fe91-4adb-4225-984f-656bcf948020" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/ea5167c5-faa9-4fe2-ae16-2b794ed63065" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/aca79e83-28d6-4bc5-ba25-70d4864869cb" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/5f36ae9d-5ef8-44c1-9a55-848d57167b6e" alt="画像説明" width="230"/>

#### 2.2. マイクボタンを押して選択した動画に関するスピーチを行い、音声を提出すると、評価が得られる。

<img src="https://github.com/user-attachments/assets/9cf1ea57-9f77-4b01-95f3-16cbb6175b07" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/05405af3-3a2d-4989-be5d-b57ade50f3c7" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/07f17f77-48e1-4135-909a-0af44ee2f203" alt="画像説明" width="230"/>

#### ＜対象ユーザー＞
* **スピーキング学習をしながら、エンタメも楽しみたいYoutube視聴者**
* **日常の娯楽の延長として英語学習をしたい人**



### 3.News
#### 3.1. 興味のあるワードを入力し、検索ワードにヒットする最近の人気なニュースを検索します。

<img src="https://github.com/user-attachments/assets/d6e468d2-d1db-4bcc-9681-171302764e69" alt="画像説明" width="230"/>

#### 3.2. 提案されたニュースを一つ選択することで、スピーチテーマを生成します(選択したニュースの左下を押すことで、ニュースをSafari等のブラウザで見れます)。gooラボAPIのキーワード抽出機能を使用することで、記事のキーワードボタンを押すことでスピーチに使える重要キーワードをニュース記事から抽出してくれます。テーマ横の電球ボタンを押すことでヒントを生成してくれます。

<img src="https://github.com/user-attachments/assets/0dc02c2f-d70c-4dde-b32b-1c4673924b2e" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/228615dc-638e-43f1-a6f0-9f10f3528708" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/6e2d1d4d-0816-462d-8538-803d66f9f0e5" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/52e7273d-fdf1-4297-8ed8-92bcb8595d03" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/28bfe4cd-46c3-4271-bf95-957fe2a36049" alt="画像説明" width="230"/>

#### 3.3. 3.2でテーマを選択した後に、マイクボタンを押して選択したテーマに関するスピーチを行い、音声を提出すると、評価が得られる。この評価は、ChatGPTに記事の内容の全文を送ることによって精度の高い評価を実現しています。

<img src="https://github.com/user-attachments/assets/b5fe5759-92f7-401c-b050-e4f201a41b6d" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/53e84d8c-43b3-4e9a-b44b-2d0bd50851b8" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/8e5d2b8f-0cb5-4841-ba28-56ec45dfff6f" alt="画像説明" width="230"/>

#### <対象ユーザー>
* **時事や経済など、最新のニュース素材を題材として勉強したい人**
* **社会情勢も英語学習と一緒に知っておきたい社会人**
* **趣味が多いわけではないが身近なテーマでスピーキングをやりたい人**





### 4.画像テーマ
#### 4.1. 自分が撮影、ダウンロードした画像を選択します。

<img src="https://github.com/user-attachments/assets/386ff0e2-df42-4925-9bf0-b84e1fed00a4" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/8a16b0c6-34f0-4344-81fe-0f1139951348" alt="画像説明" width="240"/>
<img src="https://github.com/user-attachments/assets/8a9ec03f-01bc-4331-9904-cb89c5cfd197" alt="画像説明" width="230"/>

#### 4.2. テーマ生成ボタンを押すと画像に関連するテーマが生成されます。テーマ横の電球ボタンを押すことでヒントを生成してくれます。

<img src="https://github.com/user-attachments/assets/3332200c-d293-40e4-b2b0-2587f66a335d" alt="画像説明" width="230"/>

#### 4.3. 4.2でテーマを選択した後に、マイクボタンを押して選択したテーマに関するスピーチを行い、音声を提出すると、評価が得られます。

<img src="https://github.com/user-attachments/assets/7d797fa1-2634-4cd0-b297-86af13a8a47c" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/6a521bac-ea46-4dcc-b857-c7b5c75c0ed3" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/76937c9b-55ef-423a-be12-c6388650f902" alt="画像説明" width="230"/>

#### <対象ユーザー>
* **画像や視覚的な情報から発想を広げて学びたい人**
* **自己表現を大切にする人⇒自分の経験や思いを英語で表現し、表現力を磨きたい人**
* **親子の時間を楽しみたい家庭⇒子どもが好きなモノでテーマを生成し一緒に英語を学べる**



### 5.マラソン
#### 5.1. 繰り返し回数を事前に指定します

<img src="https://github.com/user-attachments/assets/d9e8a9c4-8795-4b62-be6b-67c2f55a5ae3" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/89fd417c-0cd7-458c-91c1-1b1fb0138265" alt="画像説明" width="230"/>

#### 5.2. 指定した回数だけテーマ生成、録音、評価を繰り返します。各フェーズにはそれぞれ制限時間がついています。また、マラソン中は直前に選択したテーマを保存しているのでテーマを固定して録音、評価を繰り返すことで同じテーマに対して何度も練習することができます。これらによってテンポのよい学習が可能です。さらに、評価画面では内容評価と音声評価を換算して200点満点にして毎回保存していきます。

<img src="https://github.com/user-attachments/assets/5b0f11ce-8a1e-49c9-ae50-803d07652e2b" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/0c4e43a6-ee8d-4fea-82d1-75c240c7f03c" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/17b1a895-b285-4e5f-813c-aa13fb7c1582" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/25a8d004-884b-4f05-bcc2-0a184c69afcd" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/5022670a-018e-4e47-ad80-bfecc991748a" alt="画像説明" width="230"/>

#### 5.3.指定した回数のマラソンが終了すると、各回の得点の推移を棒グラフで見ることが出来ます。この得点の平均によって背景が金、銀、銅、青のいずれかに決まります。shareボタンを押すと、スコアのグラフ画像をコメントとともにSNSに共有できます。

<img src="https://github.com/user-attachments/assets/a5472aa1-2926-4df5-88cd-f7b58c7d28e9" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/594bf216-393f-40a7-b51c-f89dcc1801d4" alt="画像説明" width="230"/>

#### 5.4. 設定画面に戻り「過去の記録を見る」を押すと過去のマラソンの得点の平均が折れ線グラフで表示されます。直近7日間のマラソンモードの継続日数とマラソンの得点によりgold, silver, bronze, blueのいずれかが決まり、これによりランクシステムを実現しています。こちらもshareボタンを押すと、背景画像をコメントとともにSNSに共有でき、ランクが上がった喜びを友達とシェアできます。

<img src="https://github.com/user-attachments/assets/870fef05-b35a-4471-bf1b-4ff62e7c779f" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/b171f139-d419-4b24-8211-d3374fd9141a" alt="画像説明" width="230"/>
<img src="https://github.com/user-attachments/assets/c071ce64-3b90-4c52-a6b9-c79dd71b4d18" alt="画像説明" width="230"/>

#### <対象ユーザー>
* **自分の成長を可視化することでモチベーションを得たい人**
* **ランクが上がることや競技性に楽しみを感じる人**
* **日々の頑張りを共有したい人**


### 解決出来ること
まず一番は楽しく勉強をすることができるので、学生から大人まですべての英語学習者が楽しく継続的に英語スピーチ練習を学ぶことができます。 また、それぞれのモードを設定したのは、以下を解決することを目的にしているからです。
* 「好きなテーマ」モードでは、好きなテーマを融合させたテーマを生成して、他では見られない 「自分の好きが詰まったユニークなテーマ」 に対してスピーキングをするモードです。
* 「Youtube」モードでは、欲に負けてYoutubeを見る人でも、その内容をすぐにスピーキングでアウトプットすることで新たな勉強の流れを作っています。
* 「News」モードでは、リアルの時事問題を生かしてテーマを生成するので、長い時間英語学習をすることで社会情勢がわからくなることを防ぎ、むしろニュースを読む習慣を提供しています。
* 「画像テーマ」モードでは、日常の一枚を入力してそれを利用してテーマ生成を行うモードです。このような機能は他では見られず、視覚を介した新しく楽しい学習体験を提供します。
* 「マラソン」モードでは、上記4つのモードへの競技性の導入、ユーザーの努力の見える化、スコアと継続日数によるランクの設定、日々の頑張りの共有機能の実装により、ユーザーに高ランクを目指す楽しさを提供し、ユーザーのモチベーションをアップさせます。

このように自分の趣味や日常の延長線上に、英語スピーチ練習をすることが可能なので楽しく継続性の高い英語スピーキング学習アプリになっています。また、学習の際、自分の好きなことを題材にしているので、スピーチに詳細な具体例や個人の体験を入れやすくなります。


評価については音声、内容の両面で行っています。音声面の評価では音声認識にWhisper、評価にSpeechace APIを用い、高精度の発音分析による１人では見つけにくい発音ミスの指摘を可能にしています。内容については 「テーマとの一貫性」、「構成」、「独自性」、「文法」、「語彙の多様性」を観点にしています。スピーチが構成として整っているかを評価し、「独自性」の観点によりユーザーの具体例や個人の体験を高く評価するシステムを整えています。よって、このアプリを使うことでユーザーが英語で物事を説明する際の表現力が向上すると思います。


以上により背景の項で述べた3つの課題を私達なりのアプローチで解決しています。


### 今後の展望
* より集中的に学習を行える「マラソンモード」の実装。具体的には今回開発した「好きなテーマ」、「Youtube」、「News」の機能の1つ1つに制限時間を設け、ユーザーが設定した回数分繰り返すことにより、何度もフィードバックをもらいながらどんどんスピーチの中身を良くしていく仕組みの実装。さらに点数を毎回記録することで自分の点数の推移をグラフ化し、ユーザーに成長を実感させる。
* 通信機能の実装により、他者と競争しあうことで学習意欲の向上を促す
* 通知機能などを駆使して、継続的な英語学習に取り組みやすくする
* メインコンテンツをスピーキング学習としながら、他の英語能力も学べるようにする
* 英語能力をRPGのようなスキルツリーやレート（あるいはレベル）として成長度を可視化すると共に、英語学習のゲーム化を目指して楽しく学べるようなアプリケーションにする
* また、スキルツリーによる可視化により、体系的な学習を可能にする
* Android版のアプリケーション開発
* まとめると、さらに楽しく、成長を実感できるアプリにしたいです！

### 注力したこと（こだわり等）
* ワードを融合させて融合させてユニークで面白いテーマの生成
* WhisperとSpeechace APIを用いた音声認識精度の向上と、取得した音声テキストを用いてスピーチ内容の評価精度を向上させたこと
* 多くのユーザーにリーチするための副次的な目的が異なる3つのモード(楽しく簡単に学べる"好きなテーマ"モード、動画を見た延長線上で学ぶための"Youtube"モード、最新を学ぶための"News"モード)の実装

## 開発技術
### 活用した技術
#### API・データ
* Open API(ChatGPT, Whisper)
* Youtube API
* Speechace API
* News API
* gooラボAPI キーワード抽出API

#### フレームワーク・ライブラリ・モジュール
* SwiftUI
* SwiftSoup
* SDWebImageSwiftUI

#### デバイス
* iPhone(iOS18.0以降でデモをした)

### 独自技術
#### ハッカソンで開発した独自機能・技術

* テーマを自分の好きなキーワードから生成してそれをスピーチのテーマとするアイデア、機能
* 自分の好きなYoutubeを検索できるようにしてそのタイトルをもとにスピーチをするアイデア、機能
* ニュースのHTMLが長すぎて処理がうまくいかなかったり時間がかかりすぎる問題を、HTMLのニュース形式がバラバラであるが多くで共通の<p>タグによってスクレイピングすることで関数部分を除外し、ChatGPTが処理できるトークン数に収めることができることに気づき処理した機能

* これらを頑張ったことでユーザーが自分だけにしかできないスピーチを構成し、発表させ、それを評価できるシステムが、何よりも楽しい学習方法で構築できたことが一番の独自機能だと感じています。 

*高精度音声認識＆独自評価基準を開発した、commit_idのeaee9d9が力を入れた実装になります。
  


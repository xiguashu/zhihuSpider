# 知乎spider
---
#### 简单的知乎爬虫，基于python3.6，使用scrapy框架爬取数据、mysql储存结果；
#### 思路为使用request模拟请求，使用json解析response，之后提取其中有用的信息；
#### 工程文件中，spider下的三个爬虫功能分别为：
###  1.user.py 
  根据指定的用户id，爬取这些用户的个人信息（包括基本信息、回答列表及评论、文章列表及评论等；
###  2.topic.py
  根据指定的question jd，爬取这些问题的信息（包括回答列表及其评论等；
###  3.search.py
  根据指定的关键词，爬取搜索结果，分别抓取用户结果、和综合结果中的文章和问题结果信息；

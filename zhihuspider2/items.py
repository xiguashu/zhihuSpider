# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

#part 1
class followItem(scrapy.Item): #关注/粉丝列表
    name=Field()
    related=Field()
    type=Field()

class UserItem(scrapy.Item): #用户基本信息
    type=Field()
    id = Field()
    name = Field()
    answer_count = Field()
    description=Field()
    articles_count = Field()
    educations = Field()
    employments = Field()
    business=Field()
    columns_count=Field()


class answerItem(scrapy.Item): #回答
    type=Field()
    related=Field()
    comment_count=Field()
    content=Field()
    created_time=Field()
    question=Field()
    question_url=Field()
    voteup_count=Field()

class articleItem(scrapy.Item):#文章
    type=Field()
    related=Field()
    content=Field()
    title=Field()
    url=Field()
    voteup_count=Field()
    comment_count=Field()

class commentsItem(scrapy.Item):#文章的评论
    type=Field()
    author=Field()
    content=Field()
    related=Field()

#part 2
class topicItem(scrapy.Item): #问题基本信息
    id=Field()
    title=Field()
    link=Field()
    answer_count=Field()
    comment_count=Field()

class topic_commentsItem(scrapy.Item): #问题评论列表
    author=Field()
    related_topic=Field()
    content=Field()

class similar_topicItem(scrapy.Item): #镜像问题
    related_topic=Field()
    title=Field()
    id=Field()

class topic_answer_Item(scrapy.Item): #问题回答列表
    related_topic=Field()
    voteup_count=Field()
    comment_count=Field()
    author=Field()
    author_link=Field()
    author_introduction=Field()

class topic_answer_commentsItem(scrapy.Item): #问题的回答的评论列表
    author=Field()
    related_answer=Field()
    related_topic=Field()
    content=Field()

#part 3

class search_article_Item(scrapy.Item): #搜索文章
    key_word=Field()
    title=Field()
    link=Field()
    author=Field()
    voteup_count=Field()
    comment_count=Field()

class search_comment_Item(scrapy.Item): #文章评论列表
    type=Field()
    related_content=Field()
    content=Field()
    name=Field()

class search_topic_Item(scrapy.Item): #搜索问题
    id=Field()
    title=Field()
    link=Field()
    answer_count=Field()
    comment_count=Field()

class search_peopleItem(scrapy.Item): #搜索用户
    key_word=Field()
    id = Field()
    name = Field()
    answer_count = Field()
    description=Field()
    articles_count = Field()
    educations = Field()
    employments = Field()
    business=Field()
    columns_count=Field()
    locations=Field()

class search_followItem(scrapy.Item):#用户的粉丝和关注列表
    name=Field()
    related=Field()
    type=Field()

class search_similar_topicItem(scrapy.Item): #镜像问题
    related_topic=Field()
    title=Field()
    id=Field()

class search_topic_commentsItem(scrapy.Item): #问题评论列表
    author=Field()
    related_topic=Field()
    content=Field()

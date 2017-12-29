# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql




class UserPipeline(object):
    def __init__(self):
        DbConfig = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'db': 'zhihu',
            'charset': 'utf8',
        }
        self.connect = pymysql.connect(user=DbConfig['user'], passwd=DbConfig['password'], db=DbConfig['db'],
                                    host=DbConfig['host'], charset='utf8', use_unicode=True,port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        if item.__class__.__name__ == 'UserItem':

            sql = 'insert into user_imfor(id,name,answer_count,description,articles_count,columns_count,educations,employments,business) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, (item['id'],item['name'],item['answer_count'],item['description'],item['articles_count'], item['columns_count'],item['educations'], item['employments'], item['business']))
            self.connect.commit()


        if item.__class__.__name__=='followItem':
             sql = 'insert into follow(name,related_user,type) values (%s,%s,%s)'
             self.cursor.execute(sql, (
             item['name'], item['related'], item['type']))
             self.connect.commit()


        if item.__class__.__name__=='answerItem':
            sql = 'insert into user_answer(question,question_url,content,created_time,related_user,comment_count,voteup_count) values (%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, (
                item['question'], item['question_url'], item['content'],item['created_time'],item['related'],item['comment_count'],item['voteup_count']))
            self.connect.commit()

        if item.__class__.__name__=='articleItem':
            sql = 'insert into article(related_user,content,title,url,voteup_count,comment_count) values (%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, (
                item['related'], item['content'], item['title'],item['url'],item['voteup_count'],item['comment_count']))
            self.connect.commit()

        if item.__class__.__name__ == 'commentsItem':
                sql = 'insert into comments(author,content,related) values (%s,%s,%s)'
                self.cursor.execute(sql, (
                    item['author'], item['content'], item['related']))
                self.connect.commit()

        if item.__class__.__name__=='topicItem':
            if item['comment_count']!='a':
                sql = "UPDATE topic SET comment_count ='%s' WHERE id = '%s'" % (item['comment_count'],item['id'])
                self.cursor.execute(sql)
                self.connect.commit()
            else:
                sql = 'insert into topic(id,title,link,answer_count) values (%s,%s,%s,%s)'
                self.cursor.execute(sql, (
                    item['id'], item['title'], item['link'],item['answer_count']))
                self.connect.commit()

        if item.__class__.__name__ == 'topic_commentsItem':
            sql = 'insert into topic_comments(author,related_topic,content) values (%s,%s,%s)'
            self.cursor.execute(sql, (
                    item['author'], item['related_topic'], item['content']))
            self.connect.commit()

        if item.__class__.__name__ == 'similar_topicItem':
            sql = 'insert into similar_topic(related_topic,title,id) values (%s,%s,%s)'
            self.cursor.execute(sql, (
                item['related_topic'], item['title'],item['id']))
            self.connect.commit()

        if item.__class__.__name__ == 'topic_answer_Item':
            sql = 'insert into topic_answer(related_topic,voteup_count,comment_count,author,author_link,author_introduction) values (%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, (
                    item['related_topic'], item['voteup_count'], item['comment_count'],item['author'],item['author_link'],item['author_introduction']))
            self.connect.commit()

        if item.__class__.__name__ == 'topic_answer_commentsItem':
                sql = 'insert into topic_answer_comments(author,related_answer,related_topic,content) values (%s,%s,%s,%s)'
                self.cursor.execute(sql, (
                    item['author'], item['related_answer'], item['related_topic'], item['content']))
                self.connect.commit()

#part3
        if item.__class__.__name__ == 'search_topic_commentsItem':
            sql = 'insert into search_topic_comment(author,related_topic,content) values (%s,%s,%s)'
            self.cursor.execute(sql, (
                    item['author'], item['related_topic'], item['content']))
            self.connect.commit()

        if item.__class__.__name__ == 'search_similar_topicItem':
            sql = 'insert into search_similar(related_topic,title,id) values (%s,%s,%s)'
            self.cursor.execute(sql, (
                item['related_topic'], item['title'],item['id']))
            self.connect.commit()

        if item.__class__.__name__=='search_followItem':
             sql = 'insert into search_follow(name,related,type) values (%s,%s,%s)'
             self.cursor.execute(sql, (
             item['name'], item['related'], item['type']))
             self.connect.commit()

        if item.__class__.__name__=='search_topic_Item':
            if item['comment_count']!='a':
                sql = "UPDATE search_topic SET comment_count ='%s' WHERE id = '%s'" % (item['comment_count'],item['id'])
                self.cursor.execute(sql)
                self.connect.commit()
            else:
                sql = 'insert into search_topic(id,title,link,answer_count) values (%s,%s,%s,%s)'
                self.cursor.execute(sql, (
                    item['id'], item['title'], item['link'],item['answer_count']))
                self.connect.commit()

        if item.__class__.__name__ == 'search_comment_Item':
            sql = 'insert into search_comment(name,content,related_content) values (%s,%s,%s)'
            self.cursor.execute(sql, (
                item['name'], item['content'], item['related_content']))
            self.connect.commit()

        if item.__class__.__name__=='search_article_Item':
            sql = 'insert into search_article(key_word,author,title,link,voteup_count,comment_count) values (%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, (
                item['key_word'],item['author'], item['title'],item['link'],item['voteup_count'],item['comment_count']))
            self.connect.commit()


        if item.__class__.__name__ == 'search_peopleItem':

            sql = 'insert into search_people(key_word,id,name,answer_count,description,article_count,columns_count,educations,employments,business,locations) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql,
                                (item['key_word'],item['id'],item['name'],item['answer_count'],item['description'],item['articles_count'], item['columns_count'],item['educations'], item['employments'], item['business'],
                                 item['locations']))
            self.connect.commit()


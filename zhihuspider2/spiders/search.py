
import json
from scrapy import Spider, Request
from zhihuspider.items import search_article_Item,search_comment_Item,search_followItem,search_peopleItem,search_topic_Item,search_similar_topicItem,search_topic_commentsItem

import scrapy
import urllib

class search(Spider):


    name = "search"
    allowed_domains = ["www.zhihu.com"]

    words=['11','勇士','绿色','旅行','22','33','44','55','6666','77','88']
    content_url='https://www.zhihu.com/api/v4/search_v3?t=general&q={q}&correction=1&search_hash_id=1ac5e0367ab4ac5df90f9d65369c05b4&offset={offset}&limit=1'
    comment_answer_url='https://www.zhihu.com/api/v4/answers/{answer}/comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=20&offset=0&status=open'
    comment_article_url='https://www.zhihu.com/api/v4/articles/{article}/comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=20&offset=0&status=open'
    people_url='https://www.zhihu.com/api/v4/search_v3?t=people&q={q}&correction=1&offset={offset}&limit=1'
    member_url='https://www.zhihu.com/api/v4/members/{url_token}?include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Cavatar_hue%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccolumns_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cincluded_answers_count%2Cincluded_articles_count%2Cincluded_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_bind_phone%2Cis_force_renamed%2Cis_bind_sina%2Cis_privacy_protected%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cis_org_createpin_white_user%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
    followee_url='https://www.zhihu.com/api/v4/members/{user}/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
    follower_url='https://www.zhihu.com/api/v4/members/{user}/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
    topic_search_url='https://www.zhihu.com/api/v4/questions/{q_id}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=&limit=3&sort_by=default'
    search_topic_similar_url='https://www.zhihu.com/api/v4/questions/{q_id}/similar-questions?include=data%5B*%5D.answer_count%2Cauthor%2Cfollower_count&limit=5'
    topic_comment_url='https://www.zhihu.com/api/v4/questions/{q_id}/comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=10&offset=0&status=open'
    def start_requests(self):
        for word in self.words:
            yield  Request(self.content_url.format(q=word,offset=0),self.parse_content) #文章和问题
        #    yield Request(self.people_url.format(q=word,offset=0),self.parse_people) #用户

    def parse_content(self,response):
        results = json.loads(response.text)
        # 得到搜索关键词
        next_page = results.get('paging').get('next')
        index=next_page.find('&q=')
        index2=next_page.find('&limit')
        key_word=next_page[index+3:index2]
        key_word=urllib.parse.unquote(key_word)   #对url中的搜索关键词进行解码

        index = next_page.find('offset=')
        off = next_page[index + 7:index + 11]
        index = off.find('&')
        off = int(off[0:index]) #得到访问下一页信息所需的offset

        if results.get('data'):
            if off==1: #判断是不是第一页（格式不一样
                i=2
            else:
                i=0
            if results.get('data')[i].get('object').get('author'):
                a_id=results.get('data')[i].get('object').get('url')
                index=a_id.find('answers/')
                index2=a_id.find('articles/')
                if index==-1:   #is article
                    item = search_article_Item()
                    item['key_word'] = key_word
                    item['author'] = results.get('data')[i].get('object').get('author').get('name')
                    item['voteup_count'] = results.get('data')[i].get('object').get('voteup_count')
                    item['comment_count'] = results.get('data')[i].get('object').get('comment_count')
                    if results.get('data')[i].get('highlight'):
                        item['title'] = results.get('data')[i].get('highlight').get('title')
                    a_id=a_id[index2+9:len(a_id)]
                    item['link'] = 'https://zhuanlan.zhihu.com/p/' + a_id
                 #   yield item #文章信息
                    yield Request(self.comment_article_url.format(article=a_id), self.parse_article_comment) #获取文章评论
                else:        #is topic

                    q_id=results.get('data')[i].get('object').get('question').get('id')
                    yield Request(self.topic_search_url.format(q_id=q_id),self.parse_search_topic) #获取话题信息
                    yield Request(self.search_topic_similar_url.format(q_id=q_id),self.parse_search_similar)#相似话题
                    yield Request(self.topic_comment_url.format(q_id=q_id),self.parse_search_topic_comment) #话题评论和评论数




        if off<=500:
            yield Request(self.content_url.format(q=key_word,offset=off),self.parse_content)
        else:
            return

    def parse_search_similar(self,response):
        results = json.loads(response.text)
        l = len(results.get('paging').get('next'))
        id = results.get('data')[0].get('url')[38:l] #关联问题id
        item =search_similar_topicItem()
        for result in results.get('data'):
            item['title'] = result.get('title')
            item['id'] = result.get('id')
            item['related_topic'] = id
            yield item

    def parse_search_topic(self,response): #话题信息
        results=json.loads(response.text)
        item=search_topic_Item()
        if results.get('data')[0]:
            data=results.get('data')[0].get('question')
            item['id']=data.get('id')
            item['title']=data.get('title')
            item['link']=data.get('url')
            item['comment_count']='a'
        if results.get('paging'):
            item['answer_count']=results.get('paging').get('totals')
        yield item

    def parse_article_comment(self, response):
        results = json.loads(response.text)
        item = search_comment_Item()
        item['type']='article'
        if 'data' in results.keys():
            for result in results.get('data'):
                item['name'] = result.get('author').get('member').get('name')
                item['content'] = result.get('content')
                if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
                    next_page1 = results.get('paging').get('next')
                    index=next_page1.find('articles/')+9
                    art_id=next_page1[index:index+15]
                    index=art_id.find('/')
                    art_id=art_id[0:index]

                    item['related_content'] = art_id
                    yield item

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:  # 有下一页
            next_page = results.get('paging').get('next')
            yield Request(next_page,
                              self.parse_article_comment)

    def parse_people(self,response):
        results=json.loads(response.text)
        item=search_peopleItem()


        if results.get('data'):
                url_token=results.get('data')[0].get('object').get('url_token')
                yield Request(self.member_url.format(url_token=url_token),self.parse_search_user)#该用户的个人信息
          #      yield Request(self.followee_url.format(user=url_token),self.parse_search_follows) #该用户关注列表
           #     yield Request(self.follower_url.format(user=url_token), self.parse_search_followers)#粉丝列表

        if results.get('paging'):
            next_page = results.get('paging').get('next')
            index = next_page.find('&q=')
            index2 = next_page.find('&limit')
            key_word = next_page[index + 3:index2]
            key_word = urllib.parse.unquote(key_word)  # 对url中的搜索关键词进行解码
            item['key_word'] = key_word
            index = next_page.find('offset=')
            off = next_page[index + 7:index + 11]
            index = off.find('&')
            off = int(off[0:index])
            yield Request(self.people_url.format(q=key_word, offset=off), self.parse_people)

    def parse_search_user(self, response):

        result = json.loads(response.text)
        item = search_peopleItem()
        for field in item.fields: #初始为0，防止插入数据库时报错
            item[field]=0
            if field in result.keys():
                if result.get(field):
                    item[field]=result.get(field)

        if result.get('employments'):
            if result.get('employments')[0].get('company'):
                item['employments'] = result.get('employments')[0].get('company').get('name')
                if result.get('employments')[0].get('job'):
                    item['employments'] = result.get('employments')[0].get('company').get('name') + \
                                  result.get('employments')[0].get('job').get('name')
        if result.get('educations'):
                if result.get('educations')[0].get('school'):
                    item['educations'] = result.get('educations')[0].get('school').get('name')
                    if result.get('educations')[0].get('major'):
                         item['educations'] = result.get('educations')[0].get('school').get('name') + ' ' + \
                                 result.get('educations')[0].get('major').get('name')
        if result.get('business'):
             item['business'] = result.get('business').get("name")

        if result.get('locations'):
            item['locations']=result.get('locations')[0].get('name')
        yield item

    def parse_search_follows(self, response):
        results = json.loads(response.text)
        pre_page=results.get('paging').get('previous')
        index=pre_page.find('members/')
        related=pre_page[index+8:index+28]
        index=related.find('/')
        related=related[0:index]
        item2=search_followItem()
        item2['related']=related
        item2['type']='followee'
        if 'data' in results.keys():
            for result in results.get('data'):
                item2['name']=result.get('name')
                yield item2

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            le=len(next_page)
            off=next_page[le-2:le]
            p=next_page[le-3]
            if ('81'>off and p=='='):
                yield Request(next_page,
                          self.parse_search_follows)
            else:
                return

    def parse_search_followers(self, response):

        results = json.loads(response.text)
        pre_page=results.get('paging').get('previous')
        index = pre_page.find('members/')
        related = pre_page[index + 8:index + 28]
        index = related.find('/')
        related = related[0:index]
        item2=search_followItem()
        item2['related']=related
        item2['type']='follower'
        if 'data' in results.keys():
            for result in results.get('data'):
                item2['name']=result.get('name')
                yield item2

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:#有下一页
            next_page = results.get('paging').get('next')
            le=len(next_page)
            off=next_page[le-2:le]
            p=next_page[le-3]
            if ('81'>off and p=='='):
                yield Request(next_page,
                          self.parse_search_followers)
            else:
                return

    def parse_search_topic_comment(self,response):
        results=json.loads(response.text)
        l=len(results.get('data')[0].get('url'))
        id=results.get('data')[0].get('url')[37:l]
        item1=search_topic_Item()
        item1['id']=id
        item1['comment_count']=results.get('common_counts')
        yield item1
        item2=search_topic_commentsItem()
        for result in results.get('data'):
            print (result)
            item2['content']=result.get('content')
            item2['author']=result.get('author').get('member').get('name')
            item2['related_topic'] = id
            yield item2

        if results.get('paging').get('next') and results.get('paging').get('is_end')== False:
            next_page=results.get('paging').get('next')
            yield Request(next_page,self.parse_search_topic_comment)



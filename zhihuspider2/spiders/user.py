import json
import sys,os
from scrapy import Spider, Request
from zhihuspider.items import followItem,answerItem,UserItem,commentsItem,articleItem

import scrapy

class user(Spider):


    name = "user"
    allowed_domains = ["www.zhihu.com"]
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_url2='https://www.zhihu.com/api/v4/members/{user}?include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Cavatar_hue%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccolumns_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cincluded_answers_count%2Cincluded_articles_count%2Cincluded_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_bind_phone%2Cis_force_renamed%2Cis_bind_sina%2Cis_privacy_protected%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cis_org_createpin_white_user%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    answers_url='https://www.zhihu.com/api/v4/members/{user}/answers?include={include}&offset={offset}&limit={limit}&sort_by={sort_by}'
    answers_url2='https://www.zhihu.com/api/v4/members/{user}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={offset}&limit=20&sort_by=created'

    article_url='https://www.zhihu.com/api/v4/members/{user}/articles?include=data%5B*%5D.comment_count%2Csuggest_edit%2Cis_normal%2Ccan_comment%2Ccomment_permission%2Cadmin_closed_comment%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={offset}&limit=20&sort_by=created'
    comments_url='https://www.zhihu.com/api/v4/articles/{id}/comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=20&offset={offset}&status=open'

    start_user = ('excited-vczh','wuchangyexue','yu-yi-18','biubiubiubiudadada','huang-yi-qin-1-12',
                  'xiao-zhu-zhu-1-62','zhy1378','Yumemi-Hoshino','wang-qi-wen-85-23','gou-nu-si-45')

    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    answers_query='data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,collapsed_by,suggest_edit,comment_count,can_comment,content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,question,excerpt,relationship.is_authorized,voting,is_author,is_thanked,is_nothelp,upvoted_followees;data[*].author.badge[?(type=best_answerer)].topics'

    def start_requests(self):
        for user in self.start_user:
           # yield Request(self.user_url.format(user=user, include=self.user_query), self.parse_user) #用户信息


            #yield Request(self.user_url2.format(user=user, include=self.user_query), self.parse_user)  # 用户信息
   #         yield Request(                                                                             #粉丝列表
   #             self.follows_url.format(user=user, include=self.follows_query, limit=20, offset=0),
    #            self.parse_follows)
  #         yield Request(                                                                              #关注列表
     #           self.followers_url.format(user=user, include=self.followers_query, limit=20,offset=0),
     #           self.parse_followers)
     #       yield Request(self.answers_url.format(user=user,include=self.answers_query,limit=20,offset=0,sort_by='created'),
       #                   self.parse_answer)                                                                #回答列表
             yield Request(self.article_url.format(user=user,offset=0),self.parse_article)  #文章列表

    def parse_user(self, response):
        global i
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
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
        yield item

    def parse_follows(self, response):
        results = json.loads(response.text)
        pre_page=results.get('paging').get('previous')
        related=pre_page[36:60]
        valid=related.find('/')
        related=related[0:valid]
        item2=followItem()
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
                          self.parse_follows)
            else:
                return

    def parse_followers(self, response):
        global i
        global user
        results = json.loads(response.text)
        pre_page=results.get('paging').get('previous')
        related=pre_page[36:60]
        valid=related.find('/')
        related=related[0:valid]
        item2=followItem()
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
                          self.parse_followers)
            else:
                return

    def parse_answer(self,response):
        results=json.loads(response.text)
        item = answerItem()
        for field in item.fields:
            item[field]=0

        if 'data' in results.keys():
            for result in results.get('data'):
                item['related'] = result.get('author').get('url_token')
                item['content']=result.get('content')
                item['question_url']=result.get('question').get('url')
                item['question']=result.get('question').get('title')
                item['comment_count']=result.get('comment_count')
                item['voteup_count']=result.get('voteup_count')
                item['created_time']=result.get('created_time')
                item['type']='answer'

                yield item

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:  # 有下一页
            next_page = results.get('paging').get('next')

            le=len(next_page)
            off=next_page[le-3:le]
            if off[0]=='=':
                off=off[1:3]
            off=int(off)

            related = next_page[30:60]
            valid = related.find('/')
            user = related[0:valid]
            if off<500:
                yield Request(self.answers_url2.format(user=user,offset=off),
                          self.parse_answer)
            else:
                return

    def parse_article(self,response):
        results = json.loads(response.text)
        item = articleItem()

        if 'data' in results.keys():
            for result in results.get('data'):
                for field in item.fields:
                    item[field] = 0
                item['related'] = result.get('author').get('url_token')
                item['content'] = result.get('content')
                item['voteup_count'] = result.get('voteup_count')
                item['url'] = result.get('url')
                item['comment_count'] = result.get('comment_count')
                item['title'] = result.get('title')
                item['type'] = 'article'
                yield item
                id_=result.get('id')
                yield Request(self.comments_url.format(id=id_, offset=0),self.parse_comment) #评论



        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:  # 有下一页
            next_page = results.get('paging').get('next')

            le = len(next_page)
            off = next_page[le - 3:le]
            if off[0] == '=':
                off = off[1:3]
            off = int(off)

            related = next_page[30:60]
            valid = related.find('/')
            user = related[0:valid]
            if off < 50:
                yield Request(self.article_url.format(user=user, offset=off),
                              self.parse_article)

    def parse_comment(self,response):
        results = json.loads(response.text)
        item = commentsItem()

        if 'data' in results.keys():
            for result in results.get('data'):
                item['author'] = result.get('author').get('member').get('name')
                item['content'] = result.get('content')

                next_page1 = results.get('paging').get('next')
                index=next_page1.find('articles/')+9
                art_id=next_page1[index:index+15]
                index=art_id.find('/')
                art_id=art_id[0:index]
                item['related'] = art_id
                yield item

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:  # 有下一页
            next_page = results.get('paging').get('next')

            le = len(next_page)
            off = next_page[le - 2:le]
            off = int(off)

            if off < 50:
                yield Request(next_page,
                              self.parse_comment)


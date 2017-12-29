
import json
from scrapy import Spider, Request
from zhihuspider.items import topic_answer_Item,topicItem,similar_topicItem,topic_commentsItem,topic_answer_commentsItem,search_topic_commentsItem
import scrapy

class topic(Spider):


    name = "topic"
    allowed_domains = ["www.zhihu.com"]
    topic_ids=['24622770','66376141']

    topic_url='https://www.zhihu.com/api/v4/questions/{id}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20&sort_by=default'
    topic_answer_url='https://www.zhihu.com/api/v4/questions/{id}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=3&limit=20&sort_by=default'
    comment_url='https://www.zhihu.com/api/v4/questions/{id}/comments?status=open&include={include}&limit=10&order=normal&offset=0'
    similar_topic_url='https://www.zhihu.com/api/v4/questions/{id}/similar-questions?include=data%5B*%5D.answer_count%2Cauthor%2Cfollower_count&limit=5'
    answer_comments_url='https://www.zhihu.com/api/v4/questions/{id}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20&sort_by=default'
    topic_answer_comment_url='https://www.zhihu.com/api/v4/answers/{id}/comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=20&offset=0&status=open'

    topic_comment_include='data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author'
    topic_include='data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics'
    topic_answer_include='data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        for id in self.topic_ids:
           yield Request(self.topic_url.format(id=id), self.parse_topic) #话题信息 先获得话题信息 在更新其中的评论数
       #    yield Request(self.comment_url.format(id=id,include=self.topic_comment_include),self.parse_comment) #评论列表和评论数
         #    yield Request(self.similar_topic_url.format(id=id),self.parse_similar_topic) #相似回答列表
         #    yield Request(self.topic_answer_url.format(id=id),self.parse_topic_answer) #回答和回答的评论列表



    def parse_topic(self, response):
        results=json.loads(response.text)
        item=topicItem()

        if results.get('data')[0]:
            data=results.get('data')[0].get('question')
            item['id']=data.get('id')
            item['title']=data.get('title')
            item['link']=data.get('url')
            item['comment_count']='a'
        if results.get('paging'):
            item['answer_count']=results.get('paging').get('totals')
        yield item


    def parse_comment(self,response):
        results=json.loads(response.text)
        l=len(results.get('data')[0].get('url'))

        id=results.get('data')[0].get('url')[37:l]
        item1=topicItem()
        item1['id']=id
        item1['comment_count']=results.get('common_counts')
        yield item1
        item2=topic_commentsItem()
        for result in results.get('data'):
            print (result)
            item2['content']=result.get('content')
            item2['author']=result.get('author').get('member').get('name')
            item2['related_topic'] = id
            yield item2

        if results.get('paging').get('next') and results.get('paging').get('is_end')== False:
            next_page=results.get('paging').get('next')
            yield Request(next_page,self.parse_comment)

    def parse_similar_topic(self, response):
        results = json.loads(response.text)
        l = len(results.get('paging').get('next'))
        id = results.get('data')[0].get('url')[37:l]
        item = similar_topicItem()
        for result in results.get('data'):
            item['title'] = result.get('title')
            item['id'] = result.get('id')
            item['related_topic'] = id
            yield item


    def parse_topic_answer(self,response):
        results=json.loads(response.text)
        id=results.get('data')[0].get('question').get('id') #topic id
        item=topic_answer_Item()
        link='https://www.zhihu.com/people/'
        for result in results.get('data'):
            item['voteup_count']=result.get('voteup_count')
            item['comment_count']=result.get('comment_count')
            item['related_topic'] = id
            item['author']=result.get('author').get('name')
            url_token=result.get('author').get('url_token')
            item['author_link']=link+url_token
            item['author_introduction']=result.get('author').get('headline')
            yield item
            a_id=result.get('id')
            yield Request(self.topic_answer_comment_url.format(id=a_id), self.parse_topic_answer_comment)





        if results.get('paging').get('next') and results.get('paging').get('is_end')== False:

            next_page=results.get('paging').get('next')
            index=next_page.find('offset=')
            off=next_page[index+7:index+10]
            if off < '100' or off[len(off)-1]=='&' or len(off)<3:
                 yield Request(next_page,self.parse_topic_answer)
            else:
                return


    def parse_topic_answer_comment(self,response):
        results=json.loads(response.text)

        index1 = results.get('paging').get('next').find('answers/')
        a_id=results.get('paging').get('next')[index1+8:index1+20]
        index1=a_id.find('/')
        a_id=a_id[0:index1]

        item=topic_answer_commentsItem()
        for result in results.get('data'):
            item['related_topic']=0 #关联的topic
            item['author']=result.get('author').get('member').get('name')
            item['related_answer'] = a_id
            item['content']=result.get('content')
            yield item

        if results.get('paging').get('next') and results.get('paging').get('is_end')== False: #下一页
            next_page=results.get('paging').get('next')
            index=next_page.find('offset=')
            off=next_page[index+7:index+10]
            if off < '50' or off[len(off)-1]=='&' or len(off)<3: #前五百个
                yield Request(next_page,self.parse_topic_answer_comment)

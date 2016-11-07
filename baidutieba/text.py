#_*_ coding:utf-8 _*_
#输入帖子编号，爬去帖子内容
import urllib2
import urllib
import re


class Tool(object):
    removeImg = re.compile('<img.*?>| {7}')
    removeHref = re.compile('<a.*?>|</a>')
    removeBr = re.compile('<br>{1,4}')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeBr, "\n", x)
        x = re.sub(self.removeHref, "", x)
        return x.strip()


class BDTB(object):
    """docstring for BDTB"""

    def __init__(self, baseurl, see_lz, floorTag):
        super(BDTB, self).__init__()
        self.baseurl = baseurl
        self.see_lz = see_lz
        self.tool = Tool()
        self.defaultTitle = u'百度贴吧'
        self.floorTag = floorTag
        self.file = None
        self.floor = 1

    def getpage(self, page):
        url = self.baseurl + '?see_lz=' + str(self.see_lz) + '&pn=' + str(page)
        request = urllib2.Request(url)
        html = urllib2.urlopen(request)
        content = html.read()
        return content

    def gettitle(self, contents):
        pattern = re.compile(
            '<div\sclass="core_title.*?<h3\sclass="core_title_txt.*?>(.*?)</h3>', re.S)
        title = re.search(pattern, contents)
        if title:
            print title.group(1)
        else:
            return None

    def getPageNum(self, contents):
        pattern = re.compile(
            '<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        pageNum = re.search(pattern, contents)
        if pageNum:
            return pageNum.group(1)
        else:
            return None

    def getContent(self, content):
        pattern = re.compile('<div\sid="post_content_.*?>(.*?)</div>', re.S)
        pageContent = re.findall(pattern, content)
        texts = []
        for item in pageContent:
            text = "\n" + self.tool.replace(item) + "\n"
            texts.append(text.decode('utf-8').encode('gbk'))
        return texts

    def setFileName(self, title):
        if title is not None:
            self.file = open(title + '.txt', 'w')
        else:
            self.file = open(self.defaultTitle + '.txt', 'w')

    def writetext(self,contents):
        for text in contents:
            if self.floorTag == '1':
                floorLine = '\n' + \
                    str(self.floor) + \
                    u'--------------------------------------------------------------\n'
                self.file.write(floorLine)
            self.file.write(text)
            self.floor += 1

    def start(self):
        indexPage = self.getpage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.gettitle(indexPage)
        self.setFileName(title)
        if pageNum == None:
            print 'URL失效，请重试'
        try:
            print "该帖子共有" + str(pageNum) + "页"
            for i in range(1, int(pageNum) + 1):
                page = self.getpage(i)
                contents = self.getContent(page)
                self.writetext(contents)
        except IOError, e:
            print u"写入异常,原因" + e.message
        finally:
            print u"写入任务完成"

print u'请输入帖子代号'
baseurl = 'http://tieba.baidu.com/p/'+str(raw_input(u'http://tieba.baidu.com/p/'))
floorTag=raw_input("是否写入楼层，是输入1，否输入0\n")
see_lz=raw_input('是否只看楼主，是输入1，否输入0\n')
bdtb=BDTB(baseurl, see_lz, floorTag)
bdtb.start()

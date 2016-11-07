from scrapy.utils.project import get_project_settings
import random
settings = get_project_settings()


class ProcessHeaderMidware(object):

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        uagent = random.choice(settings.get('USER_AGENT_LIST'))
        if uagent:
            request.headers.setdefault('User-Agent', uagent)

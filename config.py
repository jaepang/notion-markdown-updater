import os
from notion.client import NotionClient

# Init NotionClient
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
HOME_URL = os.getenv("DOCUMENTS_URL")
client = NotionClient(token_v2=NOTION_TOKEN, monitor=True, start_monitoring=True)
blog_home = client.get_block(HOME_URL)
COLLECTION_ID = blog_home.collection.id
collection = client.get_collection(COLLECTION_ID)
posts = collection.get_rows()

# post status str
publish_ready = "🚀Ready to Publish"
published = "📰Published"

# timezone for displaying on log
timezone_log = 'Asia/Seoul'

# the absolute path where you want to place markdown file
post_path = "/home/ubuntu/blog/"
# the absolute path of this directory
where_am_i = "/home/ubuntu/jaekwang/notion-markdown-updater/"

# auto push when change made
auto_deploy = True
import requests
import oss2
from io import BytesIO

import uuid

uuid_str = uuid.uuid4().hex
file_name = 'jpg_{}.jpg'.format(uuid_str)


# 阿里云OSS配置
access_key_id = ''
access_key_secret = ''


bucket_name = 't'
endpoint = 'https://oss-cn-hangzhou.aliyuncs.com'
object_name = file_name

# 描述：输入远程URL地址，存储到oss之中.
### image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
def savejpg2oss(image_url):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
  }
  # 使用requests获取远程图片
  response = requests.get(image_url,headers=headers)
#   print(response.content)
  if response.status_code == 200:
      # 从内存中读取图片内容
      image_data = BytesIO(response.content)

      # 初始化OSS
      auth = oss2.Auth(access_key_id, access_key_secret)
      bucket = oss2.Bucket(auth, endpoint, bucket_name)

      # 上传图片到OSS
      bucket.put_object(object_name, image_data)
      print(f'图片已上传到OSS: {object_name}')
      expires = 36000  # 链接1小时后过期
      url = bucket.sign_url('GET', object_name, expires)
      print(url)
      
  else:
      print('无法从远程服务器获取图片')

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
savejpg2oss(image_url)

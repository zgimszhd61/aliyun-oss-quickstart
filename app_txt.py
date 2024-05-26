import requests
import oss2
from dotenv import load_dotenv
import os
load_dotenv()

# 阿里云OSS配置
access_key_id = os.getenv('access_key_id')
access_key_secret = os.getenv('access_key_secret')
bucket_name = 'twittervideio'
endpoint = 'https://oss-cn-hangzhou.aliyuncs.com'

# 本地文件路径
local_file_path = 'xxx.txt'
# OSS中的文件名，这里使用本地文件名，也可以自定义
object_name = os.path.basename(local_file_path)

def upload_file_to_oss(local_file_path, object_name):
    # 初始化OSS
    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    # 从本地文件系统读取文件内容
    with open(local_file_path, 'rb') as file_data:
        # 上传文件到OSS
        bucket.put_object(object_name, file_data)
        print(f'文件已上传到OSS: {object_name}')

    # 生成公开可访问的URL
    expires = 3600  # 链接1小时后过期
    url = bucket.sign_url('GET', object_name, expires)
    print(f'文件公开可访问的URL: {url}')

# 调用函数上传文件
upload_file_to_oss(local_file_path, object_name)
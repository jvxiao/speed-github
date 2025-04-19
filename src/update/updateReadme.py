import os
import shutil
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dnschecker.main import get_github_domains, get_all_ips

template_path = 'src/update/readme.template'
temp_file = 'src/update/temp'
readme_path = os.path.join(os.path.dirname(__file__), '../../', 'README.md')
print(readme_path)
if __name__ == '__main__':
  urls = get_github_domains()
  host_map = get_all_ips(urls)
  
  host_str = ''
  for key in host_map:
    if host_map[key] is not None:
      host_str += '{0:<30} {1}\n'.format(host_map[key], key)

  with open(template_path) as ft:
    template = ''.join(ft.readlines())

  content = '\n\n' + template
  content = content.replace('{{ hosts }}', host_str)

  # 获取指定时区的当前时间
  tz = ZoneInfo("Asia/Shanghai")  # 时区名称（如 "America/New_York"）
  now = datetime.now(tz)
  content = content.replace('{{ time }}', now.strftime("%Y-%m-%d %H:%M:%S"))

  with open(temp_file, 'w+') as fp:
    fp.write(content)
  
  shutil.copy(temp_file, readme_path)
  os.remove(temp_file)
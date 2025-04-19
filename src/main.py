import os
import time
import shutil
from dnschecker.main import get_all_ips, insert_or_append, get_github_domains 



cur_dir = os.path.dirname(__file__)

# host tempalte
template_path = cur_dir + '/host-template'
# temp hosts file
local_host = cur_dir +'/hosts' 
# host file on windows
host_path = 'C:\Windows\System32\drivers\etc\hosts'


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
  content = content.replace('{{ time }}', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
  
  header = '# Gennerate by Speed-github'
  tail = '# Star repo'
  new_lines = insert_or_append(host_path, header, tail, [content])

  with open(local_host, 'w+', encoding='utf-8') as fh:
    fh.writelines(new_lines)
  
  # overwrite the old hosts
  shutil.copy(local_host, host_path)
  os.system("ipconfig /flushdns")
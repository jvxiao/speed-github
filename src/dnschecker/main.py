from dns import resolver
import time
import os
import shutil

def get_ip_by_domain(hostname):
  try:
    ips = resolver.resolve(hostname, 'A')
  except:
    ips = []
  return str(ips[0]) if len(ips) else None


def get_all_ips(urls):
  host_ip_map = {}
  for url in urls:
    host_ip_map[url] = get_ip_by_domain(url)
    print(url, host_ip_map[url])
  return host_ip_map


def insert_or_append(file_path, header, tail, insert_content):
  startIndex = None
  endIndex = None
  
  if not os.path.exists(file_path):
    raise Exception('file not exist')
  
  with open(file_path, encoding='utf-8') as f:
    lines = f.readlines()
  
  for i, line in enumerate(lines):
    if line.strip().find(header.strip()) >  -1:
      startIndex = i - 1
      break
  
  for i, line in enumerate(lines):
    if line.strip().find(tail.strip()) > -1:
      endIndex = i + 1
      break
  
  if startIndex is not None and endIndex is not None:
    new_content = lines[:startIndex] + insert_content + lines[endIndex:]
  else:
    new_content = lines + insert_content

  return new_content
    


if __name__ == '__main__':
  cur_dir = os.path.dirname(__file__)
  # github resource urls
  urls_path = cur_dir + '/hosts.urls'
  # host tempalte
  template_path = cur_dir + '/host-template'
  # temp hosts file
  local_host = cur_dir +'/hosts' 
  #
  host_path = 'C:\Windows\System32\drivers\etc\hosts'
 
  with open(urls_path) as fs:
    urls = list(map(lambda x:x.replace('\n', ''), fs.readlines()))
  
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
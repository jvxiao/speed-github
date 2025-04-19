from dns import resolver
import time
import os
import shutil


# github resource urls
urls_path = os.path.dirname(__file__) + '/hosts.urls'

def get_github_domains():
  with open(urls_path) as fs:
    urls = list(map(lambda x:x.replace('\n', ''), fs.readlines()))
  return urls

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
    



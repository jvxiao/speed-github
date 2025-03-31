from dns import resolver
import time

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

if __name__ == '__main__':

  with open('./hosts.urls') as fs:
    urls = list(map(lambda x:x.replace('\n', ''), fs.readlines()))
  
  host_map = get_all_ips(urls)
 
  host_str = ''
  for key in host_map:
    if host_map[key] is not None:
      host_str += '{0:<70} {1}\n'.format(key, host_map[key])
  
  with open('./host-template') as ft:
    template = ''.join(ft.readlines())
  
  content = template.replace('{{ hosts }}', host_str)
  content = content.replace('{{ time }}', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
  
  with open('./hosts', 'w+', encoding='utf-8') as fh:
    fh.write(content)
  
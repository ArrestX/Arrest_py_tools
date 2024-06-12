from lxml import etree
from argparse import ArgumentParser

def main(xml_path, output):
    # 解析XML文件
    tree = etree.parse(xml_path)
    root = tree.getroot()

    # 按照servlet分组输出servlet元素的信息
    servlets = {}
    for servlet in root.findall('{http://java.sun.com/xml/ns/javaee}servlet'):
        servlet_name = servlet.find('{http://java.sun.com/xml/ns/javaee}servlet-name').text
        servlets[servlet_name] = {
            'servlet-class': servlet.find('{http://java.sun.com/xml/ns/javaee}servlet-class').text,
            'url-patterns': []
        }
        for mapping in root.findall('{http://java.sun.com/xml/ns/javaee}servlet-mapping'):
            if mapping.find('{http://java.sun.com/xml/ns/javaee}servlet-name').text == servlet_name:
                servlets[servlet_name]['url-patterns'].append(mapping.find('{http://java.sun.com/xml/ns/javaee}url-pattern').text)

    # 输出按照servlet分组的结果
    with open(output, 'w') as f:
        for servlet_name, servlet_info in servlets.items():
            for pattern in servlet_info['url-patterns']:
                f.write(pattern + " --> " + servlet_name + " --> " + servlet_info['servlet-class'])
            f.write('\n')
    print("[+] 解析成功，请查看当前目录下" + output)
    
if __name__ == '__main__':
    show = r'''
                        _                               
                       | |                              
        __  ___ __ ___ | |    _ __   __ _ _ __ ___  ___ 
        \ \/ / '_ ` _ \| |   | '_ \ / _` | '__/ __|/ _ \
         >  <| | | | | | |   | |_) | (_| | |  \__ \  __/
        /_/\_\_| |_| |_|_|   | .__/ \__,_|_|  |___/\___|
                       ______| |                        
                      |______|_|                        
                                    
                 @用于提取web.xml文件的servlet小脚本
    '''
    print(show + '\n')
    arg = ArgumentParser(description='提取web.xml文件的servlet小脚本')
    arg.add_argument('xml_path', help='xml文件路径 egg: web.xml')
    arg.add_argument('-o', '--output', help='结果输出路径', dest='output', type=str)
    result = arg.parse_args()
    main(result.xml_path, result.output)

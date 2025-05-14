"""
练习: 字符串分割

描述：
使用split()方法分割字符串，提取关键信息。

请补全下面的函数，使用split()方法分割字符串并提取所需信息。
"""

def extract_keywords(text):
    """
    从文本中提取关键词
    
    参数:
    - text: 包含关键词的文本字符串，关键词之间用空格分隔
    
    返回:
    - 提取出的关键词列表
    """
    # 请在下方编写代码
    # 使用split()方法分割字符串，返回关键词列表
    return text.strip().split()
    pass

def parse_csv_line(csv_line):
    """
    解析CSV格式的一行数据
    
    参数:
    - csv_line: CSV格式的字符串，字段之间用逗号分隔
    
    返回:
    - 包含各字段的列表
    """
    # 请在下方编写代码
    # 使用split()方法分割CSV行，返回字段列表
    fields = csv_line.split(',')
    result = []
    current = []
    in_quotes = False

    for field in fields:
        stripped = field.strip()
        if in_quotes:
            current.append(field)
            if stripped.endswith('"'):
                # 合并引号内的字段并清理格式
                merged = ','.join(current)
                # 去除首尾引号并处理转义引号
                if merged.startswith('"') and merged.endswith('"'):
                    merged = merged[1:-1].replace('""', '"')
                result.append(merged)
                current = []
                in_quotes = False
        else:
            if stripped.startswith('"'):
                in_quotes = True
                # 去除起始引号并保留内容
                current.append(field[1:])
            else:
                result.append(field)

    # 处理未闭合的引号（假设输入合法）
    if current:
        merged = ','.join(current).replace('""', '"')
        result.append(merged)

    return result
    pass

def extract_name_and_domain(email):
    """
    从电子邮件地址中提取用户名和域名
    
    参数:
    - email: 电子邮件地址字符串，格式为username@domain.com
    
    返回:
    - 包含用户名和域名的元组 (username, domain)
    """
    # 请在下方编写代码
    # 使用split()方法分割电子邮件地址，返回用户名和域名的元组
    parts = email.split('@')
    if len(parts) != 2:
        raise ValueError("Invalid email format")
    return (parts[0], parts[1])
    pass 
def read_logs():
    with open('./application.log','r',encoding='utf-8') as f:
        content =  f.read() 
    return content


def analyze_logs():
    content = read_logs()

    print(content.splitlines())

    log_status = {
        "ERROR": 0,
        "WARNING": 0,
        "INFO": 0
    }

    for line in content.splitlines():
        for status in log_status:
            if status in line.upper():
                log_status[status] += 1

    return log_status



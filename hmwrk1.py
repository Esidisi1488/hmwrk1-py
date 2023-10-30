
def parse(query: str) -> dict:
    if query.find('?') != -1:
        list_query = query.split('?')[1].split('&')
    else:
        list_query = ['']
    print({x.split('=')[0]: x.split('=')[1] for x in list_query if x != ""})
    return {x.split('=')[0]: x.split('=')[1] for x in list_query if x != ""}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}


def parse_cookie(query: str) -> dict:
    if query.find(';') != -1:
        list_query = query.split(';')
    else:
        list_query = ['']
    print({x.split('=',1)[0]: x.split('=',1)[1] for x in list_query if x != ""})
    return {x.split('=',1)[0]: x.split('=',1)[1] for x in list_query if x != ""}


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}

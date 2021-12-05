def parse_cookie(query):
	from http import cookies
	C = cookies.SimpleCookie()
	query = query.replace("&", ";")
	C.load(query)
	
	cookies = {k : v.value for k, v in C.items()}
	
	return cookies

if __name__ == '__main__':


    # Testing function `parse_cookie`
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Di=ma;') == {'name': 'Di=ma'}
    assert parse_cookie('name==Dima;age=28;') == {'name': '=Dima', 'age': '28'}
    assert parse_cookie('   ') == {}
    assert parse_cookie('index=None;') == {'index': 'None'}
    assert parse_cookie('name=Dima&age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('123') == {}

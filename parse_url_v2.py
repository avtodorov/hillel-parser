def parse(url):
	from urllib import parse

	res = dict(parse.parse_qsl(parse.urlsplit(url).query))

	return res

	
if __name__ == '__main__':

    # Testing function `parse`
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/') == {}
    assert parse('https://example.com/?') == {}
    assert parse('https://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=ferret&&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=') == {}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&id=123') == {'name': 'ferret', 'color': 'purple', 'id': '123'}
    assert parse('https://example.com/path/to/page?name=&color=&id=123') == {'id': '123'}
    assert parse('https://example.com//') == {}

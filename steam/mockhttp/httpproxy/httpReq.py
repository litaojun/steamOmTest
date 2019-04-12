from urllib.parse import unquote, quote

class Request:
    def __init__(self, r):
        self.content = r
        self.method = r.split()[0]
        self.path = r.split()[1]
        self.body = r.split('\r\n\r\n', 1)[1]

    def form_body(self):
        return self._parse_parameter(self.body)

    def parse_path(self):
        index = self.path.find('?')
        if index == -1:
            return self.path, {}
        else:
            path, query_string = self.path.split('?', 1)
            query = self._parse_parameter(query_string)
            return path, query

    @property
    def headers(self):
        header_content = self.content.split('\r\n\r\n', 1)[0].split('\r\n')[1:]
        result = {}
        for line in header_content:
            k, v = line.split(': ')
            result[quote(k)] = quote(v)
        return result

    @staticmethod
    def _parse_parameter(parameters):
        args = parameters.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = unquote(v)
        return query
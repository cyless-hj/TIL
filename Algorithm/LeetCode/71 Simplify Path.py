class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        while '' in path:
            path.remove('')
        while '.' in path:
            path.remove('.')
        
        while '..' in path:
            idx = path.index('..')
            del path[idx]
            if idx > 0:
                del path[idx-1]
        
        path = '/' + '/'.join(path)
        return path
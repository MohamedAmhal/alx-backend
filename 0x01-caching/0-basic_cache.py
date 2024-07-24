#!/usr/bin/python3
'''
documentation !
documentation ?
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    documentation
    inhhh
    docummentation added !!
    '''

    def put(self, key, item):
        '''
        doc
        doc
        doc doc doc doc od co doc
        '''
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''
        documentation
        documentation
        doc doc odc
        '''
        if (key is None or key not in self.cache_data.keys()):
            return None
        else:
            return self.cache_data[key]

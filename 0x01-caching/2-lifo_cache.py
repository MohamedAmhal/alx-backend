#!/usr/bin/python3
'''
documentation !
documentation ?
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    docummentation
    doc doc doc doc doc doc
    doc doc doc doc
    docccccccc
    '''
    dernel = None

    def put(self, key, item):
        '''
        doc doc doc doc doc doc
        doc dcod cod c
        dcoc dodc
        '''

        if (key is None or item is None):
            pass
        elif (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
              key not in self.cache_data.keys()):
            print("DISCARD:", LIFOCache.dernel)
            self.cache_data.pop(LIFOCache.dernel)
            self.cache_data[key] = item
            LIFOCache.dernel = key
        else:
            self.cache_data[key] = item
            LIFOCache.dernel = key

    def get(self, key):
        '''
        documentation !!
        documentation !!
        aaaaaaa aaaaaaaa
        '''
        if (key is None or key not in self.cache_data.keys()):
            return None
        else:
            return self.cache_data[key]

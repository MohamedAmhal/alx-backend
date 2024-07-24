#!/usr/bin/python3
'''
documentation !
documentation ?
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    documentation !!
    doc odc doc doc odc
    doc doc od co
    '''
    def put(self, key, item):
        '''
        doc doc doc odc
        documentation !!
        '''
        if (key is None or item is None):
            pass
        elif (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
              key not in self.cache_data.keys()):
            print("DISCARD:", list(self.cache_data.keys())[0])
            self.cache_data.pop(list(self.cache_data.keys())[0])
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

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

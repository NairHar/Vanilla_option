import pytest
from bs import price as bs

class TestVanilla(unittest.TestCase):
    
    def test_call(self):
        call_price = bs.Price(60,65,0.08,0.30,0.25,0)
        result = call_price.call()
        self.assertEqual(result,2.13337)
        
    def test_put(self):
        put_price = bs.Price(60,65,0.08,0.30,0.25,0)
        result = put_price.put()
        self.assertEqual(result,5.84628)
        
if __name__ == '__main__':
    pytest.main()
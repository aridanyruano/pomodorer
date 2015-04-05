import logging,unittest,queue_system

class TestQueueSystem(unittest.TestCase):
    
    def setUp(self):
        self.empty_queue_system = queue_system.MessageQueueSystem()
        
    def test_init_queue_should_add_new_queue(self):
        prev_value = len(self.empty_queue_system._queues)
        self.empty_queue_system.init_queue("nueva")
        self.assertEqual(prev_value+1, len(self.empty_queue_system._queues), 'no ha\
             sumado un solo elemento al listado')
        self.assertTrue("nueva" in self.empty_queue_system._queues, "no hay una cola\
             con el id pasado")
        self.assertEqual(0,len(self.empty_queue_system._queues['nueva']._subscribers),
            "¿recien creado y con subscriptores?")
    
    def test_subscribe_should_add_new_subscriptor(self):
        #preparo el test
        self.empty_queue_system.init_queue("nueva")
        self.empty_queue_system.subscribe("nueva",lambda x : f)
        
        
if __name__ == '__main__':
    logging.debug("en metodo main")
    unittest.main()
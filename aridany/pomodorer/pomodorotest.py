import logging,unittest,pomodoro

class TestPomodoro(unittest.TestCase):
    
    def setUp(self):
        logging.debug("en metodo setUp")
        self.empty_pomodorer = pomodoro.Pomodorer()
        self.pomodorer_filled = pomodoro.Pomodorer()
        self.pomodorer_filled._report = []
    
    
    def test_run_pomodoro_should_return_one_when_empty(self):
        logging.debug("en metodo de test del run")
        return_value = self.empty_pomodorer.run_pomodoro()
        self.assertEqual(1, return_value ,'Pomodorer vacio no devuelve id correcto')
    
    def test_reset_series_should_add_an_element_to_report(self):
        logging.debug("en metodo de test del reset")
        value_before = len(self.empty_pomodorer._report)
        self.empty_pomodorer.reset_series()
        self.assertEqual(value_before, return_value, """reset_series no suma un elemento 
            en el listado""")
    
    
if __name__ == '__main__':
    logging.debug("en metodo main")
    unittest.main()
        
    
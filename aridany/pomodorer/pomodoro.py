class Pomodorer:
    """Clase que representa la interfaz de comunicacion de un sistema pomodoro"""
    def __init__(self, event_system):
        self._report = [[]]
        self.event_system = event_system
    
    def run_pomodoro(self):
        pass
    
    def get_report(self):
        agg = []
        for series in self._report:
            agg+series
        return agg
    
    def reset_series(self):
        self._report = self._report + []
    
    def main():
        print('Pruebas no implementadas')
    
    if __name__ == '__main__':
        main()
    
    
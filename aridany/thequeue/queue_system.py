import logging
class MessageQueueSystem:
    """Clase que representa un sistema de subscripcion, publicacion de cola de mensajeria"""
    def __init__(self):
        self._queues = {}
        
    def subscribe(self,queue_id,callback):
        queue = _get_queue(queue_id)
        queue.subscribers.append(callback)
            
    
    def init_queue(self, queue_id):
        queue = self._Queue(queue_id)
        self._queues[queue_id] = queue
    
    def publish_message(self,queue_id,message):
        queue = _get_queue(queue_id)
        for subs in queue._subscribers:
            try:
                subs(message)
            except BaseException: #ninguna excepcion debe detener el flujo
                logging.warning("un metodo de callbak ha fallado: " + subs)

    def _get_queue(queue_id):
        if queue_id in self._queues:
            return self._queues[queue_id]
        else:
            raise QueueException("no existe esta cola: "+queue_id)

    class _Queue:
        """"Clases que representa una cola individual"""
        def __init__(self,queue_id):
            self._id = queue_id #¿Tiene sentido este atributo?
            self._queue = []
            self._subscribers = []


class QueueException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
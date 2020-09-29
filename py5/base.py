class Py5Base:

    def __init__(self, instance):
        self._instance = instance

    def _shutdown(self):
        self._shutdown_complete = True

    def _replace_instance(self, new_instance):
        self._instance = new_instance

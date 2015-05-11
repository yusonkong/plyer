class Audio(object):
    """Audio Facade.
    Used for recording audio.
    Use method `start` to start record and `stop` for stop recording.
    For hear, what you have just recorded use method `play`.

    Status will tell you about current job of the Audio.

    .. note::
        You need android permissions: RECORD_AUDIO
    """

    _state = 'ready'
    _file_path = ''

    def __init__(self, file_path):
        super(Audio, self).__init__()
        self._file_path = file_path

    def _prepare(self):
        raise NotImplementedError

    def start(self):
        """Start record."""
        self._start()
        self._state = 'recording'

    def _start(self):
        raise NotImplementedError()

    def stop(self):
        """Stop record."""
        self._stop()
        self._state = 'ready'

    def _stop(self):
        raise NotImplementedError()

    def play(self):
        """Play current recording."""
        self._play()
        self._state = 'playing'

    def _play(self):
        raise NotImplementedError()

    @property
    def state(self):
        """Return status of Microphone."""
        return self._state

    @state.setter
    def state(self, status):
        self._state = status

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, location):
        """Location of the recording."""
        assert isinstance(location, (basestring, unicode)), \
            'Location must be string or unicode'
        self._file_path = location

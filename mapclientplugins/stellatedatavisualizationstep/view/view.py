from PySide import QtGui, QtCore

from .ui_view import Ui_StellateVisualizationWidget

from opencmiss.zinchandlers.scenemanipulation import SceneManipulation


class View(QtGui.QWidget):

    def __init__(self, model, parent=None):
        super(View, self).__init__(parent)
        self._ui = Ui_StellateVisualizationWidget()
        self._ui.setupUi(self)

        self._setup_handlers()

        self._model = model
        self._ui.sceneviewerWidget.set_context(self._model.get_context())

        self._done_callback = None
        self._settings = {'view-parameters': {}}

        self._make_connections()

    def _make_connections(self):
        self._ui.sceneviewerWidget.graphics_initialized.connect(self._graphics_initialized)

    def _graphics_initialized(self):
        scene_viewer = self._ui.sceneviewerWidget.get_zinc_sceneviewer()
        if scene_viewer is not None:
            scene = self._model.get_scene()
            self._ui.sceneviewerWidget.set_scene(scene)
            if len(self._settings['view-parameters']) == 0:
                self._view_all()
            else:
                eye = self._settings['view-parameters']['eye']
                look_at = self._settings['view-parameters']['look_at']
                up = self._settings['view-parameters']['up']
                angle = self._settings['view-parameters']['angle']
                self._ui.sceneviewerWidget.set_view_parameters(eye, look_at, up, angle)

    def _view_all(self):
        if self._ui.sceneviewerWidget.get_zinc_sceneviewer() is not None:
            self._ui.sceneviewerWidget.view_all()

    def register_done_callback(self, done_callback):
        self._done_callback = done_callback

    def _setup_handlers(self):
        basic_handler = SceneManipulation()
        self._ui.sceneviewerWidget.register_handler(basic_handler)

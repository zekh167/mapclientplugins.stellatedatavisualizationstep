from opencmiss.zinc.status import OK as ZINC_OK
from opencmiss.zinc.graphics import Graphics


class CubeModel(object):

    def __init__(self, filename, context, region, material_module):
        self._filename = filename
        self._context = context
        self._region = region
        self._material_module = material_module

        self._coordinates = None
        self._scene = None
        self._magnitude = None

        self._load()
        self._generate_mesh()
        self._setup_scene()

    def _load(self):
        result = self._region.readFile(self._filename)
        if result == ZINC_OK:
            pass
        else:
            print("Scaffold ex file was not read correctly! Check the path.")

    def _setup_scene(self):
        self._scene.beginChange()
        self._create_graphics()
        self._scene.endChange()

    def _create_scene(self):
        return self._region.getScene()

    def _create_graphics(self):
        self._create_line_graphics()
        self._create_surface_graphics()

    def _create_line_graphics(self):
        lines = self._scene.createGraphicsLines()
        lines.setCoordinateField(self._coordinates)
        lines.setName('display_lines')
        black = self._material_module.findMaterialByName('cube_lines')
        lines.setMaterial(black)
        return lines

    def _create_surface_graphics(self):
        surface = self._scene.createGraphicsSurfaces()
        surface.setCoordinateField(self._coordinates)
        surface.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_SHADED)
        surface_material = self._material_module.findMaterialByName('cube_surface')
        surface.setMaterial(surface_material)
        surface.setName('display_surface')
        # surface.setVisibilityFlag(self.is_display_surface('display_surface'))
        return surface

    def _generate_mesh(self):
        fm = self._region.getFieldmodule()
        fm.beginChange()
        self._coordinates = fm.findFieldByName('coordinates')
        self._scene = self._region.getScene()
        self._magnitude = fm.createFieldMagnitude(self._coordinates)
        self._magnitude.setName('magnitude')
        self._magnitude.setManaged(True)
        fm.endChange()

    def get_scene(self):
        return self._scene

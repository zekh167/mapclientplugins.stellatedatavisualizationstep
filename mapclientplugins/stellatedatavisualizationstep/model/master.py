from opencmiss.zinc.context import Context
from opencmiss.zinc.material import Material

from opencmiss.utils.zinc import define_standard_visualisation_tools

from .cube_model import CubeModel


class MasterModel(object):

    def __init__(self, filename):
        self._context = Context('Cube')
        define_standard_visualisation_tools(self._context)
        self._material_module = self._context.getMaterialmodule()
        self._initialize_material()

        self._region = self._context.getDefaultRegion()
        self._cube_model = CubeModel(filename, self._context, self._region, self._material_module)

    def _initialize_material(self):
        tess = self._context.getTessellationmodule().getDefaultTessellation()
        tess.setRefinementFactors(12)
        self._material_module.defineStandardMaterials()
        cube_surface = self._material_module.createMaterial()
        cube_surface.setName('cube_surface')
        cube_surface.setManaged(True)
        cube_surface.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.8, 0.43, 0.33])
        cube_surface.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.8, 0.43, 0.33])
        cube_surface.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
        cube_surface.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.2, 0.2, 0.3])
        cube_surface.setAttributeReal(Material.ATTRIBUTE_ALPHA, 0.4)
        cube_surface.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.6)
        glyphmodule = self._context.getGlyphmodule()
        glyphmodule.defineStandardGlyphs()

    def get_context(self):
        return self._context

    def get_region(self):
        return self._region

    def get_scene(self):
        return self._cube_model.get_scene()

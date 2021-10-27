# Create a map using SimpleRenderer
# Data used is from The Railroad Commission of Texas
# https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/#digital-map-data-table

import arcpy

# Reference project file
project = arcpy.mp.ArcGISProject(r"C:/GIS/arcpy/arcpy_simple_render/arcpy_simple_render.aprx")

# Reference map in project
brazos_surface_wells = project.listMaps("Brazos County Surface Oil Wells")[0]

# Loop thru all available layers in map
for layer in brazos_surface_wells.listLayers():
    # Check that layer is a feature layer
    if layer.isFeatureLayer:
        # Get copy of layer's symbology
        symbology = layer.symbology
        # Make sure symbology has attribute 'renderer'
        if hasattr(symbology, 'renderer'):
            # Check if the layers name is 'well041s'
            # 'well041s' is the name of the shapefile provided by RRC
            # 041: Brazos county FIPS
            # s: 'Surface'
            if layer.name == "well041s":
                # Update the copy's renderer
                symbology.updateRenderer("SimpleRenderer")
                # Set the layer's symbology equal to copy
                layer.symbology = symbology
            else:
                print("Incorrect layer.")

project.saveACopy(r"c:/GIS/arcpy/arcpy_simple_render/brazos_co_s_wells.aprx")


print("Success")

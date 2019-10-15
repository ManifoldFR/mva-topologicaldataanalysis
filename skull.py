# state file generated using paraview version 5.6.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.6.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [988, 799]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-0.14241031557321548, 0.00016799569129943848, 0.00036950409412384033]
renderView1.HiddenLineRemoval = 1
renderView1.StereoType = 0
renderView1.CameraPosition = [1.1242974220913473, -2.4201909523716365, 0.3182156781026047]
renderView1.CameraFocalPoint = [-0.14241031557321546, 0.00016799569129939264, 0.000369504094123865]
renderView1.CameraViewUp = [-0.04567923171316795, 0.1065302893041602, 0.9932596363745316]
renderView1.CameraParallelScale = 0.7118094117210131
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.Visibility = 1
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
skullvtu = XMLUnstructuredGridReader(FileName=['/home/manifold/Documents/TopoDataAnalysis/tda-work/bettiData/skull.vtu'])
skullvtu.PointArrayStatus = []

# create a new 'Clip'
clip1 = Clip(Input=skullvtu)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Morse field']
clip1.Value = 50.0

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [-0.019451397676184617, 0.00016799569129943848, 0.00036950409412384033]

# create a new 'Calculator'
calculator1 = Calculator(Input=skullvtu)
calculator1.Function = ''

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=calculator1)

# create a new 'Connectivity'
connectivity1 = Connectivity(Input=extractSurface1)

# create a new 'Extract Edges'
extractEdges1 = ExtractEdges(Input=connectivity1)

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=connectivity1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface2)

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=skullvtu)

# create a new 'Clip'
clip2 = Clip(Input=appendDatasets1)
clip2.ClipType = 'Plane'
clip2.Scalars = [None, '']

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [-9.506940841674805e-06, 0.00016799569129943848, 0.00036950409412384033]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from connectivity1
connectivity1Display = Show(connectivity1, renderView1)

# get color transfer function/color map for 'RegionId'
regionIdLUT = GetColorTransferFunction('RegionId')
regionIdLUT.AutomaticRescaleRangeMode = 'Never'
regionIdLUT.RGBPoints = [1.1757813367477766e-42, 0.231373, 0.298039, 0.752941, 1.1757813367477768e-38, 0.0, 0.6666666666666666, 0.0]
regionIdLUT.ColorSpace = 'RGB'
regionIdLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
connectivity1Display.Representation = 'Surface'
connectivity1Display.ColorArrayName = ['POINTS', 'RegionId']
connectivity1Display.LookupTable = regionIdLUT
connectivity1Display.Opacity = 0.65
connectivity1Display.OSPRayScaleArray = 'RegionId'
connectivity1Display.OSPRayScaleFunction = 'PiecewiseFunction'
connectivity1Display.SelectOrientationVectors = 'None'
connectivity1Display.ScaleFactor = 0.0
connectivity1Display.SelectScaleArray = 'RegionId'
connectivity1Display.GlyphType = 'Arrow'
connectivity1Display.GlyphTableIndexArray = 'RegionId'
connectivity1Display.SetScaleArray = ['POINTS', 'RegionId']
connectivity1Display.ScaleTransferFunction = 'PiecewiseFunction'
connectivity1Display.OpacityArray = ['POINTS', 'RegionId']
connectivity1Display.OpacityTransferFunction = 'PiecewiseFunction'
connectivity1Display.DataAxesGrid = 'GridAxesRepresentation'
connectivity1Display.SelectionCellLabelFontFile = ''
connectivity1Display.SelectionPointLabelFontFile = ''
connectivity1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
connectivity1Display.DataAxesGrid.XTitleFontFile = ''
connectivity1Display.DataAxesGrid.YTitleFontFile = ''
connectivity1Display.DataAxesGrid.ZTitleFontFile = ''
connectivity1Display.DataAxesGrid.XLabelFontFile = ''
connectivity1Display.DataAxesGrid.YLabelFontFile = ''
connectivity1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
connectivity1Display.PolarAxes.PolarAxisTitleFontFile = ''
connectivity1Display.PolarAxes.PolarAxisLabelFontFile = ''
connectivity1Display.PolarAxes.LastRadialAxisTextFontFile = ''
connectivity1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from extractEdges1
extractEdges1Display = Show(extractEdges1, renderView1)

# trace defaults for the display properties.
extractEdges1Display.Representation = 'Surface'
extractEdges1Display.ColorArrayName = ['POINTS', 'RegionId']
extractEdges1Display.LookupTable = regionIdLUT
extractEdges1Display.OSPRayScaleArray = 'RegionId'
extractEdges1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractEdges1Display.SelectOrientationVectors = 'None'
extractEdges1Display.ScaleFactor = 0.0
extractEdges1Display.SelectScaleArray = 'RegionId'
extractEdges1Display.GlyphType = 'Arrow'
extractEdges1Display.GlyphTableIndexArray = 'RegionId'
extractEdges1Display.SetScaleArray = ['POINTS', 'RegionId']
extractEdges1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractEdges1Display.OpacityArray = ['POINTS', 'RegionId']
extractEdges1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractEdges1Display.DataAxesGrid = 'GridAxesRepresentation'
extractEdges1Display.SelectionCellLabelFontFile = ''
extractEdges1Display.SelectionPointLabelFontFile = ''
extractEdges1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractEdges1Display.DataAxesGrid.XTitleFontFile = ''
extractEdges1Display.DataAxesGrid.YTitleFontFile = ''
extractEdges1Display.DataAxesGrid.ZTitleFontFile = ''
extractEdges1Display.DataAxesGrid.XLabelFontFile = ''
extractEdges1Display.DataAxesGrid.YLabelFontFile = ''
extractEdges1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractEdges1Display.PolarAxes.PolarAxisTitleFontFile = ''
extractEdges1Display.PolarAxes.PolarAxisLabelFontFile = ''
extractEdges1Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractEdges1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from generateSurfaceNormals1
generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1)

# trace defaults for the display properties.
generateSurfaceNormals1Display.Representation = 'Surface'
generateSurfaceNormals1Display.ColorArrayName = ['POINTS', 'RegionId']
generateSurfaceNormals1Display.LookupTable = regionIdLUT
generateSurfaceNormals1Display.Opacity = 0.58
generateSurfaceNormals1Display.OSPRayScaleArray = 'RegionId'
generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.SelectOrientationVectors = 'None'
generateSurfaceNormals1Display.ScaleFactor = 0.0
generateSurfaceNormals1Display.SelectScaleArray = 'RegionId'
generateSurfaceNormals1Display.GlyphType = 'Arrow'
generateSurfaceNormals1Display.GlyphTableIndexArray = 'RegionId'
generateSurfaceNormals1Display.SetScaleArray = ['POINTS', 'RegionId']
generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.OpacityArray = ['POINTS', 'RegionId']
generateSurfaceNormals1Display.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals1Display.SelectionCellLabelFontFile = ''
generateSurfaceNormals1Display.SelectionPointLabelFontFile = ''
generateSurfaceNormals1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
generateSurfaceNormals1Display.DataAxesGrid.XTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.YTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.ZTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.XLabelFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.YLabelFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
generateSurfaceNormals1Display.PolarAxes.PolarAxisTitleFontFile = ''
generateSurfaceNormals1Display.PolarAxes.PolarAxisLabelFontFile = ''
generateSurfaceNormals1Display.PolarAxes.LastRadialAxisTextFontFile = ''
generateSurfaceNormals1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from clip2
clip2Display = Show(clip2, renderView1)

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = [None, '']
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.ScaleFactor = 0.0
clip2Display.SelectScaleArray = 'None'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'None'
clip2Display.SetScaleArray = [None, '']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = [None, '']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.SelectionCellLabelFontFile = ''
clip2Display.SelectionPointLabelFontFile = ''
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityUnitDistance = 0.0325236778318958

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip2Display.DataAxesGrid.XTitleFontFile = ''
clip2Display.DataAxesGrid.YTitleFontFile = ''
clip2Display.DataAxesGrid.ZTitleFontFile = ''
clip2Display.DataAxesGrid.XLabelFontFile = ''
clip2Display.DataAxesGrid.YLabelFontFile = ''
clip2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip2Display.PolarAxes.PolarAxisTitleFontFile = ''
clip2Display.PolarAxes.PolarAxisLabelFontFile = ''
clip2Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for regionIdLUT in view renderView1
regionIdLUTColorBar = GetScalarBar(regionIdLUT, renderView1)
regionIdLUTColorBar.Title = 'RegionId'
regionIdLUTColorBar.ComponentTitle = ''
regionIdLUTColorBar.TitleFontFile = ''
regionIdLUTColorBar.LabelFontFile = ''

# set color bar visibility
regionIdLUTColorBar.Visibility = 1

# show color legend
connectivity1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
extractEdges1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
generateSurfaceNormals1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'RegionId'
regionIdPWF = GetOpacityTransferFunction('RegionId')
regionIdPWF.Points = [1.1757813367477766e-42, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
regionIdPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(clip2)
# ----------------------------------------------------------------
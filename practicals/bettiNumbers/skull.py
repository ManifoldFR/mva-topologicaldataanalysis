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
renderView1.ViewSize = [759, 799]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-0.14241031557321548, 0.00016799569129943848, 0.00036950409412384033]
renderView1.HiddenLineRemoval = 1
renderView1.StereoType = 0
renderView1.CameraPosition = [0.9435697772784123, -2.3022736703830007, 0.4452936005614458]
renderView1.CameraFocalPoint = [-0.12428619381500648, 0.1832404651227817, -0.05030223039703619]
renderView1.CameraViewUp = [-0.05960500062248403, 0.17050590095359897, 0.9835522261887242]
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
xMLUnstructuredGridReader1 = XMLUnstructuredGridReader(FileName=['/home/manifold/Documents/TopoDataAnalysis/tda-work/bettiData/skull.vtu'])
xMLUnstructuredGridReader1.PointArrayStatus = []

# create a new 'Clip'
clip2 = Clip(Input=xMLUnstructuredGridReader1)
clip2.ClipType = 'Plane'
clip2.Scalars = ['POINTS', 'Morse field']
clip2.Value = 50.0
clip2.Crinkleclip = 1

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [-0.019451397676184617, 0.00016799569129943848, 0.00036950409412384033]

# create a new 'Calculator'
calculator1 = Calculator(Input=xMLUnstructuredGridReader1)
calculator1.Function = ''

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=calculator1)

# create a new 'Connectivity'
connectivity1 = Connectivity(Input=extractSurface1)

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=connectivity1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface2)

# create a new 'Extract Edges'
extractEdges1 = ExtractEdges(Input=connectivity1)

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[connectivity1, extractEdges1])

# create a new 'Clip'
clip1 = Clip(Input=appendDatasets1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'RegionId']
clip1.Crinkleclip = 1

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [-0.005461714134709107, -0.028723511656367863, -0.051438075181051444]
clip1.ClipType.Normal = [0.7039527663641628, -0.3076643214105468, 0.6401508947578144]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from generateSurfaceNormals1
generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1)

# get color transfer function/color map for 'RegionId'
regionIdLUT = GetColorTransferFunction('RegionId')
regionIdLUT.AutomaticRescaleRangeMode = 'Never'
regionIdLUT.RGBPoints = [1.1757813367477766e-42, 0.231373, 0.298039, 0.752941, 1.1757813367477768e-38, 0.0, 0.6666666666666666, 0.0]
regionIdLUT.ColorSpace = 'RGB'
regionIdLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
generateSurfaceNormals1Display.Representation = 'Surface'
generateSurfaceNormals1Display.ColorArrayName = ['POINTS', 'RegionId']
generateSurfaceNormals1Display.LookupTable = regionIdLUT
generateSurfaceNormals1Display.Opacity = 0.76
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

# show data from clip1
clip1Display = Show(clip1, renderView1)

# get opacity transfer function/opacity map for 'RegionId'
regionIdPWF = GetOpacityTransferFunction('RegionId')
regionIdPWF.Points = [1.1757813367477766e-42, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
regionIdPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', '']
clip1Display.LookupTable = regionIdLUT
clip1Display.Opacity = 0.76
clip1Display.Specular = 0.33
clip1Display.OSPRayScaleArray = 'RegionId'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.0
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.SetScaleArray = ['POINTS', 'RegionId']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'RegionId']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = regionIdPWF
clip1Display.ScalarOpacityUnitDistance = 0.0325236778318958

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from clip2
clip2Display = Show(clip2, renderView1)

# trace defaults for the display properties.
clip2Display.Representation = 'Surface With Edges'
clip2Display.ColorArrayName = ['POINTS', '']
clip2Display.Opacity = 0.89
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.ScaleFactor = 0.0
clip2Display.SelectScaleArray = 'None'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'None'
clip2Display.SetScaleArray = ['POINTS', '']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', '']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.SelectionCellLabelFontFile = ''
clip2Display.SelectionPointLabelFontFile = ''
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityUnitDistance = 0.033066327741430056

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
generateSurfaceNormals1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(clip1)
# ----------------------------------------------------------------
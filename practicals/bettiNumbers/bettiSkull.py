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
renderView1.CenterOfRotation = [-9.506940841674805e-06, 0.00016799569129943848, 0.00036950409412384033]
renderView1.StereoType = 0
renderView1.CameraPosition = [0.019853041514529938, -3.089101183107915, 0.29250581638608575]
renderView1.CameraFocalPoint = [-9.50694084167463e-06, 0.00016799569129943853, 0.00036950409412384]
renderView1.CameraViewUp = [-0.013448616464895194, 0.09405063629951246, 0.9954765755791731]
renderView1.CameraParallelScale = 0.8057841639433522
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
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
skullvtu.PointArrayStatus = ['Morse field']

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=skullvtu)

# create a new 'Clip'
clip1 = Clip(Input=extractSurface1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Morse field']
clip1.Value = 50.0
clip1.Crinkleclip = 1

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.03326818869737608, -0.015422794456484375, -0.037203741181040244]
clip1.ClipType.Normal = [0.9293389722245448, -0.01121599701401431, 0.3690572802636585]

# create a new 'Connectivity'
connectivity1 = Connectivity(Input=clip1)

# create a new 'TTK BettiNumbers'
tTKBettiNumbers1 = TTKBettiNumbers(Input=connectivity1)
tTKBettiNumbers1.ScalarField = 'Morse field'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from connectivity1
connectivity1Display = Show(connectivity1, renderView1)

# get color transfer function/color map for 'RegionId'
regionIdLUT = GetColorTransferFunction('RegionId')
regionIdLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RegionId'
regionIdPWF = GetOpacityTransferFunction('RegionId')
regionIdPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
connectivity1Display.Representation = 'Surface'
connectivity1Display.ColorArrayName = ['POINTS', 'RegionId']
connectivity1Display.LookupTable = regionIdLUT
connectivity1Display.Opacity = 0.51
connectivity1Display.OSPRayScaleArray = 'RegionId'
connectivity1Display.OSPRayScaleFunction = 'PiecewiseFunction'
connectivity1Display.SelectOrientationVectors = 'Morse field'
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
connectivity1Display.ScalarOpacityFunction = regionIdPWF
connectivity1Display.ScalarOpacityUnitDistance = 0.04864119876418196

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

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(tTKBettiNumbers1)
# ----------------------------------------------------------------
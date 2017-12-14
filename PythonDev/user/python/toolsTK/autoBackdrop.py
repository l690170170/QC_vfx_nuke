#
# Python code by Timur Khodzhaev
#
# - www.chimuru.com
# - chimuru@gmail.com
#

import nuke
import random
import colorsys
import os
import json
import toolsTK.common as tk

def autoBackdrop():
    '''
    Automatically puts a backdrop behind the selected nodes.

    The backdrop will be just big enough to fit all the select nodes in, with room
    at the top for some text in a large font.
    '''
    selNodes = nuke.selectedNodes()
    if not selNodes:
        return

    # Calculate bounds for the backdrop node.
    bdX = min([node.xpos() for node in selNodes])
    bdY = min([node.ypos() for node in selNodes])
    bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
    bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY

    fntSize=0
    presetList=[]
    columns=0
    # Reading settings file
    find_file=tk.where('.autoBackdrop.settings')
    if find_file:
        file=find_file[-1]

        try:
            readFile=open(file,'r')
            dict=json.load(readFile)

            if 'TK_BACKDROP_FONTSIZE' in dict.keys():
                fntSize=dict['TK_BACKDROP_FONTSIZE']
                
            if 'TK_BACKDROP_COLUMNS' in dict.keys():
                columns=dict['TK_BACKDROP_COLUMNS']
                
            if 'TK_BACKDROP_STEP' in dict.keys():
                step=dict['TK_BACKDROP_STEP']
                
            if 'presetList' in dict.keys():
                presetList=dict['presetList']
                
        except Exception,e:
                print('toolsTK::autoBackdropTK: %s' % e)

    # If nothing is set setting to default Values
    if fntSize==0:
        fntSize=50
        
    if columns==0:
        columns=7
        
    if step==0:
        step=50

    if presetList==[]:
        presetList= [
                    [ ' CG '     , 'Shaders.png'     , [0.567, 0.301 ,0.353] ],
                    [ ' FX '     , 'Light.png'       , [0.079, 0.340 ,0.242] ],
                    [ ' 3D '     , 'Geometry.png'    , [0.822, 0.312 ,0.188] ],
                    [ ' Key '    , 'Keyer.png'       , [0.333, 0.243 ,0.290] ],
                    [ 'Cleanup'  , 'FloodFill.png'   , [0.703, 0.280 ,0.322] ],
                    [ ' Ref '    , 'Read.png'        , [0.138, 0.404 ,0.474] ],
                    [ ' Pub '    , 'Vectorfield.png' , [0.221, 0.368 ,0.460] ],
                    [ 'Important', 'Glow.png'        , [0.776, 0.533 ,0.800] ]
                    ]

    # Reading os environment variable to set font size. way around not workind knobDefaults for Backdropnode
    # Overrides settings file

    if os.getenv('TK_BACKDROP_FONTSIZE'):
        fntSize=int(os.getenv('TK_BACKDROP_FONTSIZE'))

    # Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom edges respectively
    left, top, right, bottom = (-30, (-fntSize-72), 30, 30)
    bdX += left
    bdY += top
    bdW += (right - left)
    bdH += (bottom - top)

    R,G,B= colorsys.hsv_to_rgb(random.random(),.1+random.random()*.15,.15+random.random()*.15)

    n = nuke.nodes.BackdropNode(xpos = bdX,
                              bdwidth = bdW,
                              ypos = bdY,
                              bdheight = bdH,
                              tile_color = int('%02x%02x%02x%02x' % (R*255,G*255,B*255,255), 16 ),
                              note_font_size=fntSize)

    n.showControlPanel()

    #Creating additional tabs

    chTab = nuke.Tab_Knob('mainTabTK','backdropTK')
    chLogo= nuke.Text_Knob('logo1','','<font color="lightgreen" size="5">backdrop</font><font color="#FFCC66" size="5">TK</font>')
    chLogo1= nuke.Text_Knob('logo1','','<font color="lightgreen" size="2">by Timur Khodzhaev</font>')
    chlabel = nuke.Link_Knob( 'label_1','label' ) 
    chlabel.makeLink(n.name(), 'label') 
        
    n.addKnob(chTab)
#    n.addKnob(chLogo)
#    n.addKnob(chLogo1)
    n.addKnob( chlabel ) 
        
  
    
    nameList=[]

    # Creating presets buttons in the node

    for i in presetList:
        nameList.append(i[0])
    
    for i,v in enumerate(presetList):
        cmd="import colorsys\nn=nuke.thisNode()\nlist="+str(nameList)+"\nn['icon'].setValue('"+v[1]+"')\nR,G,B= "+str(v[2])+"\nR,G,B=colorsys.hsv_to_rgb(R,G,B)\nn['tile_color'].setValue( int('%02x%02x%02x%02x' % (R*255,G*255,B*255,255), 16 ))\nif ((n['label'].getValue()=='') or (n['label'].getValue() in list)):\n   n['label'].setValue('"+v[0]+"')\n\nallnodes=nuke.allNodes()\nlist=[]\nnd_name='%s_backdrop' % '"+v[0]+"'\ncurName=n['name'].getValue().split(nd_name)\n\nif ((len(curName)>0) and (not curName[0]=='')):\n    for nd in allnodes:\n        splt=nd.name().split(nd_name)\n        if (len(splt)>1):\n            num=splt[1]\n            if num.isdigit():\n                list.append(int(num))\n    if len(list)>0:\n        next=int(sorted(list)[-1])+1 \n    else: next=1\n    n['name'].setValue('%s%s' % (nd_name,next))"



        R,G,B=v[2]
        R,G,B=colorsys.hsv_to_rgb(R,G,B)
        ch_preset = nuke.PyScript_Knob('rndClrs%s' % i ,'<font style="background-color:#%02x%02x%02x"> <img size="8" src="%s">%s</font>' % (R*255,G*255,B*255,v[1],v[0]),cmd)

        n.addKnob(ch_preset)

        if ((i%columns) == 0):
            n['rndClrs%s' % i].setFlag(nuke.STARTLINE)
		
    ch_rndClr = nuke.PyScript_Knob('rndColors',' <img src="ColorBars.png">Randomize color ',"import colorsys, random\nn=nuke.thisNode()\nR,G,B= colorsys.hsv_to_rgb(random.random(),.1+random.random()*.15,.15+random.random()*.15)\nn['tile_color'].setValue( int('%02x%02x%02x%02x' % (R*255,G*255,B*255,255), 16 ) )")

    ch_rndTint = nuke.PyScript_Knob('rndTint',' <img src="HueShift.png">Randomize tint ',"import colorsys, random\nn=nuke.thisNode()\nV=int(n['tile_color'].getValue())\nR = (0xFF & V >> 24) / 255.0\nG = (0xFF & V >> 16) / 255.0\nB = (0xFF & V >> 8) / 255.0\n\nR,G,B= colorsys.rgb_to_hsv(R,G,B)\n\nR,G,B= colorsys.hsv_to_rgb(R,.1+random.random()*.15,.15+random.random()*.15)\nn['tile_color'].setValue( int('%02x%02x%02x%02x' % (R*255,G*255,B*255,255), 16 ) )")

    ch_Grow = nuke.PyScript_Knob('grow',' <img src="MergeMin.png">',"n=nuke.thisNode()\nautoBackdrop.Grow(n,%s)" % step)
    ch_Shrink = nuke.PyScript_Knob('shrink',' <img src="MergeMax.png">',"n=nuke.thisNode()\nautoBackdrop.Shrink(n,%s)" % step)

    n.addKnob(ch_rndClr)
    n['rndColors'].setFlag(nuke.STARTLINE)
    n.addKnob(ch_rndTint)
    n.addKnob(ch_Grow)
    n.addKnob(ch_Shrink)

#    n['rndColors'].setFlag(nuke.STARTLINE)
    
    # Standard chVersion tab
    
    chTab = nuke.Tab_Knob('version','version')
    ch_Class = nuke.Text_Knob('nodeClass','Class:','backdropTK')
    ch_Ver = nuke.Text_Knob('nodeVersion','Version:','v 2.1')
    cmd = 'nukescripts.openurl.start (tk.getHelpUrl(nuke.thisNode()))'

    ch_Help = nuke.PyScript_Knob('chHelp' ,'<img src=":qrc/images/Help.png"> HELP',cmd)
    ch_Help.setTooltip("Opens web page with tool's manual")

    n.addKnob(chTab)
    n.addKnob(ch_Class)
    n.addKnob(ch_Ver)
    n.addKnob(ch_Help)
    n.knob('mainTabTK').setFlag(0) 



    # revert to previous selection

    n['selected'].setValue(True)
    for node in selNodes:
        node['selected'].setValue(True)


    # Backdrop depth sorting script (not mine)
    
    sel = nuke.selectedNodes('BackdropNode')
    all = nuke.allNodes('BackdropNode')

    for i in range(0,len(sel)):
        all.sort(key = lambda x: x.screenHeight() * x.screenWidth(), reverse = True)
        try:
            [b.selectNodes() for b in all if (b in sel or len(sel) ==0)]
        except: # This will be used for Nuke versions below 6.3v5
            [selectBackdropContents(b) for b in all if (b in sel or len(sel) ==0)]

    n['selected'].setValue(False)

    return n 

# Function for increasing Backdrop size
def Grow(node=None,step=50):
    try:
        if not node:
            n=nuke.selectedNode()
        else:
            n=node
        n['xpos'].setValue(n['xpos'].getValue()-step)
        n['ypos'].setValue(n['ypos'].getValue()-step)
        n['bdwidth'].setValue(n['bdwidth'].getValue()+step*2)
        n['bdheight'].setValue(n['bdheight'].getValue()+step*2)
    except Exception,e:
        print('Error:: %s' % e)

# Function for decreasing Backdrop size
def Shrink(node=None,step=50):
    try:
        if not node:
            n=nuke.selectedNode()
        else:
            n=node
        n['xpos'].setValue(n['xpos'].getValue()+step)
        n['ypos'].setValue(n['ypos'].getValue()+step)
        n['bdwidth'].setValue(n['bdwidth'].getValue()-step*2)
        n['bdheight'].setValue(n['bdheight'].getValue()-step*2)
    except Exception,e:
        print('Error:: %s' % e)


# How to Install

---

### Copy files
 * HaneBokeh_SS.gizmo
 * sweetberry.png

into your .nuke folder.

---

### Open your menu.py file, and type this:

```python
# HaneBokeh_SS Gizmo ////////////////////////////////////////////////////////////////////////////////////////

#get main toolbar
toolbar = nuke.toolbar("Nodes")

#get 'Sweetberry' menu
ssMenu = toolbar.addMenu("Sweetberry", icon="sweetberry.png")

ssMenu.addCommand('HaneBokeh_SS','nuke.createNode("HaneBokeh_SS")')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
```

---

### restart nuke.

# enjoy!.
# How to Install

---

### Copy files
 * ErodeAlphaDir_SS.gizmo
 * sweetberry.png

into your .nuke folder.

---

### Open your menu.py file, and type this:

```python
# ErodeAlphaDir_SS Gizmo ////////////////////////////////////////////////////////////////////////////////////////

#get main toolbar
toolbar = nuke.toolbar("Nodes")

#get 'Sweetberry' menu
ssMenu = toolbar.addMenu("Sweetberry", icon="sweetberry.png")

ssMenu.addCommand('ErodeAlphaDir_SS','nuke.createNode("ErodeAlphaDir_SS")')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
```

---

### restart nuke.

# enjoy!.
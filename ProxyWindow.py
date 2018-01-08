# coding=utf-8
import maya.cmds as cmds

renderer = cmds.getAttr("defaultRenderGlobals.ren")

def ProxyWindow(any):
    if cmds.window('Proxy_optionsWindow', ex=True):
        cmds.deleteUI('Proxy_optionsWindow', wnd=True)
    win2 = cmds.window('Proxy_optionsWindow', title='Proxy_Window', widthHeight=(300, 200))
    cmds.columnLayout(adj=True)
    cmds.button(l=renderer+u'代理',en=False)
    if renderer is not "Arnold" or "redshift" or "Vray":
        cmds.button(l=u"不支持当前渲染器代理", en=False)
    else:
        cmds.textFieldGrp( label='Group 1', text='Editable')
    cmds.columnLayout(adj=True)
    #cmds.button(l=u'Redshift代理')
    cmds.showWindow(win2)

ProxyWindow(any)
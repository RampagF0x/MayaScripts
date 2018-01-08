# coding=utf-8
import maya.cmds as cmds
def checkRender(any):
    renderer = cmds.getAttr("defaultRenderGlobals.ren")
def ProxyWindow(any):
    if cmds.window('Proxy_optionsWindow', ex=True):
        cmds.deleteUI('Proxy_optionsWindow', wnd=True)
    win2 = cmds.window('Proxy_optionsWindow', title='Proxy_Window', widthHeight=(300, 200))
    cmds.columnLayout(adj=True)
    cmds.button(en=False, l='')
    cmds.button(l=u'Arnod代理')
    cmds.textFieldGrp( label='Group 1', text='Editable')
    cmds.columnLayout(adj=True)
    cmds.button(l=u'Redshift代理')
    cmds.showWindow(win2)

ProxyWindow(any)